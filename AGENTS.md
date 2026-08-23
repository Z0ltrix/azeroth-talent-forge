# Repository Agent Instructions

## Plugin release and versioning

- Before a change to shipped files below `plugins/<plugin>/` is delivered or pushed, update that plugin's `.codex-plugin/plugin.json` version.
- Use one version bump per coherent delivery. Intermediate local commits that belong to the same delivery do not require separate bumps.
- Follow Semantic Versioning: patch for compatible fixes or shipped-instruction corrections, minor for backward-compatible commands or features, and major for breaking command or output changes.
- Update tests or other files that pin the old manifest version.

## Warcraft Logs changes

- Warcraft Logs API query, response-shape, normalization, or filtering changes require fixture-backed tests. Live checks may supplement fixtures but must remain opt-in.
- Document every shipped Warcraft Logs feature and limitation in both `SKILL.md` and all applicable reference files.
- Never commit credentials, access tokens, `.env` files, or private live Warcraft Logs payloads.
