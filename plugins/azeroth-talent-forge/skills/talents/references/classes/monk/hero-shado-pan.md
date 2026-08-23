# Shado-Pan

Reviewed build: `12.1.0.69404`
Hero subtree ID: `65`
Description: Shado-Pan learn from their forebears and stand proud against their foes to defend friends and family. They bide their time to charge power before unleashing a flurry of blows to overwhelm opponents.

## Hero talents

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
