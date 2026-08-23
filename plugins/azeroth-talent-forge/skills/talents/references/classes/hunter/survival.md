# Survival

Reviewed build: `12.1.0.69404`
Spec ID: `255`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Black Arrow
- Node ID: `94987`
- Entry ID: `117584`
- Definition ID: `122596`
- Spell ID: `466932`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Kill Shot is replaced with Black Arrow.

$@spellicon466930 $@spellname466930
$@spelldesc466930
- Effect: Your Kill Shot is replaced with Black Arrow.

$@spellicon466930 $@spellname466930
$@spelldesc466930
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Black Arrow
- Node ID: `109961`
- Entry ID: `136446`
- Definition ID: `141219`
- Spell ID: `466930`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You attempt to finish off a wounded target, dealing $s1 Shadow damage and $468572o1 Shadow damage over $468572d. Only usable on enemies above $s3% health or below $s2% health.
- Effect: You attempt to finish off a wounded target, dealing $s1 Shadow damage and $468572o1 Shadow damage over $468572d. Only usable on enemies above $s3% health or below $s2% health.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Survival of the Fittest
- Node ID: `102422`
- Entry ID: `126488`
- Definition ID: `131314`
- Spell ID: `264735`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces all damage you and your pet take by $s1% for $d.
- Effect: Reduces all damage you and your pet take by $s1% for $d.
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
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
### Muzzle
- Node ID: `79837`
- Entry ID: `100543`
- Definition ID: `105545`
- Spell ID: `187707`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Interrupts spellcasting, preventing any spell in that school from being cast for $d.
- Effect: Interrupts spellcasting, preventing any spell in that school from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `109485` (type `2`), node `110157` (type `2`)
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
### Howl of the Pack Leader
- Node ID: `94991`
- Entry ID: `117588`
- Definition ID: `122600`
- Spell ID: `471876`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While in combat, every $471877d your next Kill Command summons the aid of a Beast.

$@spellicon471881 Wyvern
A Wyvern descends from the skies, letting out a battle cry that increases the damage of you and your pets by ${$471881s1*$s3}% for $471881d.

$@spellicon471936 Boar
A Boar charges through your target $s2 $Ltime:times;, dealing $471938s1 damage to nearby enemies and an additional $471936s1 physical damage to its primary target. Damage reduced beyond $471938s2 targets.

$@spellicon471993 Bear
A Bear leaps into the fray, rending the flesh of your enemies, dealing $471999o1 damage over $471999d to up to $471999s2 nearby enemies.
- Effect: While in combat, every $471877d your next Kill Command summons the aid of a Beast.

$@spellicon471881 Wyvern
A Wyvern descends from the skies, letting out a battle cry that increases the damage of you and your pets by ${$471881s1*$s3}% for $471881d.

$@spellicon471936 Boar
A Boar charges through your target $s2 $Ltime:times;, dealing $471938s1 damage to nearby enemies and an additional $471936s1 physical damage to its primary target. Damage reduced beyond $471938s2 targets.

$@spellicon471993 Bear
A Bear leaps into the fray, rending the flesh of your enemies, dealing $471999o1 damage over $471999d to up to $471999s2 nearby enemies.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pack Mentality
- Node ID: `94985`
- Entry ID: `117582`
- Definition ID: `122594`
- Spell ID: `472358`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Howl of the Pack Leader increases the damage of your Kill Command by $s1%.

Summoning a Beast reduces the cooldown of $?c1[Barbed Shot][Wildfire Bomb] by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec.
- Effect: Howl of the Pack Leader increases the damage of your Kill Command by $s1%.

Summoning a Beast reduces the cooldown of $?c1[Barbed Shot][Wildfire Bomb] by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dire Summons
- Node ID: `94992`
- Entry ID: `117589`
- Definition ID: `122601`
- Spell ID: `472352`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Kill Command reduces the cooldown of Howl of the Pack Leader by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec.

$?s259387[Mongoose Bite]?a137017[Raptor Strike][Cobra Shot] reduces the cooldown of Howl of the Pack Leader by $?c1[${$s3/1000}.1][${$s4/1000}.1] sec.
- Effect: Kill Command reduces the cooldown of Howl of the Pack Leader by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec.

$?s259387[Mongoose Bite]?a137017[Raptor Strike][Cobra Shot] reduces the cooldown of Howl of the Pack Leader by $?c1[${$s3/1000}.1][${$s4/1000}.1] sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Better Together
- Node ID: `94962`
- Entry ID: `117559`
- Definition ID: `122571`
- Spell ID: `472357`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage dealt by your pet$?c1[s][] is increased by $?c1[$s1][$s2]%.

$?c1[Barbed Shot damage increased by $s4%][Raptor Strike damage increased by $s3%].
- Effect: Damage dealt by your pet$?c1[s][] is increased by $?c1[$s1][$s2]%.

$?c1[Barbed Shot damage increased by $s4%][Raptor Strike damage increased by $s3%].
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slicked Shoes
- Node ID: `94979`
- Entry ID: `117576`
- Definition ID: `122588`
- Spell ID: `472719`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Disengage removes a movement impairing effect, its cooldown is reduced by ${$s1/1000} sec.
- Effect: When Disengage removes a movement impairing effect, its cooldown is reduced by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Masterful Call
- Node ID: `94979`
- Entry ID: `123781`
- Definition ID: `128619`
- Spell ID: `1268705`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The duration of Master's Call is increased by ${$s1/1000} sec and it increases the movement speed of its target by $s2%.
- Effect: The duration of Master's Call is increased by ${$s1/1000} sec and it increases the movement speed of its target by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ursine Fury
- Node ID: `94972`
- Entry ID: `117569`
- Definition ID: `122581`
- Spell ID: `472476`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Bear is summoned, it is joined by $s1 Dire $LBeast:Beasts;.
- Effect: When your Bear is summoned, it is joined by $s1 Dire $LBeast:Beasts;.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94985` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sharpened Claws
- Node ID: `94972`
- Entry ID: `128358`
- Definition ID: `133164`
- Spell ID: `472524`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The damage of your Bear's Rend Flesh is increased by $s1%.
- Effect: The damage of your Bear's Rend Flesh is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94985` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fury of the Wyvern
- Node ID: `94984`
- Entry ID: `117581`
- Definition ID: `122593`
- Spell ID: `472550`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your pet's attacks increase your Wyvern's damage bonus by $471881s1%, up to $s1%.

