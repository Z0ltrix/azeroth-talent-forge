![Azeroth Talent Forge — original dark forge artwork](docs/img/azeroth-talent-forge-banner.png)

# Azeroth Talent Forge

<p align="center">
  <img src="docs/img/azeroth-talent-forge-icon.png" width="72" height="72" alt="Azeroth Talent Forge anvil icon">
</p>

**Forge deliberate World of Warcraft talent builds with Codex.**

A local Codex plugin for Retail WoW talent planning and public Warcraft Logs
analysis. Talent runtime operations use a pinned LadybugDB graph and require no
network. Online access is limited to the explicit maintainer asset-refresh
pipeline.

> No opaque prebuilt builds. No personal defaults. Every talent change remains
> directed by you and visible in the resulting plan.

## What It Does

- Import, inspect, validate, compare, modify, and generate Retail Blizzard
  talent strings locally.
- Read source-attributed talent descriptions/effects for every class,
  specialization, and hero subtree.
- Enforce independent Class, Specialization, and Hero point pools for the
  requested level, including source-defined free ranks.
- Generate a Wowhead share URL locally; no account upload is performed.
- Discover public Warcraft Logs characters, guilds, rankings, and Mythic+ runs.
- Analyze selected report fights, actor metrics, events, casts, interrupts, and
  survival data with explicit scope and completeness metadata.

## Contents

```text
azeroth-talent-forge/
+-- .agents/
|   +-- plugins/
|       +-- marketplace.json
+-- plugins/
|   `-- azeroth-talent-forge/
|       +-- .codex-plugin/plugin.json
|       `-- skills/
|           +-- talents/
|           |   +-- SKILL.md
|           |   +-- references/
|           |   `-- scripts/
|           |       `-- talents.py
|           `-- warcraftlogs/
|               +-- SKILL.md
|               +-- references/
|               `-- scripts/
|                   +-- warcraftlogs.py
|                   `-- graphql/
+-- docs/
    `-- img/
        +-- azeroth-talent-forge-banner.png
        +-- azeroth-talent-forge-github-social.jpg
        `-- azeroth-talent-forge-icon.png
```

GitHub repository social preview: `docs/img/azeroth-talent-forge-github-social.jpg`
(1280×640, under 1 MB).

## Requirements

- Windows, macOS, or Linux
- Python 3.10–3.14
- `ladybug==0.19.1` for the talent runtime
- Network only when a maintainer explicitly refreshes a pinned asset snapshot
- Codex with plugin support for using the bundled skill inside Codex

Install talent dependencies in a local virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r plugins\azeroth-talent-forge\requirements-talents.txt
```

After assets are bundled, talent runtime commands work with network access
blocked. Warcraft Logs retains its separate API requirements.

## License

This repository, including the bundled Codex plugin, skills, and scripts, is
licensed under the [GNU Affero General Public License v3.0 or later](LICENSE)
(`AGPL-3.0-or-later`), unless a file states otherwise.

Third-party data provenance, attribution, bundled-content boundaries, and
redistribution caveats are documented in
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The repository license does
not relicense Blizzard or upstream platform data.

If you modify and provide this plugin through a hosted agent or another network
service, the AGPL requires you to offer the corresponding source code of that
modified version to users interacting with it remotely.

## Plugin Installation

Codex installs plugins from a configured marketplace. In this repository,
`.agents\plugins\marketplace.json` is that marketplace index. It points Codex
at the actual plugin folder under `plugins\azeroth-talent-forge`.

```text
.agents\plugins\marketplace.json
```

Install from the GitHub repository in two steps:

1. Add the GitHub repository as a Codex plugin marketplace.
2. Install the `azeroth-talent-forge` plugin from that marketplace.

```powershell
codex plugin marketplace add Z0ltrix/azeroth-talent-forge --ref main
codex plugin add azeroth-talent-forge --marketplace azeroth-talent-forge
```

The equivalent selector form is also valid:

```powershell
codex plugin add azeroth-talent-forge@azeroth-talent-forge
```

Start a new Codex thread after installation so the bundled skill metadata is loaded.

### Verify Installation

List configured marketplaces:

```powershell
codex plugin marketplace list
```

List available plugins and installed status:

```powershell
codex plugin list
```

You should see marketplace `azeroth-talent-forge` and plugin
`azeroth-talent-forge@azeroth-talent-forge`.

### Updating The Installed Plugin

Refresh the GitHub marketplace snapshot, then reinstall the plugin:

```powershell
codex plugin marketplace upgrade azeroth-talent-forge
codex plugin add azeroth-talent-forge --marketplace azeroth-talent-forge
```

