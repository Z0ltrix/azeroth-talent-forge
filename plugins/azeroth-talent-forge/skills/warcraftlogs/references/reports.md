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
| `report table REPORT` | Warcraft Logs table data for a selected view. |
| `report graph REPORT` | Graph data for a selected view. |
| `report rankings REPORT` | Report-level ranking payload. |
| `report events REPORT` | Bounded combat-event pages and optional JSONL export. |

The report must be public and positively accessible. Do not infer data from a
missing or inaccessible archive status.

## Events

Events require either `--fight-id` (or a fight in the report URL) or both
`--start-time` and `--end-time`. Use small, explicit values for:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events REPORT --fight-id 3 --max-pages 2 --output events.jsonl
```

`--max-pages` and the requested window are coverage limits, not defaults to
ignore. The CLI marks an export truncated when it reaches the configured page
limit, and rejects a non-advancing pagination cursor instead of looping.

## Analysis sequence

1. Start with `report summary` and `report fights`.
2. Use `master-data` to map actor and ability IDs.
3. Request a single fight or time window with `events`.
4. Check the envelope's scope, pagination, warnings, and errors before making
   performance claims.
