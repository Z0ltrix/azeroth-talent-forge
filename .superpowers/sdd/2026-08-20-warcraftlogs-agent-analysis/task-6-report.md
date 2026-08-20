# Task 6 report — opt-in Warcraft Logs live contract check

## Status

Implemented Task 6. Live execution was not enabled because the required live
credentials/report/fight environment was not configured (`configured=no`). No
live success is claimed.

## Changes

- Added `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_live_check.py`.
  - Requires exact `WARCRAFTLOGS_LIVE_CHECK=1` opt-in.
  - Uses `WARCRAFTLOGS_CLIENT_ID`, `WARCRAFTLOGS_CLIENT_SECRET`,
    `WARCRAFTLOGS_TEST_REPORT`, and `WARCRAFTLOGS_TEST_FIGHT`.
  - Introspects and checks the repaired `Report` contracts for fights,
    player-details combatant info, events, table, and graph.
  - Performs one bounded call each for rich fights, player details, table,
    graph, and fight-scoped events (`limit=100`).
  - Prints only counts/status and sanitized errors; credential values and full
    response payloads are not printed.
- Added fake-client and safety tests in `test_live_check.py`. Tests do not use
  network access.
- Added the exact invocation/environment contract to `references/cli.md`.
- `SKILL.md` unchanged because the final environment names match the brief and
  spec.

## Verification

- TDD RED: initial focused test run failed at the missing live-check module,
  before production implementation.
- TDD GREEN: focused live-check suite: 4 tests passed.
- Warcraft Logs focused suite: 109 tests passed.
- Complete Warcraft Logs suite: 128 tests passed.
- No-env invocation: exit 0; output `not enabled: set WARCRAFTLOGS_LIVE_CHECK=1`;
  no network call.
- Python compilation check: passed.
- Credential availability check: `configured=no`; live check not run.
- `git diff --check`: passed; Git emitted only existing line-ending warnings.

## Concerns

- Current run provides no live schema/API evidence because credentials and a
  public report/fight were absent. Run the documented command when configured.
- Existing unrelated worktree edits were preserved and excluded from the Task 6
  commit.
