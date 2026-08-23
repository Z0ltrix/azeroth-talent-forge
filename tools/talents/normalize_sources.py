"""Normalize exact-build source payloads into a deterministic talent snapshot."""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
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


def _wowhead_payload(tables: dict[str, tuple[Path, dict[str, Any]]]) -> tuple[set[int], dict[int, dict[str, Any]], dict[int, int], dict[int, set[int]], dict[int, int], dict[int, list[int]], dict[int, list[int]]]:
    """Read Wowhead's exact-build talent payload as a class/spec allow-list and fallback text."""
    item = tables.get("wowhead-talents")
    if item is None:
        return set(), {}, {}, {}, {}, {}, {}
    text = item[0].read_text(encoding="utf-8")
    trees_match = re.search(r'WH\.setPageData\("wow\.talentCalcDragonflight\.live\.trees",(\[.*?\])\);', text)
    if not trees_match:
        raise NormalizationError("Wowhead payload lacks talent trees")
    try:
        trees = json.loads(trees_match.group(1))
    except json.JSONDecodeError as exc:
        raise NormalizationError("Wowhead talent trees are not valid JSON") from exc
    node_ids: set[int] = set()
    node_classes: dict[int, int] = {}
    node_specs: dict[int, set[int]] = {}
    node_types: dict[int, int] = {}
    codec_orders: dict[int, list[int]] = {}
    node_definitions: dict[int, list[int]] = {}
    definitions: dict[int, dict[str, Any]] = {}
    for tree in trees:
        tree_nodes: list[tuple[int, int, set[int]]] = []
        for spec_nodes in tree.get("talents", {}).values():
            for node in spec_nodes:
                if isinstance(node.get("node"), int):
                    node_ids.add(node["node"])
                    if isinstance(node.get("type"), int):
                        node_types[node["node"]] = node["type"]
                    specs = set(node.get("shownForSpecs", ())) | set(node.get("defaultSpecs", ()))
                    for spell in node.get("spells", ()):
                        if isinstance(spell.get("definition"), int):
                            node_definitions.setdefault(node["node"], []).append(spell["definition"])
                        specs |= set(spell.get("shownForSpecs", ())) | set(spell.get("defaultSpecs", ()))
                    if specs:
                        node_specs.setdefault(node["node"], set()).update(specs)
                    tree_nodes.append((int(node.get("cell", 0)), node["node"], specs))
                for spell in node.get("spells", ()):  # spell text is the authoritative fallback
                    definition = spell.get("definition")
                    if not isinstance(definition, int):
                        continue
                    name = str(spell.get("name") or "").strip()
                    description = str(spell.get("descriptionSearch") or spell.get("description") or "").strip()
                    if name and description and definition not in definitions:
                        definitions[definition] = {
                            "id": definition,
                            "spell_id": spell.get("spell"),
                            "name": name,
                            "description": description,
                            "effect": description,
                            "source": "wowhead",
                        }
        # Keep the payload order available for diagnostics. Blizzard's live
        # codec explicitly serializes C_Traits.GetTreeNodes() in ascending
        # node-ID order; normalize_bundle applies that authoritative rule
        # after combining class/spec/hero membership.
        tree_nodes.sort(key=lambda item: (item[0], item[1]))
        tree_specs = set(spec for _cell, _node, specs in tree_nodes for spec in specs)
        tree_id = int(tree.get("id", 0))
        if 1 <= tree_id <= 13:
            candidates = tree_specs
        else:
            candidates = tree_specs or ({tree_id} if tree_id < 2000 else set())
        for spec in candidates:
            codec_orders.setdefault(spec, []).extend(node for _cell, node, _specs in tree_nodes)
    nodes_match = re.search(r'WH\.setPageData\("wow\.talentCalcDragonflight\.live\.nodes",(\{.*?\})\);', text)
    if nodes_match:
        try:
            node_index = json.loads(nodes_match.group(1))
            for class_id, payload in node_index.items():
                for node_id in payload.get("nodes", ()):
                    node_classes[int(node_id)] = int(class_id)
        except (ValueError, json.JSONDecodeError):
            raise NormalizationError("Wowhead talent node index is not valid JSON")
    for spec, order in codec_orders.items():
        codec_orders[spec] = list(dict.fromkeys(order))
    return node_ids, definitions, node_classes, node_specs, node_types, codec_orders, node_definitions


