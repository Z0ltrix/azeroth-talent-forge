# Sentinel

Reviewed build: `12.1.0.69404`
Hero subtree ID: `42`
Description: Sentinels draw their power from nature's forces, dealing bonus Arcane damage with their abilities and calling upon the power of the moon to rain destruction on their enemies.

## Hero talents

### Sentinel
- Node ID: `94976`
- Entry ID: `117573`
- Definition ID: `122585`
- Spell ID: `1253599`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Consuming Tip of the Spear has a $s2% chance to summon the aid of a Sentinel Owl that descends from the skies and applies Sentinel's Mark to your target][Your Eagle is replaced with a Sentinel Owl that applies an enhanced Sentinel's Mark].

$@spellicon1253601$@spellname1253601
$@spellaura1253601
- Effect: $?c3[Consuming Tip of the Spear has a $s2% chance to summon the aid of a Sentinel Owl that descends from the skies and applies Sentinel's Mark to your target][Your Eagle is replaced with a Sentinel Owl that applies an enhanced Sentinel's Mark].

$@spellicon1253601$@spellname1253601
$@spellaura1253601
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Don't Look Back
- Node ID: `94989`
- Entry ID: `117586`
- Definition ID: `122598`
- Spell ID: `450373`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming Sentinel's Mark grants you an absorb shield equal to ${$s1}.1% of your maximum health.
- Effect: Consuming Sentinel's Mark grants you an absorb shield equal to ${$s1}.1% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moon's Blessing
- Node ID: `94973`
- Entry ID: `117570`
- Definition ID: `122582`
- Spell ID: `1253825`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] has a $s1% increased chance to summon your Sentinel Owl.

When your Sentinel Owl applies Sentinel's Mark, reduce the cooldown of $?c2[Aimed Shot][Wildfire Bomb] by $?c2[${$s2/1000}.1][${$s3/1000}.1] sec.
- Effect: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] has a $s1% increased chance to summon your Sentinel Owl.

When your Sentinel Owl applies Sentinel's Mark, reduce the cooldown of $?c2[Aimed Shot][Wildfire Bomb] by $?c2[${$s2/1000}.1][${$s3/1000}.1] sec.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sanctified Armaments
- Node ID: `94981`
- Entry ID: `117578`
- Definition ID: `122590`
- Spell ID: `1253831`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: An additional $?c2[$s1][$s2]% of $?c2[Rapid Fire][Raptor Strike]'s damage is dealt as Arcane damage over $1253836d.
- Effect: An additional $?c2[$s1][$s2]% of $?c2[Rapid Fire][Raptor Strike]'s damage is dealt as Arcane damage over $1253836d.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moonlight Chakram
- Node ID: `109807`
- Entry ID: `136065`
- Definition ID: `140820`
- Spell ID: `1264902`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For $1264946d after casting $?c2[Trueshot][Takedown], $?c2[Trueshot][Takedown] is replaced with Moonlight Chakram.

$@spellicon1264949 $@spellname1264949
$@spelldesc1264949
- Effect: For $1264946d after casting $?c2[Trueshot][Takedown], $?c2[Trueshot][Takedown] is replaced with Moonlight Chakram.

$@spellicon1264949 $@spellname1264949
$@spelldesc1264949
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stargazer
- Node ID: `94958`
- Entry ID: `117555`
- Definition ID: `122567`
- Spell ID: `1253751`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] grants $1253750s1% increased critical strike damage for $1253750d. Multiple applications may overlap.
- Effect: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] grants $1253750s1% increased critical strike damage for $1253750d. Multiple applications may overlap.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94989` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Open Fire
- Node ID: `94958`
- Entry ID: `135589`
- Definition ID: `140345`
- Spell ID: `1253807`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c2[Volley damage increased by $s1%][Fire damage dealt increased by $s2%].
- Effect: $?c2[Volley damage increased by $s1%][Fire damage dealt increased by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94989` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Can't Miss, Won't Miss
- Node ID: `94990`
- Entry ID: `117587`
- Definition ID: `122599`
- Spell ID: `1253830`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Precise Shots damage bonus][Tip of the Spear damage bonus] increased by $?c2[$s1][$s2]%.

$?c2[Trueshot][Takedown] duration increased by $?c2[${$s3/1000}][${$s4/1000}] sec.
- Effect: $?c2[Precise Shots damage bonus][Tip of the Spear damage bonus] increased by $?c2[$s1][$s2]%.

