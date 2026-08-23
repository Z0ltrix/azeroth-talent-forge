---
feature: import-export
---

# Import and export

Commands: `inspect --code STRING`, `validate --code STRING`, `modify`, and `generate`.

Paste a complete Blizzard talent string. The decoder checks serialization
version, specialization, tree-hash policy, node order, ranks, and choices,
then selects the matching local Retail graph. Build-producing operations return
`export_string`, `share_url`, `valid_for_build`, `source_patch_verified`, and
validation data. Share URLs are inert formatting; no network request occurs.

The bundled `12.1.0.69404` graph contains 209 Warrior nodes, including the
three hidden hero-subtree selector nodes. Codec slots are stored per
specialization in the Ladybug graph and follow Blizzard's ascending node-ID
rule. Blizzard-compatible zero-only tail bits may be omitted on input. Exports
use a zero tree hash and omit a zero-only suffix. An accepted legacy string can
omit a first-choice marker; the importer preserves that marker when re-exporting
the unchanged build, while newly made choices use the current graph encoding.

The offline fixture matrix in `tests/fixtures/online_strings.json` contains the
full captured code corpus for all 40 playable Retail specializations: 161
Method codes, 127 Icy Veins codes, and one manually captured Wowhead
calculator code. Each records its source, page URL, class ID, spec ID, label,
verbatim import string, and expected status. `compatible` fixtures must import,
validate, and round-trip locally. `observed-drift` fixtures intentionally
record a published code that does not fit the pinned exact-build graph (with
the expected decoder error or validation violations), so upstream changes are
visible without making the local validator permissive. The 13 non-playable
`Initial` graphs have separate `local-smoke` strings solely to cover codec
slots. The test suite loads every fixture against its specialization graph and
does not assert a live-client import, because runtime testing is local-only.

`INVALID_IMPORT_STRING`, `UNSUPPORTED_SPEC`, and `UNSUPPORTED_SNAPSHOT` are
stable recovery codes. Zero-hash strings are accepted but cannot prove patch
origin. Runtime is offline and does not claim meta quality.
