# Task 2 report — Warcraft Logs GraphQL contracts

## Status

Task 2 implementation complete. Query/request contract tests pass. The focused
file and full suite retain one pre-existing/out-of-scope Task 3 failure for
actor-bound cohort filtering; no cohort behavior was changed here.

## TDD evidence

- RED before implementation: 7 failures in `test_api_contracts`.
  Failures covered stale event argument/type, obsolete table/graph filters,
  missing combatant info, missing rich fight fields, and non-absolute fight
  times. The cohort test also failed independently and is outside Task 2.
- GREEN after implementation: 8/9 focused tests pass, including all Task 2
  query, player-details, fight-time, and JSONL checks.
- Full suite: 109/110 tests pass; the sole failure is
  `AgentAnalysisContractTests.test_cohort_match_requires_ranked_actor_and_returns_unique_match`.

## Changes

- Repaired event `abilityID: Float` and `hostilityType` contracts.
- Removed obsolete pet/spec table and graph arguments; exposed typed `viewOptions: Int`.
- Expanded fights with current identity, timing, Mythic+, participant, NPC/pet,
  pull/map, bounding-box, phase, percentage, and wipe metadata.
- Enabled `includeCombatantInfo: true` for player details and retained raw payloads.
- Switched character identity guild data to `guilds` and retained valid report fields.
- Converted fight-relative times to absolute report timestamps in `report_data`.
- Aligned parser/request options for event and view filters; removed stale
  pet/spec options while preserving existing fight-window CLI behavior for the
  later local-selection work.

## Files

- `scripts/graphql/report-events.graphql`
- `scripts/graphql/report-table.graphql`
- `scripts/graphql/report-graph.graphql`
- `scripts/graphql/report-fights.graphql`
- `scripts/graphql/report-player-details.graphql`
- `scripts/graphql/character.graphql`
- `scripts/graphql/character-reports.graphql`
- `scripts/warcraftlogs_core/parser.py`
- `scripts/warcraftlogs_core/reports.py`

## Concerns

- The remaining cohort failure belongs to the explicitly excluded Task 3
  actor-bound discovery work and should be handled by that task.
- Live introspection/smoke validation was not run because no credentials or
  caller-provided public report were configured. `viewOptions` is typed as
  `Int` from the current published schema documentation.
