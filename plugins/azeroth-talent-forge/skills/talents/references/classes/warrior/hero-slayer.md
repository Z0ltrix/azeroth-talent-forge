# Slayer

Reviewed build: `12.1.0.69404`
Hero subtree ID: `60`
Description: A vicious Warrior who sets their sights on a target and pursues it relentlessly, overwhelming their foes with an onslaught of steel and might.

## Hero talents

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
