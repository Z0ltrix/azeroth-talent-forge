# Frostfire

Reviewed build: `12.1.0.69404`
Hero subtree ID: `41`
Description: Frostfire mages take the reins of seemingly incompatible elemental forces. By mastering the opposing forces, they enhance their elemental attacks and can even combine them for more power.

## Hero talents

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
