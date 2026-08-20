# Task 3 report — fight-time selection and actor-bound cohort discovery

## Status

Implemented Task 3 in the forked workspace. Task 4 output streaming was not changed.

## RED evidence

Added focused tests for absolute fight selection, invalid/missing fight timestamps, fight CLI options, and pre-request bound validation. Before production changes, the focused run failed because:

- `select_fights` did not exist.
- `report fights` rejected the new absolute-time options as unknown arguments.
- Actor-filtered global discovery returned a group candidate instead of excluding it.

## GREEN evidence

- `python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_api_contracts -v` — 13/13 passed.
- `python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_warcraftlogs -v` — 103/103 passed.
- `python -m unittest discover -s plugins/azeroth-talent-forge/skills/warcraftlogs/tests -p "test_*.py"` — 116/116 passed.

## Changes

- Added `select_fights` with started, overlap, and completed modes; absolute timestamp derivation; invalid/missing timestamp skipping; and empty successful selections.
- Added fight-only `--absolute-start-time`, `--absolute-end-time`, and `--time-mode`; report-relative windows remain unavailable to fights and absolute bounds are rejected before API access.
- Preserved absolute fight timestamps and selection scope metadata without sending selection windows to the fights query.
- Bound global class/spec/role matching to a uniquely resolved ranked actor, using ranking-row identity when present and fight-scoped actor hydration otherwise. Group-only and ambiguous matches receive `actor_identity` exclusions.
- Preserved the existing envelope, ranking basis, sampling, pagination, truncation, and count fields.

## Files

- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/reports.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/discovery.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/parser.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/dispatch.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/tests/test_api_contracts.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/tests/test_warcraftlogs.py`

## Concerns

- Warcraft Logs ranking payload variants may expose actor identity under additional field names not represented by current fixtures; the resolver covers common actor/player/character/source and ID/name forms.
- Actor class/spec derivation from a `subType`-only master-data actor remains provider-shape dependent; explicit `className`/`specName` fields are preserved when available.
