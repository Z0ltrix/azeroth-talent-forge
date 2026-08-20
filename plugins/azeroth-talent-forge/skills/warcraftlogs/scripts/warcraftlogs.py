import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence

CLIENT_ID_ENV = "WARCRAFTLOGS_CLIENT_ID"
CLIENT_SECRET_ENV = "WARCRAFTLOGS_CLIENT_SECRET"
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
GRAPHQL_URL = "https://www.warcraftlogs.com/api/v2/client"
QUERY_NAME = re.compile(r"^[a-z0-9-]+$")


class AuthenticationError(RuntimeError):
    pass


class ApiError(RuntimeError):
    pass


@dataclass(frozen=True)
class Credentials:
    client_id: str
    client_secret: str


def load_dotenv(path: Path) -> Dict[str, str]:
    values = {}
    if not path.is_file():
        return values
    for number, raw_line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise ValueError("Malformed .env entry at line %d" % number)
        key, value = line.split("=", 1)
        key = key.strip()
        if key not in (CLIENT_ID_ENV, CLIENT_SECRET_ENV):
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return values


def resolve_credentials(
    client_id: Optional[str],
    client_secret: Optional[str],
    env_file: Optional[str],
    cwd: Path,
    environ: Mapping[str, str],
) -> Credentials:
    dotenv = load_dotenv(Path(env_file) if env_file else cwd / ".env")
    resolved_id = client_id or dotenv.get(CLIENT_ID_ENV) or environ.get(CLIENT_ID_ENV)
    resolved_secret = client_secret or dotenv.get(CLIENT_SECRET_ENV) or environ.get(CLIENT_SECRET_ENV)
    missing = [name for name, value in ((CLIENT_ID_ENV, resolved_id), (CLIENT_SECRET_ENV, resolved_secret)) if not value]
    if missing:
        raise ValueError("Missing credential: %s" % ", ".join(missing))
    return Credentials(resolved_id, resolved_secret)


def load_query(name: str, query_dir: Optional[Path] = None) -> str:
    if not QUERY_NAME.fullmatch(name):
        raise ValueError("Invalid query name")
    directory = query_dir or Path(__file__).resolve().parent / "graphql"
    return (directory / (name + ".graphql")).read_text(encoding="utf-8")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sanitize_graphql_errors(errors) -> List[dict]:
    sanitized = []
    for error in errors or []:
        if not isinstance(error, Mapping):
            continue
        value = {}
        if "message" in error:
            value["message"] = error["message"]
        if "path" in error:
            value["path"] = error["path"]
        extensions = error.get("extensions")
        if isinstance(extensions, Mapping) and "code" in extensions:
            value["extensions"] = {"code": extensions["code"]}
        sanitized.append(value)
    return sanitized


class WarcraftLogsClient:
    def __init__(self, credentials: Credentials, opener=None, sleep=None):
        self.credentials = credentials
        self.opener = opener or urllib.request.urlopen
        self.sleep = sleep or time.sleep
        self._token = None
        self._token_expires_at = 0.0

    def _open_json(self, request) -> dict:
        for attempt in range(3):
            try:
                with self.opener(request) as response:
                    try:
                        payload = json.loads(response.read().decode("utf-8"))
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        raise ApiError("Response was not valid JSON")
                    if not isinstance(payload, dict):
                        raise ApiError("Response JSON must be an object")
                    return payload
            except urllib.error.HTTPError as error:
                retryable = error.code == 429 or 500 <= error.code < 600
                if not retryable or attempt == 2:
                    raise ApiError("HTTP request failed with status %d" % error.code)
                retry_after = error.headers.get("Retry-After") if error.headers else None
                self.sleep(int(retry_after) if retry_after and retry_after.isdigit() else 0)
            except urllib.error.URLError:
                raise ApiError("Network request failed")
            except OSError:
                raise ApiError("Response read failed")
        raise ApiError("HTTP request failed")

    def access_token(self) -> str:
        if self._token and time.time() < self._token_expires_at - 30:
            return self._token
        encoded = base64.b64encode(
            (self.credentials.client_id + ":" + self.credentials.client_secret).encode("utf-8")
        ).decode("ascii")
        request = urllib.request.Request(
            TOKEN_URL,
            data=urllib.parse.urlencode({"grant_type": "client_credentials"}).encode("ascii"),
            headers={"Authorization": "Basic " + encoded},
            method="POST",
        )
        try:
            payload = self._open_json(request)
            self._token = str(payload["access_token"])
            self._token_expires_at = time.time() + int(payload.get("expires_in", 3600))
        except (ApiError, KeyError, TypeError, ValueError):
            raise AuthenticationError("OAuth authentication failed")
        return self._token

    def execute(self, query_name: str, variables: Mapping[str, object]) -> dict:
        body = json.dumps(
            {"query": load_query(query_name), "variables": dict(variables)},
            separators=(",", ":"),
        ).encode("utf-8")
        request = urllib.request.Request(
            GRAPHQL_URL,
            data=body,
            headers={
                "Authorization": "Bearer " + self.access_token(),
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            return self._open_json(request)
        except ApiError:
            raise ApiError("Warcraft Logs API request failed")


def normalize_rate_limit(payload: Mapping[str, object]) -> dict:
    value = payload["data"]["rateLimitData"]
    return {
        "limit_per_hour": value["limitPerHour"],
        "points_spent_this_hour": value["pointsSpentThisHour"],
        "points_reset_in": value["pointsResetIn"],
    }


def make_envelope(
    command,
    scope,
    filters,
    completeness,
    data,
    pagination=None,
    rate_limit=None,
    warnings=None,
    errors=None,
    **metadata
) -> dict:
    result = {
        "schema_version": 1,
        "command": command,
        "source": {"provider": "warcraftlogs", "endpoint": "client", "fetched_at": utc_now()},
        "scope": dict(scope),
        "filters": dict(filters),
        "completeness": completeness,
        "pagination": pagination or {"pages_fetched": 1, "truncated": False},
        "rate_limit": rate_limit or {},
        "warnings": list(warnings or []),
        "data": data,
    }
    result.update(metadata)
    if errors:
        result["partial"] = True
        result["errors"] = sanitize_graphql_errors(errors)
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="warcraftlogs.py")
    parser.add_argument("--client-id")
    parser.add_argument("--client-secret")
    parser.add_argument("--env-file")
    parser.add_argument("--no-cache", action="store_true")
    parser.add_subparsers(dest="command").add_parser("rate-limit")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command != "rate-limit":
        return 0
    try:
        credentials = resolve_credentials(
            args.client_id,
            args.client_secret,
            args.env_file,
            Path.cwd(),
            os.environ,
        )
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    client = WarcraftLogsClient(credentials)
    try:
        payload = client.execute("rate-limit", {})
    except AuthenticationError as error:
        print(str(error), file=sys.stderr)
        return 3
    except (ApiError, OSError, ValueError):
        print("Warcraft Logs API request failed", file=sys.stderr)
        return 4
    try:
        data = normalize_rate_limit(payload)
    except (KeyError, TypeError):
        print("Warcraft Logs API response did not contain rate limit data", file=sys.stderr)
        return 4
    print(
        json.dumps(
            make_envelope(
                "rate-limit",
                {},
                {},
                "api_collection",
                data,
                errors=payload.get("errors"),
            ),
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
