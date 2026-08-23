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


def _validate_metrics_data(data):
    if not isinstance(data, Mapping):
        raise ValueError("Actor metrics data must be an object")
    if data.get("metrics_schema_version") != METRICS_SCHEMA_VERSION:
        raise ValueError("Unsupported actor metrics schema version")
    for key in ("run", "actor", "damage_components", "cast_components", "utility", "survival"):
        if key not in data:
            raise ValueError("Actor metrics data is missing %s" % key)


def _component_records(data):
    records = []
    for section in ("damage_components", "cast_components", "healing_components", "misc_components"):
        value = data.get(section, [])
        if not isinstance(value, list):
            raise ValueError("Actor metrics section %s must be a list" % section)
        records.extend(value)
    for section in ("utility", "survival"):
        value = data.get(section, {})
        if not isinstance(value, Mapping):
            raise ValueError("Actor metrics section %s must be an object" % section)
        for category, rows in value.items():
            if not isinstance(rows, list):
                raise ValueError("Actor metrics category %s must be a list" % category)
            records.extend(rows)
    return records


def _index_components(data):
    indexed = {}
    for record in _component_records(data):
        if not isinstance(record, Mapping):
            raise ValueError("Actor metric component must be an object")
        category = record.get("category")
        ability_id = record.get("ability_id")
        if not isinstance(category, str) or isinstance(ability_id, bool) or not isinstance(ability_id, int) or ability_id < 1:
            raise ValueError("Actor metric component identity is invalid")
        values = record.get("values")
        if not isinstance(values, Mapping):
            raise ValueError("Actor metric component values must be an object")
        key = (category, ability_id)
        if key not in indexed:
            indexed[key] = {
                "category": category,
                "ability_id": ability_id,
                "name": record.get("name"),
                "names": list(record.get("observed_names") or ([record.get("name")] if record.get("name") is not None else [])),
                "scopes": [record.get("scope")] if record.get("scope") is not None else [],
                "values": dict(values),
            }
            continue
        current = indexed[key]
        for name in record.get("observed_names") or ([record.get("name")] if record.get("name") is not None else []):
            if name not in current["names"]:
                current["names"].append(name)
        scope = record.get("scope")
        if scope is not None and scope not in current["scopes"]:
            current["scopes"].append(scope)
        for field, value in values.items():
            if field not in current["values"]:
                current["values"][field] = value
            elif isinstance(current["values"][field], (int, float)) and isinstance(value, (int, float)):
                current["values"][field] += value
    return indexed


def _context_warnings(target, reference):
    warnings = []
    target_run = target.get("run", {})
    reference_run = reference.get("run", {})
    target_actor = target.get("actor", {})
    reference_actor = reference.get("actor", {})
    for label, left, right in (
        ("encounter", target_run.get("encounter_id"), reference_run.get("encounter_id")),
        ("key", target_run.get("key_level"), reference_run.get("key_level")),
        ("affixes", target_run.get("keystoneAffixes"), reference_run.get("keystoneAffixes")),
        ("spec", target_actor.get("specName"), reference_actor.get("specName")),
        ("role", target_actor.get("role"), reference_actor.get("role")),
    ):
        if left is None or right is None:
            warnings.append("Comparison context missing %s." % label)
        elif left != right:
            warnings.append("Comparison context differs for %s." % label)
    return warnings


def _delta(target_value, reference_value):
    result = {"target": target_value, "reference": reference_value}
    if not isinstance(target_value, (int, float)) or isinstance(target_value, bool) or not isinstance(reference_value, (int, float)) or isinstance(reference_value, bool):
        result.update({"absolute_delta": None, "percent_delta": None, "percent_delta_reason": "missing_numeric_value"})
        return result
    result["absolute_delta"] = target_value - reference_value
    if reference_value == 0:
        result["percent_delta"] = None
        result["percent_delta_reason"] = "reference_zero"
    else:
        result["percent_delta"] = (target_value - reference_value) / reference_value * 100
    return result


def compare_actor_metrics(target: Mapping[str, object], reference: Mapping[str, object]) -> dict:
    """Compare normalized metrics locally using category plus numeric ability ID."""
    _validate_metrics_data(target)
    _validate_metrics_data(reference)
    target_index = _index_components(target)
    reference_index = _index_components(reference)
    matched = []
    for category, ability_id in sorted(set(target_index) & set(reference_index)):
        left = target_index[(category, ability_id)]
        right = reference_index[(category, ability_id)]
        fields = sorted(set(left["values"]) | set(right["values"]))
        matched.append({
            "category": category,
            "ability_id": ability_id,
            "target": {"name": left["name"], "observed_names": left["names"], "scopes": left["scopes"]},
            "reference": {"name": right["name"], "observed_names": right["names"], "scopes": right["scopes"]},
            "deltas": {field: _delta(left["values"].get(field), right["values"].get(field)) for field in fields},
            "metadata": {
                "name_changed": left["names"] != right["names"],
                "scope_changed": left["scopes"] != right["scopes"],
            },
        })
    only_target = [target_index[key] for key in sorted(set(target_index) - set(reference_index))]
    only_reference = [reference_index[key] for key in sorted(set(reference_index) - set(target_index))]
    warnings = _context_warnings(target, reference)
    if any(item["metadata"]["scope_changed"] for item in matched):
        warnings.append("Metric scope differs for at least one matched ability.")
    return {
        "comparison_schema_version": 1,
        "matched": matched,
        "only_target": only_target,
        "only_reference": only_reference,
        "warnings": warnings,
        "derivations": [
            "Components are matched by category plus numeric ability_id.",
            "Display names are metadata and do not define identity.",
            "Percent deltas are omitted when the reference value is zero.",
        ],
    }
