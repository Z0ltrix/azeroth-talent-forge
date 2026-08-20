# CLI and output contract

Run the orchestrator from the repository root:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py [shared options] <command>
```

## Credentials

Set `WARCRAFTLOGS_CLIENT_ID` and `WARCRAFTLOGS_CLIENT_SECRET` in an explicit
`.env` file or environment. Resolution is per field:

1. `--client-id` / `--client-secret`
2. `--env-file PATH`, otherwise the current directory's `./.env`
3. Process environment

`--env-file` does not search parent directories. Never use a Warcraft Logs UI
password. `--no-cache` bypasses metadata cache reads and writes.

## Command map

| Command | Purpose |
| --- | --- |
| `rate-limit` | Current public API budget. |
| `metadata KIND` | Normalized metadata collections and IDs. |
| `report KIND REPORT` | One public report surface. |
| `find character|guild|global` | Public report discovery. |

Use `--help` at each level for the exact flags:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events --help
```

For a local “today” window, calculate the timezone boundaries first, then pass
absolute epoch milliseconds to fight selection. This example uses the local
PowerShell timezone and includes fights that started today:

```powershell
$day = (Get-Date).Date
$start = [DateTimeOffset]::new($day).ToUnixTimeMilliseconds()
$end = [DateTimeOffset]::new($day.AddDays(1)).ToUnixTimeMilliseconds()
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report fights REPORTCODE --absolute-start-time $start --absolute-end-time $end --time-mode started --output today-fights.json
```

`--start-time` and `--end-time` remain report-relative bounds for event,
table, graph, and player-detail calls. `report fights` uses absolute bounds and
`--time-mode {started,overlap,completed}`. A receipt from `--output` gives the
path, record count, page count, and truncation; read it before evaluation.

## JSON response

Commands emit one JSON envelope to stdout. Inspect these fields before drawing
conclusions:

| Field | Meaning |
| --- | --- |
| `scope` | Report/fight/window or search scope actually queried. |
| `filters` | Filters accepted by the command. |
| `completeness` | `single_report`, `api_collection`, or sampled discovery. |
| `pagination.truncated` | A configured page bound stopped collection. |
| `warnings`, `errors` | Limitations or sanitized partial API failures. |
| `cache` | Metadata-cache provenance when relevant. |

Exit `2` means invalid input/configuration, `3` OAuth authentication failure,
and `4` API/data-contract/public-access failure. A usable partial JSON response
can still exit `0`; inspect its `errors` and `completeness`.

## JSONL event files

`report events --output FILE` writes the envelope first, followed by event
records as JSONL. Retain the first record when passing the export to analysis:
it establishes fight/time bounds and truncation status.

Use a fight ID and a page limit for a bounded export:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events REPORTCODE --fight-id 123 --event-limit 5000 --max-pages 3 --output run-123-events.jsonl
```

Do not request whole-report events. A truncated or partial export remains
usable only within its recorded scope and must carry its warnings/errors.
