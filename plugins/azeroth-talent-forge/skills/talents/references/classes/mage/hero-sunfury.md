# Sunfury

Reviewed build: `12.1.0.69404`
Hero subtree ID: `39`
Description: By embracing arcane flames, Sunfury mages enhance their most devastating incantations, even calling on the aid of a spellfire phoenix.

## Hero talents

### Spellfire Spheres
- Node ID: `94647`
- Entry ID: `117250`
- Definition ID: `122262`
- Spell ID: `448601`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting a damaging spell][Consuming Hot Streak] has a $?c1[$s1][$s2]% chance to conjure a Spellfire Sphere.

While you're out of combat, you will slowly conjure Spellfire Spheres over time.

$@spellicon448604 $@spellname448604
$@spelldesc448604
- Effect: $?c1[Casting a damaging spell][Consuming Hot Streak] has a $?c1[$s1][$s2]% chance to conjure a Spellfire Sphere.

While you're out of combat, you will slowly conjure Spellfire Spheres over time.

$@spellicon448604 $@spellname448604
$@spelldesc448604
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mana Cascade
- Node ID: `94653`
- Entry ID: `117256`
- Definition ID: `122268`
- Spell ID: `449293`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting Arcane Blast, Arcane Pulse, Arcane Barrage, or Prismatic Bolt][Consuming Hot Streak] grants you $?c1[${$449322s2/10}.1][${$449314s2/10}.1]% Haste for $449322d. Multiple applications may overlap.
- Effect: $?c1[Casting Arcane Blast, Arcane Pulse, Arcane Barrage, or Prismatic Bolt][Consuming Hot Streak] grants you $?c1[${$449322s2/10}.1][${$449314s2/10}.1]% Haste for $449322d. Multiple applications may overlap.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94647` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Invocation: Arcane Phoenix
- Node ID: `94652`
- Entry ID: `117255`
- Definition ID: `122267`
- Spell ID: `448658`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you cast $?c1[Arcane Surge][Combustion], summon an Arcane Phoenix to aid you in battle.

$@spellicon448659  $@spellname448659
Your Arcane Phoenix aids you for the duration of your $?c1[Arcane Surge][Combustion], casting random Arcane and Fire spells.
- Effect: When you cast $?c1[Arcane Surge][Combustion], summon an Arcane Phoenix to aid you in battle.

$@spellicon448659  $@spellname448659
Your Arcane Phoenix aids you for the duration of your $?c1[Arcane Surge][Combustion], casting random Arcane and Fire spells.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94647` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Burden of Power
- Node ID: `94644`
- Entry ID: `117247`
- Definition ID: `122259`
- Spell ID: `451035`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Arcane Blast damage increased by $s3%.

