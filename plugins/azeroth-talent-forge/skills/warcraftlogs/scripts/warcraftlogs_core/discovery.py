"""Character, guild, and sampled global report discovery services."""
import copy
import json
import math
import re
from typing import Mapping, Optional, Sequence, Tuple
from .models import (DiscoveryFilters, PublicReportError, PartialGraphQLError, report_matches, _casefold, _items,
                     _actor_field_matches, _actor_role_matches,
                     _DISCOVERY_FILTER_FIELDS, GLOBAL_TOP_MIN, GLOBAL_TOP_MAX,
                     GLOBAL_MAX_PAGES, GLOBAL_WARNING, _report_fights)
from .metadata import (MetadataResolver, normalize_name, select_named,
                        _normalize_world, _normalize_game)
from .reports import (hydrate_discovery_report, report_data, _pagination_data,
                      _public_report_payload, make_envelope)
from .transport import sanitize_graphql_errors

def _identity_variables(name, server, region) -> dict:
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Character or guild name is required")
    if not isinstance(server, str) or not server.strip():
        raise ValueError("Server is required")
    if not isinstance(region, str) or not region.strip():
        raise ValueError("Region is required")
    return {
        "name": name.strip(),
        "serverSlug": normalize_name(server).replace(" ", "-"),
        "serverRegion": region.strip().casefold(),
    }


def _discovery_filters(args, allow_partition=False) -> DiscoveryFilters:
    affixes = args.affixes if args.affixes else None
    if args.season is not None or (args.partition is not None and not allow_partition):
        raise ValueError("Discovery cannot establish a report-specific season or partition match")
    for bound_name in ("start_time", "end_time"):
        value = getattr(args, bound_name)
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ValueError("Discovery time bounds must be finite and non-negative")
    if args.start_time is not None and args.end_time is not None and args.start_time > args.end_time:
        raise ValueError("Discovery start time must not exceed end time")
    if args.key_min is not None and args.key_min < 0 or args.key_max is not None and args.key_max < 0:
        raise ValueError("Key bounds must be non-negative")
    if args.key_min is not None and args.key_max is not None and args.key_min > args.key_max:
        raise ValueError("Key minimum must not exceed key maximum")
    return DiscoveryFilters(
        **{field: getattr(args, field) for field in _DISCOVERY_FILTER_FIELDS}
    )


def _filters_dict(filters: DiscoveryFilters) -> dict:
    return {field: getattr(filters, field) for field in _DISCOVERY_FILTER_FIELDS if getattr(filters, field) is not None}


def _report_latest_time(report):
    for field in ("endTime", "startTime"):
        value = report.get(field)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value
    return float("-inf")


def _positive_id(value, label):
    if value is None:
        return None
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        raise ValueError("Global %s must be a numeric metadata ID" % label)
    if parsed < 1:
        raise ValueError("Global %s must be positive" % label)
    return parsed


def _expansion_variables(expansion_id):
    return {} if expansion_id is None else {"expansionId": expansion_id}


def _global_world(client, expansion_id):
    return _normalize_world(client.execute("metadata-world", _expansion_variables(expansion_id)))


def _resolve_global_metadata_id(value, records, label):
    if value is None:
        return None
    try:
        parsed = _positive_id(value, label)
        if records and not any(item.get("id") == parsed for item in records):
            raise ValueError("Unknown %s: %s" % (label, value))
        return parsed
    except ValueError:
        return select_named(records, value, label)["id"]


