# Mistweaver

Reviewed build: `12.1.0.69404`
Spec ID: `270`
Role: `1`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Flurry Strikes
- Node ID: `101248`
- Entry ID: `125069`
- Definition ID: `129901`
- Spell ID: `450615`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto attacks have a chance to generate $s1-$s2 Flurry Charges. When you cast $?c3[Fists of Fury][Keg Smash], unleash all Flurry Charges, dealing $450617s1 Physical damage per charge.
- Effect: Your auto attacks have a chance to generate $s1-$s2 Flurry Charges. When you cast $?c3[Fists of Fury][Keg Smash], unleash all Flurry Charges, dealing $450617s1 Physical damage per charge.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Invoke Xuen, the White Tiger
- Node ID: `101243`
- Entry ID: `125062`
- Definition ID: `129894`
- Spell ID: `123904`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summons an effigy of Xuen, the White Tiger for $d. Xuen attacks your primary target, and strikes 3 enemies within $123996A1 yards every $123999t1 sec with Tiger Lightning for $123996s1 Nature damage.$?s323999[

Every $323999s1 sec, Xuen strikes your enemies with Empowered Tiger Lightning dealing $323999s2% of the damage you have dealt to those targets in the last $323999s1 sec.][]
- Effect: Summons an effigy of Xuen, the White Tiger for $d. Xuen attacks your primary target, and strikes 3 enemies within $123996A1 yards every $123999t1 sec with Tiger Lightning for $123996s1 Nature damage.$?s323999[

Every $323999s1 sec, Xuen strikes your enemies with Empowered Tiger Lightning dealing $323999s2% of the damage you have dealt to those targets in the last $323999s1 sec.][]
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Celestial Conduit
- Node ID: `110067`
- Entry ID: `136562`
- Definition ID: `141335`
- Spell ID: `443028`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[The August Celestials empower you, causing you to radiate ${$443039s1*$s7} healing onto up to $s3 injured allies and ${$443038s1*$s7} Nature damage onto enemies within $s6 yds over $d, reduced beyond $s3 targets.][The August Celestials empower you, causing you to radiate ${$443038s1*$s7} Nature damage onto enemies and ${$443039s1*$s7} healing onto up to $s3 injured allies within $443038A2 yds over $d, reduced beyond $s3 targets.]

You may move while channeling, but casting other healing or damaging spells cancels this effect.
- Effect: $?c2[The August Celestials empower you, causing you to radiate ${$443039s1*$s7} healing onto up to $s3 injured allies and ${$443038s1*$s7} Nature damage onto enemies within $s6 yds over $d, reduced beyond $s3 targets.][The August Celestials empower you, causing you to radiate ${$443038s1*$s7} Nature damage onto enemies and ${$443039s1*$s7} healing onto up to $s3 injured allies within $443038A2 yds over $d, reduced beyond $s3 targets.]

