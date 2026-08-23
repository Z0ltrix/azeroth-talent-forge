"""Refresh the offline external Retail talent-string corpus.

Maintainer-only network tool. It stores Blizzard import strings and source-page
URLs, never page HTML or copied guide prose. Runtime skill execution remains
offline.
"""

from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "plugins" / "azeroth-talent-forge" / "skills" / "talents"
FIXTURE = SKILL / "tests" / "fixtures" / "online_strings.json"
ASSETS = SKILL / "assets"
sys.path.insert(0, str(SKILL))

from scripts.talent_engine.assets import AssetLoader
from scripts.talent_engine.codec import decode_build, decode_header
from scripts.talent_engine.errors import TalentError
from scripts.talent_engine.graph_store import GraphStore
from scripts.talent_engine.validator import validate_build

CODE_RE = re.compile(r"(?<![A-Za-z0-9])C[A-Za-z0-9+/]{70,}(?![A-Za-z0-9])")
WARRIOR_METHOD = {
    "Arms": "https://www.method.gg/guides/arms-warrior/talents",
    "Fury": "https://www.method.gg/guides/fury-warrior/talents",
    "Protection": "https://www.method.gg/guides/protection-warrior/talents",
}
CLASS_SLUGS = {
    1: "warrior", 2: "paladin", 3: "hunter", 4: "rogue", 5: "priest",
    6: "death-knight", 7: "shaman", 8: "mage", 9: "warlock", 10: "monk",
    11: "druid", 12: "demon-hunter", 13: "evoker",
}


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "azeroth-talent-forge-fixture-refresh/1.0"})
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(request, context=context, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def icy_urls() -> dict[tuple[int, int], str]:
    xml = fetch("https://www.icy-veins.com/sitemap.xml")
    urls = re.findall(r"https://www\.icy-veins\.com/wow/[^<]+spec-builds-talents", xml)
    return {url.rsplit("/", 1)[-1]: url for url in urls}


def classify(code: str, graph, spec_id: int) -> dict:
    try:
        version, decoded_spec, _tree_hash = decode_header(code)
        if (version, decoded_spec) != (2, spec_id):
            return {"expected_status": "observed-drift", "expected_decode_error": "SPEC_MISMATCH"}
        build = decode_build(code, graph)
    except TalentError as exc:
        return {"expected_status": "observed-drift", "expected_decode_error": exc.code}
    result = validate_build(build, graph)
    if result.valid:
        return {"expected_status": "compatible"}
    return {
        "expected_status": "observed-drift",
        "expected_violations": sorted({violation.code for violation in result.violations}),
    }


def main() -> None:
    fixtures = json.loads(FIXTURE.read_text(encoding="utf-8"))
    bundle = AssetLoader(ASSETS).open()
    store = GraphStore(bundle)
    specs = [spec for spec in bundle.manifest["specs"] if spec["name"] != "Initial"]
    by_spec = {(spec["class_id"], spec["id"]): spec for spec in specs}
    old_external = [item for item in fixtures if item["source_kind"] == "external"]
    old_method = {(item["class_id"], item["spec_id"]): item["url"] for item in old_external if item["source"] == "Method"}
    old_wowhead = [item for item in old_external if item["source"] == "Wowhead"]
    icy_sitemap = fetch("https://www.icy-veins.com/sitemap.xml")
    icy_candidates = re.findall(r"https://www\.icy-veins\.com/wow/[^<]+spec-builds-talents", icy_sitemap)
    new_external = []
    for source in ("Method", "Icy Veins"):
        for key, spec in sorted(by_spec.items(), key=lambda pair: pair[1]["id"]):
            class_id, spec_id = key
            if source == "Method":
                url = old_method.get(key)
                if not url and spec["name"] in WARRIOR_METHOD:
                    url = WARRIOR_METHOD[spec["name"]]
                if not url:
                    raise RuntimeError(f"missing Method URL for {spec['name']} ({spec_id})")
            else:
                class_slug = CLASS_SLUGS[class_id]
                spec_slug = spec["name"].lower().replace(" ", "-")
                matches = [url for url in icy_candidates if f"/{spec_slug}-{class_slug}-" in url]
                if not matches:
                    raise RuntimeError(f"missing Icy Veins URL for {spec['name']} ({spec_id})")
                url = matches[0]
            graph = store.load_spec(spec_id)
            codes = list(dict.fromkeys(CODE_RE.findall(fetch(url))))
            for index, code in enumerate(codes, 1):
                item = {
                    "source_kind": "external",
                    "source": source,
                    "url": url,
                    "class_id": class_id,
                    "spec_id": spec_id,
                    "label": f"{spec['name']} {source} build {index}",
                    "code": code,
                }
                item.update(classify(code, graph, spec_id))
                new_external.append(item)
    # Retain the existing manually captured Wowhead smoke fixture. Wowhead is
    # not crawled automatically (and its payload already feeds graph import).
    for item in old_wowhead:
        item = dict(item)
        item["expected_status"] = "compatible"
        new_external.insert(0, item)
    local = [item for item in fixtures if item["source_kind"] == "local-smoke"]
    output = new_external + local
    FIXTURE.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    counts = {}
    for item in new_external:
        counts[item["source"]] = counts.get(item["source"], 0) + 1
    print(json.dumps({"external": len(new_external), "sources": counts, "local_smoke": len(local)}))


if __name__ == "__main__":
    main()
