# Mountain Thane

Reviewed build: `12.1.0.69404`
Hero subtree ID: `61`
Description: Mountain Thanes are fierce fighters that live to challenge themselves against worthy opponents. Drawing strength from the earth and power from the storm, they strike with blows that hit like a thunder clap to overwhelm their enemies.

## Hero talents

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