Start a new Codex thread after updating.

## Local Development

Clone the repository only when you want to edit the plugin:

```powershell
git clone git@github.com:Z0ltrix/azeroth-talent-forge.git C:\Users\chris\Documents\GitHub\azeroth-talent-forge
```

If the folder already exists:

```powershell
cd C:\Users\chris\Documents\GitHub\azeroth-talent-forge
git pull
```

The marketplace root is the repository root because Codex looks for
`.agents\plugins\marketplace.json` there. The plugin root is:

```text
plugins\azeroth-talent-forge
```

The required plugin manifest is:

```text
plugins\azeroth-talent-forge\.codex-plugin\plugin.json
```

## Usage

Ask Codex for a WoW talent build by stating:

- class/spec
- hero tree, if desired
- content type, such as Mythic+, raid, solo, leveling, or PvP
- goal, such as survivability, DPS, utility, comfort, or a route-specific need
- must-have or must-avoid talents
- Blizzard import string or bundled preset, if you have one

Example prompt:

```text
Build me a Protection Warrior Mountain Thane Mythic+ talent setup focused on survivability.
Keep Shield Charge and give me a validated import code plus share URL.
```

## Talent Script Usage

Run commands from the repository root.

Inspect the pinned local asset:

```powershell
python plugins\azeroth-talent-forge\skills\talents\scripts\talents.py assets info
```

Inspect and validate a pasted Blizzard string:

```powershell
python plugins\azeroth-talent-forge\skills\talents\scripts\talents.py inspect --code "BLIZZARD_STRING" --level 90
python plugins\azeroth-talent-forge\skills\talents\scripts\talents.py validate --code "BLIZZARD_STRING" --level 90
```

Modify or generate locally:

```powershell
python plugins\azeroth-talent-forge\skills\talents\scripts\talents.py modify --code "BLIZZARD_STRING" --level 90 --set "20=1"
python plugins\azeroth-talent-forge\skills\talents\scripts\talents.py generate --spec 73 --level 90 --prefer 20=10 --require 40
python plugins\azeroth-talent-forge\skills\talents\scripts\talents.py presets list
```

Every build-producing command returns a validated Blizzard string, bundled
build identity, source-patch provenance, and a Wowhead share URL. Zero-hash
inputs are supported but cannot prove their originating patch.

### Public string fixtures

The end-to-end suite replays the full published-code corpus for all 40
playable specializations: 161 Method codes, 127 Icy Veins codes, and one
manually captured Wowhead calculator code. They are stored with source URLs
and labels in
`plugins/azeroth-talent-forge/skills/talents/tests/fixtures/online_strings.json`
and tested offline for import, validation, export, and selection round-trip:

```powershell
python -m unittest discover -s plugins\azeroth-talent-forge\skills\talents\tests
```

The corpus also has 13 separately marked local smoke fixtures for the
non-playable `Initial` graphs. Each external fixture is marked `compatible` or
`observed-drift`; the latter are retained to detect upstream/patch drift and
are expected to fail local validation. At least one compatible code exists for
every playable spec across the two independent guide sources. The suite makes
no live-client import assertion.

## Included Skills

### Talents

`plugins\azeroth-talent-forge\skills\talents` supports:

- offline Retail Blizzard-string import/export
- graph validation of ranks, choices, availability edges, free spec ranks,
  hero trees, and exact per-pool level budgets
- deterministic compare, modify, and constraint-based generation
- source-attributed patch-specific presets
- generated class/spec/hero talent references with descriptions and effects

## Development Notes

- Keep `SKILL.md` generic and workflow-focused.
- Keep class/spec knowledge in `plugins/azeroth-talent-forge/skills/<skill>/references/`.
- Graph and class references are generated from the same normalized snapshot.
- Every feature has one `references/features/*.md` file.
- Every talent must have source-attributed name, effect, IDs, ranks, and graph ownership.
- Build recommendations should come from the user's stated goal and current sources, not personal defaults.
- `TraitCurrencySource`, `TraitCost`, and `TraitCond` are normalized into the
  graph. The runtime charges only source-represented rules; it never guesses a
  point total or a free rank.

### Rebuilding Retail talent assets (maintainers)

The bundled talent graph and class references are generated from one pinned,
exact-build snapshot. Runtime commands never access the network; only this
maintainer workflow does.

