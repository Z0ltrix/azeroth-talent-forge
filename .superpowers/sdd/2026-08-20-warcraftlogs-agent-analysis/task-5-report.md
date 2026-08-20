# Task 5 report — Warcraft Logs skill guidance

## Scope

Implemented Task 5 documentation and deterministic interface assertions only:

- updated the Warcraft Logs skill routing guidance;
- updated CLI, discovery, and report references;
- updated `agents/openai.yaml` prompt while preserving invocation policy;
- added four pressure scenarios;
- added deterministic documentation contract assertions to
  `test_warcraftlogs.py`.

Unrelated worktree changes in `.gitignore`, `README.md`, and the metadata
GraphQL document were preserved and were not staged.

## Documentation TDD

The four RED scenarios were written before guidance edits:

1. stale events arguments;
2. report-level-only “today” filtering;
3. whole-report/unbounded event download;
4. treating global ranking samples as exhaustive.

The focused documentation assertion was run before guidance and failed because
the current skill lacked the staged local-evaluation rule. After the scoped
guidance edits it passed.

No fresh-context evaluator or repository pressure-test harness was available.
Therefore five baseline repetitions and five updated-guidance repetitions per
scenario were not run. No agent outputs or rationalizations are claimed as
observed. The scenario document records this limitation and the exact protocol
for a future evaluator; expected unsafe baselines remain explicitly labeled as
expected, not actual results.

## Guidance delivered

The final skill routes discover → fights → details → local evaluation, requires
absolute fight-time selection with an explicit mode, and requires inspection of
scope, filters, completeness, truncation, warnings, and errors. It states that
global cohorts are sampled and requires actor-bound `matched_actor` evidence.

References include exact PowerShell examples for:

- today's local-timezone fight window;
- one-file-per-run summary, fights, master data, and player details;
- default combatant-info retrieval;
- bounded event JSONL with `--event-limit`, `--max-pages`, and `--output`;
- same-spec/key sampled global cohort comparison.

Detailed schema material remains in references rather than being duplicated in
`SKILL.md`.

## Verification

- Focused RED assertion: failed as expected before guidance.
- Focused GREEN assertion: passed.
- `python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_warcraftlogs -v`: passed, 107 tests.
- `git diff --check`: passed.
- `python C:\Users\chris\.codex\skills\.system\skill-creator\scripts\quick_validate.py plugins/azeroth-talent-forge/skills/warcraftlogs`: blocked before validation because `yaml` is not installed (`ModuleNotFoundError: No module named 'yaml'`).
- Live API verification: not run; no live claim is made.

## Concerns

The skill validator needs its external `yaml` dependency installed before it
can provide validator evidence. Pressure-scenario evaluator repetitions remain
pending until an evaluator is available.
