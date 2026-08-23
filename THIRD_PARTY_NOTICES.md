# Third-Party Notices

This file documents third-party data and references used by Azeroth Talent
Forge. It is a provenance and attribution record, not a legal opinion or a
claim that every upstream term permits redistribution. The repository's
`AGPL-3.0-or-later` license applies to our code unless a file says otherwise;
it does not relicense Blizzard or third-party data.

## Scope

The Retail `talents` skill is local at runtime. It does not fetch pages, call
third-party APIs, upload builds, or load remote images. Network access exists
only in the explicit maintainer refresh workflow described in
`README.md` and `tools/talents/sources.toml`.

The bundled asset is pinned to Retail build `12.1.0.69404`, locale `enUS`.
Its manifest records every refresh URL, build, locale, timestamp, parser
version, and SHA-256 digest:

- `plugins/azeroth-talent-forge/skills/talents/assets/retail/12.1.0.69404/manifest.json`
- `tools/talents/sources.toml`
- `tools/talents/sync_sources.py`
- `tools/talents/normalize_sources.py`
- `tools/talents/compile_assets.py`

## Sources and use

### Wago DB2 exports

Source endpoint template:
`https://wago.tools/db2/{table}/csv?build={build}&locale={locale}`

The graph's structural records come from exact-build DB2 tables: classes,
specializations, trait trees, nodes, entries, definitions, spells, edges,
costs, conditions, currencies, and grants. The normalized snapshot and the
compiled Ladybug database contain derived graph records and localized
talent names/descriptions needed for offline validation and export.

Wago's public availability is not treated as a redistribution license. Before
publishing a new bundle, maintainers must check the current Wago terms and
retain the source URL and hash in the manifest.

### WoWDBDefs

Pinned DBD schema definitions are read from the public
[wowdev/WoWDBDefs repository](https://github.com/wowdev/WoWDBDefs), at the
commit recorded in `tools/talents/sources.toml`. They describe DB2 columns and
build layouts; they are not copied game assets. The upstream repository's own
license and notices remain applicable and must be checked when changing the
pinned commit.

### Wowhead

The maintainer snapshot may use the exact-build Wowhead talent payload for
class/spec/node membership and as a fallback when a DB2 definition is missing.
In the current snapshot this accounts for one fallback description
(`Surging Totem`). No Wowhead page HTML, CSS, JavaScript, images, logos, or
guide prose is bundled. The configured payload and calculator URLs are listed
in `tools/talents/sources.toml`.

### Method and Icy Veins

Method and Icy Veins pages are used only to obtain independently published
Retail import strings for offline regression fixtures. The fixture file stores
the compact functional code, a human label, and the originating URL:

`plugins/azeroth-talent-forge/skills/talents/tests/fixtures/online_strings.json`

The current matrix contains 161 Method strings and 127 Icy Veins strings
captured from 40 pages each, plus one manually captured Wowhead calculator
string. Fixtures are marked `compatible` or `observed-drift` against the
pinned exact-build graph; drift cases are retained as regression evidence and
are not presented as valid local builds. The corpus does not contain guide
text, images, page markup, stylesheets, scripts, or branding. The minimal HTML files under
`tools/talents/tests/fixtures/` are parser test wrappers containing only test
strings; they are not saved page captures.

Import strings are functional build data, but their verbatim redistribution
still requires a maintainer to review the current source terms. Publicly
reachable does not mean freely redistributable.

## What is deliberately not bundled

- No screenshots, icons, logos, artwork, audio, CSS, JavaScript, or page
  layouts from third-party platforms.
- No guide articles or recommendation prose from Method, Icy Veins, or
  Wowhead.
- No credentials, cookies, session data, or private API responses.
- No runtime network fallback that could silently refresh or scrape content.

## Refresh and review policy

1. Pin the Retail build and locale before a refresh.
2. Fetch only the allow-listed URLs in `sources.toml`.
3. Keep receipts and SHA-256 hashes for every payload.
4. Normalize and compile from that exact snapshot; never hand-edit the graph.
5. Re-check upstream terms before distributing a new snapshot, especially
   DB2-derived text and verbatim external import-string fixtures.
6. If an upstream term does not permit redistribution, keep the payload and
   affected fixtures maintainer-local and distribute only code or user-provided
   strings as appropriate.

This notice does not imply affiliation with or endorsement by Blizzard
Entertainment, Wago, wowdev, Wowhead, Method, or Icy Veins.
