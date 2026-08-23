# Arcane

Reviewed build: `12.1.0.69404`
Spec ID: `62`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Prismatic Barrier
- Node ID: `62121`
- Entry ID: `80180`
- Definition ID: `85183`
- Spell ID: `235450`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shields you with an arcane force, absorbing $<shield> damage and reducing magic damage taken by $s3% for $d.

The duration of harmful Magic effects against you is reduced by $s4%.
- Effect: Shields you with an arcane force, absorbing $<shield> damage and reducing magic damage taken by $s3% for $d.

The duration of harmful Magic effects against you is reduced by $s4%.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `2`; grants `1` rank(s) | source `node`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frostfire Bolt
- Node ID: `94636`
- Entry ID: `117239`
- Definition ID: `122251`
- Spell ID: `431044`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Launches a bolt of frostfire at the enemy, causing $468655s1 Frostfire damage, slowing movement speed by $205708s1%, and causing an additional $468655o2 Frostfire damage over $468655d.$?a1246769[

|CFFffffffApplies $1246769s1 $lstack:stacks; of Freezing.|R][]
- Effect: Launches a bolt of frostfire at the enemy, causing $468655s1 Frostfire damage, slowing movement speed by $205708s1%, and causing an additional $468655o2 Frostfire damage over $468655d.$?a1246769[

|CFFffffffApplies $1246769s1 $lstack:stacks; of Freezing.|R][]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frostfire Bolt
- Node ID: `109956`
- Entry ID: `136441`
- Definition ID: `141214`
- Spell ID: `431044`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Launches a bolt of frostfire at the enemy, causing $468655s1 Frostfire damage, slowing movement speed by $205708s1%, and causing an additional $468655o2 Frostfire damage over $468655d.$?a1246769[

|CFFffffffApplies $1246769s1 $lstack:stacks; of Freezing.|R][]
- Effect: Launches a bolt of frostfire at the enemy, causing $468655s1 Frostfire damage, slowing movement speed by $205708s1%, and causing an additional $468655o2 Frostfire damage over $468655d.$?a1246769[

|CFFffffffApplies $1246769s1 $lstack:stacks; of Freezing.|R][]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Splintering Sorcery
- Node ID: `94664`
- Entry ID: `117267`
- Definition ID: `122279`
- Spell ID: `443739`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting Arcane Blast or Arcane Pulse][Casting Frostbolt or Flurry] conjures $?c1[an Arcane][a Frost] Splinter.
$?c1[
$@spellicon443763$@spellname443763:
$@spelldesc443763
]
[
$@spellicon443722$@spellname443722:
$@spelldesc443722
]
- Effect: $?c1[Casting Arcane Blast or Arcane Pulse][Casting Frostbolt or Flurry] conjures $?c1[an Arcane][a Frost] Splinter.
$?c1[
$@spellicon443763$@spellname443763:
$@spelldesc443763
]
[
$@spellicon443722$@spellname443722:
$@spelldesc443722
]
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Augury Abounds
- Node ID: `94662`
- Entry ID: `117265`
- Definition ID: `122277`
- Spell ID: `1280165`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Conjuring one or more $?c1[Arcane][Frost] Splinters has a $s1% chance to conjure a burst of $s2 $?c1[Arcane][Frost] $LSplinter:Splinters;.
- Effect: Conjuring one or more $?c1[Arcane][Frost] Splinters has a $s1% chance to conjure a burst of $s2 $?c1[Arcane][Frost] $LSplinter:Splinters;.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94664` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Force of Will
- Node ID: `94663`
- Entry ID: `117266`
- Definition ID: `122278`
- Spell ID: `444719`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting Arcane Barrage conjures an Arcane Splinter for every $s1 Arcane Salvo stacks consumed][Ice Lance conjures a Frost Splinter for every $s3 Freezing stacks Shattered from its primary target].
- Effect: $?c1[Casting Arcane Barrage conjures an Arcane Splinter for every $s1 Arcane Salvo stacks consumed][Ice Lance conjures a Frost Splinter for every $s3 Freezing stacks Shattered from its primary target].
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94664` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Splintering Orbs
- Node ID: `94661`
- Entry ID: `117264`
- Definition ID: `122276`
- Spell ID: `444256`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies damaged by your $?c1[Arcane Orb][Frozen Orb] conjure $?c1[$s4 Arcane][$s5 Frost] $LSplinter:Splinters;, up to $?c1[$s1][$s6].

