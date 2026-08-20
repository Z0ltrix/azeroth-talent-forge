"""Public report, summary, event, and JSONL services."""
import json
import math
import os
import tempfile
import re
import urllib.parse
from pathlib import Path
from typing import Mapping, Optional, Sequence, Tuple
from .models import (
    DiscoveryFilters, PublicReportError, PartialGraphQLError, ReportReference, REPORT_CODE, REPORT_HOSTS, _items,
    KILL_TYPES, TABLE_DATA_TYPES, GRAPH_DATA_TYPES, HOSTILITY_TYPES, VIEW_TYPES,
    RANKING_COMPARE_TYPES, RANKING_TIMEFRAMES, RANKING_METRICS,
)
from .metadata import normalize_name
from .transport import sanitize_graphql_errors, utc_now

EVENT_PAGE_LIMIT = 10000
EVENT_MAX_PAGES = 5

def _fight_id(parameters) -> Optional[int]:
    values = urllib.parse.parse_qs(parameters, keep_blank_values=True).get("fight")
    if values is None:
        return None
    if len(values) != 1 or not values[0]:
        raise ValueError("Report fight must be a positive integer")
    try:
        fight_id = int(values[0])
    except (TypeError, ValueError):
        raise ValueError("Report fight must be a positive integer")
    if fight_id < 1:
        raise ValueError("Report fight must be a positive integer")
    return fight_id


def parse_report_reference(value) -> ReportReference:
    if not isinstance(value, str) or not value:
        raise ValueError("Invalid Warcraft Logs report reference")
    if REPORT_CODE.fullmatch(value):
        return ReportReference(value, None)
    parsed = urllib.parse.urlsplit(value)
    hostname = (parsed.hostname or "").rstrip(".").casefold()
    try:
        port = parsed.port
    except ValueError:
        raise ValueError("Invalid Warcraft Logs report URL")
    if (
        parsed.scheme not in ("http", "https")
        or parsed.username is not None
        or parsed.password is not None
        or hostname not in REPORT_HOSTS
        or port not in (None, 80 if parsed.scheme == "http" else 443)
    ):
        raise ValueError("Invalid Warcraft Logs report URL")
    path = urllib.parse.unquote(parsed.path)
    match = re.fullmatch(r"/reports/([A-Za-z0-9]{8,32})/?", path)
    if not match:
        raise ValueError("Invalid Warcraft Logs report URL")
    fight_id = _fight_id(parsed.fragment)
    if fight_id is None:
        fight_id = _fight_id(parsed.query)
    return ReportReference(match.group(1), fight_id)


def make_envelope(
    command,
    scope,
    filters,
    completeness,
    data,
    pagination=None,
    rate_limit=None,
    warnings=None,
    errors=None,
    **metadata
) -> dict:
    result = {
        "schema_version": 1,
        "command": command,
        "source": {"provider": "warcraftlogs", "endpoint": "client", "fetched_at": utc_now()},
        "scope": dict(scope),
        "filters": dict(filters),
        "completeness": completeness,
        "pagination": pagination or {"pages_fetched": 1, "truncated": False},
        "rate_limit": rate_limit or {},
        "warnings": list(warnings or []),
        "data": data,
    }
    result.update(metadata)
    if errors:
        result["partial"] = True
        result["errors"] = sanitize_graphql_errors(errors)
    return result


def _add_report_options(parser, window=False, translate=False, absolute_window=False) -> None:
    parser.add_argument("reference", help="report code or official Warcraft Logs report URL")
    parser.add_argument("--fight", type=int)
    if window:
        parser.add_argument("--start-time", type=float)
        parser.add_argument("--end-time", type=float)
    if absolute_window:
        parser.add_argument("--absolute-start-time", type=float)
        parser.add_argument("--absolute-end-time", type=float)
        parser.add_argument("--time-mode", choices=("started", "overlap", "completed"))
    if translate:
        parser.add_argument("--no-translate", dest="translate", action="store_false", default=True)


def _add_json_report_options(parser) -> None:
    _add_report_options(parser, window=True)
    parser.add_argument("--difficulty", type=int)
    parser.add_argument("--encounter-id", type=int)
    parser.add_argument("--kill-type")


def _enum(value, allowed, label) -> None:
    if value is not None and value not in allowed:
        raise ValueError("Invalid %s: %s" % (label, value))


