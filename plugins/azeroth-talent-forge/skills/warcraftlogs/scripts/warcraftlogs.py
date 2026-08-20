import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Mapping, Optional, Sequence

CLIENT_ID_ENV = "WARCRAFTLOGS_CLIENT_ID"
CLIENT_SECRET_ENV = "WARCRAFTLOGS_CLIENT_SECRET"


@dataclass(frozen=True)
class Credentials:
    client_id: str
    client_secret: str


def load_dotenv(path: Path) -> dict:
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="warcraftlogs.py")
    parser.add_argument("--client-id")
    parser.add_argument("--client-secret")
    parser.add_argument("--env-file")
    parser.add_argument("--no-cache", action="store_true")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    build_parser().parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