def _records_for_classes(rows: TableRows) -> list[dict[str, Any]]:
    records = []
    seen: set[int] = set()
    for row in rows.rows:
        identifier = _integer(row, "ID")
        if identifier is not None and not 1 <= identifier <= 13:
            continue
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
        class_id = _integer(row, "ClassID", "ClassID")
        if class_id is not None and not 1 <= class_id <= 13:
            continue
        if identifier is None or identifier in seen:
            raise NormalizationError(f"invalid or duplicate spec ID in {rows.kind}")
        seen.add(identifier)
        records.append(
            {
                "id": identifier,
                "name": _text(row, "Name", "Name_lang"),
                "class_id": class_id,
                "role": _text(row, "Role", "Role_lang"),
            }
        )
    return sorted(records, key=lambda item: item["id"])


def _records_for_nodes(tables: dict[str, tuple[Path, dict[str, Any]]], allowed_ids: set[int] | None = None) -> tuple[list[dict[str, Any]], dict[str, list[int]]]:
    tree_metadata = {
        _integer(row, "ID"): row
        for row in _table(tables, "TraitTree").rows
        if _integer(row, "ID") is not None
    }
    nodes: list[dict[str, Any]] = []
    seen: set[int] = set()
    for row in _table(tables, "TraitNode").rows:
        identifier = _integer(row, "ID")
        if allowed_ids and identifier not in allowed_ids:
            continue
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
                "subtree_id": _integer(row, "TraitSubTreeID", "SubTreeID", default=0),
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


def _records_for_entries(tables: dict[str, tuple[Path, dict[str, Any]]], allowed_node_ids: set[int] | None = None) -> list[dict[str, Any]]:
    links = {
        _integer(row, "TraitNodeEntryID", "NodeEntryID"): (
            _integer(row, "TraitNodeID", "NodeID"),
            _integer(row, "_Index", "Index", default=0),
        )
        for row in _table(tables, "TraitNodeXTraitNodeEntry").rows
        if _integer(row, "TraitNodeEntryID", "NodeEntryID") is not None
    }
    entries = []
    seen: set[int] = set()
    for ordinal, row in enumerate(_table(tables, "TraitNodeEntry").rows):
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError("duplicate or missing TraitNodeEntry ID")
        if links and identifier not in links:
            continue
        link = links.get(identifier)
        node_id = link[0] if link else _integer(row, "TraitNodeID", "NodeID")
        if allowed_node_ids and node_id not in allowed_node_ids:
            continue
        seen.add(identifier)
        entries.append(
            {
                "id": identifier,
                "node_id": node_id,
                "definition_id": _integer(row, "TraitDefinitionID", "DefinitionID"),
                "max_ranks": _integer(row, "MaxRanks", default=1),
                "ordinal": link[1] if link else ordinal,
            }
        )
    return sorted(entries, key=lambda item: item["id"])


def _records_for_edges(tables: dict[str, tuple[Path, dict[str, Any]]], node_ids: set[int]) -> list[dict[str, int]]:
    """Keep DB2 availability edges whose endpoints are in the exact snapshot."""
    edges = []
    for row in _table(tables, "TraitEdge").rows:
        source = _integer(row, "LeftTraitNodeID", "LeftNodeID")
        target = _integer(row, "RightTraitNodeID", "RightNodeID")
        edge_type = _integer(row, "Type", default=0)
        if source in node_ids and target in node_ids and edge_type in {0, 2, 3, 4}:
            edges.append({"source": source, "target": target, "type": edge_type})
    return sorted(edges, key=lambda item: (item["type"], item["source"], item["target"]))


def _deduplicated_grants(conditions: list[dict[str, Any]]) -> list[dict[str, int]]:
    """Return the strongest free rank granted to each spec/node pair.

    DB2 may expose one condition through both a group and the resolved node.
    Those are alternate references to the same grant, not cumulative ranks.
    """
    grants: dict[tuple[int, int], dict[str, int]] = {}
    for condition in conditions:
        node_id = int(condition["node_id"])
        ranks = int(condition["granted_ranks"])
        if not node_id or not ranks:
            continue
        for spec_id in condition["spec_ids"]:
            candidate = {
                "spec_id": int(spec_id),
                "node_id": node_id,
                "ranks": ranks,
                "source_condition_id": int(condition["source_condition_id"]),
            }
            key = (candidate["spec_id"], node_id)
            current = grants.get(key)
            if current is None or (candidate["ranks"], -candidate["source_condition_id"]) > (current["ranks"], -current["source_condition_id"]):
                grants[key] = candidate
    return [grants[key] for key in sorted(grants)]


