# Fury

Reviewed build: `12.1.0.69404`
Spec ID: `72`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Lightning Strikes
- Node ID: `94803`
- Entry ID: `117400`
- Definition ID: `122412`
- Spell ID: `434969`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damaging enemies with Thunder Clap, $?a137048[Revenge, ][Raging Blow, ]or Execute has a $s1% chance to also strike one with a lightning bolt, dealing $435791s1 Nature damage$?s436152[ and generating ${$436152s3/10} Rage][].

Lightning Strikes occur $s2% more often during Avatar.
- Effect: Damaging enemies with Thunder Clap, $?a137048[Revenge, ][Raging Blow, ]or Execute has a $s1% chance to also strike one with a lightning bolt, dealing $435791s1 Nature damage$?s436152[ and generating ${$436152s3/10} Rage][].

Lightning Strikes occur $s2% more often during Avatar.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Crashing Thunder
- Node ID: `94816`
- Entry ID: `117413`
- Definition ID: `122425`
- Spell ID: `436707`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stormstrike or Nature damage your abilities deal is increased by $s1%. Stormstrike damage ignores Armor.

Thunder Clap damage increased by $s4%$?a137050[, no longer costs Rage, and now generates ${$s5/10} Rage][].$?a137050[

Improved Whirlwind, Meat Cleaver, Storm of Blood, and Barbaric Training affect Thunder Clap in addition to Whirlwind.][]
- Effect: Stormstrike or Nature damage your abilities deal is increased by $s1%. Stormstrike damage ignores Armor.

Thunder Clap damage increased by $s4%$?a137050[, no longer costs Rage, and now generates ${$s5/10} Rage][].$?a137050[

Improved Whirlwind, Meat Cleaver, Storm of Blood, and Barbaric Training affect Thunder Clap in addition to Whirlwind.][]
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94803` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ground Current
- Node ID: `94800`
- Entry ID: `117397`
- Definition ID: `122409`
- Spell ID: `436148`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lightning Strikes also deal $460670s1 Nature damage to enemies near their target. Damage reduced beyond $460670s2 targets.
- Effect: Lightning Strikes also deal $460670s1 Nature damage to enemies near their target. Damage reduced beyond $460670s2 targets.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94803` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Strength of the Mountain
- Node ID: `94808`
- Entry ID: `117405`
- Definition ID: `122417`
- Spell ID: `437068`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shield Slam damage increased by $s1%.$?a137048[

Demoralizing Shout reduces damage enemies deal to you by an additional ${-$s2}%.][

Bloodthirst and Rampage damage increased by $s4%.]
- Effect: Shield Slam damage increased by $s1%.$?a137048[

Demoralizing Shout reduces damage enemies deal to you by an additional ${-$s2}%.][

Bloodthirst and Rampage damage increased by $s4%.]
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94803` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Berserker Stance
- Node ID: `90325`
- Entry ID: `112182`
- Definition ID: `117187`
- Spell ID: `386196`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: An aggressive combat state that increases the damage of your auto-attacks by $s1%$?a1280961[, your auto-attack speed by $s6%,][] and reduces the duration of Fear, Sap and Incapacitate effects on you by $s2%.

Lasts until canceled.
- Effect: An aggressive combat state that increases the damage of your auto-attacks by $s1%$?a1280961[, your auto-attack speed by $s6%,][] and reduces the duration of Fear, Sap and Incapacitate effects on you by $s2%.

Lasts until canceled.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `node`; type `2`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Defensive Stance
- Node ID: `92538`
- Entry ID: `114644`
- Definition ID: `119650`
- Spell ID: `386208`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: A defensive combat state that reduces all damage you take by $s1%$?a452494[ and all magic damage you take by an additional $s3%][]$?a137048[][ and all damage you deal by $s2%].$?a1280961[

When an attack deals $s5% or more of your maximum health in damage, that damage is reduced by $s6%.][]

Lasts until canceled.
- Effect: A defensive combat state that reduces all damage you take by $s1%$?a452494[ and all magic damage you take by an additional $s3%][]$?a137048[][ and all damage you deal by $s2%].$?a1280961[

When an attack deals $s5% or more of your maximum health in damage, that damage is reduced by $s6%.][]

Lasts until canceled.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `1` | source `node`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Surge
- Node ID: `109811`
- Entry ID: `136070`
- Definition ID: `140825`
- Spell ID: `275336`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Avatar increases the damage of Thunder Clap by $107574s9% and reduces its cooldown by $107574s10%.
- Effect: Avatar increases the damage of Thunder Clap by $107574s9% and reduces its cooldown by $107574s10%.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94803` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slayer's Dominance
- Node ID: `94814`
- Entry ID: `117411`
- Definition ID: `122423`
- Spell ID: `444767`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your attacks against your primary target have a $?c1[$s2][$s1]% chance to overwhelm their defenses and trigger a Slayer's Strike, dealing $445579s1 Physical damage and granting you a stack of Executioner, increasing your Execute damage by $445584s1% for $445584d. Multiple stacks of Executioner may overlap.
- Effect: Your attacks against your primary target have a $?c1[$s2][$s1]% chance to overwhelm their defenses and trigger a Slayer's Strike, dealing $445579s1 Physical damage and granting you a stack of Executioner, increasing your Execute damage by $445584s1% for $445584d. Multiple stacks of Executioner may overlap.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thunder Blast
- Node ID: `94785`
- Entry ID: `117382`
- Definition ID: `122394`
- Spell ID: `435607`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shield Slam and Bloodthirst have a $s1% chance to grant you Thunder Blast, stacking up to 2 charges.

