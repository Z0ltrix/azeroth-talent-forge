# Blood

Reviewed build: `12.1.0.69404`
Spec ID: `250`
Role: `0`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Death Strike
- Node ID: `76071`
- Entry ID: `96200`
- Definition ID: `101202`
- Spell ID: `49998`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Focuses dark power into a strike$?s137006[ with both weapons, that deals a total of ${$s1+$66188s1}][ that deals $s1] Physical damage and heals you for ${$s2}.2% of all damage taken in the last $s4 sec, minimum ${$s3}.1% of maximum health.
- Effect: Focuses dark power into a strike$?s137006[ with both weapons, that deals a total of ${$s1+$66188s1}][ that deals $s1] Physical damage and heals you for ${$s2}.2% of all damage taken in the last $s4 sec, minimum ${$s3}.1% of maximum health.
- Point cost per purchased rank: `1` × Specialization pool (Blood, Frost, Unholy) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
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
### Wave of Souls
- Node ID: `95036`
- Entry ID: `117633`
- Definition ID: `122645`
- Spell ID: `439851`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaper's Mark sends forth bursts of Shadowfrost energy and back, dealing $?a137008[$435802s1][$435802s2] Shadowfrost damage both ways to all enemies caught in its path.

Wave of Souls critical strikes cause enemies to take $443404s1% increased Shadowfrost damage for $443404d, stacking up to 2 times, and it is always a critical strike on its way back.
- Effect: Reaper's Mark sends forth bursts of Shadowfrost energy and back, dealing $?a137008[$435802s1][$435802s2] Shadowfrost damage both ways to all enemies caught in its path.

Wave of Souls critical strikes cause enemies to take $443404s1% increased Shadowfrost damage for $443404d, stacking up to 2 times, and it is always a critical strike on its way back.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wither Away
- Node ID: `95058`
- Entry ID: `117655`
- Definition ID: `122667`
- Spell ID: `441894`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Blood Plague][Frost Fever] deals its damage $?a137008[$s5]?a134735[$s7][$s6]% faster, and the second scythe of Exterminate applies $?a137008[Blood Plague][Frost Fever].
- Effect: $?a137008[Blood Plague][Frost Fever] deals its damage $?a137008[$s5]?a134735[$s7][$s6]% faster, and the second scythe of Exterminate applies $?a137008[Blood Plague][Frost Fever].
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bind in Darkness
- Node ID: `95043`
- Entry ID: `117640`
- Definition ID: `122652`
- Spell ID: `440031`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Blood Boil deals $s3% increased damage][Rime empowered Howling Blast deals $s4% increased damage to its main target], and is now Shadowfrost.

Shadowfrost damage applies 2 stacks to Reaper's Mark and 4 stacks when it is a critical strike.
- Effect: $?a137008[Blood Boil deals $s3% increased damage][Rime empowered Howling Blast deals $s4% increased damage to its main target], and is now Shadowfrost.

Shadowfrost damage applies 2 stacks to Reaper's Mark and 4 stacks when it is a critical strike.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frigid Resolve
- Node ID: `109735`
- Entry ID: `135993`
- Definition ID: `140748`
- Spell ID: `1265859`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The effectiveness of Permafrost is increased by $?c1[$s1][$s2]%$?c1[ and Exterminate grants Permafrost equal to $s3% of the damage dealt.]?c2[.][]

$@spellicon207200$@spellname207200
$@spelldesc207200
- Effect: The effectiveness of Permafrost is increased by $?c1[$s1][$s2]%$?c1[ and Exterminate grants Permafrost equal to $s3% of the damage dealt.]?c2[.][]

$@spellicon207200$@spellname207200
$@spelldesc207200
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
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
### Soul Rupture
- Node ID: `95061`
- Entry ID: `117658`
- Definition ID: `122670`
- Spell ID: `437161`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Reaper's Mark explodes, it deals $?a137008[$s1][$s2]% of the damage dealt to nearby enemies.
- Effect: When Reaper's Mark explodes, it deals $?a137008[$s1][$s2]% of the damage dealt to nearby enemies.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95036` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Grim Reaper
- Node ID: `95034`
- Entry ID: `117631`
- Definition ID: `122643`
- Spell ID: `434905`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaper's Mark initial strike grants $?a137008][$s3 charges of Bone Shield][Killing Machine].

Reaper's Mark explosion deals up to $s1% increased damage based on your target's missing health.
- Effect: Reaper's Mark initial strike grants $?a137008][$s3 charges of Bone Shield][Killing Machine].

Reaper's Mark explosion deals up to $s1% increased damage based on your target's missing health.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95058` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pact of the Deathbringer
- Node ID: `95035`
- Entry ID: `117632`
- Definition ID: `122644`
- Spell ID: `440476`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you suffer a damaging effect equal to $s1% of your maximum health, you instantly cast Death Pact at $s3% effectiveness. May only occur every $s2 min.

When a Reaper's Mark explodes, the cooldowns of this effect and Death Pact are reduced by $s4 sec.
- Effect: When you suffer a damaging effect equal to $s1% of your maximum health, you instantly cast Death Pact at $s3% effectiveness. May only occur every $s2 min.

When a Reaper's Mark explodes, the cooldowns of this effect and Death Pact are reduced by $s4 sec.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95043` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rune Carved Plates
- Node ID: `95035`
- Entry ID: `123420`
- Definition ID: `128258`
- Spell ID: `440282`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Each Rune spent reduces the magic damage you take by ${$abs($440290s1/10)}.1% and each Rune generated reduces the physical damage you take by ${$abs($440289s1/10)}.1% for $440289d, up to $440290u times.
- Effect: Each Rune spent reduces the magic damage you take by ${$abs($440290s1/10)}.1% and each Rune generated reduces the physical damage you take by ${$abs($440289s1/10)}.1% for $440289d, up to $440290u times.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95043` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deathly Blows
- Node ID: `109734`
- Entry ID: `135992`
- Definition ID: `140747`
- Spell ID: `1265932`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Frost Strike damage is increased by $s1% and Glacial Advance damage is increased by $s2%.

Reaper's Mark grants $s4 charges of Bonegrinder if it is known.]?c1[Death Strike damage increased by $s3%.][]
- Effect: $?c2[Frost Strike damage is increased by $s1% and Glacial Advance damage is increased by $s2%.

Reaper's Mark grants $s4 charges of Bonegrinder if it is known.]?c1[Death Strike damage increased by $s3%.][]
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109735` (type `2`)
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
### Swift and Painful
- Node ID: `95032`
- Entry ID: `117629`
- Definition ID: `122641`
- Spell ID: `443560`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If no enemies are struck by Soul Rupture, you gain $469169s1% Strength for $469169d.