def report_request(args) -> tuple:
    reference = parse_report_reference(args.reference)
    fight_id = args.fight if args.fight is not None else reference.fight_id
    if fight_id is not None and fight_id < 1:
        raise ValueError("Report fight must be a positive integer")
    start_time = getattr(args, "start_time", None)
    end_time = getattr(args, "end_time", None)
    absolute_start = getattr(args, "absolute_start_time", None)
    absolute_end = getattr(args, "absolute_end_time", None)
    if (start_time is not None and start_time < 0) or (end_time is not None and end_time < 0):
        raise ValueError("Report window times must not be negative")
    if start_time is not None and end_time is not None and start_time > end_time:
        raise ValueError("Report start time must not exceed end time")
    if absolute_start is not None and absolute_start < 0 or absolute_end is not None and absolute_end < 0:
        raise ValueError("Absolute fight times must not be negative")
    if absolute_start is not None and absolute_end is not None and absolute_start > absolute_end:
        raise ValueError("Absolute fight start time must not exceed end time")
    _enum(getattr(args, "kill_type", None), KILL_TYPES, "kill type")
    _enum(
        getattr(args, "data_type", None),
        TABLE_DATA_TYPES if args.report_command == "table" else GRAPH_DATA_TYPES,
        "data type",
    )
    _enum(getattr(args, "hostility_type", None), HOSTILITY_TYPES, "hostility type")
    _enum(getattr(args, "view_by", None), VIEW_TYPES, "view type")
    _enum(getattr(args, "compare", None), RANKING_COMPARE_TYPES, "ranking comparison")
    _enum(getattr(args, "timeframe", None), RANKING_TIMEFRAMES, "ranking timeframe")
    _enum(getattr(args, "player_metric", None), RANKING_METRICS, "ranking metric")

    variables = {"code": reference.code, "allowUnlisted": False}
    variable_names = {
        "start_time": "startTime", "end_time": "endTime", "difficulty": "difficulty",
        "encounter_id": "encounterID", "kill_type": "killType", "data_type": "dataType",
        "ability_id": "abilityID", "death": "death", "filter_expression": "filterExpression",
        "source_auras_absent": "sourceAurasAbsent", "source_auras_present": "sourceAurasPresent",
        "source_class": "sourceClass", "source_id": "sourceID", "source_instance_id": "sourceInstanceID",
        "target_auras_absent": "targetAurasAbsent", "target_auras_present": "targetAurasPresent",
        "target_class": "targetClass", "target_id": "targetID", "target_instance_id": "targetInstanceID",
        "wipe_cutoff": "wipeCutoff", "view_options": "viewOptions",
        "hostility_type": "hostilityType", "view_by": "viewBy", "compare": "compare",
        "player_metric": "playerMetric", "timeframe": "timeframe", "translate": "translate",
    }
    for attribute, variable_name in variable_names.items():
        value = getattr(args, attribute, None)
        if value is not None:
            variables[variable_name] = value
    if fight_id is not None and args.report_command not in ("summary", "master-data"):
        variables["fightIDs"] = [fight_id]

    scope = {"report_code": reference.code}
    if fight_id is not None:
        scope["fight_id"] = fight_id
    if start_time is not None:
        scope["start_time"] = start_time
    if end_time is not None:
        scope["end_time"] = end_time
    if absolute_start is not None:
        scope["absolute_start_time"] = absolute_start
    if absolute_end is not None:
        scope["absolute_end_time"] = absolute_end
    if getattr(args, "time_mode", None) is not None:
        scope["time_mode"] = args.time_mode
    filters = {
        variable_name: value
        for attribute, variable_name in variable_names.items()
        for value in (getattr(args, attribute, None),)
        if value is not None and attribute not in ("start_time", "end_time")
    }
    return reference, variables, scope, filters


def select_fights(fights, report_start_ms, start_ms=None, end_ms=None, mode="started") -> list:
    if mode not in ("started", "overlap", "completed"):
        raise ValueError("Invalid fight time mode")
    if isinstance(report_start_ms, bool) or not isinstance(report_start_ms, (int, float)):
        raise ValueError("Report startTime is required for fight time derivation")
    if start_ms is not None and start_ms < 0 or end_ms is not None and end_ms < 0:
        raise ValueError("Absolute fight times must not be negative")
    if start_ms is not None and end_ms is not None and start_ms > end_ms:
        raise ValueError("Absolute fight start time must not exceed end time")
    selected = []
    for fight in _items(fights):
        if not isinstance(fight, Mapping):
            continue
        start = fight.get("startTime")
        end = fight.get("endTime")
        if (
            isinstance(start, bool) or not isinstance(start, (int, float)) or
            isinstance(end, bool) or not isinstance(end, (int, float)) or end < start
        ):
            continue
        absolute_start = report_start_ms + start
        absolute_end = report_start_ms + end
        if mode == "started":
            matches = (start_ms is None or absolute_start >= start_ms) and (end_ms is None or absolute_start <= end_ms)
        elif mode == "overlap":
            matches = (start_ms is None or absolute_end >= start_ms) and (end_ms is None or absolute_start < end_ms)
        else:
            matches = (start_ms is None or absolute_end >= start_ms) and (end_ms is None or absolute_end <= end_ms)
        if matches:
            selected.append(dict(fight, startTime=absolute_start, endTime=absolute_end))
    return selected


