"""Compile a normalized Retail snapshot into a read-only Ladybug asset."""

from __future__ import annotations

import gzip
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from typing import Any, Iterable

import ladybug


class AssetCompileError(RuntimeError):
    """Raised when a snapshot cannot be compiled or verified."""


SCHEMA = Path(__file__).with_name("schema.cypher")


def _read_snapshot(path: Path) -> dict[str, Any]:
    try:
        with gzip.open(path, "rt", encoding="utf-8") as stream:
            snapshot = json.load(stream)
    except (OSError, json.JSONDecodeError) as exc:
        raise AssetCompileError(f"invalid normalized snapshot: {path}") from exc
    if snapshot.get("schema_version") != 1 or snapshot.get("product") != "wow" or snapshot.get("channel") != "retail-live":
        raise AssetCompileError("snapshot is not a Retail schema-1 snapshot")
    if snapshot.get("game_build") != "12.1.0.69404" or snapshot.get("locale") != "enUS":
        raise AssetCompileError("snapshot does not match the pinned initial Retail build")
    return snapshot


def _hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _hash_tree(root: Path) -> str:
    digest = hashlib.sha256()
    if not root.is_dir():
        return digest.hexdigest()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def _literal(value: Any) -> str:
    if value is None:
        return "0"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def _create_node(connection: ladybug.Connection, label: str, values: dict[str, Any]) -> None:
    properties = ", ".join(f"{key}: {_literal(value)}" for key, value in values.items())
    connection.execute(f"CREATE (n:{label} {{{properties}}})")


def _create_edge(connection: ladybug.Connection, relation: str, source_label: str, source_id: Any, target_label: str, target_id: Any, properties: dict[str, Any] | None = None) -> None:
    prop_text = ""
    if properties:
        prop_text = " {" + ", ".join(f"{key}: {_literal(value)}" for key, value in properties.items()) + "}"
    query = f"MATCH (a:{source_label} {{id: {_literal(source_id)}}}), (b:{target_label} {{id: {_literal(target_id)}}}) CREATE (a)-[:{relation}{prop_text}]->(b)"
    connection.execute(query)


def _create_schema(connection: ladybug.Connection) -> None:
    for statement in SCHEMA.read_text(encoding="utf-8").split(";"):
        statement = statement.strip()
        if statement:
            connection.execute(statement)


def _compile_graph(snapshot: dict[str, Any], database_path: Path) -> None:
    database = ladybug.Database(str(database_path))
    connection = ladybug.Connection(database)
    try:
        _create_schema(connection)
        _create_node(connection, "Snapshot", {"id": "snapshot", "game_build": snapshot["game_build"], "locale": snapshot["locale"], "product": snapshot["product"], "channel": snapshot["channel"]})
        for item in snapshot.get("classes", []):
            _create_node(connection, "Class", {"id": item["id"], "slug": item.get("slug", str(item["name"]).lower().replace(" ", "-")), "name": item["name"]})
        for item in snapshot.get("specs", []):
            _create_node(connection, "Spec", {"id": item["id"], "class_id": item.get("class_id", 0), "role": item.get("role", ""), "name": item["name"]})
        for item in snapshot.get("trees", []):
            _create_node(connection, "Tree", {"id": item["id"], "kind": item.get("kind", ""), "spec_id": item.get("spec_id", 0) or 0})
        orders = snapshot.get("codec_orders", {})
        tree_to_spec = {item["id"]: item.get("spec_id") for item in snapshot.get("trees", [])}
        for item in snapshot.get("nodes", []):
            tree_id = item.get("tree_id", 0) or 0
            spec_id = item.get("spec_id") or tree_to_spec.get(tree_id)
            ordinal = next((index for index, node_id in enumerate(orders.get(str(spec_id), [])) if node_id == item["id"]), 0)
            _create_node(connection, "TraitNode", {"id": item["id"], "tree_id": tree_id, "subtree_id": item.get("subtree_id", 0) or 0, "type": item.get("type", 0) or 0, "x": item.get("x", 0) or 0, "y": item.get("y", 0) or 0, "codec_ordinal": item.get("codec_ordinal", ordinal)})
        for item in snapshot.get("entries", []):
            _create_node(connection, "Entry", {"id": item["id"], "node_id": item.get("node_id", 0) or 0, "definition_id": item.get("definition_id", 0) or 0, "ordinal": item.get("ordinal", 0), "max_ranks": item.get("max_ranks", 1)})
        for item in snapshot.get("definitions", []):
            _create_node(connection, "Definition", {"id": item["id"], "spell_id": item.get("spell_id", 0) or 0, "name": item["name"], "description": item["description"], "effect": item.get("effect", item["description"]), "source": item.get("source", "")})
        for item in snapshot.get("effects", []):
            _create_node(connection, "SpellEffect", {"id": item["id"], "definition_id": item.get("definition_id", 0) or 0, "effect_index": item.get("effect_index", 0), "effect_type": item.get("effect_type", ""), "amount": item.get("amount", 0.0)})
        for item in snapshot.get("currencies", []):
            _create_node(connection, "Currency", {"id": item["id"], "kind": item.get("kind", "")})
        for item in snapshot.get("presets", []):
            _create_node(connection, "Preset", {"id": item["preset_id"], "label": item.get("label", ""), "category": item.get("category", ""), "code": item["code"], "spec_id": item.get("spec_id", 0) or 0, "hero_subtree_id": item.get("hero_subtree_id", 0) or 0, "source_url": item.get("source_url", ""), "source_name": item.get("source_name", ""), "claimed_patch": item.get("claimed_patch", "") or ""})
        class_ids = {item["id"] for item in snapshot.get("classes", [])}
        spec_ids = {item["id"] for item in snapshot.get("specs", [])}
        tree_ids = {item["id"] for item in snapshot.get("trees", [])}
        node_ids = {item["id"] for item in snapshot.get("nodes", [])}
        entry_ids = {item["id"] for item in snapshot.get("entries", [])}
        definition_ids = {item["id"] for item in snapshot.get("definitions", [])}
        for item in snapshot.get("specs", []):
            if item.get("class_id") in class_ids:
                _create_edge(connection, "HAS_SPEC", "Class", item["class_id"], "Spec", item["id"])
        for item in snapshot.get("trees", []):
            if item.get("spec_id") in spec_ids:
                _create_edge(connection, "USES_SPEC_TREE", "Spec", item["spec_id"], "Tree", item["id"])
        for item in snapshot.get("nodes", []):
            if item.get("tree_id") in tree_ids:
                _create_edge(connection, "HAS_NODE", "Tree", item["tree_id"], "TraitNode", item["id"])
        for item in snapshot.get("entries", []):
            if item.get("node_id") in node_ids:
                _create_edge(connection, "HAS_ENTRY", "TraitNode", item["node_id"], "Entry", item["id"])
            if item.get("definition_id") in definition_ids:
                _create_edge(connection, "USES_DEFINITION", "Entry", item["id"], "Definition", item["definition_id"])
        for item in snapshot.get("presets", []):
            if item.get("spec_id") in spec_ids:
                _create_edge(connection, "FOR_SPEC", "Preset", item["preset_id"], "Spec", item["spec_id"])
        connection.close()
    finally:
        database.close()


