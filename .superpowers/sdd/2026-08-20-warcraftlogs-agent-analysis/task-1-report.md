# Task 1 report — Warcraft Logs API/agent-analysis RED tests

## Status

Complete. Test/fixture/report changes only; production tree untouched.

## Implemented contracts

- Added `test_api_contracts.py` and three required fixtures.
- Added query-contract checks for fights, player details, events, table, and graph.
- Added fight-time, combatant-field, cohort, JSONL shape, and output-preservation checks.
- Corrected only the legacy `ReportFight.gameZone` assertion in `test_warcraftlogs.py`.
- Cohort tests use existing `report_data` and `discover_global` interfaces. They cover group-only rejection, unique `matched_actor` shape, and ambiguous ranked-actor exclusion.

## Verification timeline

Round 1 review corrections removed the invented `warcraftlogs.agent_analysis` dependency and unrelated realm/report-fights assertions. The subsequent scoped re-review removed the remaining unrelated `subregion` assertion and added the ambiguous cohort case.

Earlier verification entries from before those corrections are superseded and intentionally omitted; their counts and failure labels must not be used.

Current focused command:

```text
python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_api_contracts -v
```

Result: `Ran 9 tests`; `7` failures. RED causes: group-only cohort exclusion, relative-to-absolute fight-time conversion, and five query-text contracts. Remaining checks pass. No import, setup, or fixture errors.

Current existing-suite command:

```text
python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_warcraftlogs -q
```

Result: `Ran 101 tests`; `100` pass and `1` fails. The sole failure is the task-introduced, Spec-required `gameZone` assertion against the unchanged production query.

Current full-suite command:

```text
python -m unittest discover -s plugins/azeroth-talent-forge/skills/warcraftlogs/tests -p "test_*.py"
```

Result: `Ran 110 tests`; `102` pass and `8` fail: the `7` focused RED failures plus the one task-introduced `gameZone` assertion failure.

`git diff --check` is clean for task changes. Unrelated pre-existing worktree modifications remain unstaged and were not changed.
