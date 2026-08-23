"""Normalize exact-build source payloads into a deterministic talent snapshot."""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class NormalizationError(RuntimeError):
    """Raised when source data cannot prove a coherent exact-build snapshot."""


@dataclass(frozen=True)
class TableRows:
    kind: str
    rows: tuple[dict[str, str], ...]


def _integer(row: dict[str, str], *names: str, default: int | None = None) -> int | None:
    lowered = {key.lower(): value for key, value in row.items()}
    for name in names:
        value = lowered.get(name.lower())
        if value not in (None, ""):
            try:
                return int(value, 0)
            except ValueError as exc:
                raise NormalizationError(f"non-numeric {name}: {value}") from exc
    return default


def _text(row: dict[str, str], *names: str) -> str:
    lowered = {key.lower(): value for key, value in row.items()}
    for name in names:
        value = lowered.get(name.lower())
        if value:
            return value.strip()
    return ""


def _read_csv(path: Path, kind: str) -> TableRows:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = tuple(dict(row) for row in csv.DictReader(stream))
    return TableRows(kind, rows)


def _load_receipts(root: Path, build: str, locale: str) -> dict[str, tuple[Path, dict[str, Any]]]:
    receipt_path = root / "receipts.json"
    if not receipt_path.is_file():
        raise NormalizationError("source bundle lacks receipts.json")
    try:
        receipts = json.loads(receipt_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise NormalizationError("receipts.json is not valid JSON") from exc
    tables: dict[str, tuple[Path, dict[str, Any]]] = {}
    for receipt in receipts:
        if receipt.get("game_build") != build or receipt.get("locale") != locale:
            raise NormalizationError(f"source receipt build/locale mismatch: {receipt.get('kind')}")
        if receipt.get("parser_version") != 1 or receipt.get("http_status") != 200:
            raise NormalizationError(f"invalid source receipt: {receipt.get('kind')}")
        payload = Path(receipt.get("path", ""))
        if not payload.is_file() or payload.parent.resolve() != root.resolve():
            raise NormalizationError(f"receipt payload is outside bundle: {payload}")
        if hashlib.sha256(payload.read_bytes()).hexdigest() != receipt.get("content_sha256"):
            raise NormalizationError(f"source hash mismatch: {receipt.get('kind')}")
        kind = str(receipt.get("kind", ""))
        if kind in tables:
            raise NormalizationError(f"duplicate source table: {kind}")
        tables[kind] = (payload, receipt)
    return tables


def _table(tables: dict[str, tuple[Path, dict[str, Any]]], kind: str) -> TableRows:
    item = tables.get(kind)
    if item is None:
        return TableRows(kind, ())
    return _read_csv(item[0], kind)


def _verify_dbd_payload(tables: dict[str, tuple[Path, dict[str, Any]]], build: str) -> None:
    for kind, (path, _receipt) in tables.items():
        if not kind.endswith(".dbd"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if build not in text:
            raise NormalizationError(f"DB2 definition lacks target build: {kind}")


def _records_for_classes(rows: TableRows) -> list[dict[str, Any]]:
    records = []
    seen: set[int] = set()
    for row in rows.rows:
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError(f"invalid or duplicate class ID in {rows.kind}")
        seen.add(identifier)
        records.append({"id": identifier, "name": _text(row, "Name", "Name_lang")})
    return sorted(records, key=lambda item: item["id"])


def _records_for_specs(rows: TableRows) -> list[dict[str, Any]]:
    records = []
    seen: set[int] = set()
    for row in rows.rows:
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError(f"invalid or duplicate spec ID in {rows.kind}")
        seen.add(identifier)
        records.append(
            {
                "id": identifier,
                "name": _text(row, "Name", "Name_lang"),
                "class_id": _integer(row, "ClassID", "ClassID"),
                "role": _text(row, "Role", "Role_lang"),
            }
        )
    return sorted(records, key=lambda item: item["id"])


def _records_for_nodes(tables: dict[str, tuple[Path, dict[str, Any]]]) -> tuple[list[dict[str, Any]], dict[str, list[int]]]:
    tree_metadata = {
        _integer(row, "ID"): row
        for row in _table(tables, "TraitTree").rows
        if _integer(row, "ID") is not None
    }
    nodes: list[dict[str, Any]] = []
    seen: set[int] = set()
    for row in _table(tables, "TraitNode").rows:
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError("duplicate or missing TraitNode ID")
        seen.add(identifier)
        nodes.append(
            {
                "id": identifier,
                "tree_id": _integer(row, "TraitTreeID", "TreeID"),
                "x": _integer(row, "PosX", "X", default=0),
                "y": _integer(row, "PosY", "Y", default=0),
                "type": _integer(row, "Type", default=0),
            }
        )
    nodes.sort(key=lambda item: item["id"])
    orders: dict[str, list[int]] = {}
    for node in nodes:
        if node["tree_id"] is not None:
            tree_row = tree_metadata.get(node["tree_id"], {})
            order_key = _integer(tree_row, "SpecID", "SpecializationID") or node["tree_id"]
            orders.setdefault(str(order_key), []).append(node["id"])
    for order in orders.values():
        if len(order) != len(set(order)):
            raise NormalizationError("duplicate codec node ordinal")
        order.sort()
    return nodes, orders


def _records_for_entries(tables: dict[str, tuple[Path, dict[str, Any]]]) -> list[dict[str, Any]]:
    entries = []
    seen: set[int] = set()
    for ordinal, row in enumerate(_table(tables, "TraitNodeEntry").rows):
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError("duplicate or missing TraitNodeEntry ID")
        seen.add(identifier)
        entries.append(
            {
                "id": identifier,
                "node_id": _integer(row, "TraitNodeID", "NodeID"),
                "definition_id": _integer(row, "TraitDefinitionID", "DefinitionID"),
                "max_ranks": _integer(row, "MaxRanks", default=1),
                "ordinal": ordinal,
            }
        )
    return sorted(entries, key=lambda item: item["id"])


def _records_for_definitions(tables: dict[str, tuple[Path, dict[str, Any]]]) -> list[dict[str, Any]]:
    spells = {
        _integer(row, "ID"): row
        for row in _table(tables, "Spell").rows
        if _integer(row, "ID") is not None
    }
    definitions = []
    seen: set[int] = set()
    for row in _table(tables, "TraitDefinition").rows:
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError("duplicate or missing TraitDefinition ID")
        seen.add(identifier)
        spell_id = _integer(row, "SpellID", "SpellID[0]")
        spell = spells.get(spell_id, {})
        name = _text(row, "OverrideName_lang", "OverrideName", "Name_lang") or _text(spell, "Name_lang", "Name")
        description = _text(row, "OverrideDescription_lang", "OverrideDescription", "Description_lang") or _text(spell, "Description_lang", "Description")
        if not name or not description:
            raise NormalizationError(f"missing source text for definition {identifier}")
        definitions.append(
            {
                "id": identifier,
                "spell_id": spell_id,
                "name": name,
                "description": description,
                "effect": description,
                "source": "db2",
            }
        )
    return sorted(definitions, key=lambda item: item["id"])


def normalize_bundle(root: Path, build: str, locale: str, output: Path) -> Path:
    root = root.resolve()
    tables = _load_receipts(root, build, locale)
    _verify_dbd_payload(tables, build)
    classes = _records_for_classes(_table(tables, "ChrClasses"))
    specs = _records_for_specs(_table(tables, "ChrSpecialization"))
    nodes, codec_orders = _records_for_nodes(tables)
    entries = _records_for_entries(tables)
    definitions = _records_for_definitions(tables)
    node_ids = {node["id"] for node in nodes}
    definition_ids = {definition["id"] for definition in definitions}
    for entry in entries:
        if entry["node_id"] not in node_ids or entry["definition_id"] not in definition_ids:
            raise NormalizationError(f"entry {entry['id']} references missing graph data")
        if entry["max_ranks"] is None or entry["max_ranks"] < 1:
            raise NormalizationError(f"entry {entry['id']} has invalid max ranks")
    receipts = json.loads((root / "receipts.json").read_text(encoding="utf-8"))
    snapshot = {
        "schema_version": 1,
        "product": "wow",
        "channel": "retail-live",
        "game_build": build,
        "locale": locale,
        "classes": classes,
        "specs": specs,
        "trees": [],
        "nodes": nodes,
        "entries": entries,
        "definitions": definitions,
        "effects": [],
        "edges": [],
        "conditions": [],
        "currencies": [],
        "codec_orders": codec_orders,
        "presets": [],
        "source_receipts": sorted(receipts, key=lambda item: (item["kind"], item["url"])),
    }
    canonical = json.dumps(snapshot, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as raw:
        with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as stream:
            stream.write((canonical + "\n").encode("utf-8"))
    return output


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--build", required=True)
    parser.add_argument("--locale", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    normalize_bundle(args.input, args.build, args.locale, args.output)
