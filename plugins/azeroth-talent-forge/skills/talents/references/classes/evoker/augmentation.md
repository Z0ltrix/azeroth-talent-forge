# Augmentation

Reviewed build: `12.1.0.69404`
Spec ID: `1473`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

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
### Legacy of the Lifebinder
- Node ID: `94950`
- Entry ID: `117547`
- Definition ID: `122559`
- Spell ID: `1264269`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Fire Breath gains][Dream Breath and Fire Breath gain] an additional charge.
- Effect: $?c1[Fire Breath gains][Dream Breath and Fire Breath gain] an additional charge.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
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
### Landslide
- Node ID: `93305`
- Entry ID: `115614`
- Definition ID: `120626`
- Spell ID: `358385`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Conjure a path of shifting stone towards the target location, rooting enemies for $355689d. Damage may cancel the effect.
- Effect: Conjure a path of shifting stone towards the target location, rooting enemies for $355689d. Damage may cancel the effect.
- Point cost per purchased rank: `1` × Specialization pool (Augmentation, Devastation, Preservation) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Obsidian Scales
- Node ID: `93304`
- Entry ID: `115613`
- Definition ID: `120625`
- Spell ID: `363916`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reinforce your scales, reducing damage taken by $s1% $?s374348[and causing you to be healed over $374349d equal to the damage it prevented][]. Lasts $d.
- Effect: Reinforce your scales, reducing damage taken by $s1% $?s374348[and causing you to be healed over $374349d equal to the damage it prevented][]. Lasts $d.
- Point cost per purchased rank: `1` × Specialization pool (Augmentation, Devastation, Preservation) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
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
### Chrono Flame
- Node ID: `94954`
- Entry ID: `117551`
- Definition ID: `122563`
- Spell ID: `431442`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Living Flame is enhanced with Bronze magic, repeating $?c2[$s1%][$s3%] of the damage or healing you dealt to the target in the last $s2 sec as Arcane, up to $?s1260647[$<cap2>][$<cap>].
- Effect: Living Flame is enhanced with Bronze magic, repeating $?c2[$s1%][$s3%] of the damage or healing you dealt to the target in the last $s2 sec as Arcane, up to $?s1260647[$<cap2>][$<cap>].
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Warp
- Node ID: `94948`
- Entry ID: `117545`
- Definition ID: `122557`
- Spell ID: `429483`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hover now causes you to briefly warp out of existence and appear at your destination. Hover's cooldown is also reduced by ${$s1/-1000} sec.

Hover continues to allow Evoker spells to be cast while moving.
- Effect: Hover now causes you to briefly warp out of existence and appear at your destination. Hover's cooldown is also reduced by ${$s1/-1000} sec.

