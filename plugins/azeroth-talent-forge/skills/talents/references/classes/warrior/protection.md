# Protection

Reviewed build: `12.1.0.69404`
Spec ID: `73`
Role: `0`

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
### Battle Stance
- Node ID: `90261`
- Entry ID: `112112`
- Definition ID: `117117`
- Spell ID: `386164`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: A balanced combat state that increases the critical strike chance of your abilities by $s1%$?a1280961[, the critical strike damage of your abilities by $s4%,][] and reduces the duration of movement impairing effects by $s2%. 

Lasts until canceled.
- Effect: A balanced combat state that increases the critical strike chance of your abilities by $s1%$?a1280961[, the critical strike damage of your abilities by $s4%,][] and reduces the duration of movement impairing effects by $s2%. 

Lasts until canceled.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `node`; type `2`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Defensive Stance
- Node ID: `90330`
- Entry ID: `112187`
- Definition ID: `117192`
- Spell ID: `386208`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
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
### Blood and Thunder
- Node ID: `110653`
- Entry ID: `137471`
- Definition ID: `142231`
- Spell ID: `384277`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Thunder Clap affects all targets with Rend, causing them to Bleed for $388539o1 damage over $388539d.
- Effect: Thunder Clap affects all targets with Rend, causing them to Bleed for $388539o1 damage over $388539d.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90326` (type `2`), node `90344` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Intervene
- Node ID: `90329`
- Entry ID: `112186`
- Definition ID: `117191`
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
### Martial Expert
- Node ID: `94812`
- Entry ID: `117409`
- Definition ID: `122421`
- Spell ID: `429638`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strike damage of your abilities is increased by $s1% and the amount of damage blocked by your critical blocks is increased by $s2%.
- Effect: Critical strike damage of your abilities is increased by $s1% and the amount of damage blocked by your critical blocks is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Colossal Might
- Node ID: `94819`
- Entry ID: `117416`
- Definition ID: `122428`
- Spell ID: `429634`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Colossal Might increases damage dealt by your next Demolish by $440989s1%, stacking up to $440989u times.

$?c1[Mortal Strike][Shield Slam] grants a stack of Colossal Might and $?c1[Cleave][Revenge] grants a stack of Colossal Might when it strikes $s1 or more targets.
- Effect: Colossal Might increases damage dealt by your next Demolish by $440989s1%, stacking up to $440989u times.

$?c1[Mortal Strike][Shield Slam] grants a stack of Colossal Might and $?c1[Cleave][Revenge] grants a stack of Colossal Might when it strikes $s1 or more targets.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Boneshaker
- Node ID: `94789`
- Entry ID: `117386`
- Definition ID: `122398`
- Spell ID: `429639`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shockwave's stun duration is increased by ${$s1/1000} sec and reduces the movement speed of affected enemies by $458480s1% for $458480d after the stun ends.
- Effect: Shockwave's stun duration is increased by ${$s1/1000} sec and reduces the movement speed of affected enemies by $458480s1% for $458480d after the stun ends.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthquaker
- Node ID: `94789`
- Entry ID: `119858`
- Definition ID: `124758`
- Spell ID: `440992`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Shockwave also knocks enemies into the air and its cooldown is reduced by ${$s1/-1000} sec.
- Effect: Shockwave also knocks enemies into the air and its cooldown is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Decimator
- Node ID: `109814`
- Entry ID: `136073`
- Definition ID: `140828`
- Spell ID: `1270704`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Demolish's final strike applies Deep Wounds to all targets at $s1% effectiveness.
- Effect: Demolish's final strike applies Deep Wounds to all targets at $s1% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### One Against Many
- Node ID: `94799`
- Entry ID: `117396`
- Definition ID: `122408`
- Spell ID: `429637`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shockwave$?c1[, Cleave,][] and $?c1[Whirlwind][Revenge] deal $s1% more damage per target affected up to $s2.
- Effect: Shockwave$?c1[, Cleave,][] and $?c1[Whirlwind][Revenge] deal $s1% more damage per target affected up to $s2.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94812` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arterial Bleed
- Node ID: `94799`
- Entry ID: `119856`
- Definition ID: `124756`
- Spell ID: `440995`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Colossal Might increases the damage of your Rend and Deep Wounds by $440989s2% per stack.
- Effect: Colossal Might increases the damage of your Rend and Deep Wounds by $440989s2% per stack.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94812` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tide of Battle
- Node ID: `94811`
- Entry ID: `117408`
- Definition ID: `122420`
- Spell ID: `429641`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Colossal Might increases the damage of your $?c1[Overpower][Revenge] and Execute by $?c1[$440989s3][$440989s4]% per stack.
- Effect: Colossal Might increases the damage of your $?c1[Overpower][Revenge] and Execute by $?c1[$440989s3][$440989s4]% per stack.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94819` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### No Stranger to Pain
- Node ID: `94815`
- Entry ID: `117412`
- Definition ID: `122424`
- Spell ID: `429644`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage prevented by each use of Ignore Pain is increased by $s1%.
- Effect: Damage prevented by each use of Ignore Pain is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94789` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Veteran Vitality
- Node ID: `94815`
- Entry ID: `119857`
- Definition ID: `124757`
- Spell ID: `440993`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When your health is brought below 35%, you gain a Second Wind, healing you for ${$441387s1*$441387t1*$441387d}% of your max health over $441387d.

This effect cannot occur more than once every $proccooldown sec.
- Effect: When your health is brought below 35%, you gain a Second Wind, healing you for ${$441387s1*$441387t1*$441387d}% of your max health over $441387d.

This effect cannot occur more than once every $proccooldown sec.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94789` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cut to the Bone
- Node ID: `109813`
- Entry ID: `136072`
- Definition ID: `140827`
- Spell ID: `1270709`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike][Shield Slam] critical strikes increase your Rend and Deep Wounds damage by $1270840s1% for $1270840d.
- Effect: $?c1[Mortal Strike][Shield Slam] critical strikes increase your Rend and Deep Wounds damage by $1270840s1% for $1270840d.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### One-Handed Weapon Specialization
- Node ID: `90324`
- Entry ID: `112181`
- Definition ID: `117186`
- Spell ID: `382895`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `200`
- Description: While wielding one-handed weapons your damage is increased by $s1% and Leech increased by $s4%.
- Effect: While wielding one-handed weapons your damage is increased by $s1% and Leech increased by $s4%.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `108685` (type `2`), node `110118` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `81373`, index `1`, operation `1`, curve `81372`, index `2`, operation `1`, curve `81383`, index `3`, operation `1`, curve `81382`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Practiced Strikes
- Node ID: `94796`
- Entry ID: `117393`
- Definition ID: `122405`
- Spell ID: `429647`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike and Slam damage increased by $s1%.

