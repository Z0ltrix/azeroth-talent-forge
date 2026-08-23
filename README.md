![Azeroth Talent Forge — original dark forge artwork](docs/img/azeroth-talent-forge-banner.png)

# Azeroth Talent Forge

<p align="center">
  <img src="docs/img/azeroth-talent-forge-icon.png" width="72" height="72" alt="Azeroth Talent Forge anvil icon">
</p>

**Forge deliberate World of Warcraft talent builds with Codex.**

A local Codex plugin for WoW talent planning and public Warcraft Logs analysis.
It works from your stated goal and explicit changes, then returns inspectable
planner links, import strings, and bounded report data.

> No opaque prebuilt builds. No personal defaults. Every talent change remains
> directed by you and visible in the resulting plan.

## What It Does

- Inspect current Wowhead planner builds and Blizzard import strings.
- Apply explicit, name-based talent swaps; generate verified Wowhead planner
  URLs and Blizzard-compatible import strings.
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
|           +-- wowhead-talent-planner/
|           |   +-- SKILL.md
|           |   +-- references/
|           |   `-- scripts/
|           |       +-- wowhead_assets.py
|           |       `-- wowhead_talent_builder.py
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
- Python 3.8+
- Network access for refreshing current Wowhead talent data
- Codex with plugin support for using the bundled skill inside Codex

No Python package install is required for the included scripts.

## License

This repository, including the bundled Codex plugin, skills, and scripts, is
licensed under the [GNU Affero General Public License v3.0 or later](LICENSE)
(`AGPL-3.0-or-later`), unless a file states otherwise.

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
- current Wowhead link or Blizzard import string, if you have one

Example prompt:

```text
Build me a Protection Warrior Mountain Thane Mythic+ talent setup focused on survivability.
Keep Shield Charge and give me a Wowhead planner link plus import code.
```

## Script Usage

Run commands from the repository root.

Cache current Wowhead planner assets:

```powershell
python plugins\azeroth-talent-forge\skills\wowhead-talent-planner\scripts\wowhead_assets.py "https://www.wowhead.com/talent-calc/blizzard/..." --json
```

Apply explicit swaps to a base Blizzard/Wowhead import string:

```powershell
python -B plugins\azeroth-talent-forge\skills\wowhead-talent-planner\scripts\wowhead_talent_builder.py `
  --base "https://www.wowhead.com/talent-calc/blizzard/..." `
  --clear "Old Talent Name" `
  --set "New Talent Name" `
  --choice "Choice Node Name=Choice Name"
```

The builder prints:

- Wowhead planner link
- Blizzard-compatible import code
- point totals per tree
- checked talent changes

The builder does not contain bundled presets. Every build starts from the user-provided `--base` value and explicit edits.

## Included Skills

### Wowhead Talent Planner

`plugins\azeroth-talent-forge\skills\wowhead-talent-planner` supports:

- reading current Wowhead planner/talent assets
- distinguishing Wowhead path hashes from Blizzard import strings
- decoding and re-encoding Blizzard-style import strings
- applying talent changes by name
- generating a Wowhead `/talent-calc/blizzard/<hash>` URL
- storing class/spec reference notes under `references/`

It verifies named talent changes by reopening or importing the generated plan.

## Development Notes

- Keep `SKILL.md` generic and workflow-focused.
- Keep class/spec knowledge in `plugins/azeroth-talent-forge/skills/<skill>/references/`.
- Do not add bundled talent presets unless the plugin is intentionally changed to support presets.
- Build recommendations should come from the user's stated goal and current sources, not personal defaults.

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
