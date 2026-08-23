# Unholy

Reviewed build: `12.1.0.69404`
Spec ID: `252`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Raise Dead
- Node ID: `76072`
- Entry ID: `96201`
- Definition ID: `101203`
- Spell ID: `46585`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Raises a $?s58640[geist][ghoul] to fight by your side.  You can have a maximum of one $?s58640[geist][ghoul] at a time. Lasts $46585d.
- Effect: Raises a $?s58640[geist][ghoul] to fight by your side.  You can have a maximum of one $?s58640[geist][ghoul] at a time. Lasts $46585d.
- Point cost per purchased rank: `1` × Specialization pool (Blood, Frost, Unholy) (ID `2801`; group)
- Source gates: source `node`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reaper's Mark
- Node ID: `95062`
- Entry ID: `117659`
- Definition ID: `122671`
- Spell ID: `439843`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Viciously slice into the soul of your enemy, dealing $?a137008[$s1][$s4] Shadowfrost damage and applying Reaper's Mark.

Each time you deal Shadow or Frost damage, add a stack of Reaper's Mark. After $434765d or reaching $434765u stacks, the mark explodes, dealing $?a137008[$436304s1][$436304s2] damage per stack.

Reaper's Mark travels to an unmarked enemy nearby if the target dies.
- Effect: Viciously slice into the soul of your enemy, dealing $?a137008[$s1][$s4] Shadowfrost damage and applying Reaper's Mark.

Each time you deal Shadow or Frost damage, add a stack of Reaper's Mark. After $434765d or reaching $434765u stacks, the mark explodes, dealing $?a137008[$436304s1][$436304s2] damage per stack.

Reaper's Mark travels to an unmarked enemy nearby if the target dies.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Rider's Champion
- Node ID: `95066`
- Entry ID: `117663`
- Definition ID: `122675`
- Spell ID: `444005`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Spending Runes has a chance to call forth the aid of a Horsemen for $454390d.

|cFFFFFFFFMograine|R
Casts Death and Decay at his location that follows his position and extends the duration of your diseases by ${$s2/1000}.1 sec whenever it deals damage.

|cFFFFFFFFWhitemane|R
Casts Undeath on your target dealing $444633s1 Shadowfrost damage per stack every $444633t sec, for $444633d. Each time Undeath deals damage it gains a stack. Cannot be refreshed.

|cFFFFFFFFTrollbane|R
Casts Chains of Ice on your target slowing their movement speed by $444834s1% and increasing the damage they take from you by 5% for 8 sec.

|cFFFFFFFFNazgrim|R
While Nazgrim is active you gain Apocalyptic Conquest, increasing your Strength by $444763s1%.
- Effect: Spending Runes has a chance to call forth the aid of a Horsemen for $454390d.

|cFFFFFFFFMograine|R
Casts Death and Decay at his location that follows his position and extends the duration of your diseases by ${$s2/1000}.1 sec whenever it deals damage.

|cFFFFFFFFWhitemane|R
Casts Undeath on your target dealing $444633s1 Shadowfrost damage per stack every $444633t sec, for $444633d. Each time Undeath deals damage it gains a stack. Cannot be refreshed.

|cFFFFFFFFTrollbane|R
Casts Chains of Ice on your target slowing their movement speed by $444834s1% and increasing the damage they take from you by 5% for 8 sec.

|cFFFFFFFFNazgrim|R
While Nazgrim is active you gain Apocalyptic Conquest, increasing your Strength by $444763s1%.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### On a Paler Horse
- Node ID: `95060`
- Entry ID: `117657`
- Definition ID: `122669`
- Spell ID: `444008`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While outdoors you are able to mount your Acherus Deathcharger in combat.
- Effect: While outdoors you are able to mount your Acherus Deathcharger in combat.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death Charge
- Node ID: `95060`
- Entry ID: `123412`
- Definition ID: `128250`
- Spell ID: `444010`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Call upon your Death Charger to break free of movement impairment effects.

