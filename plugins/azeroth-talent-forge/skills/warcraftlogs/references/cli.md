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
