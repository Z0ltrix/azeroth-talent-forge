"""Pure normalization and comparison helpers for actor-scoped report details."""

import json
from typing import Mapping


METRICS_SCHEMA_VERSION = 1
DEFAULT_DETAIL_CATEGORIES = ("DamageDone", "Healing", "DamageTaken", "Deaths", "Interrupts", "Casts")
_VALUE_EXCLUSIONS = frozenset(("guid", "id", "abilityID", "scope", "name", "subentries"))


def _items(value):
    return value if isinstance(value, list) else []


def _ability_id(row):
    value = row.get("guid")
    if value is None:
        value = row.get("abilityID")
    ability = row.get("ability")
    if value is None and isinstance(ability, Mapping):
        value = ability.get("guid") or ability.get("id")
    if isinstance(value, bool):
        return None
    try:
        value = int(value)
    except (TypeError, ValueError):
        return None
    return value if value > 0 else None


def _display_name(row):
    ability = row.get("ability")
    if isinstance(ability, Mapping) and ability.get("name") is not None:
        return str(ability["name"])
    return str(row["name"]) if row.get("name") is not None else None


def _scope(row):
    value = row.get("scope")
    if value is None:
        value = {
            key: row[key]
            for key in ("sourceID", "targetID", "fightID")
            if key in row
        }
    if not value:
        return "actor"
    if isinstance(value, Mapping):
        return json.dumps(dict(value), sort_keys=True, separators=(",", ":"))
    return str(value)


def _numeric_values(row):
    return {
        key: value
        for key, value in row.items()
        if key not in _VALUE_EXCLUSIONS
        and not isinstance(value, bool)
        and isinstance(value, (int, float))
    }


def _iter_leaves(row, ancestry=()):
    children = row.get("subentries")
    valid_children = [child for child in children if isinstance(child, Mapping)] if isinstance(children, list) else []
    if valid_children:
        label = row.get("name") or row.get("guid") or "container"
        for child in valid_children:
            yield from _iter_leaves(child, ancestry + (str(label),))
        return
    yield row, ancestry


def _table_entries(table):
    entries = table.get("entries")
    if isinstance(entries, list):
        return entries
    data = table.get("data")
    if isinstance(data, Mapping) and isinstance(data.get("entries"), list):
        return data["entries"]
    return None


def _context(source, keys):
    if not isinstance(source, Mapping):
        return {}
    return {key: source[key] for key in keys if key in source}


def _component_section(category):
    if category == "DamageDone":
        return "damage_components"
    if category == "Casts":
        return "cast_components"
    if category == "Healing":
        return "healing_components"
    if category in ("DamageTaken", "Deaths"):
        return "survival"
    if category in ("Interrupts", "Dispels", "Resources", "ResourcesGained"):
        return "utility"
    return "misc_components"


def _append_missing(missing_data, category, reason, **extra):
    item = {"category": category, "reason": reason}
    item.update(extra)
    missing_data.append(item)


def _merge_component(existing, row):
    for key, value in row["values"].items():
        if key not in existing["values"]:
            existing["values"][key] = value
        elif isinstance(existing["values"][key], (int, float)) and isinstance(value, (int, float)):
            existing["values"][key] += value
    for name in row["observed_names"]:
        if name not in existing["observed_names"]:
            existing["observed_names"].append(name)
    for ancestry in row["ancestries"]:
        if ancestry not in existing["ancestries"]:
            existing["ancestries"].append(ancestry)


def normalize_actor_metrics(details: Mapping[str, object]) -> dict:
    """Normalize report details while preserving API uncertainty explicitly."""
    if not isinstance(details, Mapping):
        raise TypeError("Actor details must be an object")
    tables = details.get("tables")
    if not isinstance(tables, Mapping):
        raise TypeError("Actor details tables must be an object")

    fight = details.get("fight")
    player = details.get("player")
    run = _context(fight, (
        "id", "name", "encounterID", "difficulty", "keystoneLevel", "keystoneBonus",
        "keystoneAffixes", "gameZone", "startTime", "endTime", "absoluteStartTime", "absoluteEndTime",
    ))
    run = {
        ("fight_id" if key == "id" else "encounter_id" if key == "encounterID" else "key_level" if key == "keystoneLevel" else "key_bonus" if key == "keystoneBonus" else key): value
        for key, value in run.items()
    }
    actor = _context(player, ("id", "name", "subType", "className", "specName", "role"))
    actor = {("actor_id" if key == "id" else key): value for key, value in actor.items()}

    result = {
        "metrics_schema_version": METRICS_SCHEMA_VERSION,
        "run": run,
        "actor": actor,
        "totals": {},
        "damage_components": [],
        "cast_components": [],
        "healing_components": [],
        "utility": {},
        "survival": {},
        "misc_components": [],
        "missing_data": [],
        "derivations": [
            "Ability identity is category plus numeric ability_id.",
            "Composite parents with valid subentries are containers; only leaves are emitted.",
            "Component rows are API metrics and are not reconstructed button presses.",
        ],
    }
    categories = list(DEFAULT_DETAIL_CATEGORIES)
    categories.extend(sorted(str(key) for key in tables if key not in categories))
    indexes = {}
    for category in categories:
        table = tables.get(category)
        if table is None:
            _append_missing(result["missing_data"], category, "view_missing")
            continue
        if not isinstance(table, Mapping):
            _append_missing(result["missing_data"], category, "view_invalid")
            continue
        totals = _numeric_values(table)
        if totals:
            result["totals"][category] = totals
        entries = _table_entries(table)
        if entries is None:
            _append_missing(result["missing_data"], category, "entries_missing")
            continue
        section = _component_section(category)
        if section in ("utility", "survival"):
            result[section].setdefault(category, [])
            destination = result[section][category]
        else:
            destination = result[section]
        for raw_row in entries:
            if not isinstance(raw_row, Mapping):
                _append_missing(result["missing_data"], category, "row_invalid")
                continue
            for leaf, ancestry in _iter_leaves(raw_row):
                ability_id = _ability_id(leaf)
                if ability_id is None:
                    _append_missing(result["missing_data"], category, "ability_id_missing", name=_display_name(leaf))
                    continue
                values = _numeric_values(leaf)
                if not values:
                    _append_missing(result["missing_data"], category, "numeric_values_missing", ability_id=ability_id)
                    continue
                name = _display_name(leaf)
                scope = _scope(leaf)
                component = {
                    "category": category,
                    "ability_id": ability_id,
                    "name": name,
                    "observed_names": [name] if name is not None else [],
                    "scope": scope,
                    "ancestry": list(ancestry),
                    "ancestries": [list(ancestry)],
                    "values": values,
                }
                index_key = (category, ability_id, scope)
                if index_key in indexes:
                    _merge_component(indexes[index_key], component)
                else:
                    indexes[index_key] = component
                    destination.append(component)
    return result
