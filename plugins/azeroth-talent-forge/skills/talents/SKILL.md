---
name: talents
description: Use for Retail World of Warcraft talent import strings, validation, comparison, modification, generation, and export.
---

# Talents

Use the local deterministic CLI for Retail Blizzard talent strings. Runtime
network access is forbidden. Start with exactly one matching reference under
`references/features/`, then load the decoded class overview and only the
relevant class/spec/hero reference files.

Before describing bundled data as freely redistributable, read the repository
root's `THIRD_PARTY_NOTICES.md`. It records the exact-build sources, the
external test-string provenance, what content is intentionally excluded, and
the remaining upstream-terms review requirement.

Feature reference registry: `import-export`, `inspect`, `validate`, `compare`,
`modify`, `generate`, `presets`, `patch-assets`, and `errors` under
`references/features/`.

Commands:

```powershell
python scripts\talents.py assets info
python scripts\talents.py inspect --code STRING --level 90
python scripts\talents.py validate --code STRING --level 90
python scripts\talents.py compare --left STRING --right STRING --level 90
python scripts\talents.py modify --code STRING --level 90 --set ENTRY=RANK
python scripts\talents.py generate --spec SPEC --level 90 --prefer ENTRY=WEIGHT
python scripts\talents.py presets list
```

Never invent talent effects, silently browse, silently refresh assets, or claim
that a zero-hash input originated on the bundled patch. Generated strings use
the Blizzard-supported third-party zero-hash policy and include a local
Wowhead share URL.

Use `inspect` first for a pasted string, then read the matching class overview:
it explains its separate Class, Specialization, and Hero point pools, including
the exact level schedule. The graph charges each selected node to its own
Blizzard `TraitCurrencyID`; source-defined `GRANTS` are free spec ranks rather
than spendable points. `--level` defaults to 90 and must reflect the character
being planned. The bundled Retail range is 10–90; other values return
`UNSUPPORTED_LEVEL`. Feature contracts explain each command, its output, and
limits.
