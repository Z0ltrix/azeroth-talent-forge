---
feature: patch-assets
---

# Patch assets

Command: `assets info [--build BUILD]`

Selects `assets/retail/<build>`, verifies manifest, graph, preset, and
reference hashes, then opens the Ladybug graph read-only. The response exposes
build, locale, receipts, engine version, class/spec catalogue, presets, and
the hash of this reference set. Runtime never refreshes assets. New patches
require a new versioned directory built from all DB2 relationship tables:
definitions, costs, conditions, currency schedules, and topology. An
`ASSET_INTEGRITY_FAILED` result means an asset changed or is incomplete.
