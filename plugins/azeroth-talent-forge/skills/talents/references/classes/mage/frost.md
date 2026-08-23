# Frost

Reviewed build: `12.1.0.69404`
Spec ID: `64`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Ice Barrier
- Node ID: `62117`
- Entry ID: `80176`
- Definition ID: `85179`
- Spell ID: `11426`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shields you with ice, absorbing $<shield> damage$?s235297[ and increasing your armor by $s3%][] for $d.

Melee attacks against you reduce the attacker's movement speed by $205708s1%.
- Effect: Shields you with ice, absorbing $<shield> damage$?s235297[ and increasing your armor by $s3%][] for $d.

Melee attacks against you reduce the attacker's movement speed by $205708s1%.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `node`; type `2`; grants `1` rank(s)
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
### Imbued Warding
- Node ID: `94642`
- Entry ID: `117245`
- Definition ID: `122257`
- Spell ID: `431066`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Blazing Barrier also casts an Ice Barrier at $s1% effectiveness.]?c3[Ice Barrier also casts a Blazing Barrier at $s2% effectiveness.][]
- Effect: $?c2[Blazing Barrier also casts an Ice Barrier at $s1% effectiveness.]?c3[Ice Barrier also casts a Blazing Barrier at $s2% effectiveness.][]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94636` (type `2`), node `109956` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Meltdown
- Node ID: `94642`
- Entry ID: `117776`
- Definition ID: `122788`
- Spell ID: `431131`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: You melt slightly out of your Ice Block and Ice Cold, allowing you to move slowly during Ice Block and increasing your movement speed over time.

Ice Block and Ice Cold trigger a Blazing Barrier when they end.
- Effect: You melt slightly out of your Ice Block and Ice Cold, allowing you to move slowly during Ice Block and increasing your movement speed over time.

Ice Block and Ice Cold trigger a Blazing Barrier when they end.
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94636` (type `2`), node `109956` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frostfire Empowerment
- Node ID: `94641`
- Entry ID: `117244`
- Definition ID: `122256`
- Spell ID: `431176`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Frostfire spells has a $s3% chance to activate Frostfire Empowerment, causing your next Frostfire Bolt to be instant cast, deal $431177s3% increased damage, explode for $s2% of its damage to nearby enemies. Damage reduced beyond $s5 targets.$?c2[][

Damage from Frostfire Empowerment applies $s4 $Lstack:stacks; of Freezing.]
- Effect: Casting Frostfire spells has a $s3% chance to activate Frostfire Empowerment, causing your next Frostfire Bolt to be instant cast, deal $431177s3% increased damage, explode for $s2% of its damage to nearby enemies. Damage reduced beyond $s5 targets.$?c2[][

Damage from Frostfire Empowerment applies $s4 $Lstack:stacks; of Freezing.]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94636` (type `2`), node `109956` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Affinity
- Node ID: `94633`
- Entry ID: `117236`
- Definition ID: `122248`
- Spell ID: `431067`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[The cooldown of Frost spells with a base cooldown shorter than $s4 minutes is reduced by $s1%.]?c3[The cooldown of Fire spells is reduced by $s3%.][]
- Effect: $?c2[The cooldown of Frost spells with a base cooldown shorter than $s4 minutes is reduced by $s1%.]?c3[The cooldown of Fire spells is reduced by $s3%.][]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94636` (type `2`), node `109956` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flame and Frost
- Node ID: `94633`
- Entry ID: `117775`
- Definition ID: `122787`
- Spell ID: `431112`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137020[Ice Block and Ice Cold reset the cooldowns of your Fire spells.]?a137019[Cauterize resets the cooldown of your Frost spells with a base cooldown shorter than $s1 minutes when it activates.][Ice Block and Ice Cold reset the cooldowns of your Fire spells.

Cauterize resets the cooldown of your Frost spells with a base cooldown shorter than $s1 minutes when it activates.]
- Effect: $?a137020[Ice Block and Ice Cold reset the cooldowns of your Fire spells.]?a137019[Cauterize resets the cooldown of your Frost spells with a base cooldown shorter than $s1 minutes when it activates.][Ice Block and Ice Cold reset the cooldowns of your Fire spells.

Cauterize resets the cooldown of your Frost spells with a base cooldown shorter than $s1 minutes when it activates.]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94636` (type `2`), node `109956` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Duality
- Node ID: `109672`
- Entry ID: `135923`
- Definition ID: `140678`
- Spell ID: `1262843`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Casting Pyroblast has a $s2% chance to also cast a Glacial Spike, dealing $1262862s1 Frost damage][Casting Glacial Spike also casts a Pyroblast, dealing $1262863s1 Fire damage].
- Effect: $?c2[Casting Pyroblast has a $s2% chance to also cast a Glacial Spike, dealing $1262862s1 Frost damage][Casting Glacial Spike also casts a Pyroblast, dealing $1262863s1 Fire damage].
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94636` (type `2`), node `109956` (type `2`)
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
### Heat Sink
- Node ID: `94638`
- Entry ID: `117241`
- Definition ID: `122253`
- Spell ID: `1248002`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137020[Flurry]?a137019[Fire Blast][Flurry and Fire Blast] now $?a137020[deals]?a137019[deals][deal] Frostfire damage and $?a137020[its]?a137019[its][their] damage is increased by $?a137020[$s3%]?a137019[$s2%][$s2%].
- Effect: $?a137020[Flurry]?a137019[Fire Blast][Flurry and Fire Blast] now $?a137020[deals]?a137019[deals][deal] Frostfire damage and $?a137020[its]?a137019[its][their] damage is increased by $?a137020[$s3%]?a137019[$s2%][$s2%].
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94642` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thermal Conditioning
- Node ID: `94640`
- Entry ID: `117243`
- Definition ID: `122255`
- Spell ID: `431117`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Frostfire Bolt's cast time is reduced by $s1%.
- Effect: Frostfire Bolt's cast time is reduced by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94641` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Severe Temperatures
- Node ID: `94640`
- Entry ID: `134441`
- Definition ID: `139212`
- Spell ID: `431189`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Frostfire Empowerment stacks $s1 additional $Ltime:times; and it causes Frostfire Bolt to explode for an additional $s2% of its damage.
- Effect: Frostfire Empowerment stacks $s1 additional $Ltime:times; and it causes Frostfire Bolt to explode for an additional $s2% of its damage.
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94641` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dualcasting Adept
- Node ID: `94634`
- Entry ID: `117237`
- Definition ID: `122249`
- Spell ID: `1248014`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?a137020[Fire]?a137019[Frost][Frost and Fire] spells deal $?a137020[$s1]?a137019[$s2][$s1]% increased critical strike damage.

$?a137020[Shatter damage increased by $s3%.

Blizzard damage increased by $s6%.]?a137019[Pyroblast damage increased by $s4%.

Flamestrike damage increased by $s5%.][Ice Lance and Pyroblast  have their damage increased by $s3%.]
- Effect: Your $?a137020[Fire]?a137019[Frost][Frost and Fire] spells deal $?a137020[$s1]?a137019[$s2][$s1]% increased critical strike damage.

$?a137020[Shatter damage increased by $s3%.

Blizzard damage increased by $s6%.]?a137019[Pyroblast damage increased by $s4%.

Flamestrike damage increased by $s5%.][Ice Lance and Pyroblast  have their damage increased by $s3%.]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94633` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Molten Chill
- Node ID: `109671`
- Entry ID: `135922`
- Definition ID: `140677`
- Spell ID: `1262844`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Your Frostfire spells apply Ignite, dealing an additional $s1% of their damage over $1262887d][Your Frostfire spells apply Ignite at $s2% increased effectiveness].
- Effect: $?c3[Your Frostfire spells apply Ignite, dealing an additional $s1% of their damage over $1262887d][Your Frostfire spells apply Ignite at $s2% increased effectiveness].
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109672` (type `2`)
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
### Frostfire Infusion
- Node ID: `94639`
- Entry ID: `117242`
- Definition ID: `122254`
- Spell ID: `431166`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137020[Frostfire Bolt has an additional $s1% chance to grant Brain Freeze]?a137019[Frostfire Bolt's critical strike chance is increased by $s2%.][Frostfire Bolt has and additional $s1% chance to grant Brain Freeze and its critical strike chance is increased by $s2%].

The damage of your Frost spells and Fire spells are increased by $s3%.
- Effect: $?a137020[Frostfire Bolt has an additional $s1% chance to grant Brain Freeze]?a137019[Frostfire Bolt's critical strike chance is increased by $s2%.][Frostfire Bolt has and additional $s1% chance to grant Brain Freeze and its critical strike chance is increased by $s2%].

The damage of your Frost spells and Fire spells are increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94638` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flash Freezeburn
- Node ID: `94632`
- Entry ID: `117235`
- Definition ID: `122247`
- Spell ID: `431178`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137020[Glacial Spike damage increased by $s1% and it now explodes on impact, dealing $s2% of its damage to up to $s3 nearby enemies.

Additionally, Glacial Spike now grants Frostfire Empowerment][Meteor's damage is increased by $s4%.

Meteor now grants Frostfire Empowerment].
- Effect: $?a137020[Glacial Spike damage increased by $s1% and it now explodes on impact, dealing $s2% of its damage to up to $s3 nearby enemies.

Additionally, Glacial Spike now grants Frostfire Empowerment][Meteor's damage is increased by $s4%.

Meteor now grants Frostfire Empowerment].
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94640` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blast Radius
- Node ID: `94637`
- Entry ID: `117240`
- Definition ID: `122252`
- Spell ID: `1248016`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137020[Comet Storm damage increased by $s2%.

Meteor damage increased by $s1%.]?a137019[Meteor damage increased by $s3%.

Comet Storm damage increased by $s4%.][The damage of Meteor and Comet Storm is increased.]
- Effect: $?a137020[Comet Storm damage increased by $s2%.

Meteor damage increased by $s1%.]?a137019[Meteor damage increased by $s3%.

Comet Storm damage increased by $s4%.][The damage of Meteor and Comet Storm is increased.]
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94634` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Conduit
- Node ID: `109670`
- Entry ID: `135921`
- Definition ID: `140676`
- Spell ID: `1262845`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Comet Storm and Glacial Spike now apply Ignite][Meteor and Pyroblast now apply Ignite].