def _global_filters(args, client=None) -> DiscoveryFilters:
    if not args.zone and not args.instance and not args.encounter:
        raise ValueError("Global discovery requires a zone, instance, or encounter")
    if args.zone and args.instance:
        raise ValueError("Global discovery accepts either zone or instance, not both")
    for value, label in (
        (args.zone, "zone"), (args.instance, "instance"), (args.encounter, "encounter"),
        (args.partition, "partition"), (args.difficulty, "difficulty"),
        (args.class_name, "class"), (args.spec_name, "spec"),
    ):
        if value is not None and re.fullmatch(r"-?[0-9]+", str(value)):
            _positive_id(value, label)
    for bound_name in ("start_time", "end_time"):
        value = getattr(args, bound_name)
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ValueError("Discovery time bounds must be finite and non-negative")
    if args.start_time is not None and args.end_time is not None and args.start_time > args.end_time:
        raise ValueError("Discovery start time must not exceed end time")
    if (args.key_min is not None and args.key_min < 0) or (args.key_max is not None and args.key_max < 0):
        raise ValueError("Key bounds must be non-negative")
    if args.key_min is not None and args.key_max is not None and args.key_min > args.key_max:
        raise ValueError("Key minimum must not exceed key maximum")
    values = {
        "class_name": args.class_name, "spec_name": args.spec_name,
        "role": args.role.casefold() if isinstance(args.role, str) else args.role,
        "instance": None, "zone": None, "encounter": None, "partition": None,
        "difficulty": None, "key_min": args.key_min, "key_max": args.key_max,
        "affixes": args.affixes if args.affixes else None, "timed": args.timed,
        "depleted": args.depleted, "kill": args.kill, "wipe": args.wipe,
        "start_time": args.start_time, "end_time": args.end_time,
        "season": None,
    }
    world = None
    if client is not None:
        world = _global_world(client, args.expansion_id)
    selected_zone = None
    if args.zone:
        values["zone"] = _resolve_global_metadata_id(
            args.zone, world["zones"] if world else [], "zone"
        )
        selected_zone = next((z for z in (world or {}).get("zones", []) if z.get("id") == values["zone"]), None)
    if args.instance:
        values["instance"] = _resolve_global_metadata_id(
            args.instance, world["zones"] if world else [], "instance"
        )
        selected_zone = next((z for z in (world or {}).get("zones", []) if z.get("id") == values["instance"]), None)
    if args.encounter:
        encounter_records = selected_zone.get("encounters", []) if selected_zone else [
            encounter for zone in (world or {}).get("zones", []) for encounter in zone.get("encounters", [])
        ]
        values["encounter"] = _resolve_global_metadata_id(args.encounter, encounter_records, "encounter")
        if selected_zone is None and world:
            selected_zone = next(
                (zone for zone in world["zones"] if any(item.get("id") == values["encounter"] for item in zone.get("encounters", []))),
                None,
            )
    elif selected_zone and len(selected_zone.get("encounters", [])) == 1:
        values["encounter"] = selected_zone["encounters"][0].get("id")
    if args.partition:
        partition_records = selected_zone.get("partitions", []) if selected_zone else [
            partition for zone in (world or {}).get("zones", []) for partition in zone.get("partitions", [])
        ]
        values["partition"] = _resolve_global_metadata_id(args.partition, partition_records, "partition")
    if args.difficulty is not None:
        difficulty_records = selected_zone.get("difficulties", []) if selected_zone else []
        values["difficulty"] = _resolve_global_metadata_id(args.difficulty, difficulty_records, "difficulty")
    if client is not None and (args.class_name or args.spec_name):
        game = _normalize_game(client.execute("metadata-game", {"abilityLimit": 100, "abilityPage": 1}))
        selected_class = None
        if args.class_name:
            class_id = _positive_id(args.class_name, "class") if str(args.class_name).isdigit() else None
            selected_class = next((item for item in game["classes"] if item.get("id") == class_id), None) if class_id is not None else select_named(game["classes"], args.class_name, "class")
            if selected_class is None:
                raise ValueError("Unknown class: %s" % args.class_name)
        values["class_name"] = selected_class["name"] if selected_class else None
        if args.spec_name:
            specs = selected_class["specs"] if selected_class else [spec for game_class in game["classes"] for spec in game_class["specs"]]
            spec_id = _positive_id(args.spec_name, "spec") if str(args.spec_name).isdigit() else None
            selected_spec = next((item for item in specs if item.get("id") == spec_id), None) if spec_id is not None else select_named(specs, args.spec_name, "spec")
            if selected_spec is None:
                raise ValueError("Unknown spec: %s" % args.spec_name)
            values["spec_name"] = selected_spec["name"]
    if values["role"] is not None and values["role"] not in ("tank", "healer", "dps", "damage"):
        raise ValueError("Unknown role: %s" % args.role)
    return DiscoveryFilters(**values)


