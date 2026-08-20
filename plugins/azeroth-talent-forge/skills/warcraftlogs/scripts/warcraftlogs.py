import argparse
import base64
import hashlib
import json
import math
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

CLIENT_ID_ENV = "WARCRAFTLOGS_CLIENT_ID"
CLIENT_SECRET_ENV = "WARCRAFTLOGS_CLIENT_SECRET"
TOKEN_URL = "https://www.warcraftlogs.com/oauth/token"
GRAPHQL_URL = "https://www.warcraftlogs.com/api/v2/client"
QUERY_NAME = re.compile(r"^[a-z0-9-]+$")
REPORT_CODE = re.compile(r"^[A-Za-z0-9]{8,32}$")
REPORT_HOSTS = frozenset((
    "warcraftlogs.com", "www.warcraftlogs.com", "classic.warcraftlogs.com",
    "cn.warcraftlogs.com", "de.warcraftlogs.com", "es.warcraftlogs.com",
    "fr.warcraftlogs.com", "it.warcraftlogs.com", "ko.warcraftlogs.com",
    "pt.warcraftlogs.com", "ru.warcraftlogs.com", "tw.warcraftlogs.com",
    "cn.classic.warcraftlogs.com", "de.classic.warcraftlogs.com",
    "es.classic.warcraftlogs.com", "fr.classic.warcraftlogs.com",
    "it.classic.warcraftlogs.com", "ko.classic.warcraftlogs.com",
    "pt.classic.warcraftlogs.com", "ru.classic.warcraftlogs.com",
    "tw.classic.warcraftlogs.com",
))
METADATA_TTL_SECONDS = 24 * 60 * 60
REPORT_KINDS = ("summary", "fights", "master-data", "player-details", "table", "graph", "rankings")
GLOBAL_TOP_MIN = 1
GLOBAL_TOP_MAX = 100
GLOBAL_MAX_PAGES = 5
GLOBAL_WARNING = "Global discovery is ranking-based and not an exhaustive list of public reports."
TABLE_DATA_TYPES = (
    "Summary", "DamageDone", "DamageTaken", "Healing", "Casts", "Summons", "Buffs",
    "Debuffs", "Deaths", "Interrupts", "Dispels", "Resources", "ResourcesGained", "Threat",
)
GRAPH_DATA_TYPES = (
    "DamageDone", "DamageTaken", "Healing", "Casts", "Buffs", "Debuffs", "Deaths",
    "Interrupts", "Dispels", "Resources", "ResourcesGained",
)
KILL_TYPES = ("All", "Encounters", "Kills", "Trash", "Wipes")
HOSTILITY_TYPES = ("Friendlies", "Enemies")
VIEW_TYPES = ("Source", "Target", "Ability")
RANKING_COMPARE_TYPES = ("Rankings", "Parses")
RANKING_TIMEFRAMES = ("Historical", "Today")
RANKING_METRICS = ("bossdps", "dps", "hps", "playerspeed", "execution")


class AuthenticationError(RuntimeError):
    pass


class ApiError(RuntimeError):
    pass


class PublicReportError(RuntimeError):
    pass


class PartialGraphQLError(RuntimeError):
    def __init__(self, errors):
        super().__init__("GraphQL response contained errors")
        self.errors = list(errors or [])


@dataclass(frozen=True)
class Credentials:
    client_id: str
    client_secret: str


@dataclass(frozen=True)
class ReportReference:
    code: str
    fight_id: Optional[int]


@dataclass(frozen=True)
class DiscoveryFilters:
    class_name: Optional[str] = None
    spec_name: Optional[str] = None
    role: Optional[str] = None
    instance: Optional[int] = None
    zone: Optional[int] = None
    encounter: Optional[int] = None
    season: Optional[int] = None
    partition: Optional[int] = None
    key_min: Optional[int] = None
    key_max: Optional[int] = None
    affixes: Optional[Sequence[object]] = None
    timed: Optional[bool] = None
    depleted: Optional[bool] = None
    difficulty: Optional[int] = None
    kill: Optional[bool] = None
    wipe: Optional[bool] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None

    @property
    def needs_hydration(self) -> bool:
        return any(getattr(self, field) is not None for field in (
            "class_name", "spec_name", "role", "encounter", "season", "partition",
            "key_min", "key_max", "affixes", "timed", "depleted", "difficulty", "kill", "wipe",
        ))

    def direct_variables(self) -> dict:
        variables = {}
        if self.start_time is not None:
            variables["startTime"] = self.start_time
        if self.end_time is not None:
            variables["endTime"] = self.end_time
        if self.instance is not None:
            variables["zoneID"] = self.instance
        if self.zone is not None:
            variables["gameZoneID"] = self.zone
        return variables


_DISCOVERY_FILTER_FIELDS = (
    "class_name", "spec_name", "role", "instance", "zone", "encounter", "season", "partition",
    "key_min", "key_max", "affixes", "timed", "depleted", "difficulty", "kill", "wipe",
    "start_time", "end_time",
)


def _casefold(value) -> str:
    return str(value).casefold() if value is not None else ""


def _items(value) -> list:
    return value if isinstance(value, list) else []


def _report_fights(fights) -> list:
    if isinstance(fights, Mapping):
        fights = fights.get("fights", fights.get("data", []))
    return _items(fights)


