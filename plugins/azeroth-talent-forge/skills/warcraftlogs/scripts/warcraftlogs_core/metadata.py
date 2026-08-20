"""Metadata normalization, selection, and cache-backed resolution."""
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import List, Mapping, Optional
from .models import normalize_name

METADATA_TTL_SECONDS = 24 * 60 * 60

def normalize_rate_limit(payload: Mapping[str, object]) -> dict:
    value = payload["data"]["rateLimitData"]
    return {
        "limit_per_hour": value["limitPerHour"],
        "points_spent_this_hour": value["pointsSpentThisHour"],
        "points_reset_in": value["pointsResetIn"],
    }

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