Your Haste is increased by $s2%.
- Effect: $?c2[Comet Storm and Glacial Spike now apply Ignite][Meteor and Pyroblast now apply Ignite].

Your Haste is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109671` (type `2`)
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
### Isothermic Core
- Node ID: `94635`
- Entry ID: `117238`
- Definition ID: `122250`
- Spell ID: `431095`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137019[Meteor now also calls down a Comet Storm, dealing ${$438609s1*7} Frost damage to nearby enemies]?a137020[Comet Storm now also calls down a Meteor, dealing $351140s1 Fire damage to nearby enemies. Damage reduced beyond 8 targets.

Damage from Meteor Shatters $1246769s5 stacks of Freezing][Meteor now also calls down a Comet Storm, dealing ${$438609s1*7} Frost damage to nearby enemies.

Comet Storm now also calls down a Meteor, dealing $351140s1 Fire damage to nearby enemies].
- Effect: $?a137019[Meteor now also calls down a Comet Storm, dealing ${$438609s1*7} Frost damage to nearby enemies]?a137020[Comet Storm now also calls down a Meteor, dealing $351140s1 Fire damage to nearby enemies. Damage reduced beyond 8 targets.

Damage from Meteor Shatters $1246769s5 stacks of Freezing][Meteor now also calls down a Comet Storm, dealing ${$438609s1*7} Frost damage to nearby enemies.

Comet Storm now also calls down a Meteor, dealing $351140s1 Fire damage to nearby enemies].
- Point cost per purchased rank: `1` × Hero pool (Frostfire) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94632` (type `2`), node `94637` (type `2`), node `94639` (type `2`), node `109670` (type `2`)
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
### Improved Ice Barrier
- Node ID: `108655`
- Entry ID: `134185`
- Definition ID: `138965`
- Spell ID: `1244069`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Ice Barrier gains an additional charge and reduces your physical damage taken by ${-$s1}%.
- Effect: Ice Barrier gains an additional charge and reduces your physical damage taken by ${-$s1}%.
- Point cost per purchased rank: `1` × Specialization pool (Arcane, Fire, Frost) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `0`; currency `2801` spend gate `20` | source `node`; type `1`
- Incoming edges: node `62091` (type `2`), node `62092` (type `2`), node `62100` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