def discover_reports(client, kind: str, identity: Mapping[str, str], filters: DiscoveryFilters, page: int, limit: int, max_pages: int = 1, latest: Optional[int] = None) -> dict:
    if kind not in ("character", "guild"):
        raise ValueError("Unknown discovery kind")
    if page < 1 or max_pages < 1:
        raise ValueError("Discovery page and max pages must be positive")
    if not 1 <= limit <= 100:
        raise ValueError("Discovery limit must be between 1 and 100")
    if latest is not None and (not isinstance(latest, int) or isinstance(latest, bool) or latest < 1):
        raise ValueError("Discovery latest must be a positive integer")
    if filters.season is not None or filters.partition is not None:
        raise ValueError("Discovery cannot establish a report-specific season or partition match")
    reports = []
    pages_fetched = 0
    current = page
    last_page = None
    has_more = False
    character = None
    if kind == "character":
        character_payload = client.execute("character", identity)
        character = character_payload["data"]["characterData"]["character"]
        if not isinstance(character, Mapping):
            raise TypeError("Character identity was not found")
    while pages_fetched < max_pages:
        variables = dict(identity)
        variables.update(filters.direct_variables())
        variables.update({"limit": limit, "page": current})
        if kind == "character":
            variables.pop("startTime", None)
            variables.pop("endTime", None)
            variables.pop("zoneID", None)
            variables.pop("gameZoneID", None)
            payload = client.execute("character-reports", variables)
            _, page_reports, pagination = _pagination_data(payload, ("data", "characterData", "character", "recentReports"))
        else:
            variables["guildName"] = variables.pop("name")
            variables["guildServerSlug"] = variables.pop("serverSlug")
            variables["guildServerRegion"] = variables.pop("serverRegion")
            payload = client.execute("guild-reports", variables)
            _, page_reports, pagination = _pagination_data(payload, ("data", "reportData", "reports"))
        reports.extend(page_reports)
        pages_fetched += 1
        last_page = pagination["last_page"]
        has_more = bool(pagination["has_more_pages"])
        current = (pagination["current_page"] or current) + 1
        if not has_more:
            break
    matched = []
    exclusion_reasons = {}
    hydrated_count = 0
    for report in reports:
        if not isinstance(report, Mapping):
            continue
        if filters.needs_hydration:
            hydrated_count += 1
            fights, actors = hydrate_discovery_report(client, str(report.get("code", "")), filters)
        else:
            fights, actors = [], []
        is_match, reasons = report_matches(
            report, fights, actors, filters,
            identity.get("name") if kind == "character" else None,
        )
        if is_match:
            matched.append(dict(report))
        else:
            for reason in reasons:
                exclusion_reasons[reason] = exclusion_reasons.get(reason, 0) + 1
    matched_count = len(matched)
    selected = matched
    if latest is not None:
        selected = sorted(matched, key=_report_latest_time, reverse=True)[:latest]
    result = {
        "data": selected,
        "candidate_count": len(reports),
        "hydrated_count": hydrated_count,
        "matched_count": matched_count,
        "excluded_count": len(reports) - matched_count,
        "exclusion_reasons": exclusion_reasons,
        "character": dict(character) if character is not None else None,
        "pagination": {
            "requested_page": page,
            "current_page": page if pages_fetched == 1 and last_page is None else current - 1,
            "last_page": last_page,
            "has_more_pages": has_more,
            "pages_fetched": pages_fetched,
            "limit": limit,
            "truncated": has_more and pages_fetched >= max_pages,
        },
    }
    if latest is not None:
        result["selected_count"] = len(selected)
    return result


def _ranking_value(value):
    if isinstance(value, str):
        try:
            return json.loads(value)
        except (TypeError, ValueError):
            raise TypeError("Encounter rankings JSON was invalid")
    return value


def _ranking_page(payload: Mapping[str, object]) -> Tuple[list, dict]:
    if not isinstance(payload, Mapping) or not isinstance(payload.get("data"), Mapping):
        return [], {}
    world = payload["data"].get("worldData", {})
    value = world.get("encounter") if isinstance(world, Mapping) else None
    if not isinstance(value, Mapping):
        return [], {}
    raw = value.get("fightRankings")
    if raw is None:
        raw = value.get("characterRankings")
    raw = _ranking_value(raw)
    if isinstance(raw, list):
        return [item for item in raw if isinstance(item, Mapping)], {}
    if not isinstance(raw, Mapping):
        raise TypeError("Encounter rankings were not JSON")
    rows = raw.get("rankings", raw.get("data", []))
    if not isinstance(rows, list):
        raise TypeError("Encounter ranking rows were not a list")
    pagination = {
        "current_page": raw.get("current_page", raw.get("currentPage", raw.get("page"))),
        "last_page": raw.get("last_page", raw.get("lastPage")),
        "has_more_pages": bool(raw.get("has_more_pages", raw.get("hasMorePages", False))),
    }
    return [item for item in rows if isinstance(item, Mapping)], pagination


