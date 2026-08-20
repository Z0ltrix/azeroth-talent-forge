# Local run evaluation

Use this reference after discovery and detail collection when the user asks
why a run performed well or wants a comparison with similar Mythic+ runs. The
CLI supplies bounded, provenance-rich raw data; the agent performs the
comparison locally. There is intentionally no monolithic `compare-run`
endpoint.

## Evaluation recipe

1. Discover the target character's public report candidates for the user's
   timezone window. Do not treat a matching report as a matching run.
2. Fetch `report fights` for each candidate and select individual fights with
   `--absolute-start-time`, `--absolute-end-time`, and an explicit
   `--time-mode`. Keep the fight ID, report code, report-relative timestamps,
   and derived absolute timestamps together.
3. Store the target run's report-wide context once (`summary` and
   `master-data`) and its fight-scoped details in separate local files:
   `fights`, `player-details`, and, when useful, the same `table`, `graph`,
   `rankings`, and bounded `events` views used for comparison.
4. Resolve the target actor from local master/player data. Record positive
   actor ID and name, class, specialization, role, gear, talents, and key
   context. Do not identify the player solely because another group member
   matches the requested class or role.
5. Discover a bounded global cohort for the same dungeon/encounter with the
   requested actor class, specialization, role, key height, affixes, timing,
   and metric filters. Prefer an exact key range (`--key-min N --key-max N`)
   and a bounded `--top`/`--max-pages`.
6. Accept a cohort candidate only when its `matched_actor` identifies the
   ranked player that satisfied the actor filters. Hydrate accepted candidates
   with the same high-level fight/player/table data as the target. Fetch raw
   events only for the target and a small set of selected exemplars.
7. Compare like-for-like fields locally. Use the same dungeon, key range,
   role/spec, metric, fight scope, and view options for every row. Exclude or
   label missing fields instead of substituting zeros.
8. Report the target value, cohort size, cohort statistic, and provenance for
   every conclusion. State exclusions, hydration failures, missing data, page
   limits, truncation, and the fact that public ranking results are sampled.

## What to calculate

Use fields returned by the selected API views; do not invent values that the
payload does not contain. Common locally derived measures include:

| Area | Examples | Typical derivation |
| --- | --- | --- |
| Run outcome | duration, timed/depleted, key level, rating | absolute fight end minus absolute fight start; retain API outcome fields |
| Throughput | damage, healing, damage taken, per-second values | use the same table/graph data type and normalize only when its time scope is identical |
| Survival | deaths, damage taken, defensive usage | count or aggregate the same actor-scoped fields/events across comparable fights |
| Utility | interrupts, dispels, crowd control, external/defensive casts | count matching actor events within the selected fight interval |
| Route | pull count, pull duration, boss/trash split, downtime | derive from fight/pull/event timestamps only when the payload exposes those boundaries |

For each numeric metric, calculate at least the target value and cohort
sample size. When the sample is large enough, add median, lower/upper quartiles,
and the target's empirical percentile. Define the convention in the result
(for example, percentile among returned valid cohort rows); never present it as
an all-player or all-run population percentile.

Use the same missing-value policy for target and cohort. A candidate lacking a
required field belongs in `missing_data`/exclusions, not in a zero-valued
average. Keep raw values and derived values distinguishable so a reader can
trace every claim back to a local file and API scope.

## Default view mapping

Choose views by the question, and record the exact `data-type`, actor filter,
fight ID, and time window in the comparison record. This is the default
mapping; request additional views only when the question needs them:

| Question | First source | Default view |
| --- | --- | --- |
| key, rating, duration, timed/depleted, dungeon, route | `report fights` | no table/graph view |
| actor, gear, stats, specialization, talents | `report player-details` | combatant info enabled |
| damage, healing, damage taken | `report table` | `DamageDone`, `Healing`, or `DamageTaken` |
| deaths, interrupts, dispels, casts | `report table` | `Deaths`, `Interrupts`, `Dispels`, or `Casts` |
| time series or pull-by-pull shape | `report graph` | choose and record the matching graph data type |
| exact ability timing or defensive usage | `report events` | bounded `Casts`, `Deaths`, `DamageTaken`, or `CombatantInfo` events |

Keep the view mapping identical for target and cohort. A table total from one
scope cannot be compared with a graph or event total from another scope. If a
view returns a different shape or lacks the required actor field, preserve the
raw response, record the field as unavailable, and do not silently substitute
another metric.

For small cohorts (`n < 5` valid rows), report descriptive values and the
individual sample size only. Use quartiles and empirical percentiles from
`n >= 5` as a practical minimum, and state the actual `n` and percentile
method; this is a stability heuristic, not a claim about statistical
significance.

## Required comparison record

For each metric or conclusion, retain:

- target report code and fight ID;
- target actor identity and the cohort actor identity evidence;
- requested filters, ranking metric, dungeon/key scope, and view/event scope;
- target value, valid cohort count, and the statistic or percentile method;
- excluded candidates, hydration errors, missing fields, pages fetched, and
  `pagination.truncated`;
- whether the value came directly from Warcraft Logs or was derived locally.

Before drawing a conclusion, inspect every envelope's `scope`, `filters`,
`completeness`, `warnings`, `errors`, and `pagination.truncated`. A global
cohort is `completeness: "sampled"`; it is suitable for a bounded comparison,
not an exhaustive leaderboard or population estimate.

## Compact example

For “evaluate Ratelka's Protection Warrior +12 Dawnbreaker run”: discover
Ratelka's reports, select today's fight, export the target's fights/player
details/table/events, then run a global search with the same dungeon,
`--class-name Warrior --spec-name Protection --role tank --key-min 12
--key-max 12 --top 25 --max-pages 2`. Keep only actor-bound candidates,
hydrate their comparable details, compute local statistics, and report the
sampled limitations beside the result.
