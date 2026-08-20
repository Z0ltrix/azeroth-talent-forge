"""GraphQL document loading and OAuth/HTTP transport."""
import base64
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Mapping, Optional
from .models import ApiError, AuthenticationError, Credentials, PartialGraphQLError, GRAPHQL_URL, TOKEN_URL, QUERY_NAME

HTTP_TIMEOUT_SECONDS = 30

def load_query(name: str, query_dir: Optional[Path] = None) -> str:
    if not QUERY_NAME.fullmatch(name):
        raise ValueError("Invalid query name")
    # GraphQL files live one level below scripts.
    directory = query_dir or Path(__file__).resolve().parent.parent / "graphql"
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
        self.opener = (
            opener
            if opener is not None
            else lambda request: urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS)
        )
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
