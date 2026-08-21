# Discovery and metadata

Use metadata before discovery when a human name must become an API ID:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py metadata zones
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py metadata classes
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py metadata realms --region EU --name Blackhand
```

`metadata` supports `regions`, `realms`, `zones`, `encounters`, `seasons`,
`classes`, `specs`, `affixes`, and `abilities`. `--expansion-id` optionally
narrows world metadata; omitting it uses the API's available world data.

## Character and guild

Character and guild discovery require identity plus realm/server and region.
They search public report feeds and can apply direct report filters plus
fight/actor-derived filters such as class, spec, role, encounter, key range,
affix, timed/depleted, difficulty, kill/wipe, and time.

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find character --name Name --server Blackhand --region EU --class Mage --limit 25 --max-pages 1
```

For a bounded date window, filter the report candidates in the discovery call
and select the latest report directly. Convert the user's local timezone window
to epoch milliseconds. The follow-up report call uses only the returned report
ID; it does not reload every candidate report:

```powershell
$day = (Get-Date).Date
$start = [DateTimeOffset]::new($day).ToUnixTimeMilliseconds()
$end = [DateTimeOffset]::new($day.AddDays(1)).ToUnixTimeMilliseconds()
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find character --name Ratelka --server Dun-Morogh --region EU --limit 25 --max-pages 1 --start-time $start --end-time $end --latest 1
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report fights REPORTCODE --player Ratelka --absolute-start-time $start --absolute-end-time $end --time-mode started --output today-fights.json
```

Use `overlap` when the question is whether any part of a fight intersects the
window, or `completed` when completion must be inside it. Keep the report
relative and fight absolute scopes distinct in notes and output.

`--latest N` is applied after the report filters match. It sorts by report
`endTime`, falling back to `startTime`, and returns only the newest N report
records. `report fights --player NAME` then uses that report's actor mapping to
return only fights containing the named player.

These feeds cannot prove a report-specific season or partition match, so
`--season` and `--partition` are rejected rather than silently filtering.

## Sampled global discovery

Global discovery is ranking-based and requires `--zone`, `--instance`, or
`--encounter`. It is useful for finding representative public logs, not for
proving every matching report:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find global --zone "Amirdrassil, the Dream's Hope" --difficulty 5 --top 10 --max-pages 1
```

Supported global filters include class/spec, role, partition, difficulty,
keystone range, affixes, timed/depleted, kill/wipe, time, server region/slug,
and metric. The output is always `completeness: "sampled"` and carries counts
for source rows, hydrated candidates, exclusions, returned candidates, and
truncation. `--leaderboard` is intentionally rejected by the public endpoint
adapter.

## Filter semantics

- Direct ranking/report fields are evaluated without hydration when present.
- Missing fight/actor details cause a bounded public report hydration.
- Candidates without a valid report code and positive fight ID are excluded.
- `--top` is a local sample limit, never a raid-size filter.
- Stop at the requested number of matching candidates; do not treat excluded
  candidates as matches.

For same-spec/key comparison, keep the cohort bounded and label it sampled:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find global --zone "The Dawnbreaker" --class-name Warrior --spec-name Protection --role tank --key-min 12 --key-max 12 --top 25 --max-pages 2 --metric dps --server-region EU
```

The candidate's `matched_actor` must be the ranked player whose class/spec/role
was tested. Compare only the returned candidates, and report source rows,
hydrated candidates, exclusions, pages, and truncation; this is not an
exhaustive leaderboard or population estimate.

For targeted comparison, pass each returned `report_code` and `fight_id` to
the same bounded details command. Keep the target and cohort views identical:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report details REPORTCODE --fight FIGHTID --player WarriorName --views DamageDone,Deaths
```
