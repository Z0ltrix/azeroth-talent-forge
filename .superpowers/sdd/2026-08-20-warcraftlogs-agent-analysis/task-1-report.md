# Task 1 report — Warcraft Logs API/agent-analysis RED tests

## Status

Complete. Added API-contract and agent-analysis workflow tests plus required fixtures. No production files changed.

## Changes

- Added `plugins/azeroth-talent-forge/skills/warcraftlogs/tests/test_api_contracts.py`.
- Added `report-fights-rich.json`, `report-player-details-combatant.json`, and `report-events-single-page.json` fixtures.
- Corrected the existing `gameZone` assertion in `test_warcraftlogs.py` to require the Spec field.
- Covered query fields, absolute/boundary-crossing fight times, combatant field preservation, ranked cohort matching, JSONL record shape, and destination preservation on output failure.

## Verification

Focused command:

```text
python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_api_contracts -v
```

Result: 9 tests, 8 expected RED failures, 2 JSONL contract tests passing. Failures are caused by absent agent-analysis service and currently non-conforming GraphQL documents; test module imports and fixtures load correctly.

Full command:

```text
python -m unittest discover -s plugins/azeroth-talent-forge/skills/warcraftlogs/tests -p "test_*.py"
```

Result: 111 tests, 102 passing, 9 expected failures: the 8 focused RED failures plus the corrected existing `gameZone` assertion.

Self-review: `git diff --check` clean for task changes. Existing unrelated worktree modifications were preserved.

## Concerns

- Agent-analysis service API is not present yet; tests intentionally define `warcraftlogs.agent_analysis.normalize_fights`, `normalize_combatant_details`, and `match_cohort_actor` contracts for the next task.
- Full suite remains RED until production query and agent-analysis repairs land.