Cleave and Whirlwind damage increased by $s2%][Shield Slam damage increased by $s3%.

Revenge and Thunder Clap damage increased by $s4%].$?c3[

Shield Slam generates an additional ${$s5/10} Rage.][]
- Effect: $?c1[Mortal Strike and Slam damage increased by $s1%.

Cleave and Whirlwind damage increased by $s2%][Shield Slam damage increased by $s3%.

Revenge and Thunder Clap damage increased by $s4%].$?c3[

Shield Slam generates an additional ${$s5/10} Rage.][]
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94799` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Precise Might
- Node ID: `94794`
- Entry ID: `117391`
- Definition ID: `122403`
- Spell ID: `431548`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike][Shield Slam] critical strikes grant an additional stack of Colossal Might.
- Effect: $?c1[Mortal Strike][Shield Slam] critical strikes grant an additional stack of Colossal Might.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94811` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mountain of Muscle and Scars
- Node ID: `94806`
- Entry ID: `117403`
- Definition ID: `122415`
- Spell ID: `429642`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You deal $s1% more damage and take $s4% less damage.

Size increased by $s5%.
- Effect: You deal $s1% more damage and take $s4% less damage.

Size increased by $s5%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94815` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Celeritous Conclusion
- Node ID: `109812`
- Entry ID: `136071`
- Definition ID: `140826`
- Spell ID: `1270710`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Demolish's final strike grants $1270843s1% Haste for $1270843d and increases the critical strike chance of your next $?c1[Mortal Strike][Shield Slam] by $1270846s1%.
- Effect: Demolish's final strike grants $1270843s1% Haste for $1270843d and increases the critical strike chance of your next $?c1[Mortal Strike][Shield Slam] by $1270846s1%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109813` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dominance of the Colossus
- Node ID: `94793`
- Entry ID: `117390`
- Definition ID: `122402`
- Spell ID: `429636`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies affected by Demolish take up to ${$447513s2*$447513u*0.1}% more damage from you and deal up to ${$447513s1*$447513u*-0.1}% less damage to you for $447513d based on the number of stacks of Colossal Might consumed by Demolish.

Colossal Might stacks up to 10 times.
- Effect: Enemies affected by Demolish take up to ${$447513s2*$447513u*0.1}% more damage from you and deal up to ${$447513s1*$447513u*-0.1}% less damage to you for $447513d based on the number of stacks of Colossal Might consumed by Demolish.

Colossal Might stacks up to 10 times.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94794` (type `2`), node `94796` (type `2`), node `94806` (type `2`), node `109812` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
