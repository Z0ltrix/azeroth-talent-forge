---
name: warcraftlogs
description: Use when a Warcraft Logs URL or report code needs public report inspection, character/guild/global discovery, combat-log analysis, rankings, or Mythic+ key filtering.
---

# Warcraft Logs

Use the bundled `scripts/warcraftlogs.py` orchestrator for public Warcraft Logs v2
GraphQL data. This skill covers report URLs/codes, character and guild searches,
sampled global ranking discovery, metadata lookup, targeted player/run details,
and bounded combat-log analysis.

## Boundaries

- Use only the public client endpoint at `https://www.warcraftlogs.com/api/v2/client`.
- Use OAuth client credentials (`WARCRAFTLOGS_CLIENT_ID` and
  `WARCRAFTLOGS_CLIENT_SECRET`), never a Warcraft Logs UI username or password.
- Do not scrape `warcraftlogs.com` HTML or browser pages. Public API access may
  require allowing `warcraftlogs.com` HTTP `POST` requests in the execution environment.
- Credentials resolve per field in this order: CLI flags, selected `.env` file,
  then process environment. The default file is only `./.env`; use `--env-file`
  for another explicit file. Never print, cache, or include credentials or tokens
  in output, fixtures, or reports.

## Route requests

Use this staged workflow for analysis: discover compact report candidates, select
the report IDs needed, fetch one report's fights, filter to the target player,
then fetch details only for selected fight IDs. A report match is not a run
match. When the user asks for a performance comparison or an explanation of a
run, read [Local run evaluation](references/evaluation.md) for the target-actor,
cohort, metric, and provenance recipe.

Keep report-wide context separate from fight-specific details; only hydrate the
fight-specific views needed for the selected run.

Typical character workflow:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find character --name Ratelka --server Dun-Morogh --region EU --start-time $start --end-time $end --latest 1
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report fights REPORTCODE --player Ratelka --encounter "Den of Nalorakk" --key 6 --timed --latest 1
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report actor-metrics REPORTCODE --fight FIGHTID --player Ratelka --output ratelka.json
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py compare actor-metrics ratelka.json reference.json --output comparison.json
```

- For “today,” convert the user's timezone window to absolute epoch
  milliseconds and use `report fights --absolute-start-time ...
  --absolute-end-time ... --time-mode started`. Preserve the selected fight
  IDs and the chosen time mode.
- `find character|guild --latest N` applies the latest selection locally after
  the report filters match; it is never sent as a GraphQL variable.
- `report fights --player NAME` resolves actor IDs through that report's master
  data and returns only fights containing that player. `report player-details
  --player NAME` filters the returned detail payload locally.
- `report fights` also supports local `--encounter`, exact `--key`, mutually
  exclusive `--timed`/`--depleted`, and `--latest N` filters. The fixed order is
  fight, player, absolute time, encounter, key, completion, latest. The output
  records requested filters, source count, selected count, and ordering.
- `report details --fight ID --player NAME` fetches one fight, player details,
  and the default actor-scoped tables (`DamageDone`, `Healing`, `DamageTaken`,
  `Deaths`, `Interrupts`, `Casts`). Use `--views` to narrow those tables. Events
  remain a separate bounded opt-in command.
- `report actor-metrics REPORT --fight ID --player NAME` fetches the complete
  default actor-scoped detail set and emits `metrics_schema_version: 1` with
  run, actor, totals, damage components, cast components, utility, survival,
  and explicit `missing_data`. Components use category plus numeric ability ID;
  display names are metadata only. Composite parents are not counted as extra
  leaves; parent IDs/names, source view, derivation, scope, and ancestry remain
  component provenance. Component casts are not button presses.
- `compare actor-metrics TARGET.json REFERENCE.json` is local-only: it requires
  no credentials or network access, matches category plus numeric ability ID,
  reports raw values/deltas, and warns about context or scope differences. It
  does not produce a natural-language verdict.
- Before local evaluation, inspect `scope`, `filters`, `completeness`,
  `pagination.truncated`, `warnings`, and `errors`. Never turn partial or
  sampled data into an exhaustive claim.
- Global cohort results are sampled. Require every returned candidate to carry
  actor-bound `matched_actor` evidence for the ranked player; a match from
  another group member does not satisfy class/spec/role filters. Record the
  sample size, exclusions, hydration counts, and truncation in conclusions.

Run from the repository root, or use an absolute script path:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py --help
```

- A report URL/code: `report summary`, `report fights`, `report master-data`,
  `report player-details`, `report table`, `report graph`, or `report rankings`.
- Combat events: `report events` requires a fight ID or both bounded
  `--start-time` and `--end-time`; use `--max-pages` and `--output` for controlled
  JSONL downloads. Do not request an unbounded whole-report event dump.
- Character/guild discovery: `find character` or `find guild` with name, region,
  and realm/server, then add supported class/spec/role, instance/zone/encounter,
  key, affix, timed/depleted, difficulty, kill/wipe, and time filters. These
  report feeds cannot establish a report-specific season or partition, so the
  script rejects `--season` and `--partition` for these two commands.
- Cross-report discovery: `find global` requires an instance/zone or encounter
  and supports the ranking filters exposed by the CLI, including class/spec,
  role, partition, difficulty, key, affixes, kill/wipe, time, and metric. The
  public endpoint does not expose a safe leaderboard filter, so the CLI rejects
  `--leaderboard` before making an API call. It is ranking-based and always
  `completeness: "sampled"`, never an exhaustive public-report search. Keep
  `--top` and `--max-pages` bounded.
- Global exact-key discovery translates `--key-min N --key-max N` when equal to
  ranking `bracket: N-1`, then verifies the hydrated fight's actual key. Key
  ranges stay local and carry a warning that no ranking bracket was pushed.
  An embedded `fightRankings.error` is a structured fatal API error, not an
  empty successful result.
- Reference metadata: `metadata regions`, `realms`, `zones`, `encounters`,
  `seasons`, `classes`, `specs`, `affixes`, and `abilities` list normalized API
  names and IDs (with `realms` narrowed by region/name). Use these collections
  to resolve human input before passing global discovery filters. `rate-limit`
  reports current API budget.

## Analyze safely

Treat the CLI's single JSON envelope as the source of truth. Before interpreting
results, inspect `scope`, `filters`, `completeness`, `pagination.truncated`,
`warnings`, and `errors`; report sampling, page limits, cache use, and partial
data honestly. For event output, parse the JSONL records while retaining the
envelope and do not claim coverage beyond its bounded time/fight scope.

Use `--no-cache` when fresh metadata is required. Prefer fixture-backed or
bounded commands during development and keep the API query documents under
`scripts/graphql/` maintainable and reviewable.

## Detailed reference

Read only the reference needed for the request:

- [CLI and output contract](references/cli.md): credential setup, shared flags,
  envelopes, exit codes, cache, and JSONL.
- [Reports and combat events](references/reports.md): report command selection,
  bounded event exports, tables, graphs, and rankings.
- [Discovery and metadata](references/discovery.md): character/guild/global
  searches, supported filters, sampling, and ID lookup.
- [Local run evaluation](references/evaluation.md): target-actor resolution,
  comparable cohorts, local metrics, percentiles, missing data, and reporting
  provenance.
