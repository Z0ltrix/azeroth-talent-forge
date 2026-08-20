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
  and realm/server, then add supported class/spec/role, instance/season, key,
  affix, timed/depleted, difficulty, kill/wipe, and time filters.
- Cross-report discovery: `find global` requires an instance/zone or encounter.
  It is ranking-based and always `completeness: "sampled"`, never an exhaustive
  public-report search. Keep `--top` and `--max-pages` bounded.
- Names and IDs: `metadata regions`, `realms`, `zones`, `encounters`, `seasons`,
  `classes`, `specs`, `affixes`, or `abilities` resolve human input to API IDs.
  `rate-limit` reports current API budget.

## Analyze safely

Treat the CLI's single JSON envelope as the source of truth. Before interpreting
results, inspect `scope`, `filters`, `completeness`, `pagination.truncated`,
`warnings`, and `errors`; report sampling, page limits, cache use, and partial
data honestly. For event output, parse the JSONL records while retaining the
envelope and do not claim coverage beyond its bounded time/fight scope.

Use `--no-cache` when fresh metadata is required. Prefer fixture-backed or
bounded commands during development and keep the API query documents under
`scripts/graphql/` maintainable and reviewable.
