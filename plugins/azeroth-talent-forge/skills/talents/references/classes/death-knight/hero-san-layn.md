# San'layn

Reviewed build: `12.1.0.69404`
Hero subtree ID: `31`
Description: San'layn excel at using blood and shadow magic to weaken their enemies and empower their own capabilities.

## Hero talents

### Vampiric Strike
- Node ID: `95051`
- Entry ID: `117648`
- Definition ID: `122660`
- Spell ID: `433901`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Death Coil$?a137007[, Epidemic][] and Death Strike have a $s1% chance to make your next $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] become Vampiric Strike.

Vampiric Strike heals you for $?a137008[$434422s2][$434422s3]% of your maximum health and grants you Essence of the Blood Queen, increasing your Haste by ${$433925s1/10}.1%, up to ${$433925s1*$433925u/10}.1% for $433925d.
- Effect: Your Death Coil$?a137007[, Epidemic][] and Death Strike have a $s1% chance to make your next $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] become Vampiric Strike.

Vampiric Strike heals you for $?a137008[$434422s2][$434422s3]% of your maximum health and grants you Essence of the Blood Queen, increasing your Haste by ${$433925s1/10}.1%, up to ${$433925s1*$433925u/10}.1% for $433925d.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Newly Turned
- Node ID: `95064`
- Entry ID: `117661`
- Definition ID: `122673`
- Spell ID: `433934`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Raise Ally revives players at full health and grants you and your ally an absorb shield equal to $s2% of your maximum health.
- Effect: Raise Ally revives players at full health and grants you and your ally an absorb shield equal to $s2% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vampiric Speed
- Node ID: `95064`
- Entry ID: `117892`
- Definition ID: `122904`
- Spell ID: `434028`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Death's Advance and Wraith Walk movement speed bonuses are increased by $s1%.

Activating Death's Advance or Wraith Walk increases $434029s2 nearby allies movement speed by $434029s1% for $434029d.
- Effect: Death's Advance and Wraith Walk movement speed bonuses are increased by $s1%.

Activating Death's Advance or Wraith Walk increases $434029s2 nearby allies movement speed by $434029s1% for $434029d.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blood-Soaked Ground
- Node ID: `95048`
- Entry ID: `117645`
- Definition ID: `122657`
- Spell ID: `434033`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While you are within your Death and Decay, your physical damage taken is reduced by ${$434034s1*-1}% and your chance to gain Vampiric Strike is increased by $s2%.
- Effect: While you are within your Death and Decay, your physical damage taken is reduced by ${$434034s1*-1}% and your chance to gain Vampiric Strike is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Desecrate
- Node ID: `95048`
- Entry ID: `136836`
- Definition ID: `141599`
- Spell ID: `1234559`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Death and Decay deals its damage ${(1/(1+($s1/100))-1)*100}% faster.
- Effect: Death and Decay deals its damage ${(1/(1+($s1/100))-1)*100}% faster.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vampiric Aura
- Node ID: `95056`
- Entry ID: `117653`
- Definition ID: `122665`
- Spell ID: `434100`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Leech is increased by $s1%.

While Lichborne is active, the Leech bonus of this effect is increased by $434105s1%, and it affects $s2 allies within 12 yds.
- Effect: Your Leech is increased by $s1%.

While Lichborne is active, the Leech bonus of this effect is increased by $434105s1%, and it affects $s2 allies within 12 yds.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bloody Fortitude
- Node ID: `95056`
- Entry ID: `117891`
- Definition ID: `122903`
- Spell ID: `434136`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Icebound Fortitude reduces all damage you take by up to an additional $s1% based on your missing health.

Killing an enemy that yields experience or honor reduces the cooldown of Icebound Fortitude by $s2 sec.
- Effect: Icebound Fortitude reduces all damage you take by up to an additional $s1% based on your missing health.

Killing an enemy that yields experience or honor reduces the cooldown of Icebound Fortitude by $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thrill of Blood
- Node ID: `109737`
- Entry ID: `135995`
- Definition ID: `140750`
- Spell ID: `1265547`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence of the Blood Queen additionally increases your Mastery by $?c3[${$s1/10}.1][${$s3/10}.1]% per stack.

$?c3[Dread Plague deals $s5% and Virulent Plague deals $s3%][Blood Plague deals $s4%] increased damage.
- Effect: Essence of the Blood Queen additionally increases your Mastery by $?c3[${$s1/10}.1][${$s3/10}.1]% per stack.

