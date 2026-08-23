# Local graph data model

`talents.lbdb` is a read-only Ladybug property graph generated from the pinned Retail DB2 snapshot. It is the runtime authority; Markdown files explain the same facts and are not parsed at runtime.

## Main nodes and relationships

- `Class -> Spec`; a spec serializes its ordered `TraitNode` slots through `SERIALIZES`.
- `Tree -> TraitNode -> Entry -> Definition`; a definition holds the localized spell name, description, and effect text.
- `TraitNode -COSTS-> Currency -UNLOCKS-> CurrencySource`; every purchased rank is charged to its own internal point pool and that pool's exact level schedule.
- `Spec -GRANTS-> TraitNode`; a source-defined free rank reduces the charged ranks for that node without creating a user purchase.
- `REQUIRED_FOR`, `SUFFICIENT_FOR`, and `MUTUALLY_EXCLUSIVE` encode topology restrictions.

Numeric Blizzard IDs are canonical foreign keys. User builds stay in memory; the asset is never modified by import, comparison, modification, or generation.