def _records_for_constraints(
    tables: dict[str, tuple[Path, dict[str, Any]]],
    tree_ids: set[int],
    node_ids: set[int],
    entry_ids: set[int],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Resolve DB2 costs, unlock schedules, and gates to playable nodes.

    Trait costs/conditions may target a node directly or arrive through a
    TraitNodeGroup.  Store their resolved node targets so the runtime and the
    Markdown catalog need not reinterpret DB2 relationship tables.
    """
    costs_by_id = {
        identifier: row
        for row in _table(tables, "TraitCost").rows
        if (identifier := _integer(row, "ID")) is not None
    }
    groups = {
        identifier: row
        for row in _table(tables, "TraitNodeGroup").rows
        if (identifier := _integer(row, "ID")) is not None and _integer(row, "TraitTreeID", "TreeID") in tree_ids
    }
    group_nodes: dict[int, set[int]] = {}
    for row in _table(tables, "TraitNodeGroupXTraitNode").rows:
        group_id = _integer(row, "TraitNodeGroupID", "NodeGroupID")
        node_id = _integer(row, "TraitNodeID", "NodeID")
        if group_id in groups and node_id in node_ids:
            group_nodes.setdefault(group_id, set()).add(node_id)

    resolved_costs: set[tuple[int, int, int, str]] = set()

    def add_cost(node_id: int | None, cost_id: int | None, source: str) -> None:
        row = costs_by_id.get(cost_id)
        if node_id not in node_ids or row is None:
            return
        currency_id = _integer(row, "TraitCurrencyID", "CurrencyID")
        amount = _integer(row, "Amount", default=0)
        if currency_id is None or amount is None or amount < 0:
            raise NormalizationError(f"invalid TraitCost {cost_id}")
        resolved_costs.add((node_id, currency_id, amount, source))

    for row in _table(tables, "TraitNodeXTraitCost").rows:
        add_cost(_integer(row, "TraitNodeID", "NodeID"), _integer(row, "TraitCostID", "CostID"), "node")
    for row in _table(tables, "TraitNodeGroupXTraitCost").rows:
        for node_id in group_nodes.get(_integer(row, "TraitNodeGroupID", "NodeGroupID"), set()):
            add_cost(node_id, _integer(row, "TraitCostID", "CostID"), "group")
    entry_to_node = {
        _integer(row, "ID"): _integer(row, "TraitNodeID", "NodeID")
        for row in _table(tables, "TraitNodeEntry").rows
        if _integer(row, "ID") in entry_ids
    }
    for row in _table(tables, "TraitNodeEntryXTraitCost").rows:
        entry_id = _integer(row, "TraitNodeEntryID", "NodeEntryID")
        add_cost(entry_to_node.get(entry_id), _integer(row, "TraitCostID", "CostID"), f"entry:{entry_id}")

    condition_rows = {
        identifier: row
        for row in _table(tables, "TraitCond").rows
        if (identifier := _integer(row, "ID")) is not None
    }
    specs_by_set: dict[int, set[int]] = {}
    for row in _table(tables, "SpecSetMember").rows:
        set_id = _integer(row, "SpecSet", "SpecSetID")
        spec_id = _integer(row, "ChrSpecializationID", "SpecID")
        if set_id is not None and spec_id is not None:
            specs_by_set.setdefault(set_id, set()).add(spec_id)
    condition_targets: dict[int, set[tuple[str, int]]] = {}

    def add_condition_target(condition_id: int | None, source: str, target_id: int | None) -> None:
        if condition_id not in condition_rows or target_id is None:
            return
        condition_targets.setdefault(condition_id, set()).add((source, target_id))

    for row in _table(tables, "TraitNodeXTraitCond").rows:
        node_id = _integer(row, "TraitNodeID", "NodeID")
        if node_id in node_ids:
            add_condition_target(_integer(row, "TraitCondID", "ConditionID"), "node", node_id)
    for row in _table(tables, "TraitNodeGroupXTraitCond").rows:
        for node_id in group_nodes.get(_integer(row, "TraitNodeGroupID", "NodeGroupID"), set()):
            add_condition_target(_integer(row, "TraitCondID", "ConditionID"), "group", node_id)
    for condition_id, row in condition_rows.items():
        tree_id = _integer(row, "TraitTreeID", "TreeID", default=0)
        node_id = _integer(row, "TraitNodeID", "NodeID", default=0)
        entry_id = _integer(row, "TraitNodeEntryID", "NodeEntryID", default=0)
        if node_id in node_ids:
            add_condition_target(condition_id, "node", node_id)
        elif entry_id in entry_ids:
            add_condition_target(condition_id, "entry", entry_id)
        elif tree_id in tree_ids:
            add_condition_target(condition_id, "tree", tree_id)

    conditions = []
    for condition_id, targets in sorted(condition_targets.items()):
        row = condition_rows[condition_id]
        for source, target_id in sorted(targets):
            conditions.append(
                {
                    "id": condition_id if len(targets) == 1 else int(f"{condition_id}{target_id}"),
                    "source_condition_id": condition_id,
                    "source": source,
                    "tree_id": _integer(row, "TraitTreeID", "TreeID", default=0) or 0,
                    "node_id": target_id if source in {"node", "group"} else 0,
                    "entry_id": target_id if source == "entry" else 0,
                    "currency_id": _integer(row, "TraitCurrencyID", "CurrencyID", default=0) or 0,
                    "spec_ids": sorted(specs_by_set.get(_integer(row, "SpecSetID", default=0) or 0, set())),
                    "spent": _integer(row, "SpentAmountRequired", "SpentAmount", default=0) or 0,
                    "level": _integer(row, "RequiredLevel", "PlayerLevel", default=0) or 0,
                    "granted_ranks": _integer(row, "GrantedRanks", default=0) or 0,
                    "type": _integer(row, "CondType", "Type", default=0) or 0,
                }
            )

    tree_currencies = {
        (_integer(row, "TraitTreeID", "TreeID"), _integer(row, "TraitCurrencyID", "CurrencyID"))
        for row in _table(tables, "TraitTreeXTraitCurrency").rows
        if _integer(row, "TraitTreeID", "TreeID") in tree_ids and _integer(row, "TraitCurrencyID", "CurrencyID") is not None
    }
    currency_ids = {currency_id for _node, currency_id, _amount, _source in resolved_costs}
    currency_ids.update(currency_id for _tree, currency_id in tree_currencies if currency_id is not None)
    currency_ids.update(item["currency_id"] for item in conditions if item["currency_id"])
    currency_rows = {
        _integer(row, "ID"): row
        for row in _table(tables, "TraitCurrency").rows
        if _integer(row, "ID") is not None
    }
    currencies = [
        {"id": currency_id, "kind": f"type-{_integer(currency_rows.get(currency_id, {}), 'Type', default=0) or 0}"}
        for currency_id in sorted(currency_ids)
    ]
    currency_sources = [
        {
            "id": identifier,
            "currency_id": currency_id,
            "amount": amount,
            "level": _integer(row, "PlayerLevel", "RequiredLevel", default=0) or 0,
            "order": _integer(row, "OrderIndex", "_Index", default=0) or 0,
        }
        for row in _table(tables, "TraitCurrencySource").rows
        if (identifier := _integer(row, "ID")) is not None
        and (currency_id := _integer(row, "TraitCurrencyID", "CurrencyID")) in currency_ids
        and (amount := _integer(row, "Amount", default=0)) is not None
        and amount > 0
    ]
    return (
        [
            {"node_id": node_id, "currency_id": currency_id, "amount": amount, "source": source}
            for node_id, currency_id, amount, source in sorted(resolved_costs)
        ],
        sorted(conditions, key=lambda item: (item["id"], item["source"])),
        {
            "currencies": currencies,
            "currency_sources": sorted(currency_sources, key=lambda item: (item["currency_id"], item["level"], item["order"], item["id"])),
            "grants": _deduplicated_grants(conditions),
        },
    )


def _records_for_subtrees(tables: dict[str, tuple[Path, dict[str, Any]]], tree_ids: set[int]) -> list[dict[str, Any]]:
    records = []
    for row in _table(tables, "TraitSubTree").rows:
        identifier = _integer(row, "ID")
        tree_id = _integer(row, "TraitTreeID", "TreeID")
        if identifier is None or tree_id not in tree_ids:
            continue
        records.append({
            "id": identifier,
            "tree_id": tree_id,
            "name": _text(row, "Name_lang", "Name") or f"Hero subtree {identifier}",
            "description": _text(row, "Description_lang", "Description"),
        })
    return sorted({item["id"]: item for item in records}.values(), key=lambda item: item["id"])


def _records_for_definitions(tables: dict[str, tuple[Path, dict[str, Any]]], required_ids: set[int] | None = None, fallback: dict[int, dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    spells = {
        _integer(row, "ID"): row
        for row in _table(tables, "Spell").rows
        if _integer(row, "ID") is not None
    }
    spell_names = {
        _integer(row, "ID"): _text(row, "Name_lang", "Name")
        for row in _table(tables, "SpellName").rows
        if _integer(row, "ID") is not None
    }
    definitions = []
    seen: set[int] = set()
    if required_ids and 0 in required_ids:
        definitions.append(
            {
                "id": 0,
                "spell_id": 0,
                "name": "",
                "description": "",
                "effect": "",
                "source": "structural",
            }
        )
        seen.add(0)
    for row in _table(tables, "TraitDefinition").rows:
        identifier = _integer(row, "ID")
        if identifier is None or identifier in seen:
            raise NormalizationError("duplicate or missing TraitDefinition ID")
        if required_ids is not None and identifier not in required_ids:
            continue
        seen.add(identifier)
        spell_id = _integer(row, "SpellID", "SpellID[0]")
        spell = spells.get(spell_id, {})
        name = _text(row, "OverrideName_lang", "OverrideName", "Name_lang") or _text(spell, "Name_lang", "Name") or spell_names.get(spell_id, "")
        description = _text(row, "OverrideDescription_lang", "OverrideDescription", "Description_lang") or _text(spell, "Description_lang", "Description")
        if (not name or not description) and fallback and identifier in fallback:
            definitions.append(fallback[identifier])
            continue
        if not name or not description:
            if spell_id:
                raise NormalizationError(f"definition {identifier} lacks resolved localized text")
            # A zero-spell definition is an internal rank/slot record, not a
            # player-facing ability. Keep its codec position but never invent
            # a name or effect for the class reference catalog.
            definitions.append(
                {
                    "id": identifier,
                    "spell_id": 0,
                    "name": "",
                    "description": "",
                    "effect": "",
                    "source": "structural",
                }
            )
            continue
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


def _records_for_effects(tables: dict[str, tuple[Path, dict[str, Any]]], definition_ids: set[int]) -> list[dict[str, Any]]:
    records = []
    for row in _table(tables, "TraitDefinitionEffectPoints").rows:
        definition_id = _integer(row, "TraitDefinitionID", "DefinitionID")
        identifier = _integer(row, "ID")
        if identifier is None or definition_id not in definition_ids:
            continue
        records.append(
            {
                "id": identifier,
                "definition_id": definition_id,
                "effect_index": _integer(row, "EffectIndex", "Index", default=0) or 0,
                "operation_type": _integer(row, "OperationType", "Operation", default=0) or 0,
                "curve_id": _integer(row, "CurveID", default=0) or 0,
            }
        )
    return sorted(records, key=lambda item: item["id"])


def normalize_bundle(root: Path, build: str, locale: str, output: Path) -> Path:
    root = root.resolve()
    tables = _load_receipts(root, build, locale)
    _verify_dbd_payload(tables, build)
    wowhead_node_ids, wowhead_definitions, wowhead_node_classes, wowhead_node_specs, wowhead_node_types, wowhead_codec_orders, wowhead_node_definitions = _wowhead_payload(tables)
    allowed_nodes = set(wowhead_node_ids) if wowhead_node_ids else None
    if allowed_nodes:
        # Wowhead can omit hidden and otherwise non-rendered nodes. Blizzard
        # still serializes every node returned by C_Traits.GetTreeNodes(), so
        # retain every exact-build TraitNode from a discovered class tree.
        source_rows = _table(tables, "TraitNode").rows
        source_tree_ids = {
            _integer(row, "TraitTreeID", "TreeID")
            for row in source_rows
            if _integer(row, "ID") in allowed_nodes
        }
        allowed_nodes.update(
            _integer(row, "ID")
            for row in source_rows
            if (
                _integer(row, "TraitTreeID", "TreeID") in source_tree_ids
                and _integer(row, "ID") is not None
            )
        )
    classes = _records_for_classes(_table(tables, "ChrClasses"))
    specs = _records_for_specs(_table(tables, "ChrSpecialization"))
    nodes, codec_orders = _records_for_nodes(tables, allowed_nodes)
    class_by_tree: dict[int, set[int]] = {}
    for node in nodes:
        class_id = wowhead_node_classes.get(node["id"], 0)
        if class_id:
            class_by_tree.setdefault(node.get("tree_id", 0), set()).add(class_id)
    ambiguous_trees = {
        tree_id: sorted(class_ids)
        for tree_id, class_ids in class_by_tree.items()
        if len(class_ids) > 1
    }
    if ambiguous_trees:
        tree_id, class_ids = next(iter(sorted(ambiguous_trees.items())))
        raise NormalizationError(f"tree {tree_id} has ambiguous class ownership: {class_ids}")
    tree_class_id = {tree_id: min(class_ids) for tree_id, class_ids in class_by_tree.items()}
    for node in nodes:
        node["class_id"] = wowhead_node_classes.get(node["id"], 0) or tree_class_id.get(node.get("tree_id", 0), 0)
        node["spec_ids"] = sorted(wowhead_node_specs.get(node["id"], set()))
        if node["id"] in wowhead_node_types:
            node["type"] = wowhead_node_types[node["id"]]
    # Blizzard's codec is specialization-scoped. Build deterministic orders
    # from the exact-build class/spec node membership, not DB2 tree IDs.
    for spec in specs:
        spec_id = spec["id"]
        class_id = spec.get("class_id") or 0
        node_ids_for_spec = {node["id"] for node in nodes if node.get("class_id") == class_id or spec_id in node.get("spec_ids", [])}
        spec_order = sorted(node_ids_for_spec)
        if spec_order:
            codec_orders[str(spec_id)] = spec_order
    subtrees = _records_for_subtrees(tables, {node.get("tree_id") for node in nodes if node.get("tree_id") is not None})
    entries = _records_for_entries(tables, {node["id"] for node in nodes})
    entry_nodes = {entry["node_id"] for entry in entries}
    next_synthetic = 900_000_000
    for node in nodes:
        if node["id"] in entry_nodes:
            continue
        definition_id = next(iter(wowhead_node_definitions.get(node["id"], [0])), 0)
        entries.append({"id": next_synthetic, "node_id": node["id"], "definition_id": definition_id, "max_ranks": 1, "ordinal": len(entries)})
        next_synthetic += 1
    definitions = _records_for_definitions(tables, {entry["definition_id"] for entry in entries if entry.get("definition_id") is not None}, wowhead_definitions)
    node_ids = {node["id"] for node in nodes}
    edges = _records_for_edges(tables, node_ids)
    definition_ids = {definition["id"] for definition in definitions}
    for entry in entries:
        if entry["node_id"] not in node_ids or entry["definition_id"] not in definition_ids:
            raise NormalizationError(f"entry {entry['id']} references missing graph data")
        if entry["max_ranks"] is None or entry["max_ranks"] < 0:
            raise NormalizationError(f"entry {entry['id']} has invalid max ranks")
    costs, conditions, currency_data = _records_for_constraints(
        tables,
        {node.get("tree_id") for node in nodes if node.get("tree_id") is not None},
        node_ids,
        {entry["id"] for entry in entries},
    )
    receipts = json.loads((root / "receipts.json").read_text(encoding="utf-8"))
    snapshot = {
        "schema_version": 1,
        "product": "wow",
        "channel": "retail-live",
        "game_build": build,
        "locale": locale,
        "classes": classes,
        "specs": specs,
        "trees": [
            {"id": tree_id, "kind": "class", "class_id": next((node.get("class_id", 0) for node in nodes if node.get("tree_id") == tree_id and node.get("class_id")), 0), "spec_id": 0}
            for tree_id in sorted({node.get("tree_id") for node in nodes if node.get("tree_id") is not None})
        ],
        "subtrees": subtrees,
        "nodes": nodes,
        "entries": entries,
        "definitions": definitions,
        "effects": _records_for_effects(tables, definition_ids),
        "edges": edges,
        "conditions": conditions,
        "currencies": currency_data["currencies"],
        "currency_sources": currency_data["currency_sources"],
        "costs": costs,
        "grants": currency_data["grants"],
        "codec_orders": codec_orders,
        "presets": [],
        "source_receipts": [
            {**item, "path": Path(item["path"]).name}
            for item in sorted(receipts, key=lambda item: (item["kind"], item["url"]))
        ],
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
