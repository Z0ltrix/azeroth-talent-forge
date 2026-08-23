# Scalecommander

Reviewed build: `12.1.0.69404`
Hero subtree ID: `36`
Description: Scalecommanders are natural born leaders, capable of inspiring those around them to become better. They are the chosen generals of the Dracthyr and use their empower spells to send battle commands and summon troops.

## Hero talents

### Mass Disintegrate
- Node ID: `94939`
- Entry ID: `117536`
- Definition ID: `122548`
- Spell ID: `436335`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empower spells cause your next Disintegrate to strike up to $s1 targets. When striking fewer than $s1 targets, Disintegrate damage is increased by $s2% for each missing target.
- Effect: Empower spells cause your next Disintegrate to strike up to $s1 targets. When striking fewer than $s1 targets, Disintegrate damage is increased by $s2% for each missing target.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `node`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mass Eruption
- Node ID: `98931`
- Entry ID: `122279`
- Definition ID: `127179`
- Spell ID: `438587`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empower spells cause your next Eruption to strike up to $s1 targets. When striking less than $s1 targets, Eruption damage is increased by $s2% for each missing target.
- Effect: Empower spells cause your next Eruption to strike up to $s1 targets. When striking less than $s1 targets, Eruption damage is increased by $s2% for each missing target.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `node`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Might of the Black Dragonflight
- Node ID: `94952`
- Entry ID: `117549`
- Definition ID: `122561`
- Spell ID: `441705`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Black spells deal $s1% increased damage.
- Effect: Black spells deal $s1% increased damage.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bombardments
- Node ID: `94936`
- Entry ID: `117533`
- Definition ID: `122545`
- Spell ID: `434300`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mass Disintegrate][Mass Eruption] marks your primary target for destruction for the next $434473d.

You and your allies have a chance to trigger a Bombardment when attacking marked targets, dealing $<dmg> Volcanic damage split amongst all nearby enemies.
- Effect: $?c1[Mass Disintegrate][Mass Eruption] marks your primary target for destruction for the next $434473d.

You and your allies have a chance to trigger a Bombardment when attacking marked targets, dealing $<dmg> Volcanic damage split amongst all nearby enemies.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Onslaught
- Node ID: `94944`
- Entry ID: `117541`
- Definition ID: `122553`
- Spell ID: `441245`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Entering combat grants a charge of Burnout, causing your next Living Flame to cast instantly.
- Effect: Entering combat grants a charge of Burnout, causing your next Living Flame to cast instantly.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Command Squadron
- Node ID: `109795`
- Entry ID: `136053`
- Definition ID: `140808`
- Spell ID: `1260745`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While flying during $?s403631[Breath of Eons][Deep Breath] you are assisted by a squadron of Dracthyr who assault enemies with Pyre, dealing $1236970s1 Fire damage to nearby enemies up to $s3 times.
- Effect: While flying during $?s403631[Breath of Eons][Deep Breath] you are assisted by a squadron of Dracthyr who assault enemies with Pyre, dealing $1236970s1 Fire damage to nearby enemies up to $s3 times.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Melt Armor
- Node ID: `94921`
- Entry ID: `117518`
- Definition ID: `122530`
- Spell ID: `441176`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s403631[Breath of Eons][Deep Breath] causes enemies to take $s2% increased damage from Bombardments and Essence abilities for $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Effect: $?s403631[Breath of Eons][Deep Breath] causes enemies to take $s2% increased damage from Bombardments and Essence abilities for $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94952` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wingleader
- Node ID: `94953`
- Entry ID: `117550`
- Definition ID: `122562`
- Spell ID: `441206`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mass Disintegrate][Mass Eruption] reduces the remaining cooldown of $?c1[Deep Breath][Breath of Eons] by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec for each target struck.
- Effect: $?c1[Mass Disintegrate][Mass Eruption] reduces the remaining cooldown of $?c1[Deep Breath][Breath of Eons] by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec for each target struck.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94936` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unrelenting Siege
- Node ID: `94934`
- Entry ID: `117531`
- Definition ID: `122543`
- Spell ID: `441246`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For each second you are in combat, Azure Strike, Living Flame, and $?c1[Disintegrate][Eruption] deal $s1% increased damage, up to $s2%.
- Effect: For each second you are in combat, Azure Strike, Living Flame, and $?c1[Disintegrate][Eruption] deal $s1% increased damage, up to $s2%.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94944` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Concentrated Power
- Node ID: `109794`
- Entry ID: `136052`
- Definition ID: `140807`
- Spell ID: `1261448`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mass Disintegrate][Mass Eruption] strikes $s1 additional $Ltarget:targets;.
- Effect: $?c1[Mass Disintegrate][Mass Eruption] strikes $s1 additional $Ltarget:targets;.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109795` (type `2`), node `109795` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hardened Scales
- Node ID: `94933`
- Entry ID: `117530`
- Definition ID: `122542`
- Spell ID: `441180`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Obsidian Scales reduces damage taken by an additional ${$s1/-1}%.
- Effect: Obsidian Scales reduces damage taken by an additional ${$s1/-1}%.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94921` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Menacing Presence
- Node ID: `94933`
- Entry ID: `120125`
- Definition ID: `125025`
- Spell ID: `441181`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Knocking enemies up or backwards reduces their damage done to you by $s1% for $441201d.
- Effect: Knocking enemies up or backwards reduces their damage done to you by $s1% for $441201d.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94921` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Extended Battle
- Node ID: `94928`
- Entry ID: `117525`
- Definition ID: `122537`
- Spell ID: `441212`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence abilities extend Bombardments by $s1 sec.
- Effect: Essence abilities extend Bombardments by $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94953` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Diverted Power
- Node ID: `94928`
- Entry ID: `120124`
- Definition ID: `125024`
- Spell ID: `441219`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Bombardments have a chance to generate Essence Burst.
- Effect: Bombardments have a chance to generate Essence Burst.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94953` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nimble Flyer
- Node ID: `94943`
- Entry ID: `117540`
- Definition ID: `122552`
- Spell ID: `441253`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Hovering, damage taken from area of effect attacks is reduced by ${$s1/-1}%.
- Effect: While Hovering, damage taken from area of effect attacks is reduced by ${$s1/-1}%.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94934` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slipstream
- Node ID: `94943`
- Entry ID: `120123`
- Definition ID: `125023`
- Spell ID: `441257`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?s403631[Breath of Eons][Deep Breath] resets a charge of Hover.
- Effect: $?s403631[Breath of Eons][Deep Breath] resets a charge of Hover.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94934` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Refined Essence
- Node ID: `109793`
- Entry ID: `136051`
- Definition ID: `140806`
- Spell ID: `1261452`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence abilities deal $s1% additional damage.
- Effect: Essence abilities deal $s1% additional damage.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109794` (type `2`), node `109794` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Maneuverability
- Node ID: `94941`
- Entry ID: `117538`
- Definition ID: `122550`
- Spell ID: `433871`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s403631[Breath of Eons][Deep Breath] can now be steered in your desired direction.

In addition, $?s403631[Breath of Eons][Deep Breath] burns targets for $441172o1 Volcanic damage over $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Effect: $?s403631[Breath of Eons][Deep Breath] can now be steered in your desired direction.

In addition, $?s403631[Breath of Eons][Deep Breath] burns targets for $441172o1 Volcanic damage over $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94928` (type `2`), node `94933` (type `2`), node `94943` (type `2`), node `109793` (type `2`), node `109793` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
