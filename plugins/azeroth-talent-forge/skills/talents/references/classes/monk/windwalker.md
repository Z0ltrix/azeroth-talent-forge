# Windwalker

Reviewed build: `12.1.0.69404`
Spec ID: `269`
Role: `2`

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
### Pride of Pandaria
- Node ID: `101247`
- Entry ID: `125068`
- Definition ID: `129900`
- Spell ID: `450979`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Flurry Strikes have $s1% additional chance to critically strike.
- Effect: Flurry Strikes have $s1% additional chance to critically strike.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101248` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### High Impact
- Node ID: `101247`
- Entry ID: `125067`
- Definition ID: `129899`
- Spell ID: `450982`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Enemies who die within $451037d of being damaged by a Flurry Strike explode, dealing $451039s1 physical damage to uncontrolled enemies within $451039a1 yds.
- Effect: Enemies who die within $451037d of being damaged by a Flurry Strike explode, dealing $451039s1 physical damage to uncontrolled enemies within $451039a1 yds.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101248` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Veteran's Eye
- Node ID: `101249`
- Entry ID: `125070`
- Definition ID: `129902`
- Spell ID: `450987`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Haste increased by $s1%.
- Effect: Haste increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101248` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Martial Precision
- Node ID: `101246`
- Entry ID: `125066`
- Definition ID: `129898`
- Spell ID: `450990`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your attacks penetrate $s1% armor.
- Effect: Your attacks penetrate $s1% armor.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101248` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shado Over the Battlefield
- Node ID: `109697`
- Entry ID: `135955`
- Definition ID: `140710`
- Spell ID: `1262612`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Flurry Strikes deal $451250s1 Nature damage to all enemies within $451250a yds, reduced beyond $s2 targets.
- Effect: Flurry Strikes deal $451250s1 Nature damage to all enemies within $451250a yds, reduced beyond $s2 targets.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101248` (type `2`)
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
### Combat Stance
- Node ID: `101254`
- Entry ID: `125076`
- Definition ID: `129908`
- Spell ID: `1272844`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cooldown of Roll is decreased by $s1%.
- Effect: The cooldown of Roll is decreased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101247` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Initiator's Edge
- Node ID: `101254`
- Entry ID: `125075`
- Definition ID: `129907`
- Spell ID: `1272849`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Movement speed is increased by $1272850s1% for the first $1272850d of combat.
- Effect: Movement speed is increased by $1272850s1% for the first $1272850d of combat.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101247` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### One Versus Many
- Node ID: `101250`
- Entry ID: `125071`
- Definition ID: `129903`
- Spell ID: `450988`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Auto attack critical strikes generate double the amount of Flurry Charges.

$?c3[Fists of Fury damage increased by $s2%.][
Keg Smash damage increased by $s3%.]
- Effect: Auto attack critical strikes generate double the amount of Flurry Charges.

$?c3[Fists of Fury damage increased by $s2%.][
Keg Smash damage increased by $s3%.]
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101249` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Whirling Steel
- Node ID: `101245`
- Entry ID: `125065`
- Definition ID: `129897`
- Spell ID: `450991`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your health drops below $s1%, summon Whirling Steel, increasing your parry chance and avoidance by $451214s1% for $451214d.

This effect can not occur more than once every $proccooldown sec.
- Effect: When your health drops below $s1%, summon Whirling Steel, increasing your parry chance and avoidance by $451214s1% for $451214d.