def _actor_candidates(fights, actors) -> list:
    if isinstance(actors, Mapping):
        actors = actors.get("actors", [])
    actors = _items(actors)
    ids = {player for fight in _report_fights(fights) for player in _items(fight.get("friendlyPlayers"))}
    if ids:
        selected = [actor for actor in actors if actor.get("id") in ids]
        if selected:
            return selected
    return actors


def _actor_field_matches(actor, requested, fields) -> bool:
    wanted = _casefold(requested)
    for field in fields:
        value = actor.get(field)
        if isinstance(value, Mapping):
            value = value.get("name") or value.get("slug") or value.get("id")
        if wanted and wanted in _casefold(value):
            return True
    return False


def _actor_role_matches(actor, requested) -> bool:
    if _actor_field_matches(actor, requested, ("role", "roles")):
        return True
    if _casefold(requested) not in ("tank", "healer", "dps", "damage"):
        return False
    subtype = _casefold(actor.get("subType") or actor.get("specName") or actor.get("spec"))
    if _casefold(requested) == "tank":
        return any(value in subtype for value in ("protection", "guardian", "blood", "vengeance", "brewmaster"))
    if _casefold(requested) == "healer":
        return any(value in subtype for value in ("holy", "discipline", "restoration", "mistweaver", "preservation", "devotion"))
    return subtype != "" and not any(value in subtype for value in ("protection", "guardian", "blood", "vengeance", "brewmaster", "holy", "discipline", "restoration", "mistweaver", "preservation", "devotion"))


def _fight_status(fight) -> Tuple[bool, bool]:
    level = fight.get("keystoneLevel")
    bonus = fight.get("keystoneBonus")
    if level is None or bonus is None:
        return False, False
    if bonus in (1, 2, 3):
        return True, False
    return False, True


def report_matches(report, fights, actors, filters: DiscoveryFilters, character_name=None) -> Tuple[bool, List[str]]:
    """Return whether a discovered report matches, with stable filter-name reasons."""
    fights = _report_fights(fights)
    actors = _actor_candidates(fights, actors)
    reasons = []
    if character_name is not None and any(
        value is not None for value in (filters.class_name, filters.spec_name, filters.role)
    ):
        normalized_character = normalize_name(character_name)
        canonical_actors = [
            actor for actor in actors
            if isinstance(actor.get("name"), str) and normalize_name(actor["name"]) == normalized_character
        ]
        if len(canonical_actors) != 1:
            reasons.append("character_identity")
            actors = []
        else:
            actors = canonical_actors
    if filters.class_name is not None and not any(_actor_field_matches(a, filters.class_name, ("className", "class", "subType")) for a in actors):
        reasons.append("class_name")
    if filters.spec_name is not None and not any(_actor_field_matches(a, filters.spec_name, ("specName", "spec", "subType")) for a in actors):
        reasons.append("spec_name")
    if filters.role is not None and not any(_actor_role_matches(a, filters.role) for a in actors):
        reasons.append("role")
    fight_instance_ids = [
        fight.get("zoneID", fight.get("zone", {}).get("id") if isinstance(fight.get("zone"), Mapping) else None)
        for fight in fights
    ]
    fight_instance_ids.extend(
        fight.get("gameZoneID", fight.get("gameZone", {}).get("id") if isinstance(fight.get("gameZone"), Mapping) else None)
        for fight in fights
    )
    if filters.instance is not None and not (
        report.get("zoneID", report.get("zone", {}).get("id") if isinstance(report.get("zone"), Mapping) else None) == filters.instance
        or filters.instance in fight_instance_ids
    ):
        reasons.append("instance")
    fight_game_zone_ids = [
        fight.get("gameZoneID", fight.get("gameZone", {}).get("id") if isinstance(fight.get("gameZone"), Mapping) else None)
        for fight in fights
    ]
    if filters.zone is not None and not (
        report.get("gameZoneID", report.get("gameZone", {}).get("id") if isinstance(report.get("gameZone"), Mapping) else None) == filters.zone
        or filters.zone in fight_game_zone_ids
    ):
        reasons.append("zone")
    if filters.encounter is not None and not any(f.get("encounterID") == filters.encounter for f in fights):
        reasons.append("encounter")
    if filters.season is not None and not any(f.get("season") == filters.season or report.get("season") == filters.season for f in fights):
        reasons.append("season")
    if filters.partition is not None and not any(f.get("partition") == filters.partition or report.get("partition") == filters.partition for f in fights):
        reasons.append("partition")
    levels = [f.get("keystoneLevel") for f in fights if isinstance(f.get("keystoneLevel"), (int, float))]
    if filters.key_min is not None and not any(level >= filters.key_min for level in levels):
        reasons.append("key_min")
    if filters.key_max is not None and not any(level <= filters.key_max for level in levels):
        reasons.append("key_max")
    if filters.affixes:
        affix_values = [
            value for fight in fights for value in _items(fight.get("keystoneAffixes"))
        ]
        def has_affix(requested):
            return any(
                (isinstance(requested, int) and isinstance(value, Mapping) and value.get("id") == requested)
                or (_casefold(requested) == _casefold(value.get("name") if isinstance(value, Mapping) else value))
                for value in affix_values
            )
        if not all(has_affix(value) for value in filters.affixes):
            reasons.append("affixes")
    timed_values = [_fight_status(f)[0] for f in fights]
    depleted_values = [_fight_status(f)[1] for f in fights]
    if filters.timed is not None and (not timed_values or filters.timed not in timed_values):
        reasons.append("timed")
    if filters.depleted is not None and (not depleted_values or filters.depleted not in depleted_values):
        reasons.append("depleted")
    if filters.difficulty is not None and not any(f.get("difficulty") == filters.difficulty for f in fights):
        reasons.append("difficulty")
    if filters.kill is not None and not any(f.get("kill") is filters.kill for f in fights):
        reasons.append("kill")
    if filters.wipe is not None and not any((f.get("kill") is False) is filters.wipe for f in fights):
        reasons.append("wipe")
    if filters.start_time is not None and (report.get("endTime") is None or report.get("endTime") < filters.start_time):
        reasons.append("start_time")
    if filters.end_time is not None and (report.get("startTime") is None or report.get("startTime") > filters.end_time):
        reasons.append("end_time")
    return not reasons, reasons


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


