# Spellslinger

Reviewed build: `12.1.0.69404`
Hero subtree ID: `40`
Description: Mastering the inherently unstable nature of magic allows Spellslingers to splinter their magic, creating powerful and volatile new effects.

## Hero talents

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