$?c1[Arcane Orb][Frozen Orb] damage is increased by $s3%.
- Effect: Enemies damaged by your $?c1[Arcane Orb][Frozen Orb] conjure $?c1[$s4 Arcane][$s5 Frost] $LSplinter:Splinters;, up to $?c1[$s1][$s6].

$?c1[Arcane Orb][Frozen Orb] damage is increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94664` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Attuned Familiar
- Node ID: `109669`
- Entry ID: `135920`
- Definition ID: `140675`
- Spell ID: `1261106`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Your Arcane Familiar has a $s1% chance to conjure a Splinter alongside its Arcane Assault][Your Water Elemental has a $s2% chance to conjure a Splinter alongside its Waterbolt].
- Effect: $?c1[Your Arcane Familiar has a $s1% chance to conjure a Splinter alongside its Arcane Assault][Your Water Elemental has a $s2% chance to conjure a Splinter alongside its Waterbolt].
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94664` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shifting Shards
- Node ID: `109669`
- Entry ID: `135946`
- Definition ID: `140701`
- Spell ID: `444675`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Gaining $?c1[Clearcasting][Brain Freeze] conjures $s1 $?c1[Arcane][Frost] $lSplinter:Splinters;.
- Effect: Gaining $?c1[Clearcasting][Brain Freeze] conjures $s1 $?c1[Arcane][Frost] $lSplinter:Splinters;.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94664` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slippery Slinging
- Node ID: `94659`
- Entry ID: `117262`
- Definition ID: `122274`
- Spell ID: `444752`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You have $s1% increased movement speed during Alter Time$?a236457[ and Evocation][].
- Effect: You have $s1% increased movement speed during Alter Time$?a236457[ and Evocation][].
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94662` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Look Again
- Node ID: `94659`
- Entry ID: `123418`
- Definition ID: `128256`
- Spell ID: `444756`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: While in combat, Blink summons a Mirror Image at your previous location.
- Effect: While in combat, Blink summons a Mirror Image at your previous location.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94662` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Controlled Instincts
- Node ID: `94656`
- Entry ID: `117259`
- Definition ID: `122271`
- Spell ID: `444483`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[$s1%][$s4%] of the direct damage dealt by $?c1[an Arcane Splinter][a Frost Splinter] is also dealt to nearby enemies. Damage reduced beyond $s5 targets.
- Effect: $?c1[$s1%][$s4%] of the direct damage dealt by $?c1[an Arcane Splinter][a Frost Splinter] is also dealt to nearby enemies. Damage reduced beyond $s5 targets.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94663` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reactive Barrier
- Node ID: `94660`
- Entry ID: `117263`
- Definition ID: `122275`
- Spell ID: `444827`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?c1[Prismatic][Ice] Barrier can absorb up to $s1% more damage based on your missing health.

Max effectiveness when under $s1% health.
- Effect: Your $?c1[Prismatic][Ice] Barrier can absorb up to $s1% more damage based on your missing health.

Max effectiveness when under $s1% health.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94661` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Phantasmal Image
- Node ID: `94660`
- Entry ID: `123417`
- Definition ID: `128255`
- Spell ID: `444784`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your Mirror Image summons $s2 extra $Lcopy:copies; of you.
- Effect: Your Mirror Image summons $s2 extra $Lcopy:copies; of you.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94661` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Infused Splinters
- Node ID: `109668`
- Entry ID: `135919`
- Definition ID: `140674`
- Spell ID: `1261080`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Direct damage from $?c1[Arcane][Frost] Splinters have a $?c1[$s1][$s2]% chance to $?c1[grant $s3 $Lstack:stacks; Arcane Salvo][apply $s4 $Lstack:stacks; of Freezing].$?c1[

$@spellicon1242974 $@spellname1242974
$@spellaura1242974][]
- Effect: Direct damage from $?c1[Arcane][Frost] Splinters have a $?c1[$s1][$s2]% chance to $?c1[grant $s3 $Lstack:stacks; Arcane Salvo][apply $s4 $Lstack:stacks; of Freezing].$?c1[

$@spellicon1242974 $@spellname1242974
$@spellaura1242974][]
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109669` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Archmage's Wrath
- Node ID: `94658`
- Entry ID: `117261`
- Definition ID: `122273`
- Spell ID: `444968`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Arcane Surge][Ray of Frost] damage increased by $?c1[$s1][$s2]%.

Your chance to gain $?c1[Clearcasting][Brain Freeze from Frostbolt] is increased by $?c1[$s3][$s4]%.
- Effect: $?c1[Arcane Surge][Ray of Frost] damage increased by $?c1[$s1][$s2]%.

Your chance to gain $?c1[Clearcasting][Brain Freeze from Frostbolt] is increased by $?c1[$s3][$s4]%.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94659` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Signature Spell
- Node ID: `94657`
- Entry ID: `128267`
- Definition ID: `133074`
- Spell ID: `470021`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Arcane Blast and Arcane Pulse damage increased by $s3%.