def _ranking_candidate(row: Mapping[str, object]) -> Optional[dict]:
    report = row.get("report")
    report = report if isinstance(report, Mapping) else {}
    code = (
        row.get("reportCode") or row.get("reportID") or row.get("reportId") or
        row.get("report_code") or report.get("code") or report.get("id")
    )
    fight_id = row.get("fightID", row.get("fightId", row.get("fight_id")))
    if fight_id is None and isinstance(row.get("fight"), Mapping):
        fight_id = row["fight"].get("id")
    if fight_id is None:
        fight_id = report.get("fightID", report.get("fightId", report.get("fight_id")))
    if code is None:
        return None
    result = dict(row)
    result["report_code"] = str(code)
    if fight_id is not None:
        try:
            result["fight_id"] = int(fight_id)
        except (TypeError, ValueError):
            return None
        if result["fight_id"] < 1:
            return None
    else:
        return None
    return result


def _ranking_direct_match(candidate: Mapping[str, object], filters: DiscoveryFilters) -> Tuple[bool, list, list]:
    """Match ranking-provided fields and report which fields still need hydration."""
    missing = []
    reasons = []
    checks = (
        ("class_name", filters.class_name, ("className", "class")),
        ("spec_name", filters.spec_name, ("specName", "spec")),
        ("role", filters.role, ("role",)),
        ("instance", filters.instance, ("zoneID", "zoneId")),
        ("zone", filters.zone, ("gameZoneID", "gameZoneId")),
        ("encounter", None, ("encounterID", "encounterId")),
        ("partition", filters.partition, ("partition", "partitionID")),
        ("difficulty", filters.difficulty, ("difficulty",)),
        ("key_min", filters.key_min, ("keystoneLevel", "keyLevel")),
        ("key_max", filters.key_max, ("keystoneLevel", "keyLevel")),
        ("timed", filters.timed, ("timed",)),
        ("depleted", filters.depleted, ("depleted",)),
        ("kill", filters.kill, ("kill",)),
        ("wipe", filters.wipe, ("wipe",)),
        ("affixes", filters.affixes, ("affixes", "keystoneAffixes")),
        ("start_time", filters.start_time, ("startTime",)),
        ("end_time", filters.end_time, ("endTime",)),
    )
    for name, requested, fields in checks:
        if requested is None:
            continue
        values = [candidate[field] for field in fields if field in candidate]
        if not values:
            missing.append(name)
            continue
        value = values[0]
        if name == "class_name" and _casefold(value) != _casefold(requested):
            reasons.append(name)
        elif name == "spec_name" and _casefold(value) != _casefold(requested):
            reasons.append(name)
        elif name == "role" and _casefold(value) != _casefold(requested):
            reasons.append(name)
        elif name in ("instance", "zone", "encounter", "partition", "difficulty") and value != requested:
            reasons.append(name)
        elif name == "key_min" and (not isinstance(value, (int, float)) or value < requested):
            reasons.append(name)
        elif name == "key_max" and (not isinstance(value, (int, float)) or value > requested):
            reasons.append(name)
        elif name in ("timed", "depleted", "kill", "wipe") and bool(value) != requested:
            reasons.append(name)
        elif name == "start_time" and value < requested:
            reasons.append(name)
        elif name == "end_time" and value > requested:
            reasons.append(name)
        elif name == "affixes" and requested and not all(
            any(_casefold(item.get("name") if isinstance(item, Mapping) else item) == _casefold(wanted) or item == wanted
                for item in (value if isinstance(value, list) else [value]))
            for wanted in requested
        ):
            reasons.append(name)
    return not reasons, missing, reasons


def _ranking_actor(candidate: Mapping[str, object]) -> Optional[dict]:
    for key in ("actor", "player", "character", "source"):
        value = candidate.get(key)
        if isinstance(value, Mapping):
            actor = dict(value)
            if actor.get("id") is not None or actor.get("name") is not None:
                return actor
    actor_id = next((candidate.get(key) for key in ("actorID", "actorId", "playerID", "playerId", "sourceID", "sourceId") if candidate.get(key) is not None), None)
    name = next((candidate.get(key) for key in ("playerName", "characterName", "name") if candidate.get(key) is not None), None)
    if actor_id is None and name is None:
        return None
    return {"id": actor_id, "name": name}


