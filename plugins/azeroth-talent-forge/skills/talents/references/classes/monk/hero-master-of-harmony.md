# Master of Harmony

Reviewed build: `12.1.0.69404`
Hero subtree ID: `66`
Description: Masters of Harmony chase physical perfection and the refinement of the body into pure strength, allowing them to tap into the flow of chi and natural cycles of power.

## Hero talents

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
