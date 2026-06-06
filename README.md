# Azeroth Talent Forge

Local Codex plugin for World of Warcraft talent planning.

The plugin helps Codex inspect Wowhead talent planner builds, compare selected talents, apply user-directed talent swaps, and generate Blizzard-compatible Wowhead planner links/import strings. It is intentionally neutral: it does not ship class-specific prebuilt builds or personal preferences.

## Contents

```text
azeroth-talent-forge/
+-- .agents/
|   +-- plugins/
|       +-- marketplace.json
+-- plugins/
    +-- azeroth-talent-forge/
        +-- .codex-plugin/
        |   +-- plugin.json
        +-- skills/
            +-- wowhead-talent-planner/
                +-- SKILL.md
                +-- agents/openai.yaml
                +-- references/
                |   +-- protection-warrior.md
                +-- scripts/
                    +-- wowhead_assets.py
                    +-- wowhead_talent_builder.py
```

## Requirements

- Windows, macOS, or Linux
- Python 3.8+
- Network access for refreshing current Wowhead talent data
- Codex with plugin support for using the bundled skill inside Codex

No Python package install is required for the included scripts.

## Plugin Installation

Codex installs plugins from a configured marketplace. This repository includes a marketplace file at:

```text
.agents\plugins\marketplace.json
```

Install from the GitHub repository in two steps:

1. Add the GitHub repository as a Codex plugin marketplace.
2. Install the `azeroth-talent-forge` plugin from that marketplace.

```powershell
codex plugin marketplace add https://github.com/Z0ltrix/azeroth-talent-forge.git --ref main
codex plugin add azeroth-talent-forge@azeroth-talent-forge
```

Start a new Codex thread after installation so the bundled skill metadata is loaded.

### Verify Installation

List configured marketplaces:

```powershell
codex plugin marketplace list
```

List available plugins:

```powershell
codex plugin list
```

You should see marketplace `azeroth-talent-forge` and plugin `azeroth-talent-forge`.

### Updating The Installed Plugin

Refresh the GitHub marketplace snapshot, then reinstall the plugin:

```powershell
codex plugin marketplace upgrade azeroth-talent-forge
codex plugin add azeroth-talent-forge@azeroth-talent-forge
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

The marketplace root is the repository root. The plugin root is:

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

## Current Skill

`plugins\azeroth-talent-forge\skills\wowhead-talent-planner` supports:

- reading current Wowhead planner/talent assets
- distinguishing Wowhead path hashes from Blizzard import strings
- decoding and re-encoding Blizzard-style import strings
- applying talent changes by name
- generating a Wowhead `/talent-calc/blizzard/<hash>` URL
- storing class/spec reference notes under `references/`

## Development Notes

- Keep `SKILL.md` generic and workflow-focused.
- Keep class/spec knowledge in `plugins/azeroth-talent-forge/skills/<skill>/references/`.
- Do not add bundled talent presets unless the plugin is intentionally changed to support presets.
- Build recommendations should come from the user's stated goal and current sources, not personal defaults.
