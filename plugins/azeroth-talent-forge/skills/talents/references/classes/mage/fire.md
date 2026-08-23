# Fire

Reviewed build: `12.1.0.69404`
Spec ID: `63`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Blazing Barrier
- Node ID: `62119`
- Entry ID: `80178`
- Definition ID: `85181`
- Spell ID: `235313`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shields you in flame, absorbing $<shield> damage$?s194315[ and reducing Physical damage taken by $s3%][] for $d.

Melee attacks against you cause the attacker to take $235314s1 Fire damage.
- Effect: Shields you in flame, absorbing $<shield> damage$?s194315[ and reducing Physical damage taken by $s3%][] for $d.

Melee attacks against you cause the attacker to take $235314s1 Fire damage.
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
### Improved Blazing Barrier
- Node ID: `108656`
- Entry ID: `134186`
- Definition ID: `138966`
- Spell ID: `321708`
- Tree ID: `658`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Blazing Barrier gains an additional charge and cauterizes your wounds, healing you for $s1% of the damage it absorbs.
- Effect: Blazing Barrier gains an additional charge and cauterizes your wounds, healing you for $s1% of the damage it absorbs.
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
