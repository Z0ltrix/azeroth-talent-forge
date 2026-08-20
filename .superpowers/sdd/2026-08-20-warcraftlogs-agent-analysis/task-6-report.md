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

## Fix round 1

Addressed the two scoped review findings with TDD.

- RED against parent: the new fake-client drift test for missing
  `Report.playerDetails.fightIDs` failed because the validator returned success.
- Extended the expected schema contract only for arguments used by the bounded
  smoke calls: `playerDetails.fightIDs`, `events.fightIDs`, `events.limit`,
  `table.fightIDs`, `table.dataType`, `graph.fightIDs`, and `graph.dataType`.
  Types are derived from the checked-in GraphQL documents and the existing fake
  introspection representation.
- Added a fake-client test returning a top-level GraphQL `errors` response with
  secret-like message/extension values. Output retains safe error text/status
  while excluding the secret, extensions, and payload details.
- Existing payload-style `ApiError` sanitization test remains covered without
  network access.

## Fix round 2

Addressed the remaining `translate` contract finding with TDD.

- RED against parent: fake introspection subtests removing either
  `Report.fights.translate` or `Report.playerDetails.translate` still returned
  success.
- Added `translate: Boolean` to the exact expected schema argument map for both
  fields and aligned the local fake schema fixture. Smoke behavior and query
  documents were unchanged.
- Focused live-check suite after GREEN: 7 tests passed.