def report_data(payload: Mapping[str, object], kind: str, absolute_start=None, absolute_end=None, time_mode="started"):
    report = payload["data"]["reportData"]["report"]
    if not isinstance(report, Mapping):
        raise TypeError("Report was not an object")
    archive_status = report.get("archiveStatus")
    accessible = isinstance(archive_status, Mapping) and archive_status.get("isAccessible") is True
    if str(report.get("visibility", "")).casefold() != "public" or not accessible:
        raise PublicReportError("Report is not public or accessible")
    if kind == "summary":
        return dict(report)
    field = {"master-data": "masterData", "player-details": "playerDetails"}.get(kind, kind)
    value = report[field]
    if kind == "fights" and isinstance(value, list):
        report_start = report.get("startTime")
        if isinstance(report_start, bool) or not isinstance(report_start, (int, float)):
            raise ValueError("Report startTime is required for fight time derivation")
        return select_fights(value, report_start, absolute_start, absolute_end, time_mode)
    return value


def _pagination_data(payload: Mapping[str, object], path: Sequence[str]) -> Tuple[dict, list, dict]:
    value = payload
    for key in path:
        value = value[key]
    if not isinstance(value, Mapping):
        raise TypeError("Report pagination was not an object")
    data = value.get("data")
    if not isinstance(data, list):
        raise TypeError("Report pagination data was not a list")
    pagination = {
        "current_page": value.get("current_page", value.get("currentPage")),
        "last_page": value.get("last_page", value.get("lastPage")),
        "has_more_pages": value.get("has_more_pages", value.get("hasMorePages", False)),
    }
    return dict(value), list(data), pagination


def _public_report_payload(payload: Mapping[str, object], field: str):
    report = payload["data"]["reportData"]["report"]
    if not isinstance(report, Mapping):
        raise TypeError("Report was not an object")
    value = report.get(field)
    if field == "fights":
        return _items(value)
    if field == "masterData":
        return dict(value) if isinstance(value, Mapping) else {"actors": []}
    return value


def hydrate_discovery_report(client, code: str, filters: DiscoveryFilters, fight_id: Optional[int] = None) -> Tuple[list, list]:
    """Fetch only the report data needed by derived discovery filters."""
    if not filters.needs_hydration and fight_id is None:
        return [], []
    common = {"code": code, "allowUnlisted": False, "translate": True}
    if fight_id is not None:
        common["fightIDs"] = [fight_id]
    fights = []
    actors = []
    if filters.needs_hydration or fight_id is not None:
        fights_payload = client.execute("report-fights", common)
        if fights_payload.get("errors"):
            raise PartialGraphQLError(fights_payload["errors"])
        fights = _public_report_payload(fights_payload, "fights")
        if fight_id is not None:
            fights = [fight for fight in fights if fight.get("id") == fight_id]
    if filters.class_name is not None or filters.spec_name is not None or filters.role is not None:
        master_payload = client.execute("report-master-data", common)
        if master_payload.get("errors"):
            raise PartialGraphQLError(master_payload["errors"])
        master = _public_report_payload(master_payload, "masterData")
        actors = _items(master.get("actors")) if isinstance(master, Mapping) else []
    return fights, actors


def _event_page(payload: Mapping[str, object]) -> dict:
    report = payload["data"]["reportData"]["report"]
    if not isinstance(report, Mapping):
        raise TypeError("Report was not an object")
    if "visibility" in report or "archiveStatus" in report:
        archive_status = report.get("archiveStatus")
        accessible = isinstance(archive_status, Mapping) and archive_status.get("isAccessible") is True
        if str(report.get("visibility", "")).casefold() != "public" or not accessible:
            raise PublicReportError("Report is not public or accessible")
    events = report["events"]
    if not isinstance(events, Mapping) or not isinstance(events.get("data"), list):
        raise TypeError("Report events were not a list")
    cursor = events.get("nextPageTimestamp")
    if cursor is not None and not isinstance(cursor, (int, float)):
        raise TypeError("Report event cursor was not numeric")
    result = {"data": list(events["data"]), "nextPageTimestamp": cursor}
    if payload.get("errors"):
        result["errors"] = payload["errors"]
    return result


