---
feature: modify
---

# Modify

Command: `modify --code STRING [--level LEVEL] [--set ENTRY=RANK] [--clear ENTRY] [--choice ENTRY=INDEX] [--hero ID] [--cascade]`

`--set` assigns ranks, `--clear` removes ranks, `--choice` selects a choice,
`--hero` changes the hero subtree, and `--cascade` removes dependent picks
when clearing a prerequisite. Use the Entry IDs shown by `inspect`; a name is
accepted only if it is unique within the specialization. The result is checked
against prerequisites and the requested level's exact per-currency budget, then
round-tripped before export; failures produce no partial string. Success
includes a node-level diff.
