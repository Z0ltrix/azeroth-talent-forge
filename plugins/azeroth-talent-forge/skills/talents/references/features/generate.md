---
feature: generate
---

# Generate

Command: `generate --spec SPEC [--level LEVEL] [--hero ID] [--require ENTRY] [--forbid ENTRY] [--prefer ENTRY=WEIGHT]`

The deterministic solver applies required/forbidden Entry IDs, normalized
availability prerequisites, DB2 cost records, and per-currency level budgets.
For the bundled build, use a level from 10 through 90; availability differs by
currency and therefore a valid class-point total does not imply a valid hero or
spec allocation. Weighted preferences break otherwise legal alternatives;
they are not a DPS, healing, or survivability model.

The result contains a validated build, Blizzard string, share URL, and exact
asset provenance. `NO_FEASIBLE_BUILD` means the requested constraints cannot
fit the topology and level budget; `UNSUPPORTED_LEVEL` means the requested
level is outside the bundled 10–90 schedule.
