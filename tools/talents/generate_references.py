"""Generate feature and class Markdown from one normalized talent snapshot."""

from __future__ import annotations

import gzip
import json
import re
import shutil
from pathlib import Path
from typing import Any


class ReferenceGenerationError(RuntimeError):
    """Raised when factual reference coverage cannot be generated."""


CLASS_SLUGS = {
    "Death Knight": "death-knight", "Demon Hunter": "demon-hunter", "Druid": "druid",
    "Evoker": "evoker", "Hunter": "hunter", "Mage": "mage", "Monk": "monk",
    "Paladin": "paladin", "Priest": "priest", "Rogue": "rogue", "Shaman": "shaman",
    "Warlock": "warlock", "Warrior": "warrior",
}


def _load_snapshot(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        snapshot = json.load(stream)
    if snapshot.get("schema_version") != 1 or snapshot.get("game_build") != "12.1.0.69404":
        raise ReferenceGenerationError("reference snapshot is not the pinned Retail build")
    return snapshot


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n").replace("\r", "\n"), encoding="utf-8", newline="\n")


def _condition_text(condition: dict[str, Any]) -> str:
    parts = [f"source `{condition['source']}`", f"type `{condition['type']}`"]
    if condition.get("level"):
        parts.append(f"minimum level `{condition['level']}`")
    if condition.get("currency_id"):
        parts.append(f"currency `{condition['currency_id']}` spend gate `{condition.get('spent', 0)}`")
    if condition.get("granted_ranks"):
        parts.append(f"grants `{condition['granted_ranks']}` rank(s)")
    return "; ".join(parts)


def _talent_block(
    entry: dict[str, Any],
    node: dict[str, Any],
    definition: dict[str, Any],
    tree: dict[str, Any],
    notes: dict[str, Any],
    costs_by_node: dict[int, list[dict[str, Any]]],
    conditions_by_node: dict[int, list[dict[str, Any]]],
    conditions_by_entry: dict[int, list[dict[str, Any]]],
    incoming_edges: dict[int, list[dict[str, Any]]],
    effects_by_definition: dict[int, list[dict[str, Any]]],
    currency_labels: dict[int, str],
) -> str:
    tags = notes.get(str(entry["id"]), {}).get("tags", []) if isinstance(notes.get(str(entry["id"]), {}), dict) else []
    tag_text = ", ".join(tags) if tags else "source-derived only"
    title = definition["name"] or "Structural rank (no player-facing ability)"
    lines = [
            f"### {title}",
            f"- Node ID: `{node['id']}`",
            f"- Entry ID: `{entry['id']}`",
            f"- Definition ID: `{definition['id']}`",
            f"- Spell ID: `{definition.get('spell_id', 0)}`",
            f"- Tree ID: `{tree.get('id', node.get('tree_id', 0))}`; tree kind: `{tree.get('kind', 'unknown')}`",
            f"- Maximum ranks: `{entry.get('max_ranks', 1)}`; entry ordinal: `{entry.get('ordinal', 0)}`",
    ]
    if definition["source"] == "structural":
        lines.append("- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.")
    else:
        lines += [
            f"- Description: {definition['description']}",
            f"- Effect: {definition.get('effect', definition['description'])}",
        ]
    costs = costs_by_node.get(node["id"], [])
    lines.append("- Point cost per purchased rank: " + (
        ", ".join(f"`{item['amount']}` × {currency_labels.get(item['currency_id'], 'internal talent-point pool')} (ID `{item['currency_id']}`; {item['source']})" for item in costs)
        if costs else "no cost record in the exact-build source"
    ))
    conditions = conditions_by_node.get(node["id"], []) + conditions_by_entry.get(entry["id"], [])
    lines.append("- Source gates: " + (" | ".join(_condition_text(item) for item in conditions) if conditions else "none attached to this node or entry"))
    prerequisites = incoming_edges.get(node["id"], [])
    lines.append("- Incoming edges: " + (", ".join(f"node `{item['source']}` (type `{item['type']}`)" for item in prerequisites) if prerequisites else "none"))
    effect_points = effects_by_definition.get(definition["id"], [])
    if effect_points:
        lines.append("- Effect-point records: " + ", ".join(f"index `{item['effect_index']}`, operation `{item['operation_type']}`, curve `{item['curve_id']}`" for item in effect_points))
    lines += [
        f"- Planning tags: `{tag_text}`",
        f"- Source: `{definition.get('source', 'normalized snapshot')}`; build: `12.1.0.69404`",
        "",
    ]
    return "\n".join(lines)


def _currency_schedule(
    snapshot: dict[str, Any],
    node_ids: set[int],
    nodes: dict[int, dict[str, Any]],
    subtrees: dict[int, dict[str, Any]],
    specs: dict[int, dict[str, Any]],
) -> tuple[list[str], dict[int, str]]:
    currency_ids = {item["currency_id"] for item in snapshot.get("costs", []) if item["node_id"] in node_ids}
    lines = []
    labels: dict[int, str] = {}
    for currency_id in sorted(currency_ids):
        cost_nodes = [nodes[item["node_id"]] for item in snapshot.get("costs", []) if item["currency_id"] == currency_id and item["node_id"] in node_ids]
        subtree_names = sorted({subtrees[node["subtree_id"]]["name"] for node in cost_nodes if node.get("subtree_id") in subtrees and subtrees[node["subtree_id"]].get("name")})
        spec_names = sorted({specs[spec_id]["name"] for node in cost_nodes for spec_id in node.get("spec_ids", []) if spec_id in specs})
        if subtree_names:
            label = f"Hero pool ({', '.join(subtree_names)})"
        elif spec_names:
            label = f"Specialization pool ({', '.join(spec_names)})"
        else:
            label = "Class pool"
        labels[currency_id] = label
        sources = [item for item in snapshot.get("currency_sources", []) if item["currency_id"] == currency_id]
        if not sources:
            lines.append(f"- **{label}** (internal ID `{currency_id}`): used by this class, but no local level schedule is available.")
            continue
        levels = ", ".join(f"{item['level']} (+{item['amount']})" for item in sources)
        total = sum(item["amount"] for item in sources if item["level"] <= 90)
        lines.append(f"- **{label}** (internal ID `{currency_id}`): `{total}` points by level 90; unlock schedule `level (points)`: `{levels}`.")
    return lines or ["- No purchasable point currency is attached to the nodes in this reference."], labels


def generate_references(snapshot_path: Path, feature_registry: Path, planning_notes: Path, output: Path) -> Path:
    snapshot = _load_snapshot(snapshot_path)
    registry = json.loads(feature_registry.read_text(encoding="utf-8"))
    notes = json.loads(planning_notes.read_text(encoding="utf-8"))
    output.mkdir(parents=True, exist_ok=True)
    # Feature references are hand-authored contract documents. Copy them into
    # an alternate output tree when requested; never regenerate their content.
    manual_features = Path(__file__).resolve().parents[2] / "plugins" / "azeroth-talent-forge" / "skills" / "talents" / "references" / "features"
    for feature in registry:
        source = manual_features / f"{feature['id']}.md"
        target = output / "features" / source.name
        if not source.is_file():
            raise ReferenceGenerationError(f"missing hand-authored feature reference: {source}")
        if source.resolve() != target.resolve():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    _write(
        output / "internals" / "data-model.md",
        "# Local graph data model\n\n"
        "`talents.lbdb` is a read-only Ladybug property graph generated from the pinned Retail DB2 snapshot. It is the runtime authority; Markdown files explain the same facts and are not parsed at runtime.\n\n"
        "## Main nodes and relationships\n\n"
        "- `Class -> Spec`; a spec serializes its ordered `TraitNode` slots through `SERIALIZES`.\n"
        "- `Tree -> TraitNode -> Entry -> Definition`; a definition holds the localized spell name, description, and effect text.\n"
        "- `TraitNode -COSTS-> Currency -UNLOCKS-> CurrencySource`; every purchased rank is charged to its own internal point pool and that pool's exact level schedule.\n"
        "- `Spec -GRANTS-> TraitNode`; a source-defined free rank reduces the charged ranks for that node without creating a user purchase.\n"
        "- `REQUIRED_FOR`, `SUFFICIENT_FOR`, and `MUTUALLY_EXCLUSIVE` encode topology restrictions.\n\n"
        "Numeric Blizzard IDs are canonical foreign keys. User builds stay in memory; the asset is never modified by import, comparison, modification, or generation.\n",
    )
    _write(
        output / "internals" / "import-format.md",
        "# Blizzard import/export format\n\n"
        "The local codec decodes the Retail talent bitstream: serialization version, specialization ID, tree-hash field, then the spec's stored ascending node-ID order. Each selected slot records ranks and, for selection nodes, a choice marker and choice index.\n\n"
        "A non-zero tree hash must match the bundled build. A zero tree hash is accepted under Blizzard's third-party policy, but cannot prove the client patch that produced it. Zero-only tail bits may be omitted. The decoder also preserves an accepted legacy missing first-choice marker on unchanged re-export; edits emit the current marker form.\n\n"
        "Import proves only structural compatibility with this local graph. Validation additionally checks topology and the requested level's independent point pools. Export returns a Blizzard-compatible string and a Wowhead share URL without making a network request.\n",
    )
    classes = {item["id"]: item for item in snapshot.get("classes", [])}
    specs = {item["id"]: item for item in snapshot.get("specs", [])}
    trees = {item["id"]: item for item in snapshot.get("trees", [])}
    subtrees = snapshot.get("subtrees", [])
    nodes = {item["id"]: item for item in snapshot.get("nodes", [])}
    definitions = {item["id"]: item for item in snapshot.get("definitions", [])}
    entries = snapshot.get("entries", [])
    costs_by_node: dict[int, list[dict[str, Any]]] = {}
    conditions_by_node: dict[int, list[dict[str, Any]]] = {}
    conditions_by_entry: dict[int, list[dict[str, Any]]] = {}
    incoming_edges: dict[int, list[dict[str, Any]]] = {}
    effects_by_definition: dict[int, list[dict[str, Any]]] = {}
    for item in snapshot.get("costs", []):
        costs_by_node.setdefault(item["node_id"], []).append(item)
    for item in snapshot.get("conditions", []):
        if item.get("node_id"):
            conditions_by_node.setdefault(item["node_id"], []).append(item)
        if item.get("entry_id"):
            conditions_by_entry.setdefault(item["entry_id"], []).append(item)
    for item in snapshot.get("edges", []):
        incoming_edges.setdefault(item["target"], []).append(item)
    for item in snapshot.get("effects", []):
        effects_by_definition.setdefault(item["definition_id"], []).append(item)
    for class_record in classes.values():
        class_slug = class_record.get("slug") or CLASS_SLUGS.get(class_record["name"], _slug(class_record["name"]))
        class_dir = output / "classes" / class_slug
        class_specs = [spec for spec in specs.values() if spec.get("class_id") == class_record["id"]]
        overview = [
            f"# {class_record['name']}", "", "Reviewed build: `12.1.0.69404`", f"Class ID: `{class_record['id']}`", "",
            "## How to use this reference", "", "Read the matching feature contract first, then inspect a string to identify its specialization. Use Entry IDs from the spec or hero catalog for modification and generation.",
            "", "## Specs and roles", "",
        ]
        for spec in sorted(class_specs, key=lambda item: item["id"]):
            overview.append(f"- `{spec['id']}` {spec['name']} ({spec.get('role', 'unknown')})")
        class_tree_ids = {tree["id"] for tree in trees.values() if tree.get("class_id") == class_record["id"]}
        class_subtrees = [item for item in subtrees if item.get("tree_id") in class_tree_ids and item.get("name")]
        class_node_ids = {node["id"] for node in nodes.values() if node.get("class_id") == class_record["id"]}
        overview += ["", "## Point pools and level schedules", "", "The bold label is the in-game planning pool inferred from its tree placement. The numeric value is Blizzard's `TraitCurrencyID`, retained because the local graph uses it to validate exact costs and level unlocks.", ""]
        currency_lines, currency_labels = _currency_schedule(snapshot, class_node_ids, nodes, {item["id"]: item for item in subtrees}, specs)
        overview += currency_lines
        overview += ["", "## Hero subtrees", ""]
        overview += [f"- `{item['id']}` **{item['name']}** — {item.get('description') or 'No localized description.'}" for item in class_subtrees] or ["No hero subtree records are present in this snapshot."]
        overview += ["", "## Goal vocabulary", "", "single-target, cleave, aoe, survivability, utility, control, mobility, comfort, leveling.", "", "## Limits", "", "This reference describes source facts and trade-offs; it does not claim a best build.", ""]
        _write(class_dir / "overview.md", "\n".join(overview))
        class_entries = []
        for entry in entries:
            node = nodes.get(entry.get("node_id"))
            definition = definitions.get(entry.get("definition_id"))
            tree = trees.get(node.get("tree_id")) if node else None
            if node and definition and tree and (tree.get("class_id") == class_record["id"] or tree.get("spec_id") in {spec["id"] for spec in class_specs}):
                class_entries.append((entry, node, definition, tree))
        class_entries.sort(key=lambda item: (item[1].get("y", 0), item[1].get("x", 0), item[1]["id"], item[0].get("ordinal", 0), item[0]["id"]))
        block_args = (notes, costs_by_node, conditions_by_node, conditions_by_entry, incoming_edges, effects_by_definition, currency_labels)
        _write(class_dir / "class-tree.md", f"# {class_record['name']} class tree\n\nReviewed build: `12.1.0.69404`\n\nThis catalog contains shared class-tree facts. For budget schedules, see `overview.md`.\n\n" + "".join(_talent_block(*item, *block_args) for item in class_entries if item[3].get("kind") == "class"))
        for spec in sorted(class_specs, key=lambda item: item["id"]):
            spec_entries = [item for item in class_entries if spec["id"] in item[1].get("spec_ids", []) or item[3].get("spec_id") == spec["id"]]
            content = [f"# {spec['name']}", "", f"Reviewed build: `12.1.0.69404`", f"Spec ID: `{spec['id']}`", f"Role: `{spec.get('role', 'unknown')}`", "", "Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.", "", "## Talents", ""]
            content.append("".join(_talent_block(*item, *block_args) for item in spec_entries) or "No talent entries are present in this snapshot.\n")
            _write(class_dir / f"{_slug(spec['name'])}.md", "\n".join(content))
        for subtree in sorted(class_subtrees, key=lambda item: item["id"]):
            subtree_entries = [item for item in class_entries if item[1].get("subtree_id") == subtree["id"]]
            hero = [f"# {subtree['name']}", "", "Reviewed build: `12.1.0.69404`", f"Hero subtree ID: `{subtree['id']}`", f"Description: {subtree.get('description') or 'No localized description is present in the source.'}", "", "## Hero talents", ""]
            hero.append("".join(_talent_block(*item, *block_args) for item in subtree_entries) or "No hero talent entries are present in this snapshot.\n")
            _write(class_dir / f"hero-{_slug(subtree['name'])}.md", "\n".join(hero))
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", type=Path, required=True)
    parser.add_argument("--feature-registry", type=Path, required=True)
    parser.add_argument("--planning-notes", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    generate_references(args.snapshot, args.feature_registry, args.planning_notes, args.output)
