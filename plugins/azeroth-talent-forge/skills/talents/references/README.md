# Retail talent reference guide

This directory is the offline reference set for the bundled Retail build
`12.1.0.69404` (`enUS`). It describes what the `talents` skill can do, the
exact local data it uses, and the class facts behind every selectable talent.
It is generated from the same normalized snapshot as the Ladybug graph, except
for the hand-authored feature contracts in `features/`.

## Reading order

1. Open exactly one matching document under `features/` for the requested
   operation.
2. Import or identify the specialization with `inspect --code STRING`.
3. Read `classes/<class>/overview.md`, then that specialization file. Open a
   `hero-*.md` file only when the build includes that hero subtree.
4. Use numeric Entry IDs for `modify`, `generate`, and unambiguous comparison.

## What is local and what is not

Import, validation, comparison, modification, generation, preset lookup, and
export all run against the installed asset without a network request. The
maintainer-only pipeline refreshes a new build asset from pinned public DB2
receipts. A pasted zero-hash string is structurally accepted but cannot prove
which live client patch created it.

## Point pools and level schedules

Every talent cost is attached to a Blizzard-internal `TraitCurrencyID`. The
Ladybug graph keeps those numeric IDs because it must calculate each pool's
budget exactly. Class overviews translate them to **Class**, **Specialization**
or named **Hero** pools and retain the ID for traceability. Each schedule is
copied from `TraitCurrencySource`: its `level (+points)` records tell the
validator and generator exactly how many points that *one* pool has at the
requested level. The bundled Retail asset accepts levels 10–90. Pools cannot
be exchanged. A schedule is never inferred from
a guide or from a total in an imported string.

## Catalog notation

Each ability records Blizzard node, entry, definition, and spell IDs; rank
limits; point currency; source-derived gate records; incoming prerequisite
edges; description; and effect text. A **structural rank** has no spell ID and
is deliberately not described as an ability: it is a codec/topology record in
the exact source, not missing prose.
