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

## Fix round 1

Addressed reviewer findings:

- Removed invented `warcraftlogs.agent_analysis` dependency. Fight and combatant checks now use existing `warcraftlogs.report_data`; cohort workflow uses existing `warcraftlogs.discover_global`.
- Reverted unrelated realm-query and report-fights assertions in `test_warcraftlogs.py`; retained only the Spec-required `gameZone` assertion correction.
- Cohort test now checks exclusion of an unranked matching group actor and requires a unique result's `matched_actor` object with ID, name, class, spec, role, and match source.
- Corrected test arithmetic and recorded separate existing-suite baseline.

Verification after fix:

```text
python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_api_contracts -v
```

Result: 9 reported tests, 7 expected RED failures, 2 passes. Failures are contract mismatches in current production behavior/query text; no import or fixture errors.

```text
python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_warcraftlogs -q
```

Result: 101 tests, 99 pass, 2 pre-existing schema failures (`subregion { id name slug }` and required `gameZone { id name }`).

```text
python -m unittest discover -s plugins/azeroth-talent-forge/skills/warcraftlogs/tests -p "test_*.py"
```

Result: 110 tests, 101 pass, 9 failures: 7 focused RED failures plus the same 2 pre-existing schema failures.

Production tree remained untouched. Changes are test/report-only.