$@spellicon435222|cFFFFFFFF$@spellname435222|r
Your next Thunder Clap becomes a Thunder Blast that deals $435222s1 Stormstrike damage and generates ${$435222s4/10} Rage.
- Effect: Shield Slam and Bloodthirst have a $s1% chance to grant you Thunder Blast, stacking up to 2 charges.

$@spellicon435222|cFFFFFFFF$@spellname435222|r
Your next Thunder Clap becomes a Thunder Blast that deals $435222s1 Stormstrike damage and generates ${$435222s4/10} Rage.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94816` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Bolts
- Node ID: `94817`
- Entry ID: `117414`
- Definition ID: `122426`
- Spell ID: `436162`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Storm Bolt also hits $s1 additional nearby $Ltarget:targets;, stunning them for $s2 sec, but its cooldown is increased by ${$s3/1000} sec.
- Effect: Storm Bolt also hits $s1 additional nearby $Ltarget:targets;, stunning them for $s2 sec, but its cooldown is increased by ${$s3/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94800` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Shield
- Node ID: `94817`
- Entry ID: `118835`
- Definition ID: `123735`
- Spell ID: `438597`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Intervening a target grants them a shield for $438598d that absorbs magic damage equal to $s1 times your Armor.
- Effect: Intervening a target grants them a shield for $438598d that absorbs magic damage equal to $s1 times your Armor.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94800` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Conductivity
- Node ID: `109810`
- Entry ID: `136069`
- Definition ID: `140824`
- Spell ID: `1270723`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lightning Strike damage increased by $s1% and critical strike damage increased by $s2%.
- Effect: Lightning Strike damage increased by $s1% and critical strike damage increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109811` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Keep Your Feet on the Ground
- Node ID: `94798`
- Entry ID: `117395`
- Definition ID: `122407`
- Spell ID: `438590`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Physical damage taken reduced by $s2%.

Thunder Blast reduces damage you take by $438591s1% for $438591d.
- Effect: Physical damage taken reduced by $s2%.

Thunder Blast reduces damage you take by $438591s1% for $438591d.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94808` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Steadfast as the Peaks
- Node ID: `94798`
- Entry ID: `118836`
- Definition ID: `123736`
- Spell ID: `434970`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Stamina increased by $s1%.

$?s202168[Impending Victory][Victory Rush] increases your maximum health by $437152s3% for $437152d. When this health increase expires, you heal for any amount of the original $?s202168[Impending Victory][Victory Rush] that healed you in excess of your full health.
- Effect: Stamina increased by $s1%.

$?s202168[Impending Victory][Victory Rush] increases your maximum health by $437152s3% for $437152d. When this health increase expires, you heal for any amount of the original $?s202168[Impending Victory][Victory Rush] that healed you in excess of your full health.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94808` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Imminent Demise
- Node ID: `94788`
- Entry ID: `117385`
- Definition ID: `122397`
- Spell ID: `444769`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 Slayer's Strikes you gain Sudden Death.

Using Sudden Death accelerates your next Bladestorm, striking 1 additional time (max $445606u). Bladestorm's total duration is unchanged.

Sudden Death has a $s2% chance to trigger Reap the Storm at $s3% effectiveness.
- Effect: Every $s1 Slayer's Strikes you gain Sudden Death.

Using Sudden Death accelerates your next Bladestorm, striking 1 additional time (max $445606u). Bladestorm's total duration is unchanged.

