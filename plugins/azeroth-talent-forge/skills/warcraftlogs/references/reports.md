# Reports and combat events

Every report command accepts a public Warcraft Logs report URL or its report
code. URLs may include `#fight=N` or `?fight=N`; the command validates the
official host and a positive fight ID.

## Report command selection

| Command | Use for |
| --- | --- |
| `report summary REPORT` | Report identity, visibility, archive state, and time range. |
| `report fights REPORT` | Fight list, kills/wipes, difficulty, and Mythic+ fields. |
| `report master-data REPORT` | Actors and abilities needed for later filtering. |
| `report player-details REPORT` | Player detail payloads for a bounded report/fight view. |
| `report details REPORT` | One fight plus player details and actor-scoped default tables. |
| `report actor-metrics REPORT` | One fight's complete actor-scoped metrics normalized by numeric ability ID. |
| `report table REPORT` | Warcraft Logs table data for a selected view. |
| `report graph REPORT` | Graph data for a selected view. |
| `report rankings REPORT` | Report-level ranking payload. |
| `report events REPORT` | Bounded combat-event pages and optional JSONL export. |

The report must be public and positively accessible. Do not infer data from a
missing or inaccessible archive status.

## Report-wide and per-run details

`report summary` and `report master-data` return report-wide payloads. Their
shared help accepts `--fight`, but these two commands do not send a fight
filter to the API. Their payloads are not fight-filtered; `--fight` does not
change that. Store these files once per report:

```powershell
$report = "REPORTCODE"
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report summary $report --output "report-summary.json"
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report master-data $report --output "report-master-data.json"
```

After `report fights` identifies a fight, keep truly fight-scoped payloads in
per-run files. The public selector is `--fight`:

```powershell
$fight = 123
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report fights $report --fight $fight --output "run-$fight-fight.json"
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report player-details $report --fight $fight --output "run-$fight-player-details.json"
```

Fight results preserve Warcraft Logs' report-relative `startTime` and
`endTime` and add `absoluteStartTime` and `absoluteEndTime` for local calendar
and duration analysis. Invalid fight timestamps are excluded with a warning;
inspect `warnings` before evaluating the run set.

Player details request combatant information by default. Preserve gear, stats,
spec, talent-tree, and talent payloads; do not flatten them before local
evaluation.

## Targeted run details

Use `report fights --player NAME` to keep only runs containing a named actor.
The command resolves actor IDs from report master data and matches them against
each fight's `friendlyPlayers` list. The `--player` value is local and is not a
GraphQL variable.

`report fights` adds deterministic local run selectors:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report fights REPORTCODE --player Ratelka --encounter "Den of Nalorakk" --key 6 --timed --latest 1
```

`--encounter` resolves a numeric encounter/game-zone ID or a unique
case-insensitive fight/game-zone name. `--key N` is exact. `--timed` and
`--depleted` are mutually exclusive and require a completed fight with a
positive keystone level; timed means positive bonus and depleted means
non-positive bonus. `--latest N` is applied after all other local selectors,
sorting by absolute end, absolute start, then fight ID. Selection order is
fight, player, absolute time, encounter, key, completion, latest. The envelope
records `selection.requested_filters`, `selection.source_count`, and
`selection.selected_count`.

Use `report details` after selecting a fight. It requires `--fight ID` or a
fight ID in the report URL and returns one composed envelope with:

- `fight`: the selected fight summary;
- `player`: the resolved report actor, or null when no player filter was given;
- `player_details`: combatant details, filtered when `--player` is present;
- `tables`: `DamageDone`, `Healing`, `DamageTaken`, `Deaths`, `Interrupts`, and
  `Casts` by default.

With `--player`, source-oriented tables receive `sourceID` and target-oriented
tables receive `targetID`. Use `--views DamageDone,Deaths` to narrow the table
set. An unknown player fails rather than silently returning unscoped data.
Inspect `filters`, `warnings`, `errors`, and the fight scope in the envelope.

## Actor metrics

After selecting a fight, fetch the full default actor-scoped details with:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report actor-metrics REPORTCODE --fight FIGHTID --player Ratelka --output target.json
```

The inner data uses `metrics_schema_version: 1` and contains `run`, `actor`,
`totals`, `damage_components`, `cast_components`, utility, survival,
`missing_data`, and derivation notes. Ability identity is the pair
`(category, ability_id)`; names are display metadata only. Composite rows with
valid `subentries` contribute leaves while the parent is omitted. Repeated
leaves aggregate only with compatible scope. Invalid or missing numeric data is
listed in `missing_data` instead of becoming zero. Component casts are API
components, not reconstructed button presses.

## Events

Events require either `--fight` (or a fight in the report URL) or both
`--start-time` and `--end-time`. Use small, explicit values for:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events REPORT --fight 3 --max-pages 2 --output events.jsonl
```

For a stricter bounded export, add `--event-limit` and retain the first JSONL
envelope record:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events REPORTCODE --fight 123 --event-limit 5000 --max-pages 3 --output run-123-events.jsonl
```

`--max-pages` and the requested window are coverage limits, not defaults to
ignore. The CLI marks an export truncated when it reaches the configured page
limit, and rejects a non-advancing pagination cursor instead of looping.

## Analysis sequence

1. Start with filtered discovery and `report fights --player NAME`.
2. Use `report details --fight ID --player NAME` for the selected run.
3. Request a single fight or time window with `events` only when exact timing
   is needed.
4. Check the envelope's scope, pagination, warnings, and errors before making
   performance claims.

Use the local run files to resolve the target actor and compute comparisons.
Global ranking candidates are a bounded sample; require actor-bound
`matched_actor` evidence and retain exclusions, hydration counts, and
`pagination.truncated` alongside any same-spec/key result.
