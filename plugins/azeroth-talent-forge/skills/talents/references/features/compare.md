---
feature: compare
---

# Compare

Command: `compare --left STRING --right STRING [--level LEVEL]`

Both strings must use the same specialization and immutable asset. The stable
node-level diff reports `ADD`, `REMOVE`, `RANK`, and `CHOICE` changes with Entry
IDs and before/after values, ordered by node ID. The optional level is used
when validating each side's independent point pools. `UNSUPPORTED_SPEC` and
`UNSUPPORTED_SNAPSHOT` reject incompatible inputs. It reports differences only,
not DPS/healing/survivability impact.