def compile_assets(snapshot_path: Path, output: Path, references: Path) -> dict[str, Any]:
    snapshot = _read_snapshot(snapshot_path)
    output = output.resolve()
    if output.exists() and any(output.iterdir()):
        raise AssetCompileError(f"immutable asset output is not empty: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=output.parent) as temp_dir:
        temp_output = Path(temp_dir)
        database_path = temp_output / "talents.lbdb"
        _compile_graph(snapshot, database_path)
        presets_path = temp_output / "presets.json"
        presets_path.write_text(json.dumps(snapshot.get("presets", []), ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        manifest = {
            "asset_schema_version": 1,
            "product": "wow",
            "channel": "retail-live",
            "game_version": snapshot["game_build"].rsplit(".", 1)[0],
            "game_build": snapshot["game_build"],
            "locale": snapshot["locale"],
            "serialization_versions": [2],
            "codec_node_order": "ascending-node-id",
            "export_tree_hash": "zero",
            "sources": snapshot.get("source_receipts", []),
            "normalized_sha256": _hash_file(snapshot_path),
            "graph": {"engine": "ladybug", "engine_version": ladybug.__version__, "file": "talents.lbdb", "sha256": _hash_file(database_path)},
            "presets": {"file": "presets.json", "sha256": _hash_file(presets_path)},
            "references_sha256": _hash_tree(references),
            "classes": snapshot.get("classes", []),
            "specs": snapshot.get("specs", []),
        }
        (temp_output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        output.mkdir(parents=True, exist_ok=False)
        for item in temp_output.iterdir():
            shutil.copy2(item, output / item.name)
    return manifest


def verify_assets(database: Path, manifest_path: Path, presets_path: Path, references: Path) -> list[str]:
    errors: list[str] = []
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("graph", {}).get("sha256") != _hash_file(database):
        errors.append("graph hash mismatch")
    if manifest.get("presets", {}).get("sha256") != _hash_file(presets_path):
        errors.append("preset hash mismatch")
    if manifest.get("references_sha256") != _hash_tree(references):
        errors.append("reference hash mismatch")
    return errors


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    compile_parser = subparsers.add_parser("compile")
    compile_parser.add_argument("snapshot", type=Path)
    compile_parser.add_argument("output", type=Path)
    compile_parser.add_argument("references", type=Path)
    verify_parser = subparsers.add_parser("verify")
    verify_parser.add_argument("database", type=Path)
    verify_parser.add_argument("manifest", type=Path)
    verify_parser.add_argument("presets", type=Path)
    verify_parser.add_argument("references", type=Path)
    args = parser.parse_args()
    if args.command == "compile":
        compile_assets(args.snapshot, args.output, args.references)
    else:
        errors = verify_assets(args.database, args.manifest, args.presets, args.references)
        if errors:
            raise SystemExit("; ".join(errors))