For $444347d, while upon your Death Charger your movement speed is increased by $444347s5%, you cannot be slowed below $444347s10% of normal speed, and you are immune to forced movement effects and knockbacks.
- Effect: Call upon your Death Charger to break free of movement impairment effects.

For $444347d, while upon your Death Charger your movement speed is increased by $444347s5%, you cannot be slowed below $444347s10% of normal speed, and you are immune to forced movement effects and knockbacks.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mograine's Might
- Node ID: `95067`
- Entry ID: `117664`
- Definition ID: `122676`
- Spell ID: `444047`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your damage is increased by $444505s1% and you gain $?c3[the benefits of your Death and Decay]?c2[$444505s4% critical strike chance][] while inside Mograine's Death and Decay.
- Effect: Your damage is increased by $444505s1% and you gain $?c3[the benefits of your Death and Decay]?c2[$444505s4% critical strike chance][] while inside Mograine's Death and Decay.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Horsemen's Aid
- Node ID: `95037`
- Entry ID: `117634`
- Definition ID: `122646`
- Spell ID: `444074`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While at your aid, the Horsemen will occasionally cast Anti-Magic Shell on you and themselves at $s1% effectiveness.

You may only benefit from this effect every $451777d.
- Effect: While at your aid, the Horsemen will occasionally cast Anti-Magic Shell on you and themselves at $s1% effectiveness.

