---
name: talents
description: Use when working with Retail World of Warcraft talent import strings, local graph validation, build comparison or modification, deterministic build generation, presets, or Blizzard-string export.
---

# Talents

Use the local deterministic CLI for Retail Blizzard talent strings. Runtime
network access is forbidden: pasted strings work, but URLs are never fetched,
and exports are never uploaded to WoW, Wowhead, Method, or Icy Veins.

The current bundled snapshot is Retail `12.1.0.69404`, locale `enUS`, with a
supported planning range of levels 10–90. A different `--build` is usable only
when a complete, hash-verified asset directory has already been installed.
Runtime never downloads, refreshes, or silently changes an asset.

Start with exactly one matching reference under `references/features/`, then
load the decoded class overview and only the relevant class/spec/hero files.
Every supported class, specialization, and hero tree has a reference file
with talent names, IDs, descriptions/effects, costs, gates, and point pools.
Structural codec nodes without an ability definition are documented as such,
not given invented effects.

Before describing bundled data as freely redistributable, read the repository
root's `THIRD_PARTY_NOTICES.md`. It records the exact-build sources, the
external test-string provenance, what content is intentionally excluded, and
the remaining upstream-terms review requirement.

Feature reference registry: `import-export`, `inspect`, `validate`, `compare`,
`modify`, `generate`, `presets`, `patch-assets`, and `errors` under
`references/features/`. Read the matching file before executing that mode.

Commands:

```powershell
python scripts\talents.py assets info
python scripts\talents.py inspect --code STRING --level 90
python scripts\talents.py validate --code STRING --level 90
python scripts\talents.py compare --left STRING --right STRING --level 90
python scripts\talents.py modify --code STRING --level 90 --set ENTRY=RANK
python scripts\talents.py generate --spec SPEC --level 90 --prefer ENTRY=WEIGHT
python scripts\talents.py presets list
python scripts\talents.py presets show --id PRESET_ID
```

Command capabilities:

- `assets info` reports the selected build, locale, graph/preset/reference
  hashes, catalogue, and preset count.
- `inspect` decodes a pasted string and reports class/spec, hero subtree,
  selected nodes, Entry IDs, names, purchased/granted ranks, choices,
  descriptions/effects, validation violations, observed tree hash, and patch
  verification.
- `validate` checks codec structure, entries, ranks, choices, prerequisites,
  sufficient edges, exclusions, DB2 costs, independent currency budgets,
  grants, and the requested level.
- `compare` requires the same specialization and immutable asset, then reports
  only structural `ADD`, `REMOVE`, `RANK`, and `CHOICE` differences.
- `modify` supports repeated `--set ENTRY=RANK`, `--clear ENTRY`,
  `--choice ENTRY=INDEX`, `--hero ID`, and `--cascade`; it returns no partial
  result when validation or round-trip checks fail.
- `generate` is a deterministic structural solver with `--require`, `--forbid`,
  `--prefer ENTRY=WEIGHT`, `--hero`, and `--level`. `--prefer` is a tie-breaker,
  not a DPS/healing/survivability model.
- `presets list` filters by spec/category; `presets show` decodes and inspects a
  source-attributed preset. The bundled initial asset currently has no accepted
  online presets.

Build-producing operations (`modify` and `generate`) return a validated
Blizzard import string, zero-tree-hash export policy, local Wowhead share URL,
asset/build provenance, validation data, warnings, and a node-level diff where
applicable. A share URL is inert formatting; it is not a network operation.

All commands emit JSON. Success uses `status: "ok"`; handled talent errors use
`status: "error"` with a stable code, message, and structured details. Normal
handled failures exit with code 4, asset-integrity failures with 5, and argument
parser failures with argparse's code 2. See `references/features/errors.md` for
recovery guidance.

Never invent talent effects, silently browse, silently refresh assets, or claim
that a zero-hash input originated on the bundled patch. Generated strings use
the Blizzard-supported third-party zero-hash policy and include a local
Wowhead share URL. The skill does not simulate combat, rank guide quality, or
guarantee a live-client import.

Use `inspect` first for a pasted string, then read the matching class overview:
it explains its separate Class, Specialization, and Hero point pools, including
the exact level schedule. The graph charges each selected node to its own
Blizzard `TraitCurrencyID`; source-defined `GRANTS` are free spec ranks rather
than spendable points. `--level` defaults to 90 and must reflect the character
being planned. Other values return `UNSUPPORTED_LEVEL`. Feature contracts
explain each command, output, limits, and recovery path.

Online Method, Icy Veins, and Wowhead strings in the repository are provenance-
labelled regression fixtures only. They are not a runtime guide catalogue and
do not authorize copying guide text, images, HTML, or branding. Before making
redistribution claims, read the repository root `THIRD_PARTY_NOTICES.md`.