def iter_event_pages(client, code, variables, max_pages=EVENT_MAX_PAGES):
    if not isinstance(max_pages, int) or isinstance(max_pages, bool) or max_pages < 1:
        raise ValueError("Event max pages must be a positive integer")
    request = dict(variables)
    fight_ids = request.get("fightIDs")
    if "fightIDs" in request and (
        not isinstance(fight_ids, list) or not fight_ids or
        any(not isinstance(fight_id, int) or isinstance(fight_id, bool) or fight_id < 1 for fight_id in fight_ids)
    ):
        raise ValueError("Report fight must be a positive integer")
    has_fight = "fightIDs" in request
    has_window = request.get("startTime") is not None and request.get("endTime") is not None
    if not has_fight and not has_window:
        raise ValueError("Event download requires a fight ID or both startTime and endTime")
    for bound_name in ("startTime", "endTime"):
        bound = request.get(bound_name)
        if bound is not None and (
            isinstance(bound, bool) or not isinstance(bound, (int, float)) or not math.isfinite(bound) or bound < 0
        ):
            raise ValueError("Event window bounds must be finite, numeric, and non-negative")
    if has_window and request["startTime"] > request["endTime"]:
        raise ValueError("Report start time must not exceed end time")
    limit = request.get("limit", EVENT_PAGE_LIMIT)
    if not isinstance(limit, int) or isinstance(limit, bool) or not 100 <= limit <= EVENT_PAGE_LIMIT:
        raise ValueError("Event limit must be between 100 and 10000")
    request["code"] = code
    request["limit"] = limit
    current_start = request.get("startTime")
    previous_cursor = current_start if current_start is not None else 0
    for unused_page_number in range(max_pages):
        if current_start is None:
            request.pop("startTime", None)
        else:
            request["startTime"] = current_start
        page = _event_page(client.execute("report-events", request))
        cursor = page["nextPageTimestamp"]
        if cursor is not None and previous_cursor is not None and cursor <= previous_cursor:
            raise RuntimeError("Event pagination cursor did not advance")
        yield page
        if cursor is None:
            return
        end_time = request.get("endTime")
        if end_time is not None and cursor >= end_time:
            return
        previous_cursor = cursor
        current_start = cursor


def write_event_jsonl(path, metadata, events):
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary_name = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=str(destination.parent),
            prefix=destination.name + ".", suffix=".tmp", delete=False,
        ) as temporary:
            temporary_name = temporary.name
            temporary.write(json.dumps({"type": "metadata", "metadata": dict(metadata)}, ensure_ascii=False, separators=(",", ":")) + "\n")
            for event in events:
                temporary.write(json.dumps({"type": "event", "event": event}, ensure_ascii=False, separators=(",", ":")) + "\n")
        os.replace(temporary_name, str(destination))
        temporary_name = None
    finally:
        if temporary_name:
            try:
                os.unlink(temporary_name)
            except OSError:
                pass


def event_request(args) -> tuple:
    reference = parse_report_reference(args.reference)
    fight_id = args.fight if args.fight is not None else reference.fight_id
    if fight_id is not None and fight_id < 1:
        raise ValueError("Report fight must be a positive integer")
    start_time = args.start_time
    end_time = args.end_time
    if (start_time is not None and start_time < 0) or (end_time is not None and end_time < 0):
        raise ValueError("Report window times must not be negative")
    if start_time is not None and end_time is not None and start_time > end_time:
        raise ValueError("Report start time must not exceed end time")
    if fight_id is None and (start_time is None or end_time is None):
        raise ValueError("Event download requires a fight ID or both startTime and endTime")
    if not 100 <= args.event_limit <= EVENT_PAGE_LIMIT:
        raise ValueError("Event limit must be between 100 and 10000")
    if args.max_pages < 1:
        raise ValueError("Event max pages must be a positive integer")
    variables = {"allowUnlisted": False, "limit": args.event_limit}
    if fight_id is not None:
        variables["fightIDs"] = [fight_id]
    if start_time is not None:
        variables["startTime"] = start_time
    if end_time is not None:
        variables["endTime"] = end_time
    for attribute, variable_name in (
        ("data_type", "dataType"), ("source_id", "sourceID"), ("target_id", "targetID"),
        ("ability_id", "abilityID"), ("hostility_type", "hostilityType"),
        ("filter_expression", "filterExpression"), ("include_resources", "includeResources"),
        ("use_actor_ids", "useActorIDs"), ("use_ability_ids", "useAbilityIDs"),
    ):
        value = getattr(args, attribute)
        if value is not None:
            variables[variable_name] = value
    scope = {"report_code": reference.code}
    if fight_id is not None:
        scope["fight_id"] = fight_id
    if start_time is not None:
        scope["start_time"] = start_time
    if end_time is not None:
        scope["end_time"] = end_time
    filters = {
        key: variables[key]
        for key in variables
        if key not in ("allowUnlisted", "fightIDs", "startTime", "endTime", "limit")
    }
    return reference, variables, scope, filters