You may only benefit from this effect every $451777d.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pact of the Apocalypse
- Node ID: `95037`
- Entry ID: `123410`
- Definition ID: `128248`
- Spell ID: `444083`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you take damage, $s1% of the damage is redirected to each active horsemen.
- Effect: When you take damage, $s1% of the damage is redirected to each active horsemen.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ride or Die!
- Node ID: `109741`
- Entry ID: `135999`
- Definition ID: `140754`
- Spell ID: `1265959`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Pillar of Frost summons forth Trollbane for $s1 sec.][Dark Transformation summons forth Whitemane for $s2 sec.]
- Effect: $?c2[Pillar of Frost summons forth Trollbane for $s1 sec.][Dark Transformation summons forth Whitemane for $s2 sec.]
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Whitemane's Famine
- Node ID: `95047`
- Entry ID: `117644`
- Definition ID: `122656`
- Spell ID: `444033`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When $?a137006[Obliterate or Frostscythe]?s207311[Clawing Shadows][Scourge Strike] damages an enemy affected by Undeath it gains $s1 $Lstack:stacks; and infects another nearby enemy.
- Effect: When $?a137006[Obliterate or Frostscythe]?s207311[Clawing Shadows][Scourge Strike] damages an enemy affected by Undeath it gains $s1 $Lstack:stacks; and infects another nearby enemy.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95060` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nazgrim's Conquest
- Node ID: `95059`
- Entry ID: `117656`
- Definition ID: `122668`
- Spell ID: `444052`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If an enemy dies while Nazgrim is active, the strength of Apocalyptic Conquest is increased by $s1%.

Additionally, each Rune you spend increase its value by $s2%.
- Effect: If an enemy dies while Nazgrim is active, the strength of Apocalyptic Conquest is increased by $s1%.

Additionally, each Rune you spend increase its value by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Trollbane's Icy Fury
- Node ID: `95063`
- Entry ID: `117660`
- Definition ID: `122672`
- Spell ID: `444097`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137006[Obliterate and Frostscythe]?s207311[Clawing Shadows][Scourge Strike] $?a137006[shatter][shatters] Trollbane's Chains of Ice when hit, dealing $444834s2 Shadowfrost damage to nearby enemies, and slowing them by $444834s1% for $444834d. Deals reduced damage beyond $s1 targets.
- Effect: $?a137006[Obliterate and Frostscythe]?s207311[Clawing Shadows][Scourge Strike] $?a137006[shatter][shatters] Trollbane's Chains of Ice when hit, dealing $444834s2 Shadowfrost damage to nearby enemies, and slowing them by $444834s1% for $444834d. Deals reduced damage beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95037` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Let Terror Reign
- Node ID: `109740`
- Entry ID: `135998`
- Definition ID: `140753`
- Spell ID: `1265949`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Casting Obliterate or Frostscythe orders Trollbane to cast his Obliterate or Frostscythe alongside you at $s1% effectiveness.][Casting Death Coil or Epidemic orders Whitemane to cast her Death Coil or Epidemic alongside you at $s2% effectiveness.]
- Effect: $?c2[Casting Obliterate or Frostscythe orders Trollbane to cast his Obliterate or Frostscythe alongside you at $s1% effectiveness.][Casting Death Coil or Epidemic orders Whitemane to cast her Death Coil or Epidemic alongside you at $s2% effectiveness.]
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109741` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hungering Thirst
- Node ID: `95044`
- Entry ID: `117641`
- Definition ID: `122653`
- Spell ID: `444037`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The damage of your diseases and $?a137006[Frost Strike][Death Coil] are increased by $s1%.
- Effect: The damage of your diseases and $?a137006[Frost Strike][Death Coil] are increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95047` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fury of the Horsemen
- Node ID: `95042`
- Entry ID: `117639`
- Definition ID: `122651`
- Spell ID: `444069`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 Runic Power you spend extends the duration of the Horsemen's aid in combat by $s3 sec, up to $s2 sec.
- Effect: Every $s1 Runic Power you spend extends the duration of the Horsemen's aid in combat by $s3 sec, up to $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95059` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### A Feast of Souls
- Node ID: `95042`
- Entry ID: `123411`
- Definition ID: `128249`
- Spell ID: `444072`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: While you have $s1 or more Horsemen aiding you, your $?c2[Runic Power spending abilities deal $440861s1%]?c3[Death Coil deals $440861s1% and Epidemic deals $440861s3%][] increased damage.
- Effect: While you have $s1 or more Horsemen aiding you, your $?c2[Runic Power spending abilities deal $440861s1%]?c3[Death Coil deals $440861s1% and Epidemic deals $440861s3%][] increased damage.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95059` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mawsworn Menace
- Node ID: `95054`
- Entry ID: `117651`
- Definition ID: `122663`
- Spell ID: `444099`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137006[Obliterate deals $s4]?s207311[Clawing Shadows deals $s3][Scourge Strike deals $s3]% increased damage and $?s152280[the cooldown of your Defile is reduced by ${$s2/-1000}]?a137006[your Remorseless Winter lasts ${$s5/1000} sec longer][the cooldown of your Death and Decay is reduced by ${$s1/-1000} sec].
- Effect: $?a137006[Obliterate deals $s4]?s207311[Clawing Shadows deals $s3][Scourge Strike deals $s3]% increased damage and $?s152280[the cooldown of your Defile is reduced by ${$s2/-1000}]?a137006[your Remorseless Winter lasts ${$s5/1000} sec longer][the cooldown of your Death and Decay is reduced by ${$s1/-1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95063` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unholy Armaments
- Node ID: `109739`
- Entry ID: `135997`
- Definition ID: `140752`
- Spell ID: `1265971`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The abilities that Horsemen cast deal $s1% increased damage.$?c3[

Your Ghoul and skeletal archer deals $s3% and Lesser Ghouls deal $s5% increased damage][].
- Effect: The abilities that Horsemen cast deal $s1% increased damage.$?c3[

Your Ghoul and skeletal archer deals $s3% and Lesser Ghouls deal $s5% increased damage][].
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109740` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Apocalypse Now
- Node ID: `95041`
- Entry ID: `117638`
- Definition ID: `122650`
- Spell ID: `444040`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Army of the Dead and Frostwyrm's Fury call upon all 4 Horsemen to aid you for ${$s2/1000} sec.
- Effect: Army of the Dead and Frostwyrm's Fury call upon all 4 Horsemen to aid you for ${$s2/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95042` (type `2`), node `95044` (type `2`), node `95054` (type `2`), node `109739` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