def _actor_identity(actor: Mapping[str, object], match_source: str) -> dict:
    subtype = actor.get("subType") or actor.get("specName") or actor.get("spec")
    return {
        "id": actor.get("id"),
        "name": actor.get("name"),
        "class": actor.get("className") or actor.get("class") or (
            subtype.replace(actor.get("specName", ""), "") if isinstance(subtype, str) and actor.get("specName") else subtype
        ),
        "spec": actor.get("specName") or actor.get("spec") or subtype,
        "role": actor.get("role") or actor.get("roles"),
        "match_source": match_source,
    }


def _resolve_ranked_actor(candidate: Mapping[str, object], fights, actors, filters: DiscoveryFilters):
    if not any(getattr(filters, field) is not None for field in ("class_name", "spec_name", "role")):
        return None, None
    row_actor = _ranking_actor(candidate)
    if row_actor is not None:
        if not actors:
            return dict(candidate, **row_actor), "ranking_row"
        matches = [
            actor for actor in actors
            if (row_actor.get("id") is None or actor.get("id") == row_actor.get("id")) and
            (row_actor.get("name") is None or _casefold(actor.get("name")) == _casefold(row_actor.get("name")))
        ]
        if len(matches) == 1:
            return matches[0], "ranking_row"
        return None, "ambiguous"
    def satisfies(actor):
        return (
            (filters.class_name is None or _actor_field_matches(actor, filters.class_name, ("className", "class", "subType"))) and
            (filters.spec_name is None or _actor_field_matches(actor, filters.spec_name, ("specName", "spec", "subType"))) and
            (filters.role is None or _actor_role_matches(actor, filters.role))
        )
    ranked = [actor for actor in actors if actor.get("ranked") is True and satisfies(actor)]
    if len(ranked) == 1:
        return ranked[0], "ranked_group_member"
    if any("ranked" in actor for actor in actors):
        return None, "missing" if not ranked else "ambiguous"
    unique = [actor for actor in actors if satisfies(actor)]
    if len(unique) == 1:
        return unique[0], "unique_group_match"
    if len(unique) > 1:
        return None, "ambiguous"
    return None, "group_only"


def _filters_without(filters: DiscoveryFilters, names) -> DiscoveryFilters:
    values = {field: getattr(filters, field) for field in _DISCOVERY_FILTER_FIELDS}
    for name in names:
        values[name] = None
    return DiscoveryFilters(**values)


def _dedupe_global_candidates(rows: Sequence[Mapping[str, object]]) -> list:
    result = []
    seen = set()
    for row in rows:
        candidate = _ranking_candidate(row)
        if candidate is None:
            continue
        key = (candidate["report_code"], candidate.get("fight_id"))
        if key in seen:
            continue
        seen.add(key)
        result.append(candidate)
    return result


def _invalid_ranking_key(row: Mapping[str, object]):
    report = row.get("report") if isinstance(row.get("report"), Mapping) else {}
    code = row.get("reportCode") or row.get("reportID") or row.get("reportId") or row.get("report_code") or report.get("code") or report.get("id")
    fight_id = row.get("fightID", row.get("fightId", row.get("fight_id")))
    if fight_id is None and isinstance(row.get("fight"), Mapping):
        fight_id = row["fight"].get("id")
    if fight_id is None:
        fight_id = report.get("fightID", report.get("fightId", report.get("fight_id")))
    if code is not None and fight_id is None:
        return ("report", str(code), "missing-fight")
    if code is not None:
        return ("report", str(code), "invalid-fight", str(fight_id))
    return ("row", json.dumps(dict(row), sort_keys=True, ensure_ascii=True))


