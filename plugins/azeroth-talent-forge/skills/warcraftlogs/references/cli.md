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
| `compare actor-metrics TARGET REFERENCE` | Offline comparison of two saved actor-metrics envelopes; no credentials or network. |
| `find character|guild|global` | Public report discovery. |

The targeted report flow is deliberately staged: discovery returns report IDs,
`report fights` selects runs inside one report, and `report details` hydrates one
fight. This keeps report-wide and run-specific data separate.

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

For report discovery, `find character` and `find guild` accept `--latest N`.
After all other report filters match, the CLI sorts by report `endTime` (falling
back to `startTime`) and returns only the newest N reports. The flag is local
selection and is recorded in the output envelope, not sent to the API.

For report targeting, `report fights --player NAME` and `report player-details
--player NAME` apply a local actor-name filter. `report details` additionally
requires `--fight ID` or a fight ID in the report URL.

## Realm-filtered global discovery

For a realm-filtered Mythic+ cohort, provide both fields and keep the sample
bounded:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find global --encounter 12923 --server-region EU --server-slug DunMorogh --class Warrior --spec Fury --top 10 --max-pages 1
```

`DunMorogh`, `Dun-Morogh`, and `dun-morogh` normalize to the metadata slug
`dun-morogh`. The ranking request sends `serverRegion` only: M+ `fightRankings`
does not safely support `serverSlug`. Each returned candidate must expose
`realm_filter.verification: "matched_actor.server"`; otherwise it was excluded.
`RANKING_ERROR` remains a fatal API result, never a successful zero-result
response. The realm fallback is still sampled and may find no candidate within
the chosen page bound.

## Targeted fight selection

`report fights REPORT` accepts these local selectors:

```text
--encounter NAME_OR_ID
--key N
--timed | --depleted
--latest N
```

The selection order is fixed: explicit fight, player, absolute time, encounter,
key, completion outcome, then latest. `--encounter` accepts a positive numeric
encounter/game-zone ID or a unique case-insensitive fight/game-zone name;
unknown names return no rows and ambiguous names are invalid input. `--key` is
an exact positive `keystoneLevel`. Timed and depleted require a completed,
positive-level key; they are mutually exclusive. `--latest` sorts by absolute
end time, then absolute start time, then fight ID. The envelope's `selection`
metadata contains requested filters, `source_count`, `selected_count`, and the
selection order.

## Actor metrics and offline comparison

Fetch one actor's complete default detail set after selecting a fight:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report actor-metrics REPORTCODE --fight FIGHTID --player Ratelka --output ratelka.json
```

The data has `metrics_schema_version: 1` and preserves run/actor context,
totals, `damage_components`, `cast_components`, utility, survival,
`missing_data`, and derivation notes. Component identity is `(category,
ability_id)` using numeric IDs. Display names are metadata; composite parents
with valid children are not added to child totals; and component casts are not
treated as button presses.

Compare saved outputs without OAuth or an API request:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py compare actor-metrics ratelka.json reference.json --output comparison.json
```

The comparison matches only category plus numeric ability ID, reports raw
target/reference values and absolute/percent deltas, handles zero reference
values explicitly, and emits warnings for dungeon, encounter, key, affix,
spec, role, or scope differences. It produces data for the calling agent; it
does not emit a natural-language performance verdict.

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
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events REPORTCODE --fight 123 --event-limit 5000 --max-pages 3 --output run-123-events.jsonl
```

Do not request whole-report events. A truncated or partial export remains
usable only within its recorded scope and must carry its warnings/errors.

## Opt-in live check

The live schema/report check is disabled unless the explicit opt-in variable is
set. It uses only a caller-provided public report and fight, and smoke calls
remain bounded.

```powershell
$env:WARCRAFTLOGS_LIVE_CHECK = "1"
$env:WARCRAFTLOGS_CLIENT_ID = "<client-id>"
$env:WARCRAFTLOGS_CLIENT_SECRET = "<client-secret>"
$env:WARCRAFTLOGS_TEST_REPORT = "REPORTCODE"
$env:WARCRAFTLOGS_TEST_FIGHT = "123"
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs_live_check.py
```

Without `WARCRAFTLOGS_LIVE_CHECK=1`, the command reports `not enabled` and
makes no network request. The check prints status/counts and sanitized API
messages only; it never prints credentials or response payloads.