Sudden Death has a $s2% chance to trigger Reap the Storm at $s3% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overwhelming Blades
- Node ID: `94810`
- Entry ID: `117407`
- Definition ID: `122419`
- Spell ID: `444772`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each strike of Bladestorm applies Overwhelmed to all enemies affected, increasing damage you deal to them by $445836s1% for $445836d, max $445836u stacks.
- Effect: Each strike of Bladestorm applies Overwhelmed to all enemies affected, increasing damage you deal to them by $445836s1% for $445836d, max $445836u stacks.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Relentless Pursuit
- Node ID: `94795`
- Entry ID: `117392`
- Definition ID: `122404`
- Spell ID: `444776`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Charge increases your movement speed by $446044s1% for $446044d.

Charge removes all movement impairing effects, this effect cannot occur more than once every $458386d.
- Effect: Charge increases your movement speed by $446044s1% for $446044d.

Charge removes all movement impairing effects, this effect cannot occur more than once every $458386d.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vicious Agility
- Node ID: `94795`
- Entry ID: `123408`
- Definition ID: `128246`
- Spell ID: `444777`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Heroic Leap reduces the cooldown of Charge by $s1 sec and Charge reduces the cooldown of Heroic Leap by $s2 sec.
- Effect: Heroic Leap reduces the cooldown of Charge by $s1 sec and Charge reduces the cooldown of Heroic Leap by $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Violent Euphoria
- Node ID: `109817`
- Entry ID: `136076`
- Definition ID: `140831`
- Spell ID: `1270717`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Bladestorm puts you into a battle trance, granting you 15% haste for 8 sec after you stop Bladestorming.
- Effect: Bladestorm puts you into a battle trance, granting you 15% haste for 8 sec after you stop Bladestorming.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gathering Clouds
- Node ID: `94792`
- Entry ID: `117389`
- Definition ID: `122401`
- Spell ID: `436201`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your attacks trigger Lightning Strikes $s1% more often.
- Effect: Your attacks trigger Lightning Strikes $s1% more often.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94817` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thorim's Might
- Node ID: `94792`
- Entry ID: `118834`
- Definition ID: `123734`
- Spell ID: `436152`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Lightning Strikes generate ${$s1/10} Rage.

$?a137048[Revenge][Raging Blow] and Execute damage increased by $s2%.
- Effect: Lightning Strikes generate ${$s1/10} Rage.

$?a137048[Revenge][Raging Blow] and Execute damage increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94817` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flashing Skies
- Node ID: `94797`
- Entry ID: `117394`
- Definition ID: `122406`
- Spell ID: `437079`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Thunder Blast calls down a Lightning Strike on an enemy it hits.
- Effect: Thunder Blast calls down a Lightning Strike on an enemy it hits.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94785` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Snap Induction
- Node ID: `94797`
- Entry ID: `118833`
- Definition ID: `123733`
- Spell ID: `456270`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Activating $?a137048[Demoralizing Shout][Recklessness] grants a charge of Thunder Blast.
- Effect: Activating $?a137048[Demoralizing Shout][Recklessness] grants a charge of Thunder Blast.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94785` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Burst of Power
- Node ID: `94807`
- Entry ID: `117404`
- Definition ID: `122416`
- Spell ID: `437118`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lightning Strikes have a $h% chance to make your next $s1 $?a137048[Shield Slams][Bloodthirsts] have no cooldown$?a137050[, deal $437121s2% increased damage, and generate ${$437121s3/10} additional Rage][].
- Effect: Lightning Strikes have a $h% chance to make your next $s1 $?a137048[Shield Slams][Bloodthirsts] have no cooldown$?a137050[, deal $437121s2% increased damage, and generate ${$437121s3/10} additional Rage][].
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94798` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Capacitance
- Node ID: `109809`
- Entry ID: `136068`
- Definition ID: `140823`
- Spell ID: `1270724`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: During Avatar, Thunder Blast extends Avatar's duration by ${$s1/1000}.1 sec.
- Effect: During Avatar, Thunder Blast extends Avatar's duration by ${$s1/1000}.1 sec.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109810` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death Drive
- Node ID: `94813`
- Entry ID: `117410`
- Definition ID: `122422`
- Spell ID: `444770`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You heal for $s1% of damage dealt by Sudden Death.
- Effect: You heal for $s1% of damage dealt by Sudden Death.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94788` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Culling Cyclone
- Node ID: `94786`
- Entry ID: `117383`
- Definition ID: `122395`
- Spell ID: `444778`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each strike of Bladestorm deals an additional $s1% damage evenly split across all targets.
- Effect: Each strike of Bladestorm deals an additional $s1% damage evenly split across all targets.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94810` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Brutal Finish
- Node ID: `94786`
- Entry ID: `123409`
- Definition ID: `128247`
- Spell ID: `446085`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your next $?c1[Mortal Strike][Rampage] after Bladestorm ends deals $?c1[$446918s1][$446918s2]% additional damage.
- Effect: Your next $?c1[Mortal Strike][Rampage] after Bladestorm ends deals $?c1[$446918s1][$446918s2]% additional damage.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94810` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fierce Followthrough
- Node ID: `94787`
- Entry ID: `117384`
- Definition ID: `122396`
- Spell ID: `444773`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike][Bloodthirst] critical strikes increase the damage of your next $?c1[Mortal Strike][Bloodthirst] by $?c1[$458689s1][$458689s2]%.
- Effect: $?c1[Mortal Strike][Bloodthirst] critical strikes increase the damage of your next $?c1[Mortal Strike][Bloodthirst] by $?c1[$458689s1][$458689s2]%.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94795` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Opportunist
- Node ID: `94787`
- Entry ID: `123770`
- Definition ID: `128608`
- Spell ID: `444774`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[When Overpower has its cooldown reset by Tactician, your next Overpower deals $456120s3% additional damage and $456120s4% additional critical damage.][When Raging Blow resets its own cooldown, your next Raging Blow deals $456120s1% additional damage and $456120s2% additional critical damage.] Stacking up to $456120u times.
- Effect: $?c1[When Overpower has its cooldown reset by Tactician, your next Overpower deals $456120s3% additional damage and $456120s4% additional critical damage.][When Raging Blow resets its own cooldown, your next Raging Blow deals $456120s1% additional damage and $456120s2% additional critical damage.] Stacking up to $456120u times.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94795` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deadly Focus
- Node ID: `109816`
- Entry ID: `136075`
- Definition ID: `140830`
- Spell ID: `1270718`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Executioner's duration is increased by ${$s1/1000} sec.
- Effect: Executioner's duration is increased by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109817` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm of Blood
- Node ID: `110654`
- Entry ID: `137472`
- Definition ID: `142232`
- Spell ID: `1299025`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Whirlwind $?a436707[and Thunder Clap ][]affects all targets with Rend, causing them to Bleed for $388539o1 damage over $388539d.
- Effect: Whirlwind $?a436707[and Thunder Clap ][]affects all targets with Rend, causing them to Bleed for $388539o1 damage over $388539d.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90326` (type `2`), node `90344` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Intervene
- Node ID: `108674`
- Entry ID: `134214`
- Definition ID: `138992`
- Spell ID: `3411`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Run at high speed toward an ally, intercepting all melee and ranged attacks against them for $147833d while they remain within $147833A1 yds.
- Effect: Run at high speed toward an ally, intercepting all melee and ranged attacks against them for $147833d while they remain within $147833A1 yds.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `entry`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `90337` (type `2`), node `90371` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Interpose
- Node ID: `108674`
- Entry ID: `134213`
- Definition ID: `138991`
- Spell ID: `1244088`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Run at high speed toward a target location near your allies, taking $1244091s1% of all damage dealt to allies within $a1 yards for $1244091d or until you take at least ${($1244091s3/100)*$MHP} damage from this effect.
- Effect: Run at high speed toward a target location near your allies, taking $1244091s1% of all damage dealt to allies within $a1 yards for $1244091d or until you take at least ${($1244091s3/100)*$MHP} damage from this effect.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `90337` (type `2`), node `90371` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Avatar of the Storm
- Node ID: `94805`
- Entry ID: `117402`
- Definition ID: `122414`
- Spell ID: `437134`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Avatar grants you $s1 charges of Thunder Blast and resets the cooldown of Thunder Clap.

While Avatar is not active, Lightning Strikes have a $s2% chance to grant you Avatar for $s3 secs.

$@spellicon435222|cFFFFFFFF$@spellname435222|r
Your next Thunder Clap becomes a Thunder Blast that deals Stormstrike damage.
- Effect: Casting Avatar grants you $s1 charges of Thunder Blast and resets the cooldown of Thunder Clap.

While Avatar is not active, Lightning Strikes have a $s2% chance to grant you Avatar for $s3 secs.

$@spellicon435222|cFFFFFFFF$@spellname435222|r
Your next Thunder Clap becomes a Thunder Blast that deals Stormstrike damage.
- Point cost per purchased rank: `1` × Hero pool (Mountain Thane) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94792` (type `2`), node `94797` (type `2`), node `94807` (type `2`), node `109809` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Show No Mercy
- Node ID: `94784`
- Entry ID: `117381`
- Definition ID: `122393`
- Spell ID: `444771`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Executioner also increases your Execute critical strike chance and critical strike damage by $445584s2% per stack.
- Effect: Executioner also increases your Execute critical strike chance and critical strike damage by $445584s2% per stack.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94813` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reap the Storm
- Node ID: `94809`
- Entry ID: `117406`
- Definition ID: `122418`
- Spell ID: `444775`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When $?c1[Cleave hits][Rampage hits] $s2 or more targets$?c2[ via Improved Whirlwind][] you have a $?c1[$s3][$s4]% chance to unleash a flurry of steel, striking all nearby enemies for $446005s1 Physical damage and applying Overwhelmed. Deals reduced damage beyond $s1 targets.
- Effect: When $?c1[Cleave hits][Rampage hits] $s2 or more targets$?c2[ via Improved Whirlwind][] you have a $?c1[$s3][$s4]% chance to unleash a flurry of steel, striking all nearby enemies for $446005s1 Physical damage and applying Overwhelmed. Deals reduced damage beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94786` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slayer's Malice
- Node ID: `94801`
- Entry ID: `117398`
- Definition ID: `122410`
- Spell ID: `444779`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Overpower][Raging Blow] and Execute damage increased by $?c1[$s1][$s2]%.
- Effect: $?c1[Overpower][Raging Blow] and Execute damage increased by $?c1[$s1][$s2]%.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94787` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unhinged
- Node ID: `109815`
- Entry ID: `136074`
- Definition ID: `140829`
- Spell ID: `386628`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 strikes of Bladestorm, you automatically cast a $?c1[Mortal Strike][Bloodthirst] at your target or random nearby enemy, dealing $s2% of normal damage.
- Effect: Every $s1 strikes of Bladestorm, you automatically cast a $?c1[Mortal Strike][Bloodthirst] at your target or random nearby enemy, dealing $s2% of normal damage.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `109816` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unrelenting Onslaught
- Node ID: `94820`
- Entry ID: `117417`
- Definition ID: `122429`
- Spell ID: `444780`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Using Sudden Death causes you to both reduce the cooldown of Bladestorm by $s1 sec and apply $s2 stack of Overwhelmed to your primary target per stack of Executioner you have.

You can use Pummel and Storm Bolt while Bladestorming.

Bladestorm damage increased by $s4%.
- Effect: Using Sudden Death causes you to both reduce the cooldown of Bladestorm by $s1 sec and apply $s2 stack of Overwhelmed to your primary target per stack of Executioner you have.

You can use Pummel and Storm Bolt while Bladestorming.

Bladestorm damage increased by $s4%.
- Point cost per purchased rank: `1` × Hero pool (Slayer) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94784` (type `2`), node `94801` (type `2`), node `94809` (type `2`), node `109815` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Demolish
- Node ID: `94818`
- Entry ID: `117415`
- Definition ID: `122427`
- Spell ID: `436358`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash a series of precise and powerful strikes against your target, dealing ${$440884s1+$440886s1+$440888s1} damage to it, and $440888s1 damage to enemies within $440888A1 yds of it. Deals reduced damage beyond $s1 targets.

While channeling Demolish, you take $s4% less damage and are immune to stuns, knockbacks, and forced movement effects.

You can block, parry, dodge, and use certain defensive abilities while channeling Demolish.
- Effect: Unleash a series of precise and powerful strikes against your target, dealing ${$440884s1+$440886s1+$440888s1} damage to it, and $440888s1 damage to enemies within $440888A1 yds of it. Deals reduced damage beyond $s1 targets.

While channeling Demolish, you take $s4% less damage and are immune to stuns, knockbacks, and forced movement effects.

You can block, parry, dodge, and use certain defensive abilities while channeling Demolish.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dual Wield Specialization
- Node ID: `90373`
- Entry ID: `112240`
- Definition ID: `117245`
- Spell ID: `382900`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: While dual wielding your damage is increased by $s1% and movement speed is increased by $s4%.
- Effect: While dual wielding your damage is increased by $s1% and movement speed is increased by $s4%.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1`
- Incoming edges: node `108685` (type `2`), node `110118` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `81374`, index `1`, operation `1`, curve `81381`, index `2`, operation `1`, curve `81380`, index `3`, operation `1`, curve `81407`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