def load_dotenv(path: Path) -> Dict[str, str]:
    values = {}
    if not path.is_file():
        return values
    for number, raw_line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            raise ValueError("Malformed .env entry at line %d" % number)
        key, value = line.split("=", 1)
        key = key.strip()
        if key not in (CLIENT_ID_ENV, CLIENT_SECRET_ENV):
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return values


def resolve_credentials(
    client_id: Optional[str],
    client_secret: Optional[str],
    env_file: Optional[str],
    cwd: Path,
    environ: Mapping[str, str],
) -> Credentials:
    dotenv = load_dotenv(Path(env_file) if env_file else cwd / ".env")
    resolved_id = client_id or dotenv.get(CLIENT_ID_ENV) or environ.get(CLIENT_ID_ENV)
    resolved_secret = client_secret or dotenv.get(CLIENT_SECRET_ENV) or environ.get(CLIENT_SECRET_ENV)
    missing = [name for name, value in ((CLIENT_ID_ENV, resolved_id), (CLIENT_SECRET_ENV, resolved_secret)) if not value]
    if missing:
        raise ValueError("Missing credential: %s" % ", ".join(missing))
    return Credentials(resolved_id, resolved_secret)


def load_query(name: str, query_dir: Optional[Path] = None) -> str:
    if not QUERY_NAME.fullmatch(name):
        raise ValueError("Invalid query name")
    directory = query_dir or Path(__file__).resolve().parent / "graphql"
    return (directory / (name + ".graphql")).read_text(encoding="utf-8")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sanitize_graphql_errors(errors) -> List[dict]:
    sanitized = []
    for error in errors or []:
        if not isinstance(error, Mapping):
            continue
        value = {}
        if "message" in error:
            value["message"] = error["message"]
        if "path" in error:
            value["path"] = error["path"]
        extensions = error.get("extensions")
        if isinstance(extensions, Mapping) and "code" in extensions:
            value["extensions"] = {"code": extensions["code"]}
        sanitized.append(value)
    return sanitized


