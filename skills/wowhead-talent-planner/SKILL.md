---
name: wowhead-talent-planner
description: Use when analyzing, modifying, exporting, or troubleshooting World of Warcraft Wowhead talent planner builds, Blizzard import strings, Midnight talent builds, class/spec/hero trees, or survivability/DPS talent swap requests.
---

# Wowhead Talent Planner

Use for WoW talent builds when the user wants more than copy/paste: inspect current Wowhead builds, compare selected talents, apply user-directed swaps, and produce or verify Blizzard import strings.

## Workflow

1. Identify target: class, spec, hero tree, content type, and user goal (`survivability`, `DPS`, `utility`, comfort, route-specific needs, etc.).
2. Prefer current Wowhead planner/guide source; web-search/browse because builds change by patch.
3. Use `scripts/wowhead_assets.py <planner-url> --json` to cache current planner HTML, TalentCalc JS, and talent data URLs.
4. Distinguish formats:
   - `/talent-calc/blizzard/<hash>` = Blizzard-style import/export hash from Wowhead.
   - `/talent-calc/<class>/<spec>/<hero>/<path>` = Wowhead path hash, not necessarily game import text.
5. For build edits, first list selected/unselected talent names from the planner. Then define exact swaps from the user's requested priorities before generating a code.
6. Use `scripts/wowhead_talent_builder.py` to apply name-based swaps locally and generate a new `/talent-calc/blizzard/<hash>` URL plus import code.
7. Verify final output by reopening the generated planner URL or importing into Wowhead and checking named talents.

## References

For class/spec-specific planning, read the matching file in `references/` after identifying the target. Keep class facts, talent roles, and guide summaries there instead of in `SKILL.md`. If no matching reference exists, browse current sources and make the build from the user's stated goal rather than from a bundled preset.

Current references:

- `references/protection-warrior.md`

## Script

```powershell
python skills\wowhead-talent-planner\scripts\wowhead_assets.py "https://www.wowhead.com/talent-calc/blizzard/..." --json
```

The script downloads current Wowhead assets into `~/.codex/cache/wowhead-talent-planner/` and reports discovered JS/data URLs plus hash format. If network is sandboxed, rerun with normal approval flow.

Build from a base import URL/hash:

```powershell
python -B skills\wowhead-talent-planner\scripts\wowhead_talent_builder.py --base "https://www.wowhead.com/talent-calc/blizzard/..." --set "Talent Name" --clear "Talent Name"
```

For custom swaps:

```powershell
python -B skills\wowhead-talent-planner\scripts\wowhead_talent_builder.py --base "https://www.wowhead.com/talent-calc/blizzard/..." --clear "Old Talent Name" --set "New Talent Name" --choice "Choice Node Name=Choice Name"
```

## Common Mistakes

- Treating Wowhead path hash as Blizzard import string.
- Trusting guide labels without reading actual selected talents.
- Optimizing toward a default meta goal while the user asked for a different goal.
- Generating a code without reopening/import-verifying named talent changes.