def make_global_result(rows, sample_size, filters, ranking_basis="encounter_rankings", metric=None, **metadata) -> dict:
    if not isinstance(sample_size, int) or isinstance(sample_size, bool) or sample_size < 0:
        raise ValueError("Global top must be a non-negative integer")
    candidates = _dedupe_global_candidates(rows)
    data = candidates[:sample_size]
    truncated = bool(metadata.get("truncated", len(candidates) > sample_size))
    scope = {"ranking_basis": ranking_basis}
    if metric is not None:
        scope["metric"] = metric
    result = make_envelope(
        "find global",
        scope,
        filters,
        "sampled",
        data,
        pagination={
            "pages_fetched": int(metadata.get("pages_fetched", 1)),
            "truncated": truncated,
        },
        warnings=[GLOBAL_WARNING],
    )
    result.update({
        "ranking_basis": ranking_basis,
        "requested_top": sample_size,
        "source_rows": int(metadata.get("source_rows", len(rows))),
        "unique_candidates": int(metadata.get("unique_candidates", len(candidates))),
        "hydrated_candidates": int(metadata.get("hydrated_candidates", 0)),
        "excluded_candidates": int(metadata.get("excluded_candidates", 0)),
        "returned_candidates": int(metadata.get("returned_candidates", len(data))),
        "pages_fetched": int(metadata.get("pages_fetched", 1)),
        "truncated": truncated,
    })
    if metric is not None:
        result["ranking_metric"] = metric
    if metadata.get("exclusion_reasons"):
        result["exclusion_reasons"] = dict(metadata["exclusion_reasons"])
    if metadata.get("errors"):
        result["partial"] = True
        result["errors"] = sanitize_graphql_errors(metadata["errors"])
    return result