Wave of Souls is $s2% more effective on the main target of your Reaper's Mark.
- Effect: If no enemies are struck by Soul Rupture, you gain $469169s1% Strength for $469169d.

Wave of Souls is $s2% more effective on the main target of your Reaper's Mark.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95061` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Talons
- Node ID: `95057`
- Entry ID: `117654`
- Definition ID: `122666`
- Spell ID: `436687`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Marrowrend and Heart Strike have][Consuming Killing Machine or Rime has] a $s1% chance to grant $s2 stacks of Icy Talons and increase its maximum stacks by the same amount for 6 sec.

Runic Power spending abilities count as Shadowfrost while Icy Talons is active.
- Effect: $?a137008[Marrowrend and Heart Strike have][Consuming Killing Machine or Rime has] a $s1% chance to grant $s2 stacks of Icy Talons and increase its maximum stacks by the same amount for 6 sec.

Runic Power spending abilities count as Shadowfrost while Icy Talons is active.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95034` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reaper's Onslaught
- Node ID: `95057`
- Entry ID: `128266`
- Definition ID: `133073`
- Spell ID: `469870`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Reaper's Mark by ${$s1/-1000} sec, but the amount of $?a137008[Marrowrends][Obliterates and Frostscythes] empowered by Exterminate is reduced by $s2.
- Effect: Reduces the cooldown of Reaper's Mark by ${$s1/-1000} sec, but the amount of $?a137008[Marrowrends][Obliterates and Frostscythes] empowered by Exterminate is reduced by $s2.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95034` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death's Messenger
- Node ID: `95049`
- Entry ID: `117646`
- Definition ID: `122658`
- Spell ID: `437122`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldowns of Lichborne and Raise Dead by ${$s1/-1000} sec.
- Effect: Reduces the cooldowns of Lichborne and Raise Dead by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95035` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expelling Shield
- Node ID: `95049`
- Entry ID: `128234`
- Definition ID: `133041`
- Spell ID: `439948`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When an enemy deals direct damage to your Anti-Magic Shell, their cast speed is reduced by $440739s1% for $440739d.
- Effect: When an enemy deals direct damage to your Anti-Magic Shell, their cast speed is reduced by $440739s1% for $440739d.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95035` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echoing Fury
- Node ID: `109733`
- Entry ID: `135991`
- Definition ID: `140746`
- Spell ID: `1265855`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaper's Mark deals $s7% increased damage.

Casting $?c1?[Dancing Rune Weapon][Reaper's Mark] grants $?c1?[$s4][$s1] $Lstack:stacks; of Exterminate with $?c1?[$s5][$s2]% first scythe and $?c1?[$s6][$s3]% second scythe effectiveness.
- Effect: Reaper's Mark deals $s7% increased damage.

Casting $?c1?[Dancing Rune Weapon][Reaper's Mark] grants $?c1?[$s4][$s1] $Lstack:stacks; of Exterminate with $?c1?[$s5][$s2]% first scythe and $?c1?[$s6][$s3]% second scythe effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109734` (type `2`)
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
### Exterminate
- Node ID: `95068`
- Entry ID: `117665`
- Definition ID: `122677`
- Spell ID: `441378`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After Reaper's Mark explodes, your next $s3 $?a137008[$LMarrowrend:Marrowrends;][$LObliterate:Obliterates; or $LFrostscythe:Frostscythes;] cost $s4 $LRune:Runes; and summon $s1 $Lscythe:scythes; to strike your enemies.

The first scythe strikes your target for $?a137008[$441424s1][$441424s2] Shadowfrost damage $?c2[and has a $s6% chance to grant Killing Machine,][and] the second scythe strikes all enemies around your target for $?a137008[$441426s1][$441426s2] Shadowfrost damage$?(a441894&a137008)[ and applies Blood Plague]?(a441894&$a137006)[ and applies Frost Fever][]. Deals reduced damage beyond $s5 targets.
- Effect: After Reaper's Mark explodes, your next $s3 $?a137008[$LMarrowrend:Marrowrends;][$LObliterate:Obliterates; or $LFrostscythe:Frostscythes;] cost $s4 $LRune:Runes; and summon $s1 $Lscythe:scythes; to strike your enemies.

The first scythe strikes your target for $?a137008[$441424s1][$441424s2] Shadowfrost damage $?c2[and has a $s6% chance to grant Killing Machine,][and] the second scythe strikes all enemies around your target for $?a137008[$441426s1][$441426s2] Shadowfrost damage$?(a441894&a137008)[ and applies Blood Plague]?(a441894&$a137006)[ and applies Frost Fever][]. Deals reduced damage beyond $s5 targets.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95032` (type `2`), node `95049` (type `2`), node `95057` (type `2`), node `109733` (type `2`)
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
