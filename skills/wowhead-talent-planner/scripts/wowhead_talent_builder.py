#!/usr/bin/env python3
"""Build local Wowhead/Blizzard talent import strings.

Uses Wowhead's talent data model and the Blizzard loadout bit format used by
Wowhead's /talent-calc/blizzard/<hash> URLs. No browser automation required.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

B64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
BASE = "https://www.wowhead.com"
TYPE_CHOICE = 3
TYPE_MULTI = 5
GRID_WIDTH = 19
UA = "Mozilla/5.0 (Codex Wowhead talent builder)"


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def cache_dir() -> Path:
    return Path.home() / ".codex" / "cache" / "wowhead-talent-planner"


def extract_blizzard_hash(text: str) -> str:
    m = re.search(r"/talent-calc/blizzard/([A-Za-z0-9+/=]+)", text)
    if m:
        return m.group(1)
    if re.fullmatch(r"[A-Za-z0-9+/=]+", text):
        return text
    raise SystemExit(f"No Blizzard hash found in: {text}")


def discover_assets(planner_url: str) -> dict[str, str]:
    html = fetch(planner_url).decode("utf-8", "replace")
    srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html, re.I)
    urls = [urljoin(planner_url, src) for src in srcs]
    out = {}
    for url in urls:
        if "talents-dragonflight" in url:
            out["talent_data"] = url
    if "talent_data" not in out:
        m = re.search(r'https://nether\.wowhead\.com/data/talents-dragonflight[^"\'<>]+', html)
        if m:
            out["talent_data"] = m.group(0)
    if "talent_data" not in out:
        raise SystemExit("Could not discover Wowhead talent data URL")
    return out


def latest_data_file() -> Path | None:
    c = cache_dir()
    files = sorted(c.glob("talent_data-*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[0] if files else None


def load_talent_data(base_url: str, refresh: bool = False) -> str:
    c = cache_dir()
    c.mkdir(parents=True, exist_ok=True)
    if not refresh:
        p = latest_data_file()
        if p:
            return p.read_text(encoding="utf-8", errors="replace")
    assets = discover_assets(base_url)
    body = fetch(assets["talent_data"])
    path = c / "talent_data-current.txt"
    path.write_bytes(body)
    return body.decode("utf-8", "replace")


def extract_page_data(data_text: str, key: str):
    prefix = f'WH.setPageData("{key}",'
    start = data_text.find(prefix)
    if start < 0:
        raise SystemExit(f"Missing Wowhead page data key: {key}")
    i = start + len(prefix)
    open_ch = data_text[i]
    close_ch = "]" if open_ch == "[" else "}"
    depth = 0
    in_str = False
    esc = False
    for j in range(i, len(data_text)):
        ch = data_text[j]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return json.loads(data_text[i:j + 1])
    raise SystemExit(f"Unterminated Wowhead page data key: {key}")


class BitReader:
    def __init__(self, text: str):
        self.values = [B64.index(ch) for ch in text]
        self.index = 0
        self.used = 0
        self.remaining = self.values[0]

    def read(self, bits: int) -> int | None:
        if self.index >= len(self.values):
            return None
        value = 0
        shift = 0
        while bits > 0:
            avail = 6 - self.used
            take = min(avail, bits)
            self.used += take
            mod = 1 << take
            chunk = self.remaining % mod
            self.remaining >>= take
            value += chunk << shift
            shift += take
            bits -= take
            if take < avail:
                break
            self.index += 1
            self.used = 0
            self.remaining = self.values[self.index] if self.index < len(self.values) else 0
        return value


class BitWriter:
    def __init__(self):
        self.entries: list[tuple[int, int]] = []

    def add(self, bits: int, value: int) -> None:
        self.entries.append((bits, value))

    def finish(self) -> str:
        out = []
        current = 0
        used = 0
        for width, value in self.entries:
            while width > 0:
                avail = 6 - used
                mod = 1 << avail
                chunk = value % mod
                value >>= avail
                current += chunk << used
                if avail > width:
                    used = (used + width) % 6
                    width = 0
                else:
                    out.append(B64[current])
                    current = 0
                    used = 0
                    width -= avail
        if used > 0:
            out.append(B64[current])
        return "".join(out)


class TalentModel:
    def __init__(self, trees: list[dict], nodes: dict):
        self.trees = trees
        self.nodes = nodes

    def tree(self, tree_id: int) -> dict:
        for tree in self.trees:
            if tree["id"] == tree_id:
                return tree
        raise KeyError(tree_id)

    def class_for_spec(self, spec_id: int) -> int:
        tree = self.tree(spec_id)
        return int(tree["playerClass"])

    def variants(self, tree_id: int, spec_id: int) -> list[dict]:
        tree = self.tree(tree_id)
        variants = []
        for cell_s in sorted(tree["talents"], key=lambda x: int(x)):
            arr = tree["talents"][cell_s]
            chosen = None
            for talent in arr:
                if spec_id in talent.get("shownForSpecs", [spec_id]):
                    chosen = talent
                    break
            if chosen:
                variants.append(chosen)
        return variants

    def hero_trees_for_spec(self, spec_id: int) -> list[dict]:
        out = []
        for tree in self.trees:
            if tree.get("type") != 3:
                continue
            if any(spec_id in talent.get("shownForSpecs", []) for arr in tree.get("talents", {}).values() for talent in arr):
                out.append(tree)
        return sorted(out, key=lambda x: x.get("name", ""))

    def granted_nodes(self, spec_id: int) -> list[int]:
        out = set()
        for tree in self.hero_trees_for_spec(spec_id):
            for arr in tree.get("talents", {}).values():
                if any(spec_id in t.get("shownForSpecs", []) and spec_id in t.get("defaultSpecs", []) for t in arr):
                    out.add(arr[0]["node"])
        return list(out)

    def find_talent(self, state: dict, name: str) -> tuple[dict, int, dict, int | None]:
        needle = name.lower()
        for tree_state in state["trees"]:
            variants = self.variants(tree_state["treeId"], state["specId"])
            choice_seq = 0
            for idx, talent in enumerate(variants):
                spell_names = [s["name"] for s in talent["spells"]]
                joined = " / ".join(spell_names)
                matched = needle == joined.lower() or any(needle == s.lower() for s in spell_names)
                current_choice_seq = choice_seq if talent["type"] == TYPE_CHOICE else None
                if matched:
                    return tree_state, idx, talent, current_choice_seq
                if talent["type"] == TYPE_CHOICE and tree_state["points"][idx] > 0:
                    choice_seq += 1
        raise SystemExit(f"Talent not found in current build/spec: {name}")

    def choice_for_index(self, tree_state: dict, variants: list[dict], idx: int) -> int:
        if variants[idx]["type"] != TYPE_CHOICE or tree_state["points"][idx] <= 0:
            return 0
        seq = 0
        for j in range(idx):
            if variants[j]["type"] == TYPE_CHOICE and tree_state["points"][j] > 0:
                seq += 1
        return tree_state["choices"][seq] if seq < len(tree_state["choices"]) else 0

    def rebuild_choices(self, tree_state: dict, explicit: dict[int, int] | None = None) -> None:
        explicit = explicit or {}
        variants = self.variants(tree_state["treeId"], tree_state.get("specId", 0) or 0)
        # specId is not stored per tree_state normally; fallback patched by caller.
        raise NotImplementedError


def points_for_talent(talent: dict, choice: int = 0) -> int:
    if talent["type"] == TYPE_MULTI:
        return sum(spell["points"] for spell in talent["spells"])
    return talent["spells"][choice].get("points", 1)


def rebuild_choices(model: TalentModel, state: dict, tree_state: dict, explicit: dict[int, int] | None = None) -> None:
    explicit = explicit or {}
    variants = model.variants(tree_state["treeId"], state["specId"])
    old = {}
    seq = 0
    for idx, talent in enumerate(variants):
        if talent["type"] == TYPE_CHOICE and tree_state["points"][idx] > 0:
            old[talent["cell"]] = tree_state["choices"][seq] if seq < len(tree_state["choices"]) else 0
            seq += 1
    choices = []
    for idx, talent in enumerate(variants):
        if talent["type"] == TYPE_CHOICE and tree_state["points"][idx] > 0:
            choices.append(explicit.get(talent["cell"], old.get(talent["cell"], 0)))
    tree_state["choices"] = choices


def decode(model: TalentModel, text: str) -> dict:
    reader = BitReader(text)
    version = reader.read(8)
    spec_id = reader.read(16)
    for _ in range(0, 128, 8):
        reader.read(8)
    entries = []
    while reader.index < len(reader.values):
        selected = reader.read(1) == 1
        purchased = selected
        if version > 1 and selected:
            purchased = reader.read(1) == 1
        partial = False
        ranks = 0
        is_choice = False
        choice = 0
        if purchased:
            partial = reader.read(1) == 1
            if partial:
                ranks = reader.read(6)
            is_choice = reader.read(1) == 1
            if is_choice:
                choice = reader.read(2)
        entries.append({
            "selected": selected, "purchased": purchased, "partial": partial,
            "ranks": ranks, "isChoice": is_choice, "choice": choice,
        })
    class_id = model.class_for_spec(spec_id)
    node_list = model.nodes[str(class_id)]["nodes"]
    hero_choices = model.nodes[str(class_id)].get("heroTreeChoices", {})
    tree_ids = [class_id, spec_id]
    for node_s, choices in hero_choices.items():
        idx = node_list.index(int(node_s)) if int(node_s) in node_list else -1
        if idx >= 0 and idx < len(entries) and entries[idx].get("purchased"):
            tree_ids.append(choices[entries[idx]["choice"]])
            break
    state = {"version": version, "specId": spec_id, "trees": []}
    for tree_id in tree_ids:
        tree_state = {"treeId": tree_id, "points": [], "choices": []}
        for talent in model.variants(tree_id, spec_id):
            pts = 0
            selected_choice = None
            if talent["node"] in node_list:
                entry = entries[node_list.index(talent["node"])]
                if entry.get("purchased"):
                    selected_choice = entry["choice"]
                    pts = entry["ranks"] if entry["partial"] else points_for_talent(talent, selected_choice)
            tree_state["points"].append(pts)
            if talent["type"] == TYPE_CHOICE and selected_choice is not None:
                tree_state["choices"].append(selected_choice)
        while tree_state["points"] and tree_state["points"][-1] == 0:
            tree_state["points"].pop()
        # Pad back to variant length for easier editing.
        tree_state["points"].extend([0] * (len(model.variants(tree_id, spec_id)) - len(tree_state["points"])))
        state["trees"].append(tree_state)
    return state


def encode(model: TalentModel, state: dict) -> str:
    writer = BitWriter()
    spec_id = state["specId"]
    class_id = model.class_for_spec(spec_id)
    node_list = model.nodes[str(class_id)]["nodes"]
    writer.add(8, 2)
    writer.add(16, spec_id)
    for _ in range(0, 128, 8):
        writer.add(8, 0)

    hero_choice_map = {}
    hero_choices = model.nodes[str(class_id)].get("heroTreeChoices", {})
    hero_ids = [t["id"] for t in model.hero_trees_for_spec(spec_id)]
    hero_tree_id = state["trees"][2]["treeId"] if len(state["trees"]) > 2 else None
    for node_s, choices in hero_choices.items():
        entry = {"entryIndex": 0, "isChoiceNode": True, "isGranted": False, "maxRanks": 1, "ranksPurchased": 0}
        if all(c in hero_ids for c in choices) and hero_tree_id in choices:
            entry["entryIndex"] = choices.index(hero_tree_id)
            entry["ranksPurchased"] = 1
        hero_choice_map[int(node_s)] = entry
    for node in model.granted_nodes(spec_id):
        hero_choice_map[node] = {"entryIndex": 0, "isChoiceNode": False, "isGranted": True, "maxRanks": 1, "ranksPurchased": 0}

    info_by_node = {}
    for tree_state in state["trees"]:
        variants = model.variants(tree_state["treeId"], spec_id)
        for idx, talent in enumerate(variants):
            ranks = tree_state["points"][idx] if idx < len(tree_state["points"]) else 0
            if ranks <= 0:
                continue
            choice = 0
            if talent["type"] == TYPE_CHOICE:
                seq = sum(1 for j in range(idx) if variants[j]["type"] == TYPE_CHOICE and tree_state["points"][j] > 0)
                choice = tree_state["choices"][seq] if seq < len(tree_state["choices"]) else 0
            info_by_node[talent["node"]] = {
                "entryIndex": choice,
                "isChoiceNode": talent["type"] == TYPE_CHOICE,
                "isGranted": False,
                "maxRanks": points_for_talent(talent, choice),
                "ranksPurchased": ranks,
            }

    for node in node_list:
        info = info_by_node.get(node) or hero_choice_map.get(node) or {
            "entryIndex": 0, "isChoiceNode": False, "isGranted": False, "maxRanks": 0, "ranksPurchased": 0,
        }
        selected = info["ranksPurchased"] > 0
        purchased = info["isGranted"] or selected
        partial = info["ranksPurchased"] != info["maxRanks"]
        writer.add(1, 1 if purchased else 0)
        if purchased:
            writer.add(1, 1 if selected else 0)
            if selected:
                writer.add(1, 1 if partial else 0)
                if partial:
                    writer.add(6, info["ranksPurchased"])
                writer.add(1, 1 if info["isChoiceNode"] else 0)
                if info["isChoiceNode"]:
                    writer.add(2, info["entryIndex"])
    return writer.finish()


def set_talent(model: TalentModel, state: dict, name: str, points: int = 1, choice_name: str | None = None) -> None:
    tree_state, idx, talent, _ = model.find_talent(state, name)
    variants = model.variants(tree_state["treeId"], state["specId"])
    while len(tree_state["points"]) < len(variants):
        tree_state["points"].append(0)
    explicit = {}
    if talent["type"] == TYPE_CHOICE:
        choice = 0
        if choice_name:
            spell_names = [s["name"].lower() for s in talent["spells"]]
            try:
                choice = spell_names.index(choice_name.lower())
            except ValueError:
                raise SystemExit(f"Choice '{choice_name}' not found for {' / '.join(s['name'] for s in talent['spells'])}")
        else:
            # If user set a specific spell name, choose that spell.
            spell_names = [s["name"].lower() for s in talent["spells"]]
            if name.lower() in spell_names:
                choice = spell_names.index(name.lower())
        explicit[talent["cell"]] = choice
    tree_state["points"][idx] = points
    rebuild_choices(model, state, tree_state, explicit)


def clear_talent(model: TalentModel, state: dict, name: str) -> None:
    tree_state, idx, _talent, _ = model.find_talent(state, name)
    tree_state["points"][idx] = 0
    rebuild_choices(model, state, tree_state)


def summarize(model: TalentModel, state: dict, names: list[str]) -> dict[str, str]:
    out = {}
    for name in names:
        try:
            tree_state, idx, talent, _ = model.find_talent(state, name)
            pts = tree_state["points"][idx] if idx < len(tree_state["points"]) else 0
            if talent["type"] == TYPE_CHOICE and pts > 0:
                variants = model.variants(tree_state["treeId"], state["specId"])
                choice = model_choice_for_index(tree_state, variants, idx)
                out[name] = f"{pts}/{points_for_talent(talent, choice)} ({talent['spells'][choice]['name']})"
            else:
                out[name] = f"{pts}/{points_for_talent(talent, 0)}"
        except SystemExit:
            out[name] = "not found"
    return out


def model_choice_for_index(tree_state: dict, variants: list[dict], idx: int) -> int:
    seq = 0
    for j in range(idx):
        if variants[j]["type"] == TYPE_CHOICE and tree_state["points"][j] > 0:
            seq += 1
    return tree_state["choices"][seq] if seq < len(tree_state["choices"]) else 0


def spent(model: TalentModel, state: dict) -> list[dict]:
    return [{"treeId": ts["treeId"], "spent": sum(ts["points"])} for ts in state["trees"]]


def main() -> int:
    ap = argparse.ArgumentParser(description="Build a local Wowhead talent code and planner link.")
    ap.add_argument("--base", required=True, help="Base /talent-calc/blizzard/<hash> URL or raw Blizzard hash")
    ap.add_argument("--set", action="append", default=[], metavar="TALENT", help="Set talent to 1 point by name")
    ap.add_argument("--clear", action="append", default=[], metavar="TALENT", help="Clear talent by name")
    ap.add_argument("--choice", action="append", default=[], metavar="NODE=CHOICE", help="Set choice node, e.g. 'Choice Node Name=Choice Name'")
    ap.add_argument("--refresh-data", action="store_true", help="Re-download Wowhead talent data")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    base = args.base
    data_text = load_talent_data(base, args.refresh_data)
    trees = extract_page_data(data_text, "wow.talentCalcDragonflight.live.trees")
    nodes = extract_page_data(data_text, "wow.talentCalcDragonflight.live.nodes")
    model = TalentModel(trees, nodes)
    base_hash = extract_blizzard_hash(base)
    state = decode(model, base_hash)

    for name in args.clear:
        clear_talent(model, state, name)
    for name in args.set:
        set_talent(model, state, name)
    for item in args.choice:
        if "=" not in item:
            raise SystemExit("--choice must be NODE=CHOICE")
        node, choice = item.split("=", 1)
        set_talent(model, state, node.strip(), 1, choice.strip())

    code = encode(model, state)
    link = f"{BASE}/talent-calc/blizzard/{code}"
    watched = []
    watched.extend(args.set)
    watched.extend(args.clear)
    watched.extend([x.split("=", 1)[-1].strip() for x in args.choice if "=" in x])
    watched = list(dict.fromkeys(watched))
    result = {
        "code": code,
        "link": link,
        "spent": spent(model, state),
        "summary": summarize(model, state, watched) if watched else {},
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("Planner link:")
        print(link)
        print("\nImport code:")
        print(code)
        print("\nSpent:")
        for row in result["spent"]:
            print(f"- tree {row['treeId']}: {row['spent']}")
        if result["summary"]:
            print("\nChecked talents:")
            for k, v in result["summary"].items():
                print(f"- {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
