"""Validate immutable runtime assets before opening the graph."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


class AssetIntegrityError(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


class AssetBundle:
    def __init__(self, root: Path, manifest: dict, presets: list):
        self.root = root
        self.manifest = manifest
        self.presets = presets
        self.database_path = root / manifest["graph"]["file"]
        self.asset_sha256 = manifest["graph"]["sha256"]


class AssetLoader:
    def __init__(self, assets_root: Path, default_build: str = "12.1.0.69404"):
        self.assets_root = Path(assets_root)
        self.default_build = default_build

    def open(self, build: str | None = None) -> AssetBundle:
        selected_build = build or self.default_build
        root = self.assets_root / "retail" / selected_build
        manifest_path = root / "manifest.json"
        if not manifest_path.is_file():
            raise AssetIntegrityError(f"unsupported snapshot: {selected_build}")
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise AssetIntegrityError("manifest is not valid JSON") from exc
        required = ("asset_schema_version", "product", "channel", "game_build", "locale", "graph", "presets", "references_sha256")
        if any(key not in manifest for key in required):
            raise AssetIntegrityError("manifest is missing a required field")
        if manifest["asset_schema_version"] != 1 or manifest["product"] != "wow" or manifest["channel"] != "retail-live":
            raise AssetIntegrityError("manifest is not a Retail schema-1 asset")
        if manifest["game_build"] != selected_build or manifest["locale"] != "enUS":
            raise AssetIntegrityError("manifest identity does not match selected asset")
        if manifest.get("codec_node_order") != "ascending-node-id" or manifest.get("export_tree_hash") != "zero":
            raise AssetIntegrityError("manifest has unsupported codec policy")
        if manifest["graph"].get("engine_version") != "0.19.1":
            raise AssetIntegrityError("Ladybug engine version mismatch")
        database_path = root / manifest["graph"].get("file", "")
        presets_path = root / manifest["presets"].get("file", "")
        if not database_path.is_file() or not presets_path.is_file():
            raise AssetIntegrityError("manifest references a missing asset file")
        if _sha256(database_path) != manifest["graph"].get("sha256"):
            raise AssetIntegrityError("graph hash mismatch")
        if _sha256(presets_path) != manifest["presets"].get("sha256"):
            raise AssetIntegrityError("preset hash mismatch")
        try:
            presets = json.loads(presets_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise AssetIntegrityError("presets are not valid JSON") from exc
        return AssetBundle(root, manifest, presets)