This effect can not occur more than once every $proccooldown sec.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101246` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Predictive Training
- Node ID: `101245`
- Entry ID: `125064`
- Definition ID: `129896`
- Spell ID: `450992`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you dodge or parry an attack, reduce all damage taken by $451230s1% for the next $451230d.
- Effect: When you dodge or parry an attack, reduce all damage taken by $451230s1% for the next $451230d.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101246` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stand Ready
- Node ID: `109698`
- Entry ID: `135956`
- Definition ID: `140711`
- Spell ID: `1262603`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating $?c1[Invoke Niuzao, the Black Ox][Zenith] instantly grants $s1 stacks of Flurry Strikes that trigger on your next attack at $s2% effectiveness.
- Effect: Activating $?c1[Invoke Niuzao, the Black Ox][Zenith] instantly grants $s1 stacks of Flurry Strikes that trigger on your next attack at $s2% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109697` (type `2`)
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
### Detox
- Node ID: `101150`
- Entry ID: `124941`
- Definition ID: `129779`
- Spell ID: `218164`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Removes all Poison and Disease effects from the target.
- Effect: Removes all Poison and Disease effects from the target.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101149` (type `2`), node `101185` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Against All Odds
- Node ID: `101253`
- Entry ID: `125074`
- Definition ID: `129906`
- Spell ID: `450986`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your agility is increased by $s1%.
- Effect: Your agility is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101254` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Efficient Training
- Node ID: `101251`
- Entry ID: `125072`
- Definition ID: `129904`
- Spell ID: `450989`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Energy spenders deal an additional $s1% damage.
The cooldown of $?c1[Invoke Niuzao, the Black Ox is reduced by ${$s6/-1000} sec][Zenith is reduced by ${$s4/-1000} sec].
- Effect: Energy spenders deal an additional $s1% damage.
The cooldown of $?c1[Invoke Niuzao, the Black Ox is reduced by ${$s6/-1000} sec][Zenith is reduced by ${$s4/-1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101250` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vigilant Watch
- Node ID: `101244`
- Entry ID: `125063`
- Definition ID: `129895`
- Spell ID: `450993`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blackout Kick deals an additional $s1% critical damage.
- Effect: Blackout Kick deals an additional $s1% critical damage.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101245` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Weapons of the Wall
- Node ID: `109699`
- Entry ID: `135957`
- Definition ID: `140712`
- Spell ID: `1262610`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Invoke Niuzao, the Black Ox's stomp damage increased by $s2%][Zenith Stomp damage increased by $s1%].
- Effect: $?c1[Invoke Niuzao, the Black Ox's stomp damage increased by $s2%][Zenith Stomp damage increased by $s1%].
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109698` (type `2`)
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
### Vivacious Vivification
- Node ID: `110023`
- Entry ID: `136515`
- Definition ID: `141288`
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
### Spear Hand Strike
- Node ID: `110098`
- Entry ID: `136599`
- Definition ID: `141372`
- Spell ID: `116705`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Jabs the target in the throat, interrupting spellcasting and preventing any spell from that school of magic from being cast for $d.
- Effect: Jabs the target in the throat, interrupting spellcasting and preventing any spell from that school of magic from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101148` (type `2`), node `101150` (type `2`), node `101153` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wisdom of the Wall
- Node ID: `101252`
- Entry ID: `125073`
- Definition ID: `129905`
- Spell ID: `1272821`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Invoke Niuzao, the Black Ox][Zenith] causes $?c1[Breath of Fire][Rising Sun Kick and Spinning Crane Kick] to launch $s1 Flurry Strikes.
- Effect: $?c1[Invoke Niuzao, the Black Ox][Zenith] causes $?c1[Breath of Fire][Rising Sun Kick and Spinning Crane Kick] to launch $s1 Flurry Strikes.
- Point cost per purchased rank: `1` × Hero pool (Shado-Pan) (ID `3621`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `101244` (type `2`), node `101251` (type `2`), node `101253` (type `2`), node `109699` (type `2`)
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
### Tiger Fang
- Node ID: `101159`
- Entry ID: `124953`
- Definition ID: `129791`
- Spell ID: `1272781`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto attack critical strike chance is increased by $s1%.
- Effect: Your auto attack critical strike chance is increased by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `101145` (type `2`), node `101160` (type `2`), node `110023` (type `2`), node `110024` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Energy Transfer
- Node ID: `110095`
- Entry ID: `136596`
- Definition ID: `141369`
- Spell ID: `450631`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Successfully interrupting an enemy reduces the cooldown of Paralysis and Roll by ${$s1/-1000} sec.
- Effect: Successfully interrupting an enemy reduces the cooldown of Paralysis and Roll by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `110098` (type `2`)
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
### Vigorous Expulsion
- Node ID: `110020`
- Entry ID: `136511`
- Definition ID: `141284`
- Spell ID: `392900`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Expel Harm's healing increased by $s1% and critical strike chance increased by $s2%.
- Effect: Expel Harm's healing increased by $s1% and critical strike chance increased by $s2%.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `101158` (type `2`), node `101159` (type `2`), node `101166` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dance of the Wind
- Node ID: `101137`
- Entry ID: `124927`
- Definition ID: `129765`
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
### Strength of Spirit
- Node ID: `110022`
- Entry ID: `136514`
- Definition ID: `141287`
- Spell ID: `387276`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Expel Harm's healing is increased by up to $s1%, based on your missing health.
- Effect: Expel Harm's healing is increased by up to $s1%, based on your missing health.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `group`; type `0`; currency `3623` spend gate `23` | source `node`; type `1`
- Incoming edges: node `101165` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Profound Rebuttal
- Node ID: `110022`
- Entry ID: `136513`
- Definition ID: `141286`
- Spell ID: `392910`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Expel Harm's critical healing is increased by $s1%.
- Effect: Expel Harm's critical healing is increased by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `group`; type `0`; currency `3623` spend gate `23` | source `node`; type `1`
- Incoming edges: node `101165` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Zenith Stomp
- Node ID: `101162`
- Entry ID: `124956`
- Definition ID: `129794`
- Spell ID: `1272694`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating Zenith causes you to release a powerful stomp, dealing $1272696s1 Nature damage to nearby enemies, reduced beyond $s1 targets.

|cFFFFFFFFGenerates $1272696s2 Chi.
- Effect: Activating Zenith causes you to release a powerful stomp, dealing $1272696s1 Nature damage to nearby enemies, reduced beyond $s1 targets.

|cFFFFFFFFGenerates $1272696s2 Chi.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1` | source `group`; type `0`; currency `3623` spend gate `23`
- Incoming edges: node `101163` (type `2`), node `101165` (type `2`), node `101173` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
