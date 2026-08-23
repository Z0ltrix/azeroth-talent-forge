"""Access source-attributed build presets bundled with an asset."""

from __future__ import annotations

from .codec import decode_build
from .errors import TalentError
from .models import SpecGraph


class PresetStore:
    def __init__(self, presets: list[dict]):
        self.presets = tuple(presets)

    def list(self, *, spec_id: int | None = None, category: str | None = None) -> list[dict]:
        return [preset for preset in self.presets if (spec_id is None or preset.get("spec_id") == spec_id) and (category is None or preset.get("category") == category)]

    def show(self, preset_id: str, graph: SpecGraph) -> tuple[dict, object]:
        matches = [preset for preset in self.presets if preset.get("preset_id") == preset_id]
        if not matches:
            raise TalentError("PRESET_NOT_FOUND", f"unknown preset: {preset_id}")
        preset = matches[0]
        build = decode_build(preset["code"], graph)
        return preset, build
