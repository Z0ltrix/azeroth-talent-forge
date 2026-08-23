---
feature: errors
---

# Errors

All commands return JSON. Success has `status: "ok"`; failure has
`status: "error"`, code, message, and structured details. Common codes:
`INVALID_IMPORT_STRING`, `UNSUPPORTED_SPEC`, `UNSUPPORTED_SNAPSHOT`,
`UNKNOWN_ENTRY`, `AMBIGUOUS_NAME`, `ILLEGAL_BUILD`, `CHOICE_CONFLICT`,
`UNSUPPORTED_LEVEL`, `CURRENCY_BUDGET_MISMATCH`,
`CURRENCY_BUDGET_UNAVAILABLE`, `NO_FEASIBLE_BUILD`,
`ASSET_INTEGRITY_FAILED`, and `ROUND_TRIP_MISMATCH`.

Use IDs from `inspect` for ambiguous names, relax constraints for
`NO_FEASIBLE_BUILD`, and rebuild/restore the asset for integrity errors. Errors
never trigger network access or silently alter a build. For `UNSUPPORTED_LEVEL`
choose a level from the asset's documented range (10–90); for a currency
mismatch, inspect the matching class overview to see which independent pool is
overspent.