Arcane Pulse damage increased by $s4%][Pyroblast damage increased by $s1%.

Flamestrike damage increased by $s2%].
- Effect: $?c1[Arcane Blast damage increased by $s3%.

Arcane Pulse damage increased by $s4%][Pyroblast damage increased by $s1%.

Flamestrike damage increased by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94647` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Glorious Incandescence
- Node ID: `109675`
- Entry ID: `135926`
- Definition ID: `140681`
- Spell ID: `449394`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Generating a Spellfire Sphere causes your next cast of Fire Blast to call down a storm of $s1 Meteorites on its target.][Arcane Barrage summons $s6 $LMeteorite:Meteorites; for every $s4 Arcane Salvo stacks consumed.]

$@spellicon449559 $@spellname449559
$@spelldesc449559
- Effect: $?c2[Generating a Spellfire Sphere causes your next cast of Fire Blast to call down a storm of $s1 Meteorites on its target.][Arcane Barrage summons $s6 $LMeteorite:Meteorites; for every $s4 Arcane Salvo stacks consumed.]

$@spellicon449559 $@spellname449559
$@spelldesc449559
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94647` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Merely a Setback
- Node ID: `94649`
- Entry ID: `117252`
- Definition ID: `122264`
- Spell ID: `449330`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The bonuses provided by your Barrier spells persist at $s3% effectiveness for an additional $?c1[$449336d][$1246023d] after your Barrier is removed.$?c1[][

Additionally, Cauterize no longer deals damage to you.]
- Effect: The bonuses provided by your Barrier spells persist at $s3% effectiveness for an additional $?c1[$449336d][$1246023d] after your Barrier is removed.$?c1[][

Additionally, Cauterize no longer deals damage to you.]
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94653` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Time Twist
- Node ID: `94649`
- Entry ID: `135598`
- Definition ID: `140354`
- Spell ID: `1255166`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The cooldown of Alter Time is reduced by ${-$s1/1000} sec.
- Effect: The cooldown of Alter Time is reduced by ${-$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94653` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Codex of the Sunstriders
- Node ID: `94645`
- Entry ID: `117248`
- Definition ID: `122260`
- Spell ID: `449382`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Arcane Phoenix is summoned, it consumes all your Spellfire Spheres.

Each Sphere consumed increases your spell damage during $?c1[Arcane Surge][Combustion] by $?c1[$s1][$s2]% and causes your Arcane Phoenix to cast an exceptional Arcane or Fire spell over its duration.
- Effect: When your Arcane Phoenix is summoned, it consumes all your Spellfire Spheres.

Each Sphere consumed increases your spell damage during $?c1[Arcane Surge][Combustion] by $?c1[$s1][$s2]% and causes your Arcane Phoenix to cast an exceptional Arcane or Fire spell over its duration.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94652` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lessons in Debilitation
- Node ID: `94651`
- Entry ID: `117254`
- Definition ID: `122266`
- Spell ID: `449627`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Arcane Phoenix has picked up a few tricks, and will Spellsteal when it is summoned and when it expires.
- Effect: Your Arcane Phoenix has picked up a few tricks, and will Spellsteal when it is summoned and when it expires.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94644` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Explosive Potential
- Node ID: `94651`
- Entry ID: `134249`
- Definition ID: `139025`
- Spell ID: `1246030`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: After casting $?c1[Arcane Surge][Combustion], your next $?s212653[Shimmer][Blink] will cause a Blast Wave at your previous location, dealing $157981s1 Fire damage, knocking enemies back $s1 yds, and slowing them by $157981s2% for $157981d.
- Effect: After casting $?c1[Arcane Surge][Combustion], your next $?s212653[Shimmer][Blink] will cause a Blast Wave at your previous location, dealing $157981s1 Fire damage, knocking enemies back $s1 yds, and slowing them by $157981s2% for $157981d.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94644` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pyrocosm
- Node ID: `109674`
- Entry ID: `135925`
- Definition ID: `140680`
- Spell ID: `1260673`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Each wave of Arcane Missiles][Damage from Fireball] has a $?c1[$s1][$s2]% chance to summon a Meteorite.

When a Meteorite lands, $?c1[you have a $s5% chance to gain Clearcasting][the cooldown of Fire Blast is reduced by ${$s4/1000}.1 sec].
- Effect: $?c1[Each wave of Arcane Missiles][Damage from Fireball] has a $?c1[$s1][$s2]% chance to summon a Meteorite.

When a Meteorite lands, $?c1[you have a $s5% chance to gain Clearcasting][the cooldown of Fire Blast is reduced by ${$s4/1000}.1 sec].
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109675` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Savor the Moment
- Node ID: `94650`
- Entry ID: `117253`
- Definition ID: `122265`
- Spell ID: `449412`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you cast $?c1[Arcane Surge][Combustion], its duration is extended by ${$s1/1000}.1 sec for each Spellfire Sphere you have, up to ${$s2/1000}.1 sec.
- Effect: When you cast $?c1[Arcane Surge][Combustion], its duration is extended by ${$s1/1000}.1 sec for each Spellfire Sphere you have, up to ${$s2/1000}.1 sec.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94649` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sunfury Execution
- Node ID: `94650`
- Entry ID: `123867`
- Definition ID: `128705`
- Spell ID: `449349`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c2[Pyroclasm's damage bonus is increased by $s1% and Meteor grants Pyroclasm if talented.][Arcane Barrage deals $s2% increased damage to enemies affected by your Touch of the Magi.]
- Effect: $?c2[Pyroclasm's damage bonus is increased by $s1% and Meteor grants Pyroclasm if talented.][Arcane Barrage deals $s2% increased damage to enemies affected by your Touch of the Magi.]
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94649` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ashes of Inspiration
- Node ID: `94643`
- Entry ID: `117246`
- Definition ID: `122258`
- Spell ID: `1260272`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each time your Phoenix casts a spell, gain $s1 stack of Mana Cascade.

Exceptional spells grant $s2 additional $Lstack:stacks;.
- Effect: Each time your Phoenix casts a spell, gain $s1 stack of Mana Cascade.

Exceptional spells grant $s2 additional $Lstack:stacks;.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94645` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rondurmancy
- Node ID: `94648`
- Entry ID: `117251`
- Definition ID: `122263`
- Spell ID: `449596`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your chance to generate a Spellfire Sphere is increased by $?c1[$s1][$s2]%.

Spellfire Spheres grant an additional $s3% spell damage.
- Effect: Your chance to generate a Spellfire Sphere is increased by $?c1[$s1][$s2]%.

Spellfire Spheres grant an additional $s3% spell damage.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94651` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spellfire Salvo
- Node ID: `109673`
- Entry ID: `135924`
- Definition ID: `140679`
- Spell ID: `1260616`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Arcane Salvo can stack $s1 additional times][Fire Blast cooldown reduced by ${-$s2/1000}.1 sec].

Meteorite damage increased by $s3%.
- Effect: $?c1[Arcane Salvo can stack $s1 additional times][Fire Blast cooldown reduced by ${-$s2/1000}.1 sec].

Meteorite damage increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109674` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Memory of Al'ar
- Node ID: `94646`
- Entry ID: `117249`
- Definition ID: `122261`
- Spell ID: `449619`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Arcane Phoenix expires it empowers you, granting $?c1[Arcane Soul][Hyperthermia] for $?c1[${$s1/1000}.1][${$s2/1000}.1] sec.

$?c1[$@spellicon451038$@spellname451038:
$@spelldesc451038][$@spellicon383874 $@spellname383874:
$@spellaura383874]
- Effect: When your Arcane Phoenix expires it empowers you, granting $?c1[Arcane Soul][Hyperthermia] for $?c1[${$s1/1000}.1][${$s2/1000}.1] sec.

$?c1[$@spellicon451038$@spellname451038:
$@spelldesc451038][$@spellicon383874 $@spellname383874:
$@spellaura383874]
- Point cost per purchased rank: `1` × Hero pool (Sunfury) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94643` (type `2`), node `94648` (type `2`), node `94650` (type `2`), node `109673` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
