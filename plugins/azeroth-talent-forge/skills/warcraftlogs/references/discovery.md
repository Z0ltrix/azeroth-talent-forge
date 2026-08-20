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