$?c3[Dread Plague deals $s5% and Virulent Plague deals $s3%][Blood Plague deals $s4%] increased damage.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95051` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Infliction of Sorrow
- Node ID: `95033`
- Entry ID: `117630`
- Definition ID: `122642`
- Spell ID: `434143`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Vampiric Strike damages an enemy affected by your $?a137008[Blood Plague][plagues], it extends the duration of the $?a137008[disease][plagues] by $?c1[${$s3/1000}.1][${$s5/1000}.1] sec$?c1[, and deals $s2% of the remaining damage to the enemy.][, and erupts them with $s6% increased effectiveness.]
- Effect: When Vampiric Strike damages an enemy affected by your $?a137008[Blood Plague][plagues], it extends the duration of the $?a137008[disease][plagues] by $?c1[${$s3/1000}.1][${$s5/1000}.1] sec$?c1[, and deals $s2% of the remaining damage to the enemy.][, and erupts them with $s6% increased effectiveness.]
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95064` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frenzied Bloodthirst
- Node ID: `95065`
- Entry ID: `117662`
- Definition ID: `122674`
- Spell ID: `434075`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence of the Blood Queen stacks $s1 additional times and increases the damage of your $?s137008[Death Coil and Death Strike by $s2%][Death Coil and Death Strike by $s2%, and Epidemic by $s3%] per stack.
- Effect: Essence of the Blood Queen stacks $s1 additional times and increases the damage of your $?s137008[Death Coil and Death Strike by $s2%][Death Coil and Death Strike by $s2%, and Epidemic by $s3%] per stack.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95048` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### The Blood is Life
- Node ID: `95046`
- Entry ID: `117643`
- Definition ID: `122655`
- Spell ID: `434260`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Dancing Rune Weapon]?s275699[Apocalypse][Dark Transformation] summons a Blood Beast to attack your enemy for $434237d.

Each time the Blood Beast attacks, it stores a portion of the damage dealt. When the Blood Beast dies, it explodes, dealing $?a137007[$s2][$s1]% of the damage accumulated to nearby enemies and healing the Death Knight for the same amount. Deals reduced damage beyond $s3 targets.
- Effect: $?a137008[Dancing Rune Weapon]?s275699[Apocalypse][Dark Transformation] summons a Blood Beast to attack your enemy for $434237d.

Each time the Blood Beast attacks, it stores a portion of the damage dealt. When the Blood Beast dies, it explodes, dealing $?a137007[$s2][$s1]% of the damage accumulated to nearby enemies and healing the Death Knight for the same amount. Deals reduced damage beyond $s3 targets.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95056` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Visceral Strength
- Node ID: `109738`
- Entry ID: `135996`
- Definition ID: `140751`
- Spell ID: `434157`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When $?a137008[Crimson Scourge][Sudden Doom] is consumed, you gain $?a137008[$461130s1][$434159s1]% Strength for $?a137008[$461130d][$434159d].
- Effect: When $?a137008[Crimson Scourge][Sudden Doom] is consumed, you gain $?a137008[$461130s1][$434159s1]% Strength for $?a137008[$461130d][$434159d].
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109737` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Inevitable
- Node ID: `95045`
- Entry ID: `117642`
- Definition ID: `122654`
- Spell ID: `1280658`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Blood Plague deals up to $s2%][Your plagues deal up to $s1%] increased damage based on the target's missing health.$?a137007[

Vampiric Strike grants maximum stacks of Clawing Shadows.][]
- Effect: $?a137008[Blood Plague deals up to $s2%][Your plagues deal up to $s1%] increased damage based on the target's missing health.$?a137007[

Vampiric Strike grants maximum stacks of Clawing Shadows.][]
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95033` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Incite Terror
- Node ID: `95040`
- Entry ID: `117637`
- Definition ID: `122649`
- Spell ID: `434151`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vampiric Strike and $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] cause your targets to take $458478s1% increased Shadow damage, up to ${$458478s1*$458478U}% for $458478d.

Vampiric Strike benefits from Incite Terror at $s2% effectiveness.
- Effect: Vampiric Strike and $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] cause your targets to take $458478s1% increased Shadow damage, up to ${$458478s1*$458478U}% for $458478d.

Vampiric Strike benefits from Incite Terror at $s2% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95065` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pact of the San'layn
- Node ID: `95055`
- Entry ID: `117652`
- Definition ID: `122664`
- Spell ID: `434261`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You store $s1% of all Shadow damage dealt into your Blood Beast to explode for additional damage when it expires.
- Effect: You store $s1% of all Shadow damage dealt into your Blood Beast to explode for additional damage when it expires.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95046` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sanguine Scent
- Node ID: `95055`
- Entry ID: `117893`
- Definition ID: `122905`
- Spell ID: `434263`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your Death Coil$?a137007[, Epidemic][] and Death Strike have a $s2% increased chance to trigger Vampiric Strike when damaging enemies below $s1% health.
- Effect: Your Death Coil$?a137007[, Epidemic][] and Death Strike have a $s2% increased chance to trigger Vampiric Strike when damaging enemies below $s1% health.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95046` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Transfusion
- Node ID: `109736`
- Entry ID: `135994`
- Definition ID: `140749`
- Spell ID: `1265574`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vampiric Strike increases the damage of $?c3[your Lesser Ghouls][your Dancing Rune Weapons] by $?c3[$1280386s1][$1236822s3]% for $1236822d.$?c1[

Multiple applications may overlap.][]
- Effect: Vampiric Strike increases the damage of $?c3[your Lesser Ghouls][your Dancing Rune Weapons] by $?c3[$1280386s1][$1236822s3]% for $1236822d.$?c1[

Multiple applications may overlap.][]
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109738` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gift of the San'layn
- Node ID: `95053`
- Entry ID: `117650`
- Definition ID: `122662`
- Spell ID: `434152`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While $?a137008[Dancing Rune Weapon][Dark Transformation] is active you gain Gift of the San'layn.

Gift of the San'layn increases the effectiveness of your Essence of the Blood Queen by $?a137007[$434153s1][$434153s4]%, and Vampiric Strike replaces your $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] for the duration.
- Effect: While $?a137008[Dancing Rune Weapon][Dark Transformation] is active you gain Gift of the San'layn.

Gift of the San'layn increases the effectiveness of your Essence of the Blood Queen by $?a137007[$434153s1][$434153s4]%, and Vampiric Strike replaces your $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] for the duration.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95040` (type `2`), node `95045` (type `2`), node `95055` (type `2`), node `109736` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
