# Task 4 report — bounded atomic output and streaming event export

## Status

Implemented Task 4. Report commands now support bounded atomic JSON output with compact stdout receipts. Event output uses a bounded two-phase temporary process: pages are fetched once, event lines are spooled, then metadata plus event lines are atomically replaced into the destination. No Task 3 fight-time or cohort semantics changed.

## RED evidence

- Added receipt and JSON atomic-write contract tests in `test_api_contracts.py`.
- Updated event output assertions to require compact receipts rather than full payloads.
- Added report output and pre-network output-directory validation tests.
- Focused RED run failed as expected:
  - `write_json_atomic` and `output_receipt` were undefined.
  - `--output` event behavior still printed the full envelope.
  - report output receipt/validation behavior was absent.
  - parser initially exposed duplicate `--output` after common report option wiring; fixed before GREEN.

## GREEN evidence

- `python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_api_contracts -v` — 15/15 passed.
- `python -m unittest plugins.azeroth-talent-forge.skills.warcraftlogs.tests.test_warcraftlogs -v` — 105/105 passed.
- `python -m unittest discover -s plugins/azeroth-talent-forge/skills/warcraftlogs/tests -p "test_*.py"` — 120/120 passed.
- `git diff --check` — no whitespace errors; only existing line-ending warnings.

## Changes

- Added compact receipts with command, output path, records written, pages fetched, truncation, and sanitized errors when present.
- Added same-directory temporary JSON serialization and atomic replacement; serialization/write failures preserve an existing destination.
- Applied `--output` to all report command families through shared parser options.
- Validated output parent directories and destination type before API access.
- Added bounded event-page export that writes one metadata record plus one record per event, without embedding an event array in metadata.
- Preserved full JSON envelopes on stdout when `--output` is absent.
- Preserved existing event pagination bounds, cursor safety, partial errors, and truncation semantics.

## Files

- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/dispatch.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/parser.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/scripts/warcraftlogs_core/reports.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/tests/test_api_contracts.py`
- `plugins/azeroth-talent-forge/skills/warcraftlogs/tests/test_warcraftlogs.py`

## Concerns

- Event export uses bounded temporary disk spooling rather than retaining event objects in memory; available temporary disk space remains an operational prerequisite.
- No live Warcraft Logs call was made; verification is fixture/unit based.
- Existing unrelated worktree changes in `.gitignore`, `README.md`, and `metadata-realm.graphql` were not staged.

## Fix round 1 — semantic errors with event output

### RED

Added `EventTests.test_events_output_preserves_private_report_error`, an end-to-end `main()`/dispatch regression using `--output`. Before the fix it failed because a private report produced `could not write event output file` instead of the semantic public/accessibility error.

### GREEN

- Focused regression + receipt/atomic tests — 4/4 passed.
- `test_api_contracts` — 15/15 passed.
- `test_warcraftlogs` — 106/106 passed.
- Full discovery — 121/121 passed.
- `git diff --check` — no whitespace errors; only existing line-ending warnings.

### Fixes

- Added `OutputWriteError` for filesystem/serialization failures during event spooling and atomic replacement.
- `PublicReportError`, `RuntimeError` cursor failures, authentication, and API/parser errors now remain outside the file-write catch and retain semantic messages/statuses.
- Successful receipt and atomic output behavior retained.

### Fix-round concerns

- Regression uses the private/inaccessible-report branch; non-advancing cursor behavior remains covered without `--output` and shares the same narrowed dispatch boundary.
- No live Warcraft Logs call made.
