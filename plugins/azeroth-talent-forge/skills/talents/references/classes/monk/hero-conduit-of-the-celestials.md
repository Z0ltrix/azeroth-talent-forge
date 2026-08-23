# Conduit of the Celestials

Reviewed build: `12.1.0.69404`
Hero subtree ID: `64`
Description: Conduits of the Celestials devote themselves to the teachings of the August Celestials to embody their wisdom and harness their strength. Master Conduits may briefly channel the power of all Celestials at once.

## Hero talents

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
### Restore Balance
- Node ID: `110221`
- Entry ID: `136760`
- Definition ID: `141531`
- Spell ID: `442719`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Healing increased by $322118s8% while Chi-Ji, the Red Crane or Yu'lon, the Jade Serpent is active.]?c3[Damage increased by $123904s4% while Xuen, the White Tiger is active.][]
- Effect: $?c2[Healing increased by $322118s8% while Chi-Ji, the Red Crane or Yu'lon, the Jade Serpent is active.]?c3[Damage increased by $123904s4% while Xuen, the White Tiger is active.][]
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `node`; type `1`
- Incoming edges: node `101243` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Xuen's Bond
- Node ID: `110221`
- Entry ID: `136744`
- Definition ID: `141516`
- Spell ID: `392986`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Invoke Xuen, the White Tiger's damage is increased by ${$s1}% and its cooldown is reduced by ${$s2/-1000} sec.
- Effect: Invoke Xuen, the White Tiger's damage is increased by ${$s1}% and its cooldown is reduced by ${$s2/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1` | source `node`; type `1`
- Incoming edges: node `101243` (type `2`)
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
### Celestial Conduit
- Node ID: `110220`
- Entry ID: `136745`
- Definition ID: `141517`
- Spell ID: `1248989`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After Invoking Xuen, the White Tiger you may cast Celestial Conduit within $1248992d.

$@spellicon443028 $@spellname443028:
$@spelldesc443028
- Effect: After Invoking Xuen, the White Tiger you may cast Celestial Conduit within $1248992d.

$@spellicon443028 $@spellname443028:
$@spelldesc443028
- Point cost per purchased rank: `1` × Hero pool (Conduit of the Celestials) (ID `3622`; group)
- Source gates: source `group`; type `1`
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
