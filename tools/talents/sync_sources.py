"""Fetch pinned public talent sources for the maintainer-only asset pipeline."""

from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PARSER_VERSION = 1
MAX_RESPONSE_BYTES = 50 * 1024 * 1024
ALLOWED_HOSTS = {
    "wago.tools",
    "raw.githubusercontent.com",
    "nether.wowhead.com",
    "www.wowhead.com",
    "www.method.gg",
}
BLIZZARD_ALPHABET = re.compile(r"^[A-Za-z0-9+/]+$")


class SourceSyncError(RuntimeError):
    """Raised when a source cannot be fetched or is outside the registry."""


def _parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def load_config(path: Path) -> dict[str, dict[str, str]]:
    """Parse the intentionally small, flat TOML registry without dependencies."""
    config: dict[str, dict[str, str]] = {}
    section: dict[str, str] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            name = line[1:-1].strip()
            section = config.setdefault(name, {})
            continue
        if section is None or "=" not in line:
            raise SourceSyncError(f"invalid source registry line: {raw_line}")
        key, value = line.split("=", 1)
        section[key.strip()] = _parse_scalar(value)
    required = {"snapshot", "wago", "wowdbdefs", "wowhead"}
    if not required.issubset(config):
        raise SourceSyncError("source registry is missing a required section")
    return config


def build_source_urls(config: dict[str, dict[str, str]], build: str, locale: str) -> dict[str, str]:
    snapshot = config["snapshot"]
    if build != snapshot["build"] or locale != snapshot["locale"]:
        raise SourceSyncError("requested build/locale does not match the pinned source registry")
    urls: dict[str, str] = {}
    for table in (item.strip() for item in config["wago"]["tables"].split(",")):
        if table:
            urls[table] = config["wago"]["url"].format(table=table, build=build, locale=locale)
            urls[f"{table}.dbd"] = config["wowdbdefs"]["base_url"].format(table=table)
    urls["wowhead-talents"] = config["wowhead"]["talent_data_url"]
    return urls


def _safe_payload_name(url: str, kind: str) -> str:
    parsed = urllib.parse.urlparse(url)
    base = Path(parsed.path).name or "payload"
    suffix = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
    safe_kind = re.sub(r"[^A-Za-z0-9_.-]", "_", kind)
    return f"{safe_kind}-{suffix}-{base}"


def _validate_url(url: str) -> urllib.parse.ParseResult:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise SourceSyncError(f"source host is not configured: {url}")
    return parsed


def sync_url(url: str, output: Path, build: str, locale: str, *, kind: str) -> tuple[Path, dict[str, Any]]:
    """Fetch one configured URL and write its immutable payload plus receipt."""
    _validate_url(url)
    output.mkdir(parents=True, exist_ok=True)
    payload_path = output / _safe_payload_name(url, kind)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AzerothTalentForge-source-sync/1.0", "Accept": "*/*"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
            status = int(response.getcode() or 200)
            headers = {str(key).lower(): str(value) for key, value in response.getheaders()}
    except Exception as exc:  # urllib has several platform-specific error types.
        raise SourceSyncError(f"source fetch failed for {url}: {exc}") from exc
    if len(body) > MAX_RESPONSE_BYTES:
        raise SourceSyncError(f"source response exceeds {MAX_RESPONSE_BYTES} bytes: {url}")
    if status != 200:
        raise SourceSyncError(f"source returned HTTP {status}: {url}")
    payload_path.write_bytes(body)
    receipt = {
        "kind": kind,
        "url": url,
        "path": str(payload_path),
        "game_build": build,
        "locale": locale,
        "fetched_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "content_sha256": hashlib.sha256(body).hexdigest(),
        "parser_version": PARSER_VERSION,
        "http_status": status,
        "etag": headers.get("etag"),
        "last_modified": headers.get("last-modified"),
    }
    receipt_path = payload_path.with_suffix(payload_path.suffix + ".receipt.json")
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload_path, receipt


def extract_build_samples(html: str, source_url: str, source_name: str) -> list[dict[str, Any]]:
    """Extract only Blizzard-looking strings; never retain surrounding page text."""
    found: list[dict[str, Any]] = []
    seen: set[str] = set()
    for match in re.finditer(r"[A-Za-z0-9+/]{40,}", html):
        code = match.group(0)
        if code in seen or not BLIZZARD_ALPHABET.fullmatch(code):
            continue
        seen.add(code)
        found.append(
            {
                "preset_id": f"{source_name.lower().replace(' ', '-')}-{hashlib.sha256(code.encode()).hexdigest()[:12]}",
                "label": source_name,
                "category": "guide",
                "code": code,
                "source_url": source_url,
                "source_name": source_name,
            }
        )
    return found


def sync_registry(config_path: Path, build: str, locale: str, output: Path) -> list[dict[str, Any]]:
    config = load_config(config_path)
    urls = build_source_urls(config, build, locale)
    receipts = []
    for key, url in sorted(urls.items()):
        payload, receipt = sync_url(url, output, build, locale, kind=key)
        receipt["path"] = str(payload)
        receipts.append(receipt)
    (output / "receipts.json").write_text(json.dumps(receipts, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipts


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--build", required=True)
    parser.add_argument("--locale", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sync_registry(args.config, args.build, args.locale, args.output)
