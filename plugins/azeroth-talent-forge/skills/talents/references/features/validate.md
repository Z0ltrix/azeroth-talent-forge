---
feature: validate
---

# Validate

Command: `validate --code STRING [--level LEVEL]`

Checks rank limits, selected entries, choices, imported granted ranks, asset
compatibility, and normalized prerequisite/exclusion edges. It also applies
the exact DB2 node costs and `TraitCurrencySource` level schedules bundled for
the selected build; each currency is checked independently, so class, spec,
hero, and special pools cannot be traded against one another. Source-defined
spec grants are free ranks and do not consume their node's currency budget.

`CURRENCY_BUDGET_MISMATCH` reports a real overspend for the requested level;
`CURRENCY_BUDGET_UNAVAILABLE` means the asset lacks the schedule required to
judge that currency. `UNSUPPORTED_LEVEL` rejects a level outside the bundled
Retail schedule (10–90). A decodable string can still be illegal. Structural only:
no combat simulation or performance ranking.
