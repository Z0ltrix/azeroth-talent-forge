---
name: warcraftlogs
description: Use when a Warcraft Logs URL or report code needs public report inspection, character/guild/global discovery, combat-log analysis, rankings, or Mythic+ key filtering.
---

# Warcraft Logs

Use the bundled `scripts/warcraftlogs.py` orchestrator for public Warcraft Logs v2
GraphQL data. This skill covers report URLs/codes, character and guild searches,
sampled global ranking discovery, metadata lookup, and bounded combat-log analysis.

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

Use this staged workflow for analysis: discover candidate reports, fetch rich
fights, fetch details for selected fights, then perform local evaluation. A
report match is not a run match. When the user asks for a performance
comparison or an explanation of a run, read [Local run evaluation](references/evaluation.md)
for the target-actor, cohort, metric, and provenance recipe.

- For “today,” convert the user's timezone window to absolute epoch
  milliseconds and use `report fights --absolute-start-time ...
  --absolute-end-time ... --time-mode started`. Preserve the selected fight
  IDs and the chosen time mode.
- For each selected fight, retrieve rich fights, player-details, and bounded
  events scoped to that fight. Use table/graph/rankings only as needed within
  their supported scope. Summary and master-data are optional report-wide
  context, not fight-specific data. Use `--output` for substantial payloads
  and inspect the receipt.
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