Casting Touch of the Magi conjures $s1 Arcane Splinters][Frostbolt and Blizzard damage increased by $s4%.

Glacial Spike conjures $s2 additional Frost Splinters].
- Effect: $?c1[Arcane Blast and Arcane Pulse damage increased by $s3%.

Casting Touch of the Magi conjures $s1 Arcane Splinters][Frostbolt and Blizzard damage increased by $s4%.

Glacial Spike conjures $s2 additional Frost Splinters].
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94656` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spellfrost Teachings
- Node ID: `94655`
- Entry ID: `117258`
- Definition ID: `122270`
- Spell ID: `444986`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Direct damage from $?c1[Arcane][Frost] Splinters reduces the cooldown of $?c1[Arcane][Frozen] Orb by $?c1[${$s1/1000}.2][${$s2/1000}.2] sec.
- Effect: Direct damage from $?c1[Arcane][Frost] Splinters reduces the cooldown of $?c1[Arcane][Frozen] Orb by $?c1[${$s1/1000}.2][${$s2/1000}.2] sec.
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94660` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Polished Focus
- Node ID: `109667`
- Entry ID: `135918`
- Definition ID: `140673`
- Spell ID: `1261082`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting Arcane Barrage while at $s1 or more Arcane Salvo stacks refunds $s2 Arcane Salvo $Lstack:stacks;.

Arcane Barrage damage increased by $s4%.][Ice Lance Shatters $s3 additional $Lstack:stacks; of Freezing.

Shatter damage increased by $s5%.]
- Effect: $?c1[Casting Arcane Barrage while at $s1 or more Arcane Salvo stacks refunds $s2 Arcane Salvo $Lstack:stacks;.

Arcane Barrage damage increased by $s4%.][Ice Lance Shatters $s3 additional $Lstack:stacks; of Freezing.

Shatter damage increased by $s5%.]
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109668` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Splinterstorm
- Node ID: `94654`
- Entry ID: `117257`
- Definition ID: `122269`
- Spell ID: `443783`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting Arcane Surge generates $s1 Arcane Splinters][Each time Ray of Frost damages one or more enemies, it generates $s3 Frost $LSplinter:Splinters;].

$?c1[During Arcane Surge, your chance to conjure an additional Arcane Splinter is increased to $s2%][For $1247908d after casting Ray of Frost, your chance to conjure an additional Frost Splinter is increased to $s2%].
- Effect: $?c1[Casting Arcane Surge generates $s1 Arcane Splinters][Each time Ray of Frost damages one or more enemies, it generates $s3 Frost $LSplinter:Splinters;].

$?c1[During Arcane Surge, your chance to conjure an additional Arcane Splinter is increased to $s2%][For $1247908d after casting Ray of Frost, your chance to conjure an additional Frost Splinter is increased to $s2%].
- Point cost per purchased rank: `1` × Hero pool (Spellslinger) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94655` (type `2`), node `94657` (type `2`), node `94658` (type `2`), node `109667` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Improved Prismatic Barrier
- Node ID: `108664`
- Entry ID: `134194`
- Definition ID: `138974`
- Spell ID: `321745`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Prismatic Barrier gains an additional charge and further reduces magic damage taken by $s1%.
- Effect: Prismatic Barrier gains an additional charge and further reduces magic damage taken by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Arcane, Fire, Frost) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `0`; currency `2801` spend gate `20` | source `node`; type `1`
- Incoming edges: node `62091` (type `2`), node `62092` (type `2`), node `62100` (type `2`)
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
