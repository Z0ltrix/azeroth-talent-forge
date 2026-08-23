# Arms

Reviewed build: `12.1.0.69404`
Spec ID: `71`
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
### Battle Stance
- Node ID: `90327`
- Entry ID: `112184`
- Definition ID: `117189`
- Spell ID: `386164`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
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
- Node ID: `92537`
- Entry ID: `114643`
- Definition ID: `119649`
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
- Source gates: source `node`; type `2`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
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
### Rend
- Node ID: `109391`
- Entry ID: `135597`
- Definition ID: `140353`
- Spell ID: `772`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Wounds the target, causing $s1 Physical damage instantly and an additional $388539o1 Bleed damage over $388539d.
- Effect: Wounds the target, causing $s1 Physical damage instantly and an additional $388539o1 Bleed damage over $388539d.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90326` (type `2`), node `90344` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Intervene
- Node ID: `108676`
- Entry ID: `134217`
- Definition ID: `141828`
- Spell ID: `3411`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Run at high speed toward an ally, intercepting all melee and ranged attacks against them for $147833d while they remain within $147833A1 yds.
- Effect: Run at high speed toward an ally, intercepting all melee and ranged attacks against them for $147833d while they remain within $147833A1 yds.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `90337` (type `2`), node `90371` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Interpose
- Node ID: `108676`
- Entry ID: `134216`
- Definition ID: `138994`
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
### Two-Handed Weapon Specialization
- Node ID: `90322`
- Entry ID: `112179`
- Definition ID: `117184`
- Spell ID: `382896`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `0`
- Description: While wielding two-handed weapons your damage is increased by $s1% and damage taken from area of effect attacks is reduced by $s4%.
- Effect: While wielding two-handed weapons your damage is increased by $s1% and damage taken from area of effect attacks is reduced by $s4%.
- Point cost per purchased rank: `1` × Specialization pool (Arms, Fury, Protection) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1`
- Incoming edges: node `108685` (type `2`), node `110118` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `81375`, index `1`, operation `1`, curve `81379`, index `2`, operation `1`, curve `81378`, index `3`, operation `1`, curve `81408`
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
