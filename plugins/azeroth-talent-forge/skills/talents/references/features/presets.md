---
feature: presets
---

# Presets

Commands: `presets list [--spec SPEC] [--category CATEGORY]` and `presets show --id PRESET_ID`.

Presets are immutable, source-attributed Blizzard strings bundled with an
asset. Listing is local; showing a preset decodes, validates, and inspects it
against the matching graph. Records carry source URL/name, claimed patch, spec,
and category. The initial asset currently has zero accepted online presets;
none are silently invented. Runtime never performs network access.
