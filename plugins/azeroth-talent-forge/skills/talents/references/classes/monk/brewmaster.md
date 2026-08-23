# Brewmaster

Reviewed build: `12.1.0.69404`
Spec ID: `268`
Role: `0`

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
### Stagger
- Node ID: `109827`
- Entry ID: `136086`
- Definition ID: `140841`
- Spell ID: `115069`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You shrug off attacks, delaying a portion of Physical damage based on your Agility, instead taking it over $124273d. Affects magical attacks at $s5% effectiveness.$?s383714[

$@spelldesc383714][]
- Effect: You shrug off attacks, delaying a portion of Physical damage based on your Agility, instead taking it over $124273d. Affects magical attacks at $s5% effectiveness.$?s383714[

$@spelldesc383714][]
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1`
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
### Fast Feet
- Node ID: `109826`
- Entry ID: `136085`
- Definition ID: `140840`
- Spell ID: `1261543`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blackout Kick deals $s1% increased damage. Spinning Crane Kick deals $s2% additional damage.
- Effect: Blackout Kick deals $s1% increased damage. Spinning Crane Kick deals $s2% additional damage.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `109827` (type `2`)
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
### Detox
- Node ID: `101090`
- Entry ID: `124867`
- Definition ID: `129705`
- Spell ID: `218164`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Removes all Poison and Disease effects from the target.
- Effect: Removes all Poison and Disease effects from the target.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101149` (type `2`), node `101185` (type `2`), node `109826` (type `2`)
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
### Vivacious Vivification
- Node ID: `101145`
- Entry ID: `124935`
- Definition ID: `129773`
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
- Node ID: `101152`
- Entry ID: `124943`
- Definition ID: `129781`
- Spell ID: `116705`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Jabs the target in the throat, interrupting spellcasting and preventing any spell from that school of magic from being cast for $d.
- Effect: Jabs the target in the throat, interrupting spellcasting and preventing any spell from that school of magic from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `101089` (type `2`), node `101090` (type `2`), node `101148` (type `2`), node `101153` (type `2`)
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
### Chi Wave
- Node ID: `102433`
- Entry ID: `126502`
- Definition ID: `131328`
- Spell ID: `450391`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $t1 sec, your next $?a137023[Keg Smash][Rising Sun Kick] or $?s399491[Sheilun's Gift][Vivify] releases a wave of Chi energy that flows through friends and foes, dealing $132467s1 Nature damage or $132463s1 healing. Bounces up to $115098s1 times to targets within $132466a2 yards.
- Effect: Every $t1 sec, your next $?a137023[Keg Smash][Rising Sun Kick] or $?s399491[Sheilun's Gift][Vivify] releases a wave of Chi energy that flows through friends and foes, dealing $132467s1 Nature damage or $132463s1 healing. Bounces up to $115098s1 times to targets within $132466a2 yards.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `4`; currency `3623` spend gate `0` | source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1` | source `node`; type `4`; currency `3623` spend gate `0`
- Incoming edges: node `101145` (type `2`), node `101160` (type `2`), node `110024` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chi Burst
- Node ID: `102433`
- Entry ID: `126501`
- Definition ID: `131327`
- Spell ID: `123986`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Hurls a torrent of Chi energy up to $460485s1 yds forward, dealing $148135s1 Nature damage to all enemies, and $130654s1 healing to the Monk and all allies in its path. Healing and damage reduced beyond $s1 targets.
$?c1[

Casting Chi Burst does not prevent avoiding attacks.][]
- Effect: Hurls a torrent of Chi energy up to $460485s1 yds forward, dealing $148135s1 Nature damage to all enemies, and $130654s1 healing to the Monk and all allies in its path. Healing and damage reduced beyond $s1 targets.
$?c1[

Casting Chi Burst does not prevent avoiding attacks.][]
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `node`; type `4`; currency `3623` spend gate `0` | source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1` | source `node`; type `4`; currency `3623` spend gate `0`
- Incoming edges: node `101145` (type `2`), node `101160` (type `2`), node `110024` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Energy Transfer
- Node ID: `101151`
- Entry ID: `124942`
- Definition ID: `129780`
- Spell ID: `450631`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Successfully interrupting an enemy reduces the cooldown of Paralysis and Roll by ${$s1/-1000} sec.
- Effect: Successfully interrupting an enemy reduces the cooldown of Paralysis and Roll by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `101152` (type `2`)
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
### Vigorous Expulsion
- Node ID: `101156`
- Entry ID: `124948`
- Definition ID: `129786`
- Spell ID: `392900`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Expel Harm's healing increased by $s1% and critical strike chance increased by $s2%.
- Effect: Expel Harm's healing increased by $s1% and critical strike chance increased by $s2%.
- Point cost per purchased rank: `1` × Specialization pool (Brewmaster, Mistweaver, Windwalker) (ID `3623`; group)
- Source gates: source `group`; type `0`; currency `3623` spend gate `8` | source `node`; type `1`
- Incoming edges: node `101158` (type `2`), node `101159` (type `2`), node `101166` (type `2`), node `102432` (type `2`), node `102433` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dance of the Wind
- Node ID: `101181`
- Entry ID: `124979`
- Definition ID: `129817`
- Spell ID: `414132`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your dodge chance is increased by $s1%.
- Effect: Your dodge chance is increased by $s1%.
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
### Strength of Spirit
- Node ID: `101135`
- Entry ID: `124924`
- Definition ID: `129762`
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
- Node ID: `101135`
- Entry ID: `124923`
- Definition ID: `129761`
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
### Summon Black Ox Statue
- Node ID: `101172`
- Entry ID: `124967`
- Definition ID: `129805`
- Spell ID: `115315`
- Tree ID: `1000`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summons a Black Ox Statue at the target location for $d, pulsing threat to all enemies within $163178A1 yards.

You may cast Provoke on the statue to taunt all enemies near the statue.
- Effect: Summons a Black Ox Statue at the target location for $d, pulsing threat to all enemies within $163178A1 yards.

You may cast Provoke on the statue to taunt all enemies near the statue.
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
