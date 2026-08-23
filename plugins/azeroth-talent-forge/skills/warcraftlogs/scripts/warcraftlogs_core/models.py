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
HTTP_TIMEOUT_SECONDS = 30
REPORT_KINDS = ("summary", "fights", "master-data", "player-details", "details", "table", "graph", "rankings")
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

    @property
    def exact_key(self) -> Optional[int]:
        if self.key_min is None or self.key_max is None or self.key_min != self.key_max:
            return None
        return self.key_min

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
    completed = fight.get("kill") is True and fight.get("inProgress") is not True
    if (
        not completed
        or isinstance(level, bool) or not isinstance(level, (int, float)) or level <= 0
        or isinstance(bonus, bool) or not isinstance(bonus, (int, float))
    ):
        return False, False
    if bonus in (1, 2, 3):
        return True, False
    if bonus <= 0:
        return False, True
    return False, False


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
    if filters.exact_key is not None:
        if not any(level == filters.exact_key for level in levels):
            reasons.append("key")
    else:
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



def normalize_name(value) -> str:
    if not isinstance(value, str):
        raise ValueError("Name must be a string")
    return re.sub(r"[\s-]+", " ", value.casefold()).strip()