def discover_global(client, filters: DiscoveryFilters, top: int, page: int, max_pages: int = 1,
                    metric=None, leaderboard=None, server_region=None, server_slug=None,
                    expansion_id=None) -> dict:
    if leaderboard is not None:
        raise ValueError("Global leaderboard filtering is not supported by the public Warcraft Logs API")
    if not isinstance(top, int) or isinstance(top, bool) or not GLOBAL_TOP_MIN <= top <= GLOBAL_TOP_MAX:
        raise ValueError("Global top must be between 1 and 100")
    if (
        not isinstance(page, int) or isinstance(page, bool) or page < 1 or
        not isinstance(max_pages, int) or isinstance(max_pages, bool) or
        max_pages < 1 or max_pages > GLOBAL_MAX_PAGES
    ):
        raise ValueError("Global page and max pages must be between 1 and 5")
    if filters.encounter is None:
        try:
            world = _global_world(client, expansion_id)
        except Exception as error:
            return make_global_result([], top, _filters_dict(filters), metric=metric, errors=[{"message": str(error)}])
        zone_id = filters.zone if filters.zone is not None else filters.instance
        encounters = [
            encounter["id"]
            for zone in world["zones"]
            if zone_id is None or zone.get("id") == zone_id
            for encounter in zone.get("encounters", [])
        ]
        if not encounters:
            raise ValueError("Global discovery could not resolve an encounter for the requested zone")
        parts = []
        for encounter in encounters:
            values = {field: getattr(filters, field) for field in _DISCOVERY_FILTER_FIELDS}
            values["encounter"] = encounter
            parts.append(discover_global(
                client, DiscoveryFilters(**values), top, page, max_pages,
                metric=metric, leaderboard=leaderboard,
                server_region=server_region, server_slug=server_slug, expansion_id=expansion_id,
            ))
        rows = [row for part in parts for row in part["data"]]
        child_errors = [error for part in parts for error in part.get("errors", [])]
        return make_global_result(
            rows, top, _filters_dict(filters),
            source_rows=sum(part["source_rows"] for part in parts),
            unique_candidates=len(_dedupe_global_candidates(rows)),
            hydrated_candidates=sum(part["hydrated_candidates"] for part in parts),
            excluded_candidates=sum(part["excluded_candidates"] for part in parts),
            returned_candidates=min(len(_dedupe_global_candidates(rows)), top),
            pages_fetched=sum(part["pages_fetched"] for part in parts),
            truncated=any(part["truncated"] for part in parts),
            metric=metric,
            errors=child_errors,
        )
    zone_id = filters.zone or filters.instance
    if zone_id is None:
        try:
            world = _global_world(client, expansion_id)
            zone_id = next(
                zone.get("id") for zone in world["zones"]
                if any(item.get("id") == filters.encounter for item in zone.get("encounters", []))
            )
        except Exception as error:
            return make_global_result([], top, _filters_dict(filters), metric=metric, errors=[{"message": str(error)}])
    variables = {
        "encounterID": filters.encounter,
        "zoneID": zone_id,
        "page": page,
    }
    variables.update(filters.direct_variables())
    for field, value in (
        ("difficulty", filters.difficulty), ("partition", filters.partition),
        ("metric", metric), ("leaderboard", leaderboard),
        ("serverRegion", server_region), ("serverSlug", server_slug),
    ):
        if value is not None:
            variables[field] = value
    rows = []
    pages_fetched = 0
    has_more = False
    current_page = page
    hydrated_count = 0
    exclusion_reasons = {}
    errors = []
    while pages_fetched < max_pages and (pages_fetched == 0 or has_more):
        variables["page"] = current_page
        try:
            payload = client.execute("encounter-rankings", variables)
            errors.extend(payload.get("errors", []) if isinstance(payload, Mapping) else [])
            page_rows, pagination = _ranking_page(payload)
        except Exception as error:
            errors.append({"message": str(error)})
            break
        rows.extend(page_rows)
        pages_fetched += 1
        has_more = pagination.get("has_more_pages", False)
        if not has_more or not page_rows:
            break
        current_page = (pagination.get("current_page") or current_page) + 1
    candidates = _dedupe_global_candidates(rows)
    invalid_candidates = 0
    invalid_keys = set()
    for row in rows:
        if _ranking_candidate(row) is None:
            key = _invalid_ranking_key(row)
            if key not in invalid_keys:
                invalid_keys.add(key)
                invalid_candidates += 1
                exclusion_reasons["fight_id"] = exclusion_reasons.get("fight_id", 0) + 1
    matched = []
    processed_exclusions = 0
    for candidate in candidates:
        direct_match, missing, direct_reasons = _ranking_direct_match(candidate, filters)
        if not direct_match:
            for reason in direct_reasons:
                exclusion_reasons[reason] = exclusion_reasons.get(reason, 0) + 1
            processed_exclusions += 1
            continue
        actor_filters_requested = any(getattr(filters, field) is not None for field in ("class_name", "spec_name", "role"))
        if missing or (actor_filters_requested and _ranking_actor(candidate) is None):
            hydrated_count += 1
            hydration_fields = set(missing)
            if actor_filters_requested:
                hydration_fields.update(("class_name", "spec_name", "role"))
            try:
                fights, actors = hydrate_discovery_report(
                    client, candidate["report_code"],
                    _filters_without(filters, set(_DISCOVERY_FILTER_FIELDS) - hydration_fields),
                    fight_id=candidate.get("fight_id"),
                )
            except PartialGraphQLError as error:
                errors.extend(error.errors)
                exclusion_reasons["hydration"] = exclusion_reasons.get("hydration", 0) + 1
                processed_exclusions += 1
                continue
            except Exception as error:
                errors.append({"message": str(error), "path": [candidate["report_code"]]})
                exclusion_reasons["hydration"] = exclusion_reasons.get("hydration", 0) + 1
                processed_exclusions += 1
                continue
            hydrated_filters = _filters_without(filters, set(_DISCOVERY_FILTER_FIELDS) - hydration_fields)
            report = dict(candidate)
            matched_actor, actor_source = _resolve_ranked_actor(candidate, fights, actors, filters)
            if actor_filters_requested:
                if matched_actor is None:
                    exclusion_reasons["actor_identity"] = exclusion_reasons.get("actor_identity", 0) + 1
                    processed_exclusions += 1
                    continue
                actors = [matched_actor]
            is_match, reasons = report_matches(report, fights, actors, hydrated_filters)
            if not is_match:
                for reason in reasons:
                    exclusion_reasons[reason] = exclusion_reasons.get(reason, 0) + 1
                processed_exclusions += 1
                continue
            if matched_actor is not None:
                candidate = dict(candidate, matched_actor=_actor_identity(matched_actor, actor_source))
        elif any(getattr(filters, field) is not None for field in ("class_name", "spec_name", "role")):
            matched_actor, actor_source = _resolve_ranked_actor(candidate, [], [], filters)
            if matched_actor is None:
                exclusion_reasons["actor_identity"] = exclusion_reasons.get("actor_identity", 0) + 1
                processed_exclusions += 1
                continue
            candidate = dict(candidate, matched_actor=_actor_identity(matched_actor, actor_source))
        matched.append(candidate)
        if len(matched) >= top:
            break
    truncated = has_more and pages_fetched >= max_pages or len(candidates) > top
    return make_global_result(
        matched,
        top,
        _filters_dict(filters),
        source_rows=len(rows),
        unique_candidates=len(candidates),
        hydrated_candidates=hydrated_count,
        excluded_candidates=processed_exclusions + invalid_candidates,
        returned_candidates=min(len(matched), top),
        pages_fetched=pages_fetched,
        truncated=truncated,
        exclusion_reasons=exclusion_reasons,
        errors=errors,
        metric=metric,
    )


EVENT_PAGE_LIMIT = 10000
EVENT_MAX_PAGES = 5