Casting $?c1[Kill Command][Wildfire Bomb] extends the duration of your Wyvern by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec, up to $?c1[$s4][$s5] additional sec.
- Effect: Your pet's attacks increase your Wyvern's damage bonus by $471881s1%, up to $s1%.

Casting $?c1[Kill Command][Wildfire Bomb] extends the duration of your Wyvern by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec, up to $?c1[$s4][$s5] additional sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94992` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hogstrider
- Node ID: `94988`
- Entry ID: `117585`
- Definition ID: `122597`
- Spell ID: `472639`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[When your Boar deals damage, the damage of your next Cobra Shot is increased by $472640s1%.

Each additional enemy damaged by your Boar causes Cobra Shot to strike $472640s3 additional $Ltarget:targets;, up to $472640u][Each time your Boar deals damage, the damage of your next Boomstick is increased by $472640s2%, up to ${$472640s2*$472640u}%].
- Effect: $?c1[When your Boar deals damage, the damage of your next Cobra Shot is increased by $472640s1%.

Each additional enemy damaged by your Boar causes Cobra Shot to strike $472640s3 additional $Ltarget:targets;, up to $472640u][Each time your Boar deals damage, the damage of your next Boomstick is increased by $472640s2%, up to ${$472640s2*$472640u}%].
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94962` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lethal Barbs
- Node ID: `109803`
- Entry ID: `136061`
- Definition ID: `140816`
- Spell ID: `1264781`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?c1[auto shot][auto attacks] have a very high chance to grant$?c1[s][] $1264783s1 Focus to you and your pet.

$?c1[Auto shot][Auto attack] damage increased by $?c1[$s2][$s3]%.
- Effect: Your $?c1[auto shot][auto attacks] have a very high chance to grant$?c1[s][] $1264783s1 Focus to you and your pet.

$?c1[Auto shot][Auto attack] damage increased by $?c1[$s2][$s3]%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94979` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Intimidation
- Node ID: `103989`
- Entry ID: `128412`
- Definition ID: `133218`
- Spell ID: `19577`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Commands your pet to intimidate the target stunning your target for $24394d$?a1258509[ and nearby enemies for ${$1258508d}.1 sec][].
- Effect: Commands your pet to intimidate the target stunning your target for $24394d$?a1258509[ and nearby enemies for ${$1258508d}.1 sec][].
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1`
- Incoming edges: node `102424` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### No Mercy
- Node ID: `94969`
- Entry ID: `117566`
- Definition ID: `122578`
- Spell ID: `472660`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Bleed effects deal $?c1[$s1][$s2]% increased damage.
- Effect: Your Bleed effects deal $?c1[$s1][$s2]% increased damage.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94972` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shell Cover
- Node ID: `94967`
- Entry ID: `117564`
- Definition ID: `122576`
- Spell ID: `472707`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Survival of the Fittest now summons a Turtle to aid you, further increasing its damage reduction effect by ${-$s1}%.
- Effect: Survival of the Fittest now summons a Turtle to aid you, further increasing its damage reduction effect by ${-$s1}%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94984` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hoof and Blade
- Node ID: `109804`
- Entry ID: `136062`
- Definition ID: `140817`
- Spell ID: `1264797`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Hogstrider further increases the damage of Cobra Shot by $s1% and it now strikes up to $s3 additional targets][Hogstrider further increases the damage of Boomstick by $s2%].
- Effect: $?c1[Hogstrider further increases the damage of Cobra Shot by $s1% and it now strikes up to $s3 additional targets][Hogstrider further increases the damage of Boomstick by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wyvern's Gaze
- Node ID: `109804`
- Entry ID: `136236`
- Definition ID: `141009`
- Spell ID: `1264792`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The damage bonus from your Wyvern now lasts an additional ${$s2/1000}.1 sec.
- Effect: The damage bonus from your Wyvern now lasts an additional ${$s2/1000}.1 sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sharpened Fangs
- Node ID: `109802`
- Entry ID: `136060`
- Definition ID: `140815`
- Spell ID: `1264775`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your mastery is increased by $s1%.$?c3[

Wildfire Bomb deals an additional $s2% increased damage to its primary target.][]
- Effect: Your mastery is increased by $s1%.$?c3[

Wildfire Bomb deals an additional $s2% increased damage to its primary target.][]
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109803` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stampede!
- Node ID: `94966`
- Entry ID: `117563`
- Definition ID: `122575`
- Spell ID: `472741`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?c1[Bestial Wrath][Takedown] grants Howl of the Pack Leader and causes your next Kill Command to rouse the nearby wildlife into a Stampede, charging your target and dealing ${$201594s1* $s1} Physical damage over $201430d.
- Effect: Casting $?c1[Bestial Wrath][Takedown] grants Howl of the Pack Leader and causes your next Kill Command to rouse the nearby wildlife into a Stampede, charging your target and dealing ${$201594s1* $s1} Physical damage over $201430d.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94967` (type `2`), node `94969` (type `2`), node `109802` (type `2`), node `109804` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