1. Pin the Retail build and locale in `tools/talents/sources.toml`.
2. Download the configured Wago DB2/WoWDBDefs/Wowhead inputs into a temporary
   raw bundle. Receipts contain URLs, build, locale, timestamps, and SHA-256
   hashes:

   ```powershell
   python tools\talents\sync_sources.py `
     --config tools\talents\sources.toml `
     --build 12.1.0.69404 --locale enUS `
     --output "$env:TEMP\atf-talents-12.1.0.69404-full"
   ```

3. Normalize and filter the exact-build data. Wowhead supplies patch-matched
   talent text and spec/node membership where DB2 is incomplete:

   ```powershell
   python tools\talents\normalize_sources.py `
     --input "$env:TEMP\atf-talents-12.1.0.69404-full" `
     --build 12.1.0.69404 --locale enUS `
     --output tools\talents\snapshots\12.1.0.69404\snapshot.json.gz
   ```

4. Generate the Markdown feature/class/spec references from that snapshot:

   ```powershell
   python tools\talents\generate_references.py `
     --snapshot tools\talents\snapshots\12.1.0.69404\snapshot.json.gz `
     --feature-registry tools\talents\reference_sources\features.json `
     --planning-notes tools\talents\reference_sources\planning_notes.json `
     --output plugins\azeroth-talent-forge\skills\talents\references
   ```

5. Compile the immutable Ladybug graph and manifest, then verify all hashes:

   ```powershell
   python tools\talents\compile_assets.py compile `
     tools\talents\snapshots\12.1.0.69404\snapshot.json.gz `
     plugins\azeroth-talent-forge\skills\talents\assets\retail\12.1.0.69404 `
     plugins\azeroth-talent-forge\skills\talents\references

   python tools\talents\compile_assets.py verify `
     plugins\azeroth-talent-forge\skills\talents\assets\retail\12.1.0.69404\talents.lbdb `
     plugins\azeroth-talent-forge\skills\talents\assets\retail\12.1.0.69404\manifest.json `
     plugins\azeroth-talent-forge\skills\talents\assets\retail\12.1.0.69404\presets.json `
     plugins\azeroth-talent-forge\skills\talents\references
   ```

The generated snapshot, graph, manifest, and references are the reviewable
build artifacts. Raw downloads stay outside the repository and may be removed
after verification. A patch change requires a new snapshot directory and a
fresh asset manifest; never silently refresh the runtime asset.

## Warcraft Logs

The plugin also includes the implicitly discoverable `warcraftlogs` skill and
the standard-library orchestrator:

```text
plugins\azeroth-talent-forge\skills\warcraftlogs\
+-- SKILL.md
+-- agents\openai.yaml
+-- scripts\warcraftlogs.py
`-- scripts\graphql\*.graphql
```

This integration uses the public Warcraft Logs v2 GraphQL client endpoint. It
does not use Warcraft Logs UI username/password credentials and does not scrape
HTML. Create an OAuth API client in the Warcraft Logs API settings, then set
the client ID and secret in a local `.env` file (never commit it):

```dotenv
WARCRAFTLOGS_CLIENT_ID=your-client-id
WARCRAFTLOGS_CLIENT_SECRET=your-client-secret
```

Credential precedence is per field: CLI parameters (`--client-id` and
`--client-secret`) > the explicit `--env-file` (or repository `./.env`) >
process environment variables. The script accepts `rate-limit`, `metadata`,
`report`, `find`, and local `compare actor-metrics` commands. Examples:

```powershell
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py rate-limit
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py metadata zones
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report summary https://www.warcraftlogs.com/reports/REPORTCODE
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report events REPORTCODE --fight 1 --max-pages 1
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report fights REPORTCODE --player Ratelka --encounter "Den of Nalorakk" --key 6 --timed --latest 1
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py report actor-metrics REPORTCODE --fight 1 --player Ratelka --output target.json
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py compare actor-metrics target.json reference.json --output comparison.json
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find character --name Character --server Area-52 --region us
python plugins\azeroth-talent-forge\skills\warcraftlogs\scripts\warcraftlogs.py find global --instance 1300 --top 10
```

Metadata is cached locally for 24 hours; use `--no-cache` for a refresh. Event
downloads are deliberately bounded by a fight ID or time window and page limit.
Every command prints JSON with scope, filters, completeness, pagination, and
warnings so sampled or truncated results are not mistaken for exhaustive data.
`report actor-metrics` preserves numeric ability IDs and explicit missing data;
`compare actor-metrics` is offline and does not resolve credentials.

For Codex cloud execution, allow outbound `warcraftlogs.com` and HTTP `POST`
to the public API endpoint. No API client secret or access token belongs in
the repository, fixtures, or command output.
