# Warcraft Logs skill pressure scenarios

Documentation-TDD control record for Task 5. The scenarios are written before
the skill guidance was edited. No evaluator or fresh-context subagent harness
is available in this repository or session, so the required five repetitions
per scenario were not run. The baseline and post-guidance observations below
are therefore test contracts and expected failure modes, not invented agent
results. A future evaluator must run five fresh contexts per scenario, record
the exact response and rationalization, and manually inspect every flagged
result.

## Scenario 1: stale events arguments

- User request: “Fetch the target run's combat events with the Warcraft Logs
  CLI and give me the interrupt timeline.”
- No-guidance baseline: An agent may reuse a remembered `events` query or CLI
  spelling, such as an integer `abilityID` or `hostility`, without checking the
  current wrapper contract.
- Expected risk: GraphQL validation failure, or an apparently successful path
  that does not represent the requested filter.
- Observable failure to prevent: stale argument names/types appear in the
  command/query, or the agent reports event findings without inspecting API
  errors.
- Pass condition after guidance: The agent uses the current CLI help/reference,
  bounded event scope, and reports envelope errors/truncation before analysis.

## Scenario 2: report-level-only “today” filtering

- User request: “Show this character's Mythic+ runs from today, including a
  run that crossed midnight.”
- No-guidance baseline: An agent may filter candidate reports by report date
  and treat every matching report as a run from today.
- Expected risk: A report containing several fights, or a fight crossing
  midnight, is included or excluded incorrectly.
- Observable failure to prevent: no rich-fights fetch, no absolute fight
  interval, or no declared `started`, `overlap`, or `completed` mode.
- Pass condition after guidance: The agent discovers reports, fetches fights,
  derives absolute fight timestamps with an explicit timezone and mode, and
  evaluates individual fights locally.

## Scenario 3: whole-report event download

- User request: “Download the report's events so I can inspect the run.”
- No-guidance baseline: An agent may request the whole report or omit page/time
  bounds, then load the complete event collection into the response.
- Expected risk: excessive cost/memory, duplicated JSONL events, and an
  unverifiable scope.
- Observable failure to prevent: no fight ID or bounded time window, no
  `--max-pages`, no local output path, or no truncation check.
- Pass condition after guidance: The agent selects one fight or explicit
  bounded window, sets a page limit, writes locally, and labels incomplete
  output from the envelope/receipt.

## Scenario 4: exhaustive global ranking claim

- User request: “Compare the target Warrior with the best same-spec, same-key
  public runs.”
- No-guidance baseline: An agent may treat `find global` results as an
  exhaustive leaderboard and accept a class/spec/role match from another
  member of the ranked group.
- Expected risk: unsupported population claims and player-identity leakage
  into the cohort.
- Observable failure to prevent: missing `completeness: sampled`, missing
  source/hydration/truncation counts, or no actor-bound `matched_actor`
  evidence.
- Pass condition after guidance: The agent requests a bounded comparable
  sample, binds filters to the ranked actor, records exclusions and counts,
  and calls the result sampled rather than exhaustive.

## Evaluator follow-up

When a fresh-context evaluator is available, run each scenario five times
without this skill, then five times with the updated skill. Preserve exact
outputs, rationalizations, and manually inspected flags in this file or a
linked report. Do not convert expected baselines into observed results.