$?c2[Trueshot][Takedown] duration increased by $?c2[${$s3/1000}][${$s4/1000}] sec.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94973` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Invigorating Pulse
- Node ID: `94971`
- Entry ID: `117568`
- Definition ID: `122580`
- Spell ID: `450379`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Steady Shot][Kill Command] grants an additional $s1 Focus and its damage is increased by $s4%. 

Maximum Focus increased by $s2.
- Effect: $?c2[Steady Shot][Kill Command] grants an additional $s1 Focus and its damage is increased by $s4%. 

Maximum Focus increased by $s2.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94981` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twilight Requiem
- Node ID: `110028`
- Entry ID: `136522`
- Definition ID: `141295`
- Spell ID: `1264904`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Moonlight Chakram expires, it summons an explosion of moonlight, dealing $1266096s1 Arcane damage to nearby enemies. Damage reduced beyond $s1 targets.
- Effect: When your Moonlight Chakram expires, it summons an explosion of moonlight, dealing $1266096s1 Arcane damage to nearby enemies. Damage reduced beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109807` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stalk and Strike
- Node ID: `110028`
- Entry ID: `136521`
- Definition ID: `141294`
- Spell ID: `1266069`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Throwing your Moonlight Chakram $?c2[grants you Lock and Load][reduces the cooldown of Wildfire Bomb by ${$s1/1000} sec].
- Effect: Throwing your Moonlight Chakram $?c2[grants you Lock and Load][reduces the cooldown of Wildfire Bomb by ${$s1/1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109807` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arcane Talons
- Node ID: `94970`
- Entry ID: `117567`
- Definition ID: `122579`
- Spell ID: `1253846`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Sentinel's Mark further increases the damage of $?c2[Aimed Shot][Wildfire Bomb]$?a1273128[ and Rapid Fire][] by $?c2[$s1][$s2]%
- Effect: Sentinel's Mark further increases the damage of $?c2[Aimed Shot][Wildfire Bomb]$?a1273128[ and Rapid Fire][] by $?c2[$s1][$s2]%
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94958` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lunar Calling
- Node ID: `94965`
- Entry ID: `117562`
- Definition ID: `122574`
- Spell ID: `1253852`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Feathered Frenzy further increases your chance to summon your Sentinel Owl during Trueshot by $s1%][Takedown summons your Sentinel Owl and your chance to summon your Sentinel Owl is increased by an additional $s2% during Takedown].
- Effect: $?c2[Feathered Frenzy further increases your chance to summon your Sentinel Owl during Trueshot by $s1%][Takedown summons your Sentinel Owl and your chance to summon your Sentinel Owl is increased by an additional $s2% during Takedown].
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94990` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Conditioning
- Node ID: `94980`
- Entry ID: `117577`
- Definition ID: `122589`
- Spell ID: `1253887`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your movement speed is increased by $s1%.

Aspect of the Cheetah's cooldown is reduced by ${-$s2/1000} sec.
- Effect: Your movement speed is increased by $s1%.

Aspect of the Cheetah's cooldown is reduced by ${-$s2/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94971` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Scout's Vigil
- Node ID: `94980`
- Entry ID: `123870`
- Definition ID: `128708`
- Spell ID: `1253892`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Enemy detection radius reduced by $s1 yds.
- Effect: Enemy detection radius reduced by $s1 yds.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94971` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Radiant Edge
- Node ID: `109805`
- Entry ID: `136063`
- Definition ID: `140818`
- Spell ID: `1264903`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Moonlight Chakram deals $1264949s3% increased damage each time it bounces.
- Effect: Your Moonlight Chakram deals $1264949s3% increased damage each time it bounces.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110028` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lunar Storm
- Node ID: `94978`
- Entry ID: `117575`
- Definition ID: `122587`
- Spell ID: `1253732`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Sentinel's Mark is consumed, it summons a barrage of $s1 lunar missiles, each dealing $1253733s1 Arcane damage to enemies within $s2 yds.
- Effect: When Sentinel's Mark is consumed, it summons a barrage of $s1 lunar missiles, each dealing $1253733s1 Arcane damage to enemies within $s2 yds.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94965` (type `2`), node `94970` (type `2`), node `94980` (type `2`), node `109805` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
