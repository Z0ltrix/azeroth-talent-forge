#!/usr/bin/env python3
"""Fetch and inspect Wowhead talent planner assets.

Purpose: make Wowhead talent work repeatable. The script does not rely on
hard-coded build IDs; it discovers the current TalentCalcDragonflight JS and
Talent data URLs from a planner page, downloads them, and extracts useful
signals for later decoding/export work.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

DEFAULT_URL = "https://www.wowhead.com/talent-calc/warrior/protection/colossus"
UA = "Mozilla/5.0 (Codex Wowhead talent skill)"


@dataclass
class Asset:
    kind: str
    url: str
    path: str
    sha256: str
    bytes: int


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def save(cache: Path, kind: str, url: str, body: bytes) -> Asset:
    cache.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(body).hexdigest()
    suffix = ".js" if ".js" in url else ".txt"
    name = f"{kind}-{digest[:12]}{suffix}"
    path = cache / name
    path.write_bytes(body)
    return Asset(kind, url, str(path), digest, len(body))


def discover(html: str, base_url: str) -> dict[str, str]:
    srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html, re.I)
    urls = [urljoin(base_url, src) for src in srcs]
    out: dict[str, str] = {}
    for url in urls:
        if "TalentCalcDragonflight.js" in url:
            out["talent_calc_js"] = url
        if "talents-dragonflight" in url:
            out["talent_data"] = url
    # Fallback: server sometimes omits async data script until hydration.
    if "talent_data" not in out:
        m = re.search(r'https://nether\.wowhead\.com/data/talents-dragonflight[^"\'<>]+', html)
        if m:
            out["talent_data"] = m.group(0)
    return out


def extract_hash(url: str) -> dict[str, str | None]:
    m = re.search(r'/talent-calc/blizzard/([A-Za-z0-9+/=]+)', url)
    blizzard = m.group(1) if m else None
    m = re.search(r'/talent-calc/([^?#]+)', url)
    wowhead = m.group(1) if m else None
    return {"blizzard_hash": blizzard, "wowhead_path": wowhead}


def inspect_js(js: str) -> dict[str, object]:
    markers = ["getHash", "readHash", "copyToClipboard", "TalentCalcDragonflight", "EVENT_HASH_UPDATE"]
    return {
        "markers": {marker: js.find(marker) for marker in markers},
        "length": len(js),
        "sha256": hashlib.sha256(js.encode("utf-8", "replace")).hexdigest(),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch current Wowhead talent planner JS/data assets.")
    ap.add_argument("url", nargs="?", default=DEFAULT_URL, help="Wowhead talent planner URL or /blizzard/ URL")
    ap.add_argument("--cache", default=str(Path.home() / ".codex" / "cache" / "wowhead-talent-planner"))
    ap.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = ap.parse_args()

    cache = Path(args.cache)
    html_b = fetch(args.url)
    html = html_b.decode("utf-8", "replace")
    assets = [save(cache, "planner-html", args.url, html_b)]
    discovered = discover(html, args.url)

    js_info = None
    for kind, url in discovered.items():
        body = fetch(url)
        assets.append(save(cache, kind, url, body))
        if kind == "talent_calc_js":
            js_info = inspect_js(body.decode("utf-8", "replace"))

    result = {
        "input": args.url,
        "hashes": extract_hash(args.url),
        "discovered": discovered,
        "assets": [asdict(a) for a in assets],
        "js": js_info,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Input: {args.url}")
        print(f"Blizzard hash: {result['hashes']['blizzard_hash'] or '-'}")
        print(f"Wowhead path: {result['hashes']['wowhead_path'] or '-'}")
        for a in assets:
            print(f"Saved {a.kind}: {a.path} ({a.bytes} bytes)")
        if js_info:
            print("JS markers:", json.dumps(js_info["markers"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