You may move while channeling, but casting other healing or damaging spells cancels this effect.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Paralysis
- Node ID: `101142`
- Entry ID: `124932`
- Definition ID: `129770`
- Spell ID: `115078`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Incapacitates the target for $d. Limit 1. Damage may cancel the effect.
- Effect: Incapacitates the target for $d. Limit 1. Damage may cancel the effect.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rising Sun Kick
- Node ID: `101186`
- Entry ID: `124985`
- Definition ID: `129823`
- Spell ID: `107428`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Kick upwards, dealing $?s137025[${$185099s1*$<CAP>/$AP}][$185099s1] Physical damage$?s128595[, and reducing the effectiveness of healing on the target for $115804d][].$?a388847[

Applies Renewing Mist for $388847s1 seconds to an ally within $388847r yds][]
- Effect: Kick upwards, dealing $?s137025[${$185099s1*$<CAP>/$AP}][$185099s1] Physical damage$?s128595[, and reducing the effectiveness of healing on the target for $115804d][].$?a388847[

Applies Renewing Mist for $388847s1 seconds to an ally within $388847r yds][]
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s) | source `node`; type `1` | source `node`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Temple Training
- Node ID: `101236`
- Entry ID: `125054`
- Definition ID: `129886`
- Spell ID: `442743`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[The healing of Enveloping Mist, Vivify, and Sheilun's Gift is increased by $s1%.]?c3[Fists of Fury and Spinning Crane Kick deal $s2% more damage.][]
- Effect: $?c2[The healing of Enveloping Mist, Vivify, and Sheilun's Gift is increased by $s1%.]?c3[Fists of Fury and Spinning Crane Kick deal $s2% more damage.][]
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101243` (type `2`), node `110067` (type `2`), node `110067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Xuen's Guidance
- Node ID: `101236`
- Entry ID: `125053`
- Definition ID: `129885`
- Spell ID: `442687`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Teachings of the Monastery has a $s1% chance to refund a charge when consumed. 

The damage of Tiger Palm is increased by $s2%.
- Effect: Teachings of the Monastery has a $s1% chance to refund a charge when consumed. 

The damage of Tiger Palm is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101243` (type `2`), node `110067` (type `2`), node `110067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Courage of the White Tiger
- Node ID: `101242`
- Entry ID: `125061`
- Definition ID: `129893`
- Spell ID: `443087`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Tiger Palm, Vivify, and Sheilun's Gift have a chance to cause Xuen to claw a nearby enemy for $457917s1 Physical damage, healing a nearby ally for $s2% of the damage done.]?c3[Tiger Palm has a chance to cause Xuen to claw your target for $457917s1 Physical damage, healing a nearby ally for $s2% of the damage done.][Xuen claws your target for $457917s1 Physical damage, healing a nearby ally for $s2% of the damage done.]

$?c2[Invoke Yu'lon, the Jade Serpent or Invoke Chi-Ji, the Red Crane]?c3[Invoke Xuen, the White Tiger][Invoking a celestial] guarantees your next cast activates this effect.
- Effect: $?c2[Tiger Palm, Vivify, and Sheilun's Gift have a chance to cause Xuen to claw a nearby enemy for $457917s1 Physical damage, healing a nearby ally for $s2% of the damage done.]?c3[Tiger Palm has a chance to cause Xuen to claw your target for $457917s1 Physical damage, healing a nearby ally for $s2% of the damage done.][Xuen claws your target for $457917s1 Physical damage, healing a nearby ally for $s2% of the damage done.]

$?c2[Invoke Yu'lon, the Jade Serpent or Invoke Chi-Ji, the Red Crane]?c3[Invoke Xuen, the White Tiger][Invoking a celestial] guarantees your next cast activates this effect.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101243` (type `2`), node `110067` (type `2`), node `110067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Restore Balance
- Node ID: `101233`
- Entry ID: `125049`
- Definition ID: `129881`
- Spell ID: `442719`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Healing increased by $322118s8% while Chi-Ji, the Red Crane or Yu'lon, the Jade Serpent is active.]?c3[Damage increased by $123904s4% while Xuen, the White Tiger is active.][]
- Effect: $?c2[Healing increased by $322118s8% while Chi-Ji, the Red Crane or Yu'lon, the Jade Serpent is active.]?c3[Damage increased by $123904s4% while Xuen, the White Tiger is active.][]
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `110067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Yu'lon's Knowledge
- Node ID: `101233`
- Entry ID: `125048`
- Definition ID: `129880`
- Spell ID: `443625`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Rising Sun Kick damage increased by $s1%.
- Effect: Rising Sun Kick damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `110067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Heart of the Jade Serpent
- Node ID: `109701`
- Entry ID: `135959`
- Definition ID: `140714`
- Spell ID: `443294`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Thunder Focus Tea calls]?c3[Strike of the Windlord and Whirling Dragon Punch call][] upon Yu'lon to increase the cooldown recovery rate of $?c2[Renewing Mist, Rising Sun Kick, Life Cocoon, and Thunder Focus Tea]?c3[Fists of Fury, Strike of the Windlord, Rising Sun Kick, and Whirling Dragon Punch][] by $443421s2% for $?c2[${$s1/1000} sec]?c3[$443421d][].$?c3[ 

The channel time of Fists of Fury is reduced by $443421s5% while Yu'lon is active.][]
- Effect: $?c2[Thunder Focus Tea calls]?c3[Strike of the Windlord and Whirling Dragon Punch call][] upon Yu'lon to increase the cooldown recovery rate of $?c2[Renewing Mist, Rising Sun Kick, Life Cocoon, and Thunder Focus Tea]?c3[Fists of Fury, Strike of the Windlord, Rising Sun Kick, and Whirling Dragon Punch][] by $443421s2% for $?c2[${$s1/1000} sec]?c3[$443421d][].$?c3[ 

The channel time of Fists of Fury is reduced by $443421s5% while Yu'lon is active.][]
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101243` (type `2`), node `110067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fast Feet
- Node ID: `101185`
- Entry ID: `124984`
- Definition ID: `129822`
- Spell ID: `388809`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Rising Sun Kick deals $s1% increased damage. Spinning Crane Kick deals $s2% additional damage.
- Effect: Rising Sun Kick deals $s1% increased damage. Spinning Crane Kick deals $s2% additional damage.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `101186` (type `2`), node `109827` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chi-Ji's Swiftness
- Node ID: `101237`
- Entry ID: `125055`
- Definition ID: `129887`
- Spell ID: `443566`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your movement speed is increased by $s1% during Celestial Conduit and by $443569s1% for $443569d after being assisted by any Celestial.
- Effect: Your movement speed is increased by $s1% during Celestial Conduit and by $443569s1% for $443569d after being assisted by any Celestial.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101236` (type `2`), node `101236` (type `2`), node `101236` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Strength of the Black Ox
- Node ID: `110211`
- Entry ID: `136747`
- Definition ID: `141519`
- Spell ID: `443110`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[After Xuen assists you, your next Enveloping Mist's cast time is reduced by $443112s1% and causes Niuzao to grant an absorb shield to $443113s3 nearby allies for $443113s1.]?c3[After Xuen assists you, your next Blackout Kick refunds $s3 stacks of Teachings of the Monastery and causes Niuzao to stomp at your target's location, dealing $443127s1 damage to nearby enemies, reduced beyond $s2 targets.][]
- Effect: $?c2[After Xuen assists you, your next Enveloping Mist's cast time is reduced by $443112s1% and causes Niuzao to grant an absorb shield to $443113s3 nearby allies for $443113s1.]?c3[After Xuen assists you, your next Blackout Kick refunds $s3 stacks of Teachings of the Monastery and causes Niuzao to stomp at your target's location, dealing $443127s1 damage to nearby enemies, reduced beyond $s2 targets.][]
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101242` (type `2`), node `101242` (type `2`), node `101242` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Path of the Falling Star
- Node ID: `101234`
- Entry ID: `125050`
- Definition ID: `129882`
- Spell ID: `1273154`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Celestial Conduit's healing and damage is increased by $s1% when striking a single target.

Each addtional target reduces this bonus by $s2%.
- Effect: Celestial Conduit's healing and damage is increased by $s1% when striking a single target.

Each addtional target reduces this bonus by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101233` (type `2`), node `110221` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Yu'lon's Avatar
- Node ID: `110218`
- Entry ID: `136754`
- Definition ID: `141526`
- Spell ID: `1262667`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Heart of the Jade Serpent additionally triggers for ${$s1/1000} sec at $s2% effectiveness after you cast Zenith][Vivify and Sheilun's Gift have a chance to trigger Heart of the Jade Serpent for ${$s1/1000} sec at $s2% effectiveness].
- Effect: $?c3[Heart of the Jade Serpent additionally triggers for ${$s1/1000} sec at $s2% effectiveness after you cast Zenith][Vivify and Sheilun's Gift have a chance to trigger Heart of the Jade Serpent for ${$s1/1000} sec at $s2% effectiveness].
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109701` (type `2`), node `109701` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Detox
- Node ID: `101089`
- Entry ID: `124866`
- Definition ID: `129704`
- Spell ID: `388874`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Detox additionally removes all Poison and Disease effects.
- Effect: Detox additionally removes all Poison and Disease effects.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101149` (type `2`), node `101185` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Niuzao's Protection
- Node ID: `101238`
- Entry ID: `125057`
- Definition ID: `129889`
- Spell ID: `442747`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fortifying Brew grants you an absorb shield for $442749s2% of your maximum health.
- Effect: Fortifying Brew grants you an absorb shield for $442749s2% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101237` (type `2`), node `101237` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Jade Sanctuary
- Node ID: `101238`
- Entry ID: `125056`
- Definition ID: `129888`
- Spell ID: `443059`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: You heal for $s2% of your maximum health instantly when you activate Celestial Conduit and receive $s1% less damage for its duration. 

This effect lingers for an additional $448508d after Celestial Conduit ends.
- Effect: You heal for $s2% of your maximum health instantly when you activate Celestial Conduit and receive $s1% less damage for its duration. 

This effect lingers for an additional $448508d after Celestial Conduit ends.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101237` (type `2`), node `101237` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stampede of the Ancients
- Node ID: `101240`
- Entry ID: `125059`
- Definition ID: `129891`
- Spell ID: `1262756`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Strength of the Black Ox's effect is $?c3[$s1][$s2]% more effective on your primary target.
- Effect: Strength of the Black Ox's effect is $?c3[$s1][$s2]% more effective on your primary target.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `node`; type `1`
- Incoming edges: node `110211` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Inner Compass
- Node ID: `101235`
- Entry ID: `125052`
- Definition ID: `129884`
- Spell ID: `443571`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You switch between alignments every $t1 sec, increasing a corresponding secondary stat by $443572s1%.

|cFFFFFFFFCrane Stance|r:
Haste

|cFFFFFFFFTiger Stance|r:
Critical Strike

|cFFFFFFFFOx Stance|r:
Versatility

|cFFFFFFFFSerpent Stance|r: 
Mastery
- Effect: You switch between alignments every $t1 sec, increasing a corresponding secondary stat by $443572s1%.

|cFFFFFFFFCrane Stance|r:
Haste

|cFFFFFFFFTiger Stance|r:
Critical Strike

|cFFFFFFFFOx Stance|r:
Versatility

|cFFFFFFFFSerpent Stance|r: 
Mastery
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101234` (type `2`), node `101234` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `101235`
- Entry ID: `125051`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101234` (type `2`), node `101234` (type `2`)
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Flowing Wisdom
- Node ID: `109700`
- Entry ID: `135958`
- Definition ID: `140713`
- Spell ID: `1262672`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heart of the Jade Serpent increases your haste by $443421s8% while active.
- Effect: Heart of the Jade Serpent increases your haste by $443421s8% while active.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110218` (type `2`), node `110218` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vivacious Vivification
- Node ID: `110026`
- Entry ID: `136519`
- Definition ID: `141292`
- Spell ID: `388812`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After casting $?a137023[Keg Smash][Rising Sun Kick], your next $?s399491[Sheilun's Gift][Vivify] becomes instant cast.$?c1[

This effect also reduces the energy cost of Vivify by $392883s3%.]?c3[

This effect also reduces the energy cost of Vivify by $392883s3%.][]
- Effect: After casting $?a137023[Keg Smash][Rising Sun Kick], your next $?s399491[Sheilun's Gift][Vivify] becomes instant cast.$?c1[

This effect also reduces the energy cost of Vivify by $392883s3%.]?c3[

This effect also reduces the energy cost of Vivify by $392883s3%.][]
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101144` (type `2`), node `101146` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Serene Surge
- Node ID: `110026`
- Entry ID: `136516`
- Definition ID: `141289`
- Spell ID: `1266734`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: After casting Enveloping Mist, your next $?s399491[Sheilun's Gift][Vivify] becomes instant cast.
- Effect: After casting Enveloping Mist, your next $?s399491[Sheilun's Gift][Vivify] becomes instant cast.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101144` (type `2`), node `101146` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chi Warding
- Node ID: `110097`
- Entry ID: `136598`
- Definition ID: `141371`
- Spell ID: `1277444`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You heal for $s1% of all magical damage taken.
- Effect: You heal for $s1% of all magical damage taken.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101089` (type `2`), node `101148` (type `2`), node `101153` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unity Within
- Node ID: `101239`
- Entry ID: `125058`
- Definition ID: `129890`
- Spell ID: `443589`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Celestial Conduit can be recast once during its duration to call upon all of the August Celestials to assist you at $s1% effectiveness.

Unity Within is automatically cast when Celestial Conduit ends if not used before expiration.
- Effect: Celestial Conduit can be recast once during its duration to call upon all of the August Celestials to assist you at $s1% effectiveness.

Unity Within is automatically cast when Celestial Conduit ends if not used before expiration.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101235` (type `2`), node `101235` (type `2`), node `101238` (type `2`), node `101238` (type `2`), node `101238` (type `2`), node `101240` (type `2`), node `109700` (type `2`), node `109700` (type `2`), node `110220` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chi Wave
- Node ID: `102432`
- Entry ID: `126500`
- Definition ID: `131326`
- Spell ID: `450391`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $t1 sec, your next $?a137023[Keg Smash][Rising Sun Kick] or $?s399491[Sheilun's Gift][Vivify] releases a wave of Chi energy that flows through friends and foes, dealing $132467s1 Nature damage or $132463s1 healing. Bounces up to $115098s1 times to targets within $132466a2 yards.
- Effect: Every $t1 sec, your next $?a137023[Keg Smash][Rising Sun Kick] or $?s399491[Sheilun's Gift][Vivify] releases a wave of Chi energy that flows through friends and foes, dealing $132467s1 Nature damage or $132463s1 healing. Bounces up to $115098s1 times to targets within $132466a2 yards.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `4`; currency `3623` spend gate `0` | source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1` | source `node`; type `4`; currency `3623` spend gate `0`
- Incoming edges: node `101145` (type `2`), node `101160` (type `2`), node `110024` (type `2`), node `110026` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aspect of Harmony
- Node ID: `101223`
- Entry ID: `125033`
- Definition ID: `129869`
- Spell ID: `450508`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Store vitality from $?a137023[$s1%][$s2%] of your damage dealt and $?a137023[$s3%][$s4%] of your $?a137023[effective ][]healing.$?a137024[ Vitality stored from overhealing is reduced.][]

For $450711d after casting $?a137023[Celestial Brew or Celestial Infusion][Thunder Focus Tea] your spells and abilities draw upon the stored vitality to deal $s6% additional $?a137023[damage over $450763d][healing over $450769d].
- Effect: Store vitality from $?a137023[$s1%][$s2%] of your damage dealt and $?a137023[$s3%][$s4%] of your $?a137023[effective ][]healing.$?a137024[ Vitality stored from overhealing is reduced.][]

For $450711d after casting $?a137023[Celestial Brew or Celestial Infusion][Thunder Focus Tea] your spells and abilities draw upon the stored vitality to deal $s6% additional $?a137023[damage over $450763d][healing over $450769d].
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `3625` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Manifestation
- Node ID: `101222`
- Entry ID: `125032`
- Definition ID: `129868`
- Spell ID: `450875`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Chi Burst and Chi Wave deal][Chi Wave deals] $s1% increased damage and healing.
- Effect: $?c1[Chi Burst and Chi Wave deal][Chi Wave deals] $s1% increased damage and healing.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `3623` spend gate `0` | source `node`; type `4`; currency `3623` spend gate `0`
- Incoming edges: node `101223` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Purified Spirit
- Node ID: `101224`
- Entry ID: `125035`
- Definition ID: `129871`
- Spell ID: `450867`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Aspect of Harmony ends, any remaining vitality is expelled as $?a137023[damage over $450820d][healing over $450805d], split among nearby targets.
- Effect: When Aspect of Harmony ends, any remaining vitality is expelled as $?a137023[damage over $450820d][healing over $450805d], split among nearby targets.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101223` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Harmonic Gambit
- Node ID: `101224`
- Entry ID: `125034`
- Definition ID: `129870`
- Spell ID: `450870`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: During Aspect of Harmony, $?a137023[Expel Harm and Vivify withdraw vitality to heal for an additional $s1% over $450769d][Rising Sun Kick, Blackout Kick, and Tiger Palm also withdraw vitality to damage enemies for an additional $s2% over $450763d].
- Effect: During Aspect of Harmony, $?a137023[Expel Harm and Vivify withdraw vitality to heal for an additional $s1% over $450769d][Rising Sun Kick, Blackout Kick, and Tiger Palm also withdraw vitality to damage enemies for an additional $s2% over $450763d].
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101223` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Balanced Stratagem
- Node ID: `101230`
- Entry ID: `125043`
- Definition ID: `129879`
- Spell ID: `450889`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting a Physical spell or ability increases the damage and healing of your next Fire or Nature spell or ability by $451508s1%, and vice versa. Stacks up to $451508U.
- Effect: Casting a Physical spell or ability increases the damage and healing of your next Fire or Nature spell or ability by $451508s1%, and vice versa. Stacks up to $451508U.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101223` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Harmonic Surge
- Node ID: `109694`
- Entry ID: `135952`
- Definition ID: `140707`
- Spell ID: `1270958`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?s322507[Celestial Brew]?s1241059[Celestial Infusion][Thunder Focus Tea] grants $?c1[$s5][$s6] $Lcharge:charges; of Potential Energy. Your next cast of Tiger Palm or Vivify consumes all charges of Potential Energy to cause a Harmonic Surge.

$@spellicon1271011$@spellname1271011:
$@spelldesc1271011
- Effect: Casting $?s322507[Celestial Brew]?s1241059[Celestial Infusion][Thunder Focus Tea] grants $?c1[$s5][$s6] $Lcharge:charges; of Potential Energy. Your next cast of Tiger Palm or Vivify consumes all charges of Potential Energy to cause a Harmonic Surge.

$@spellicon1271011$@spellname1271011:
$@spelldesc1271011
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101223` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mist Caller
- Node ID: `110019`
- Entry ID: `136510`
- Definition ID: `141283`
- Spell ID: `1266811`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vivify and Sheilun's Gift trigger a Gust of Mist on yourself.
- Effect: Vivify and Sheilun's Gift trigger a Gust of Mist on yourself.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `101158` (type `2`), node `101166` (type `2`), node `102432` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dance of the Wind
- Node ID: `101139`
- Entry ID: `124929`
- Definition ID: `129767`
- Spell ID: `432181`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your physical damage taken is reduced by $s2% and an additional $432180s2% every $t1 sec until you receive a physical attack, stacking up to $432180u.
- Effect: Your physical damage taken is reduced by $s2% and an additional $432180s2% every $t1 sec until you receive a physical attack, stacking up to $432180u.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `101138` (type `2`), node `101140` (type `2`), node `101182` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tiger's Vigor
- Node ID: `101221`
- Entry ID: `125031`
- Definition ID: `129867`
- Spell ID: `451041`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Tiger's Lust reduces the remaining cooldown on Roll by ${$s1/1000} sec.
- Effect: Casting Tiger's Lust reduces the remaining cooldown on Roll by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101222` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Roar from the Heavens
- Node ID: `101221`
- Entry ID: `125030`
- Definition ID: `129866`
- Spell ID: `451043`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Tiger's Lust grants $452701s1% movement speed to up to $452701i allies near its target.
- Effect: Tiger's Lust grants $452701s1% movement speed to up to $452701i allies near its target.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101222` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Endless Draught
- Node ID: `101225`
- Entry ID: `125036`
- Definition ID: `129872`
- Spell ID: `450892`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137023[Celestial Brew and Celestial Infusion have][Thunder Focus Tea has] $s1 additional charge.
- Effect: $?a137023[Celestial Brew and Celestial Infusion have][Thunder Focus Tea has] $s1 additional charge.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101224` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mantra of Purity
- Node ID: `101229`
- Entry ID: `125042`
- Definition ID: `129878`
- Spell ID: `451036`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137023[Purifying Brew removes $s1% additional Stagger and causes you to absorb up to $<value> incoming Stagger][When cast on yourself, your single-target healing spells heal for $s2% more and restore an additional $451452o1 health over $451452d].
- Effect: $?a137023[Purifying Brew removes $s1% additional Stagger and causes you to absorb up to $<value> incoming Stagger][When cast on yourself, your single-target healing spells heal for $s2% more and restore an additional $451452o1 health over $451452d].
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101230` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mantra of Tenacity
- Node ID: `101229`
- Entry ID: `125041`
- Definition ID: `129877`
- Spell ID: `451029`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137023[Fortifying Brew applies a Chi Cocoon, absorbing $<value> damage][Fortifying Brew grants $s1% Stagger].
- Effect: $?a137023[Fortifying Brew applies a Chi Cocoon, absorbing $<value> damage][Fortifying Brew grants $s1% Stagger].
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101230` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Potential Energy
- Node ID: `109695`
- Entry ID: `135953`
- Definition ID: `140708`
- Spell ID: `1271048`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?c1[Keg Smash][Rising Sun Kick or Rushing Wind Kick] grants a charge of Potential Energy.
- Effect: Casting $?c1[Keg Smash][Rising Sun Kick or Rushing Wind Kick] grants a charge of Potential Energy.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109694` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vital Clarity
- Node ID: `110021`
- Entry ID: `136512`
- Definition ID: `141285`
- Spell ID: `1266748`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vivify and Sheilun's Gift critical strike chances are increased by $s1% on yourself.
- Effect: Vivify and Sheilun's Gift critical strike chances are increased by $s1% on yourself.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `group`; type `0`; currency `3623` spend gate `23` | source `node`; type `1`
- Incoming edges: node `101165` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Jade Infusion
- Node ID: `101164`
- Entry ID: `124958`
- Definition ID: `129796`
- Spell ID: `1242910`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Thunder Focus Tea summons a Jade Serpent Statue at your location. When you channel Soothing Mist, the statue will also begin to channel Soothing Mist on your target, healing for $198533o1 over $198533d.
- Effect: Thunder Focus Tea summons a Jade Serpent Statue at your location. When you channel Soothing Mist, the statue will also begin to channel Soothing Mist on your target, healing for $198533o1 over $198533d.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1` | source `group`; type `0`; currency `3623` spend gate `23`
- Incoming edges: node `101163` (type `2`), node `101165` (type `2`), node `101173` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Summon Jade Serpent Statue
- Node ID: `101164`
- Entry ID: `133997`
- Definition ID: `138783`
- Spell ID: `115313`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Summons a Jade Serpent Statue at the target location. When you channel Soothing Mist, the statue will also begin to channel Soothing Mist on your target, healing for $198533o1 over $198533d.
- Effect: Summons a Jade Serpent Statue at the target location. When you channel Soothing Mist, the statue will also begin to channel Soothing Mist on your target, healing for $198533o1 over $198533d.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1` | source `group`; type `0`; currency `3623` spend gate `23`
- Incoming edges: node `101163` (type `2`), node `101165` (type `2`), node `101173` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overwhelming Force
- Node ID: `101220`
- Entry ID: `125029`
- Definition ID: `129865`
- Spell ID: `451024`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137023[][Rising Sun Kick, ]Blackout Kick and Tiger Palm deal $s1% additional damage to enemies in a line in front of you. Damage reduced above $s2 targets.
- Effect: $?a137023[][Rising Sun Kick, ]Blackout Kick and Tiger Palm deal $s1% additional damage to enemies in a line in front of you. Damage reduced above $s2 targets.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101221` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Path of Resurgence
- Node ID: `101226`
- Entry ID: `125038`
- Definition ID: `129874`
- Spell ID: `450912`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a450391[Chi Wave][Chi Burst] increases vitality stored by $451084s1% for $451084d.
- Effect: $?a450391[Chi Wave][Chi Burst] increases vitality stored by $451084s1% for $451084d.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101225` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Way of a Thousand Strikes
- Node ID: `101226`
- Entry ID: `125037`
- Definition ID: `129873`
- Spell ID: `450965`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137023[][Rising Sun Kick, ]Blackout Kick and Tiger Palm contribute $s1% additional vitality.
- Effect: $?a137023[][Rising Sun Kick, ]Blackout Kick and Tiger Palm contribute $s1% additional vitality.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101225` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Clarity of Purpose
- Node ID: `101228`
- Entry ID: `125040`
- Definition ID: `129876`
- Spell ID: `451017`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?a137023[Purifying Brew][Enveloping Mist] stores $<value> additional vitality.
- Effect: Casting $?a137023[Purifying Brew][Enveloping Mist] stores $<value> additional vitality.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101229` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Meditative Focus
- Node ID: `109696`
- Entry ID: `135954`
- Definition ID: `140709`
- Spell ID: `1271105`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a388023[Ancient Teachings transfers an additional $s1% damage to healing.][$@spellicon196736 Blackout Combo:
Increases Tiger Palm damage by an additional $s2% and Keg Smash reduces the cooldown on your Brews by an additional ${$s3/1000}.1 sec.

$@spellicon418359  Press the Advantage:
Nature damage dealt by your main hand auto-attacks is increased by $s4% and they now reduce the cooldown on your Brews by an additional ${$s5/1000}.2 sec.]
- Effect: $?a388023[Ancient Teachings transfers an additional $s1% damage to healing.][$@spellicon196736 Blackout Combo:
Increases Tiger Palm damage by an additional $s2% and Keg Smash reduces the cooldown on your Brews by an additional ${$s3/1000}.1 sec.

$@spellicon418359  Press the Advantage:
Nature damage dealt by your main hand auto-attacks is increased by $s4% and they now reduce the cooldown on your Brews by an additional ${$s5/1000}.2 sec.]
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109695` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Coalescence
- Node ID: `101227`
- Entry ID: `125039`
- Definition ID: `129875`
- Spell ID: `450529`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Aspect of Harmony $?a450870[deals damage or heals]?a137023[deals damage][heals], it has a chance to spread to a nearby $?a450870[target]?a137023[enemy][ally]. When you directly $?a450870[attack or heal]?a137023[attack][heal] an affected target, it has a chance to intensify, withdrawing additional vitality to increase its effect by up to $450508s9%.

$?a137023[Keg Smash][Vivify] no longer contributes vitality. While Aspect of Harmony is not active, $?a137023[Keg Smash][Vivify] instead draws on available vitality to deal an additional $s2% $?a137023[damage over $1292919d][healing over $1292922d].

Vitality stored by other abilities is increased by $s3%.
- Effect: When Aspect of Harmony $?a450870[deals damage or heals]?a137023[deals damage][heals], it has a chance to spread to a nearby $?a450870[target]?a137023[enemy][ally]. When you directly $?a450870[attack or heal]?a137023[attack][heal] an affected target, it has a chance to intensify, withdrawing additional vitality to increase its effect by up to $450508s9%.

$?a137023[Keg Smash][Vivify] no longer contributes vitality. While Aspect of Harmony is not active, $?a137023[Keg Smash][Vivify] instead draws on available vitality to deal an additional $s2% $?a137023[damage over $1292919d][healing over $1292922d].

Vitality stored by other abilities is increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Master of Harmony) (ID `3624`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101220` (type `2`), node `101226` (type `2`), node `101228` (type `2`), node `109696` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