class WarcraftLogsClient:
    def __init__(self, credentials: Credentials, opener=None, sleep=None):
        self.credentials = credentials
        self.opener = opener or urllib.request.urlopen
        self.sleep = sleep or time.sleep
        self._token = None
        self._token_expires_at = 0.0

    def _open_json(self, request) -> dict:
        for attempt in range(3):
            try:
                with self.opener(request) as response:
                    try:
                        payload = json.loads(response.read().decode("utf-8"))
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        raise ApiError("Response was not valid JSON")
                    if not isinstance(payload, dict):
                        raise ApiError("Response JSON must be an object")
                    return payload
            except urllib.error.HTTPError as error:
                retryable = error.code == 429 or 500 <= error.code < 600
                if not retryable or attempt == 2:
                    raise ApiError("HTTP request failed with status %d" % error.code)
                retry_after = error.headers.get("Retry-After") if error.headers else None
                self.sleep(int(retry_after) if retry_after and retry_after.isdigit() else 0)
            except urllib.error.URLError:
                raise ApiError("Network request failed")
            except OSError:
                raise ApiError("Response read failed")
        raise ApiError("HTTP request failed")

    def access_token(self) -> str:
        if self._token and time.time() < self._token_expires_at - 30:
            return self._token
        encoded = base64.b64encode(
            (self.credentials.client_id + ":" + self.credentials.client_secret).encode("utf-8")
        ).decode("ascii")
        request = urllib.request.Request(
            TOKEN_URL,
            data=urllib.parse.urlencode({"grant_type": "client_credentials"}).encode("ascii"),
            headers={"Authorization": "Basic " + encoded},
            method="POST",
        )
        try:
            payload = self._open_json(request)
            self._token = str(payload["access_token"])
            self._token_expires_at = time.time() + int(payload.get("expires_in", 3600))
        except (ApiError, KeyError, TypeError, ValueError):
            raise AuthenticationError("OAuth authentication failed")
        return self._token

    def execute(self, query_name: str, variables: Mapping[str, object]) -> dict:
        body = json.dumps(
            {"query": load_query(query_name), "variables": dict(variables)},
            separators=(",", ":"),
        ).encode("utf-8")
        request = urllib.request.Request(
            GRAPHQL_URL,
            data=body,
            headers={
                "Authorization": "Bearer " + self.access_token(),
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            return self._open_json(request)
        except ApiError:
            raise ApiError("Warcraft Logs API request failed")


def normalize_rate_limit(payload: Mapping[str, object]) -> dict:
    value = payload["data"]["rateLimitData"]
    return {
        "limit_per_hour": value["limitPerHour"],
        "points_spent_this_hour": value["pointsSpentThisHour"],
        "points_reset_in": value["pointsResetIn"],
    }


def normalize_name(value) -> str:
    if not isinstance(value, str):
        raise ValueError("Name must be a string")
    return re.sub(r"[\s-]+", " ", value.casefold()).strip()


def select_named(items, name, kind) -> dict:
    exact = [item for item in items if isinstance(item, Mapping) and item.get("name") == name]
    if len(exact) == 1:
        return dict(exact[0])
    normalized = normalize_name(name)
    matches = [
        item
        for item in items
        if isinstance(item, Mapping) and isinstance(item.get("name"), str) and normalize_name(item["name"]) == normalized
    ]
    if len(matches) == 1:
        return dict(matches[0])
    if len(matches) > 1:
        names = ", ".join(str(item["name"]) for item in matches)
        raise ValueError("Ambiguous %s: %s" % (kind, names))
    raise ValueError("Unknown %s: %s" % (kind, name))


def default_metadata_cache_dir() -> Path:
    if os.name == "nt":
        local_app_data = os.environ.get("LOCALAPPDATA")
        root = Path(local_app_data) if local_app_data else Path.home() / ".cache"
    else:
        xdg_cache_home = os.environ.get("XDG_CACHE_HOME")
        root = Path(xdg_cache_home) if xdg_cache_home else Path.home() / ".cache"
    return root / "azeroth-talent-forge" / "warcraftlogs"


def _records(items, fields) -> List[dict]:
    if not isinstance(items, list):
        raise TypeError("Metadata collection was not a list")
    result = []
    for item in items:
        if not isinstance(item, Mapping):
            raise TypeError("Metadata collection item was not an object")
        result.append({field: item[field] for field in fields if field in item})
    return result


def _normalize_world(payload: Mapping[str, object]) -> dict:
    world = payload["data"]["worldData"]
    if not isinstance(world, Mapping):
        raise TypeError("World metadata was not an object")
    zones = []
    for zone in _records(world["zones"], ("id", "name", "difficulties", "encounters", "partitions")):
        zone["difficulties"] = _records(zone.get("difficulties", []), ("id", "name"))
        zone["encounters"] = _records(zone.get("encounters", []), ("id", "name"))
        zone["partitions"] = _records(zone.get("partitions", []), ("id", "name"))
        zones.append(zone)
    return {
        "regions": _records(world["regions"], ("id", "name", "slug")),
        "expansions": _records(world["expansions"], ("id", "name")),
        "zones": zones,
    }


def _normalize_game(payload: Mapping[str, object]) -> dict:
    game = payload["data"]["gameData"]
    if not isinstance(game, Mapping):
        raise TypeError("Game metadata was not an object")
    classes = []
    for game_class in _records(game["classes"], ("id", "name", "slug", "specs")):
        game_class["specs"] = _records(game_class.get("specs", []), ("id", "name", "slug"))
        classes.append(game_class)
    return {
        "classes": classes,
        "affixes": _records(game["affixes"], ("id", "name")),
        "abilities": _records(game["abilities"]["data"], ("id", "name")),
    }


def _normalize_realm(payload: Mapping[str, object]) -> dict:
    world = payload["data"]["worldData"]
    if not isinstance(world, Mapping) or not isinstance(world["server"], Mapping):
        raise TypeError("Realm metadata was not an object")
    server = world["server"]
    result = {
        field: server[field]
        for field in ("id", "name", "normalizedName", "slug")
        if field in server
    }
    for field in ("region", "subregion"):
        if field in server:
            result[field] = _records([server[field]], ("id", "name", "slug"))[0]
    return result


class MetadataResolver:
    def __init__(self, client, cache: Optional[Path] = None, no_cache: bool = False, now=None):
        self.client = client
        self.cache = Path(cache) if cache is not None else default_metadata_cache_dir()
        self.no_cache = no_cache
        self.now = now or time.time
        self.errors = []

    def _cache_path(self, query_name: str, variables: Mapping[str, object]) -> Path:
        encoded = json.dumps(dict(variables), sort_keys=True, separators=(",", ":")).encode("utf-8")
        return self.cache / (query_name + "-" + hashlib.sha256(encoded).hexdigest() + ".json")

    def _query(self, query_name: str, variables: Mapping[str, object]) -> tuple:
        cache_path = self._cache_path(query_name, variables)
        if not self.no_cache and cache_path.is_file():
            try:
                cached = json.loads(cache_path.read_text(encoding="utf-8"))
                if isinstance(cached, Mapping) and cached["expires_at"] > self.now() and isinstance(cached["payload"], Mapping):
                    payload = cached["payload"]
                    self.errors = payload.get("errors", [])
                    return payload, {"status": "hit"}
            except (KeyError, TypeError, ValueError, OSError):
                pass
        payload = self.client.execute(query_name, variables)
        if not isinstance(payload, Mapping):
            raise TypeError("Metadata response was not an object")
        self.errors = payload.get("errors", [])
        if not self.no_cache:
            self.cache.mkdir(parents=True, exist_ok=True)
            fetched_at = self.now()
            temporary = cache_path.with_suffix(cache_path.suffix + ".tmp")
            temporary.write_text(
                json.dumps(
                    {"variables": dict(variables), "payload": payload, "fetched_at": fetched_at, "expires_at": fetched_at + METADATA_TTL_SECONDS},
                    ensure_ascii=True,
                    separators=(",", ":"),
                ),
                encoding="utf-8",
            )
            temporary.replace(cache_path)
        return payload, {"status": "bypassed" if self.no_cache else "miss"}

    def world(self, variables: Mapping[str, object]) -> tuple:
        payload, provenance = self._query("metadata-world", variables)
        return _normalize_world(payload), provenance

    def game(self, variables: Mapping[str, object]) -> tuple:
        payload, provenance = self._query("metadata-game", variables)
        return _normalize_game(payload), provenance

    def realm(self, region, name) -> tuple:
        if not isinstance(region, str) or not region.strip():
            raise ValueError("Realm lookup requires region")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Realm lookup requires name")
        slug = normalize_name(name).replace(" ", "-")
        payload, provenance = self._query("metadata-realm", {"region": region.strip(), "slug": slug})
        return _normalize_realm(payload), provenance


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


def _add_report_options(parser, window=False, translate=False) -> None:
    parser.add_argument("reference", help="report code or official Warcraft Logs report URL")
    parser.add_argument("--fight", type=int)
    if window:
        parser.add_argument("--start-time", type=float)
        parser.add_argument("--end-time", type=float)
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
    if (start_time is not None and start_time < 0) or (end_time is not None and end_time < 0):
        raise ValueError("Report window times must not be negative")
    if start_time is not None and end_time is not None and start_time > end_time:
        raise ValueError("Report start time must not exceed end time")
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
        "source_pet_type": "sourcePetType", "source_spec": "sourceSpec",
        "target_auras_absent": "targetAurasAbsent", "target_auras_present": "targetAurasPresent",
        "target_class": "targetClass", "target_id": "targetID", "target_instance_id": "targetInstanceID",
        "target_pet_type": "targetPetType", "target_spec": "targetSpec", "wipe_cutoff": "wipeCutoff",
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
    filters = {
        variable_name: value
        for attribute, variable_name in variable_names.items()
        for value in (getattr(args, attribute, None),)
        if value is not None and attribute not in ("start_time", "end_time")
    }
    return reference, variables, scope, filters


def report_data(payload: Mapping[str, object], kind: str):
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
    return report[field]


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


def _global_world(client, expansion_id):
    return _normalize_world(client.execute("metadata-world", {"expansionId": expansion_id}))


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
    for bound_name in ("start_time", "end_time"):
        value = values[bound_name]
        if value is not None and (not math.isfinite(value) or value < 0):
            raise ValueError("Discovery time bounds must be finite and non-negative")
    if values["start_time"] is not None and values["end_time"] is not None and values["start_time"] > values["end_time"]:
        raise ValueError("Discovery start time must not exceed end time")
    if values["key_min"] is not None and values["key_min"] < 0 or values["key_max"] is not None and values["key_max"] < 0:
        raise ValueError("Key bounds must be non-negative")
    if values["key_min"] is not None and values["key_max"] is not None and values["key_min"] > values["key_max"]:
        raise ValueError("Key minimum must not exceed key maximum")
    return DiscoveryFilters(**values)


def discover_reports(client, kind: str, identity: Mapping[str, str], filters: DiscoveryFilters, page: int, limit: int, max_pages: int = 1) -> dict:
    if kind not in ("character", "guild"):
        raise ValueError("Unknown discovery kind")
    if page < 1 or max_pages < 1:
        raise ValueError("Discovery page and max pages must be positive")
    if not 1 <= limit <= 100:
        raise ValueError("Discovery limit must be between 1 and 100")
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
    return {
        "data": matched,
        "candidate_count": len(reports),
        "hydrated_count": hydrated_count,
        "matched_count": len(matched),
        "excluded_count": len(reports) - len(matched),
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


def make_global_result(rows, sample_size, filters, ranking_basis="encounter_rankings", **metadata) -> dict:
    if not isinstance(sample_size, int) or isinstance(sample_size, bool) or sample_size < 0:
        raise ValueError("Global top must be a non-negative integer")
    candidates = _dedupe_global_candidates(rows)
    data = candidates[:sample_size]
    truncated = bool(metadata.get("truncated", len(candidates) > sample_size))
    result = make_envelope(
        "find global",
        {"ranking_basis": ranking_basis},
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
    if metadata.get("exclusion_reasons"):
        result["exclusion_reasons"] = dict(metadata["exclusion_reasons"])
    if metadata.get("errors"):
        result["partial"] = True
        result["errors"] = sanitize_graphql_errors(metadata["errors"])
    return result


def discover_global(client, filters: DiscoveryFilters, top: int, page: int, max_pages: int = 1,
                    metric=None, leaderboard=None, server_region=None, server_slug=None,
                    expansion_id=11) -> dict:
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
            return make_global_result([], top, _filters_dict(filters), errors=[{"message": str(error)}])
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
            return make_global_result([], top, _filters_dict(filters), errors=[{"message": str(error)}])
    variables = {
        "encounterID": filters.encounter,
        "zoneID": zone_id,
        "page": page,
        "size": top,
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
    while pages_fetched < max_pages and len(_dedupe_global_candidates(rows)) < top:
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
    for row in rows:
        if _ranking_candidate(row) is None:
            report = row.get("report") if isinstance(row, Mapping) else None
            code = row.get("reportID", row.get("reportCode")) if isinstance(row, Mapping) else None
            if isinstance(report, Mapping):
                code = code or report.get("code") or report.get("id")
            if code is not None:
                invalid_candidates += 1
                exclusion_reasons["fight_id"] = exclusion_reasons.get("fight_id", 0) + 1
    matched = []
    for candidate in candidates:
        direct_match, missing, direct_reasons = _ranking_direct_match(candidate, filters)
        if not direct_match:
            for reason in direct_reasons:
                exclusion_reasons[reason] = exclusion_reasons.get(reason, 0) + 1
            continue
        if missing:
            hydrated_count += 1
            try:
                fights, actors = hydrate_discovery_report(
                    client, candidate["report_code"],
                    _filters_without(filters, set(_DISCOVERY_FILTER_FIELDS) - set(missing)),
                    fight_id=candidate.get("fight_id"),
                )
            except PartialGraphQLError as error:
                errors.extend(error.errors)
                exclusion_reasons["hydration"] = exclusion_reasons.get("hydration", 0) + 1
                continue
            except Exception as error:
                errors.append({"message": str(error), "path": [candidate["report_code"]]})
                exclusion_reasons["hydration"] = exclusion_reasons.get("hydration", 0) + 1
                continue
            hydrated_filters = _filters_without(filters, set(_DISCOVERY_FILTER_FIELDS) - set(missing))
            report = dict(candidate)
            is_match, reasons = report_matches(report, fights, actors, hydrated_filters)
            if not is_match:
                for reason in reasons:
                    exclusion_reasons[reason] = exclusion_reasons.get(reason, 0) + 1
                continue
        matched.append(candidate)
    truncated = has_more and pages_fetched >= max_pages or len(candidates) > top
    return make_global_result(
        matched,
        top,
        _filters_dict(filters),
        source_rows=len(rows),
        unique_candidates=len(candidates),
        hydrated_candidates=hydrated_count,
        excluded_candidates=len(candidates) - len(matched) + invalid_candidates,
        returned_candidates=min(len(matched), top),
        pages_fetched=pages_fetched,
        truncated=truncated,
        exclusion_reasons=exclusion_reasons,
        errors=errors,
    )


EVENT_PAGE_LIMIT = 10000
EVENT_MAX_PAGES = 5


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
        ("ability_id", "abilityID"), ("hostility", "hostility"),
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="warcraftlogs.py")
    parser.add_argument("--client-id")
    parser.add_argument("--client-secret")
    parser.add_argument("--env-file")
    parser.add_argument("--no-cache", action="store_true")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("rate-limit")
    metadata = subparsers.add_parser("metadata")
    metadata.add_argument(
        "kind",
        choices=("regions", "realms", "zones", "encounters", "seasons", "classes", "specs", "affixes", "abilities"),
    )
    metadata.add_argument("--region")
    metadata.add_argument("--name")
    metadata.add_argument("--expansion-id", type=int, default=11)
    metadata.add_argument("--ability-limit", type=int, default=100)
    metadata.add_argument("--ability-page", type=int, default=1)
    report = subparsers.add_parser("report")
    report_parsers = report.add_subparsers(dest="report_command")
    summary = report_parsers.add_parser("summary")
    _add_report_options(summary)
    fights = report_parsers.add_parser("fights")
    _add_report_options(fights, window=True, translate=True)
    master_data = report_parsers.add_parser("master-data")
    _add_report_options(master_data, translate=True)
    player_details = report_parsers.add_parser("player-details")
    _add_json_report_options(player_details)
    player_details.add_argument("--no-translate", dest="translate", action="store_false", default=True)
    for kind in ("table", "graph"):
        command = report_parsers.add_parser(kind)
        _add_json_report_options(command)
        command.add_argument("--data-type", required=True)
        command.add_argument("--ability-id", type=float)
        command.add_argument("--death", type=int)
        command.add_argument("--filter-expression")
        command.add_argument("--source-auras-absent")
        command.add_argument("--source-auras-present")
        command.add_argument("--source-class")
        command.add_argument("--source-id", type=int)
        command.add_argument("--source-instance-id", type=int)
        command.add_argument("--source-pet-type")
        command.add_argument("--source-spec")
        command.add_argument("--target-auras-absent")
        command.add_argument("--target-auras-present")
        command.add_argument("--target-class")
        command.add_argument("--target-id", type=int)
        command.add_argument("--target-instance-id", type=int)
        command.add_argument("--target-pet-type")
        command.add_argument("--target-spec")
        command.add_argument("--hostility-type")
        command.add_argument("--view-by")
        command.add_argument("--wipe-cutoff", type=int)
        command.add_argument("--no-translate", dest="translate", action="store_false", default=True)
    events = report_parsers.add_parser("events")
    _add_report_options(events, window=True)
    events.add_argument("--data-type")
    events.add_argument("--source-id", type=int)
    events.add_argument("--target-id", type=int)
    events.add_argument("--ability-id", type=int)
    events.add_argument("--hostility")
    events.add_argument("--filter-expression")
    events.add_argument("--include-resources", action="store_true", default=None)
    events.add_argument("--use-actor-ids", action="store_true", default=None)
    events.add_argument("--use-ability-ids", action="store_true", default=None)
    events.add_argument("--event-limit", type=int, default=EVENT_PAGE_LIMIT)
    events.add_argument("--max-pages", type=int, default=EVENT_MAX_PAGES)
    events.add_argument("--output")
    rankings = report_parsers.add_parser("rankings")
    _add_report_options(rankings)
    rankings.add_argument("--difficulty", type=int)
    rankings.add_argument("--encounter-id", type=int)
    rankings.add_argument("--compare")
    rankings.add_argument("--player-metric")
    rankings.add_argument("--timeframe")
    find = subparsers.add_parser("find")
    find_parsers = find.add_subparsers(dest="find_command")

    def add_discovery_parser(command):
        command.add_argument("--name", required=True)
        command.add_argument("--server", required=True)
        command.add_argument("--region", required=True)
        command.add_argument("--page", type=int, default=1)
        command.add_argument("--limit", type=int, default=100)
        command.add_argument("--max-pages", type=int, default=1)
        command.add_argument("--class-name", "--class", dest="class_name")
        command.add_argument("--spec-name", "--spec", dest="spec_name")
        command.add_argument("--role")
        command.add_argument("--instance", type=int)
        command.add_argument("--zone", type=int)
        command.add_argument("--encounter", "--encounter-id", dest="encounter", type=int)
        command.add_argument("--season", type=int)
        command.add_argument("--partition", type=int)
        command.add_argument("--key-min", type=int)
        command.add_argument("--key-max", type=int)
        command.add_argument("--affixes", "--affix", dest="affixes", action="append")
        command.add_argument("--timed", action="store_true", default=None)
        command.add_argument("--depleted", action="store_true", default=None)
        command.add_argument("--difficulty", type=int)
        command.add_argument("--kill", action="store_true", default=None)
        command.add_argument("--wipe", action="store_true", default=None)
        command.add_argument("--start-time", type=float)
        command.add_argument("--end-time", type=float)

    add_discovery_parser(find_parsers.add_parser("character"))
    add_discovery_parser(find_parsers.add_parser("guild"))
    global_find = find_parsers.add_parser("global")
    global_scope = global_find.add_mutually_exclusive_group(required=True)
    global_scope.add_argument("--zone")
    global_scope.add_argument("--instance")
    global_scope.add_argument("--encounter", "--encounter-id", dest="encounter")
    global_find.add_argument("--expansion-id", type=int, default=11)
    global_find.add_argument("--page", type=int, default=1)
    global_find.add_argument("--top", type=int, default=100)
    global_find.add_argument("--max-pages", type=int, default=1)
    global_find.add_argument("--class-name", "--class", dest="class_name")
    global_find.add_argument("--spec-name", "--spec", dest="spec_name")
    global_find.add_argument("--role")
    global_find.add_argument("--partition")
    global_find.add_argument("--difficulty")
    global_find.add_argument("--key-min", type=int)
    global_find.add_argument("--key-max", type=int)
    global_find.add_argument("--affixes", "--affix", dest="affixes", action="append")
    global_find.add_argument("--timed", action="store_true", default=None)
    global_find.add_argument("--depleted", action="store_true", default=None)
    global_find.add_argument("--kill", action="store_true", default=None)
    global_find.add_argument("--wipe", action="store_true", default=None)
    global_find.add_argument("--start-time", type=float)
    global_find.add_argument("--end-time", type=float)
    global_find.add_argument("--metric")
    global_find.add_argument("--leaderboard")
    global_find.add_argument("--server-region")
    global_find.add_argument("--server-slug")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command not in ("rate-limit", "metadata", "report", "find"):
        return 0
    try:
        credentials = resolve_credentials(
            args.client_id,
            args.client_secret,
            args.env_file,
            Path.cwd(),
            os.environ,
        )
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    client = WarcraftLogsClient(credentials)
    if args.command == "find":
        if args.find_command == "global":
            try:
                if not 1 <= args.top <= GLOBAL_TOP_MAX:
                    raise ValueError("Global top must be between 1 and 100")
                if args.page < 1 or args.max_pages < 1 or args.max_pages > GLOBAL_MAX_PAGES:
                    raise ValueError("Global page and max pages must be between 1 and 5")
                filters = _global_filters(args, client)
                result = discover_global(
                    client, filters, args.top, args.page, args.max_pages,
                    metric=args.metric, leaderboard=args.leaderboard,
                    server_region=args.server_region, server_slug=args.server_slug,
                    expansion_id=args.expansion_id,
                )
            except AuthenticationError as error:
                print(json.dumps(make_global_result([], args.top, {}, errors=[{"message": str(error)}]), ensure_ascii=True))
                return 3
            except ValueError as error:
                print(str(error), file=sys.stderr)
                return 2
            except (ApiError, KeyError, TypeError, OSError):
                print(json.dumps(make_global_result([], args.top, {}, errors=[{"message": "Warcraft Logs API response did not contain global discovery data"}]), ensure_ascii=True))
                return 4
            print(json.dumps(result, ensure_ascii=True))
            return 0
        if args.find_command not in ("character", "guild"):
            return 0
        try:
            identity = _identity_variables(args.name, args.server, args.region)
            filters = _discovery_filters(args)
            if args.page < 1 or args.max_pages < 1:
                raise ValueError("Discovery page and max pages must be positive")
            if not 1 <= args.limit <= 100:
                raise ValueError("Discovery limit must be between 1 and 100")
            result = discover_reports(
                client, args.find_command, identity, filters, args.page, args.limit, args.max_pages
            )
        except AuthenticationError as error:
            print(str(error), file=sys.stderr)
            return 3
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        except (ApiError, KeyError, TypeError, OSError):
            print("Warcraft Logs API response did not contain discovery data", file=sys.stderr)
            return 4
        scope = {
            "name": identity["name"],
            "server": identity["serverSlug"],
            "region": identity["serverRegion"],
        }
        if result.get("character") is not None:
            scope["character"] = result["character"].get("name")
        envelope = make_envelope(
            "find " + args.find_command, scope, _filters_dict(filters), "api_collection",
            result["data"], pagination=result["pagination"],
            candidate_count=result["candidate_count"],
            hydrated_count=result["hydrated_count"],
            matched_count=result["matched_count"],
            excluded_count=result["excluded_count"],
            exclusion_reasons=result["exclusion_reasons"],
        )
        print(json.dumps(envelope, ensure_ascii=True))
        return 0
    if args.command == "report":
        if args.report_command == "events":
            try:
                unused, variables, scope, filters = event_request(args)
            except ValueError as error:
                print(str(error), file=sys.stderr)
                return 2
            try:
                pages = list(iter_event_pages(client, unused.code, variables, args.max_pages))
            except AuthenticationError as error:
                print(str(error), file=sys.stderr)
                return 3
            except PublicReportError as error:
                print(str(error), file=sys.stderr)
                return 4
            except RuntimeError as error:
                print(str(error), file=sys.stderr)
                return 4
            except (ApiError, KeyError, TypeError, OSError, ValueError):
                print("Warcraft Logs API response did not contain event data", file=sys.stderr)
                return 4
            data = [event for page in pages for event in page["data"]]
            last_cursor = pages[-1]["nextPageTimestamp"] if pages else None
            truncated = bool(
                pages and last_cursor is not None and
                (args.end_time is None or last_cursor < args.end_time) and
                len(pages) >= args.max_pages
            )
            pagination = {"pages_fetched": len(pages), "truncated": truncated}
            errors = [error for page in pages for error in page.get("errors", [])]
            envelope = make_envelope(
                "report events", scope, filters, "api_collection", data,
                pagination=pagination, errors=errors,
            )
            try:
                if args.output:
                    write_event_jsonl(args.output, envelope, data)
            except OSError:
                print("Could not write event output file", file=sys.stderr)
                return 4
            print(json.dumps(envelope, ensure_ascii=True))
            return 0
        if args.report_command not in REPORT_KINDS:
            return 0
        try:
            unused, variables, scope, filters = report_request(args)
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        try:
            payload = client.execute("report-" + args.report_command, variables)
            data = report_data(payload, args.report_command)
        except AuthenticationError as error:
            print(str(error), file=sys.stderr)
            return 3
        except PublicReportError as error:
            print(str(error), file=sys.stderr)
            return 4
        except (ApiError, KeyError, TypeError, OSError, ValueError):
            print("Warcraft Logs API response did not contain a public report", file=sys.stderr)
            return 4
        print(
            json.dumps(
                make_envelope(
                    "report " + args.report_command,
                    scope,
                    filters,
                    "single_report",
                    data,
                    errors=payload.get("errors"),
                ),
                ensure_ascii=True,
            )
        )
        return 0
    if args.command == "metadata":
        resolver = MetadataResolver(client, no_cache=args.no_cache)
        try:
            if args.kind == "realms":
                data, provenance = resolver.realm(args.region, args.name)
                scope = {"region": args.region}
                filters = {"name": args.name}
            elif args.kind in ("regions", "zones", "encounters", "seasons"):
                world, provenance = resolver.world({"expansionId": args.expansion_id})
                scope = {"expansion_id": args.expansion_id}
                filters = {}
                if args.kind == "regions":
                    data = world["regions"]
                elif args.kind == "zones":
                    data = world["zones"]
                elif args.kind == "encounters":
                    data = [
                        dict(encounter, zone={"id": zone["id"], "name": zone["name"]})
                        for zone in world["zones"]
                        for encounter in zone["encounters"]
                    ]
                else:
                    data = [
                        dict(partition, zone={"id": zone["id"], "name": zone["name"]})
                        for zone in world["zones"]
                        for partition in zone["partitions"]
                    ]
            else:
                game, provenance = resolver.game({"abilityLimit": args.ability_limit, "abilityPage": args.ability_page})
                scope = {}
                filters = {"limit": args.ability_limit, "page": args.ability_page} if args.kind == "abilities" else {}
                if args.kind == "classes":
                    data = [{field: value for field, value in item.items() if field != "specs"} for item in game["classes"]]
                elif args.kind == "specs":
                    data = [
                        dict(spec, game_class={"id": game_class["id"], "name": game_class["name"], "slug": game_class["slug"]})
                        for game_class in game["classes"]
                        for spec in game_class["specs"]
                    ]
                else:
                    data = game[args.kind]
        except AuthenticationError as error:
            print(str(error), file=sys.stderr)
            return 3
        except ValueError as error:
            print(str(error), file=sys.stderr)
            return 2
        except (ApiError, KeyError, TypeError, OSError):
            print("Warcraft Logs API response did not contain metadata", file=sys.stderr)
            return 4
        print(
            json.dumps(
                make_envelope(
                    "metadata " + args.kind,
                    scope,
                    filters,
                    "api_collection",
                    data,
                    errors=resolver.errors,
                    cache=provenance,
                ),
                ensure_ascii=True,
            )
        )
        return 0
    try:
        payload = client.execute("rate-limit", {})
    except AuthenticationError as error:
        print(str(error), file=sys.stderr)
        return 3
    except (ApiError, OSError, ValueError):
        print("Warcraft Logs API request failed", file=sys.stderr)
        return 4
    try:
        data = normalize_rate_limit(payload)
    except (KeyError, TypeError):
        print("Warcraft Logs API response did not contain rate limit data", file=sys.stderr)
        return 4
    print(
        json.dumps(
            make_envelope(
                "rate-limit",
                {},
                {},
                "api_collection",
                data,
                errors=payload.get("errors"),
            ),
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