Hover continues to allow Evoker spells to be cast while moving.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Temporal Burst
- Node ID: `94955`
- Entry ID: `117552`
- Definition ID: `122564`
- Spell ID: `431695`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tip the Scales overloads you with temporal energy, increasing your haste, movement speed, and cooldown recovery rate by ${$431698u*$431698s1}%, decreasing over $431698d.
- Effect: Tip the Scales overloads you with temporal energy, increasing your haste, movement speed, and cooldown recovery rate by ${$431698u*$431698s1}%, decreasing over $431698d.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reverberations
- Node ID: `94925`
- Entry ID: `117522`
- Definition ID: `122534`
- Spell ID: `431615`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Verdant Embrace heals for an additional $s1% over $409895d.][Upheaval deals $s2% additional damage over $431620d.]
- Effect: $?c2[Verdant Embrace heals for an additional $s1% over $409895d.][Upheaval deals $s2% additional damage over $431620d.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chronoboon
- Node ID: `109510`
- Entry ID: `135743`
- Definition ID: `140498`
- Spell ID: `1260484`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tip the Scales' cooldown is reduced by ${$s1/-1000} sec.
- Effect: Tip the Scales' cooldown is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Temporality
- Node ID: `94935`
- Entry ID: `117532`
- Definition ID: `122544`
- Spell ID: `431873`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Warp reduces damage taken by ${$s1/-1}%, starting high and reducing over $431872d.
- Effect: Warp reduces damage taken by ${$s1/-1}%, starting high and reducing over $431872d.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94948` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Motes of Acceleration
- Node ID: `94935`
- Entry ID: `117784`
- Definition ID: `122796`
- Spell ID: `432008`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Warp leaves a trail of Motes of Acceleration. Allies who come in contact with a mote gain 20% increased movement speed for 30 sec.
- Effect: Warp leaves a trail of Motes of Acceleration. Allies who come in contact with a mote gain 20% increased movement speed for 30 sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94948` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nozdormu Adept
- Node ID: `94947`
- Entry ID: `117544`
- Definition ID: `122556`
- Spell ID: `431715`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Temporal Anomaly mana cost reduced by $s1% and cooldown reduced by ${$s2/-1000} sec.][Prescience cooldown reduced by ${$s3/-1000} sec and it grants $s4% additional critical strike chance.]
- Effect: $?c2[Temporal Anomaly mana cost reduced by $s1% and cooldown reduced by ${$s2/-1000} sec.][Prescience cooldown reduced by ${$s3/-1000} sec and it grants $s4% additional critical strike chance.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94955` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chronal Dynamo
- Node ID: `109509`
- Entry ID: `135742`
- Definition ID: `140497`
- Spell ID: `1291522`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Living Flame's cast time is reduced by ${$s1/-1000}.1 sec, and it deals $s2% increased damage or healing when it is a non-instant cast.
- Effect: Living Flame's cast time is reduced by ${$s1/-1000}.1 sec, and it deals $s2% increased damage or healing when it is a non-instant cast.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `109510` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primacy
- Node ID: `94951`
- Entry ID: `117548`
- Definition ID: `122560`
- Spell ID: `431657`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For each $?c2[healing over time effect from Verdant Embrace][damage over time effect from Upheaval], gain $s1% haste, up to $s2%.
- Effect: For each $?c2[healing over time effect from Verdant Embrace][damage over time effect from Upheaval], gain $s1% haste, up to $s2%.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94925` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Double-time
- Node ID: `94932`
- Entry ID: `117529`
- Definition ID: `122541`
- Spell ID: `431874`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[When Dream Breath or Fire Breath critically strike, their duration is extended by $s1 sec, up to a maximum of ${$s1*6} sec.][Ebon Might and Prescience gain a chance equal to your critical strike chance to grant $s2% additional stats. For Ebon Might, this increase lasts $<dura> sec.]
- Effect: $?c2[When Dream Breath or Fire Breath critically strike, their duration is extended by $s1 sec, up to a maximum of ${$s1*6} sec.][Ebon Might and Prescience gain a chance equal to your critical strike chance to grant $s2% additional stats. For Ebon Might, this increase lasts $<dura> sec.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94935` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Time Convergence
- Node ID: `94932`
- Entry ID: `117786`
- Definition ID: `122798`
- Spell ID: `431984`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Non-defensive abilities with a $s1 second or longer cooldown grant $431991s1% Intellect for $431991d.

Essence spells extend the duration by $s2 sec.
- Effect: Non-defensive abilities with a $s1 second or longer cooldown grant $431991s1% Intellect for $431991d.

Essence spells extend the duration by $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94935` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overclock
- Node ID: `109508`
- Entry ID: `135741`
- Definition ID: `140496`
- Spell ID: `1260647`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Chrono Flames' maximum damage or healing is increased by $s1%, up to $<cap> Arcane.
- Effect: Chrono Flames' maximum damage or healing is increased by $s1%, up to $<cap> Arcane.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `109509` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Golden Opportunity
- Node ID: `94942`
- Entry ID: `117539`
- Definition ID: `122551`
- Spell ID: `432004`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Echo is $s1% more effective.][Prescience lasts $s2% longer.]
- Effect: $?c2[Echo is $s1% more effective.][Prescience lasts $s2% longer.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94951` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Instability Matrix
- Node ID: `94930`
- Entry ID: `126310`
- Definition ID: `131136`
- Spell ID: `431484`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Each time you cast an empower spell, unstable time magic reduces its cooldown by up to $s1 sec.
- Effect: Each time you cast an empower spell, unstable time magic reduces its cooldown by up to $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94947` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Afterimage
- Node ID: `94929`
- Entry ID: `117526`
- Definition ID: `122538`
- Spell ID: `431875`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empower spells send up to $s1 Chrono Flames to your targets.
- Effect: Empower spells send up to $s1 Chrono Flames to your targets.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94930` (type `2`), node `94932` (type `2`), node `94942` (type `2`), node `109508` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
