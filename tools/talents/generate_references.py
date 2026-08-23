"""Generate feature and class Markdown from one normalized talent snapshot."""

from __future__ import annotations

import gzip
import json
import re
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


def _talent_block(entry: dict[str, Any], node: dict[str, Any], definition: dict[str, Any], tree: dict[str, Any], notes: dict[str, Any]) -> str:
    tags = notes.get(str(entry["id"]), {}).get("tags", []) if isinstance(notes.get(str(entry["id"]), {}), dict) else []
    tag_text = ", ".join(tags) if tags else "source-derived only"
    return "\n".join(
        [
            f"### {definition['name']}",
            f"- Node ID: `{node['id']}`",
            f"- Entry ID: `{entry['id']}`",
            f"- Definition ID: `{definition['id']}`",
            f"- Spell ID: `{definition.get('spell_id', 0)}`",
            f"- Tree ID: `{tree.get('id', node.get('tree_id', 0))}`; tree kind: `{tree.get('kind', 'unknown')}`",
            f"- Maximum ranks: `{entry.get('max_ranks', 1)}`; entry ordinal: `{entry.get('ordinal', 0)}`",
            f"- Description: {definition['description']}",
            f"- Effect: {definition.get('effect', definition['description'])}",
            f"- Planning tags: `{tag_text}`",
            f"- Source: `{definition.get('source', 'normalized snapshot')}`; build: `12.1.0.69404`",
            "",
        ]
    )


def generate_references(snapshot_path: Path, feature_registry: Path, planning_notes: Path, output: Path) -> Path:
    snapshot = _load_snapshot(snapshot_path)
    registry = json.loads(feature_registry.read_text(encoding="utf-8"))
    notes = json.loads(planning_notes.read_text(encoding="utf-8"))
    output.mkdir(parents=True, exist_ok=True)
    for feature in registry:
        feature_id = feature["id"]
        text = "\n".join(
            [
                "---", f"feature: {feature_id}", "---", "",
                f"# {feature['title']}", "",
                f"Command: `{feature['command']}`", "",
                "Runtime is offline and uses the explicitly selected bundled Retail build.",
                "Zero-hash inputs are legal but do not prove their originating patch.",
                "Errors and recovery details are returned as stable JSON codes.", "",
                "## Limits", "", "This reference does not claim current-meta or a universally best build.", "",
            ]
        )
        _write(output / "features" / f"{feature_id}.md", text)
    _write(output / "internals" / "data-model.md", "# Data model\n\nNumeric Blizzard IDs are canonical. Graph facts are immutable and user builds remain in memory.\n")
    _write(output / "internals" / "import-format.md", "# Import format\n\nSerialization version, specialization ID, zero/non-zero tree-hash field, and ascending node-ID codec order are validated before use.\n")
    classes = {item["id"]: item for item in snapshot.get("classes", [])}
    specs = {item["id"]: item for item in snapshot.get("specs", [])}
    trees = {item["id"]: item for item in snapshot.get("trees", [])}
    nodes = {item["id"]: item for item in snapshot.get("nodes", [])}
    definitions = {item["id"]: item for item in snapshot.get("definitions", [])}
    entries = snapshot.get("entries", [])
    for class_record in classes.values():
        class_slug = class_record.get("slug") or CLASS_SLUGS.get(class_record["name"], _slug(class_record["name"]))
        class_dir = output / "classes" / class_slug
        class_specs = [spec for spec in specs.values() if spec.get("class_id") == class_record["id"]]
        overview = [f"# {class_record['name']}", "", "Reviewed build: `12.1.0.69404`", f"Class ID: `{class_record['id']}`", "", "## Specs and roles", ""]
        for spec in sorted(class_specs, key=lambda item: item["id"]):
            overview.append(f"- `{spec['id']}` {spec['name']} ({spec.get('role', 'unknown')})")
        overview += ["", "## Hero subtrees", "", "No hero subtree records are present in this snapshot.", "", "## Goal vocabulary", "", "single-target, cleave, aoe, survivability, utility, control, mobility, comfort, leveling.", "", "## Limits", "", "This reference describes source facts and trade-offs; it does not claim a best build.", ""]
        _write(class_dir / "overview.md", "\n".join(overview))
        class_entries = []
        for entry in entries:
            node = nodes.get(entry.get("node_id"))
            definition = definitions.get(entry.get("definition_id"))
            tree = trees.get(node.get("tree_id")) if node else None
            if node and definition and tree and (tree.get("spec_id") in {spec["id"] for spec in class_specs}):
                class_entries.append((entry, node, definition, tree))
        _write(class_dir / "class-tree.md", f"# {class_record['name']} class tree\n\nReviewed build: `12.1.0.69404`\n\nNo class-tree entries in this fixture unless listed below.\n\n" + "".join(_talent_block(*item, notes) for item in class_entries if item[3].get("kind") == "class"))
        for spec in sorted(class_specs, key=lambda item: item["id"]):
            spec_entries = [item for item in class_entries if item[3].get("spec_id") == spec["id"]]
            content = [f"# {spec['name']}", "", f"Reviewed build: `12.1.0.69404`", f"Spec ID: `{spec['id']}`", f"Role: `{spec.get('role', 'unknown')}`", "", "## Talents", ""]
            content.append("".join(_talent_block(*item, notes) for item in spec_entries) or "No talent entries are present in this snapshot.\n")
            _write(class_dir / f"{_slug(spec['name'])}.md", "\n".join(content))
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
