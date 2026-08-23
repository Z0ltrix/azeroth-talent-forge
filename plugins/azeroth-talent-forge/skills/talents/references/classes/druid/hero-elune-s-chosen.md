# Elune's Chosen

Reviewed build: `12.1.0.69404`
Hero subtree ID: `24`
Description: Elune's Chosen dedicate themselves to the Moon Goddess and are granted her connection to the moon and stars. Their abilities are infused with astral might and they can call down potent lunar magics.

## Hero talents

### Boundless Moonlight
- Node ID: `94608`
- Entry ID: `117205`
- Definition ID: `122217`
- Spell ID: `424058`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137010[$@spellicon204066 $@spellname204066
Lunar Beam now causes you to leech life equal to $425217s1% of all damage dealt to enemies within the beam.

$@spellicon202770 $@spellname202770
Fury of Elune now ends with a flash of energy, blasting nearby enemies for $428682s1 Astral damage.]

[$@spellicon202770 $@spellname202770
Fury of Elune now ends with a flash of energy, blasting nearby enemies for $428682s1 Astral damage.

$@spellicon274283 $@spellname274283
$@spelldesc424588]
- Effect: $?a137010[$@spellicon204066 $@spellname204066
Lunar Beam now causes you to leech life equal to $425217s1% of all damage dealt to enemies within the beam.

$@spellicon202770 $@spellname202770
Fury of Elune now ends with a flash of energy, blasting nearby enemies for $428682s1 Astral damage.]

[$@spellicon202770 $@spellname202770
Fury of Elune now ends with a flash of energy, blasting nearby enemies for $428682s1 Astral damage.

$@spellicon274283 $@spellname274283
$@spelldesc424588]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moon Guardian
- Node ID: `94598`
- Entry ID: `117193`
- Definition ID: `122205`
- Spell ID: `429520`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Moonfire and Starfire generate ${$s1/10} additional Astral Power.][Free automatic Moonfires from Galactic Guardian generate ${$430581s1/10} Rage.]
- Effect: $?a137013[Moonfire and Starfire generate ${$s1/10} additional Astral Power.][Free automatic Moonfires from Galactic Guardian generate ${$430581s1/10} Rage.]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94608` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lunar Insight
- Node ID: `94588`
- Entry ID: `117181`
- Definition ID: `122193`
- Spell ID: `429530`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Moonfire deals $s1% increased damage.$?a137010[

Red Moon deals $s3% increased damage.][]
- Effect: Moonfire deals $s1% increased damage.$?a137010[

Red Moon deals $s3% increased damage.][]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94608` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Glistening Fur
- Node ID: `94594`
- Entry ID: `117769`
- Definition ID: `122781`
- Spell ID: `429533`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Bear Form and Moonkin Form reduce Arcane damage taken by $s2% and all other magic damage taken by $s1%.
- Effect: Bear Form and Moonkin Form reduce Arcane damage taken by $s2% and all other magic damage taken by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94608` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Star Cascade
- Node ID: `109720`
- Entry ID: `135978`
- Definition ID: `140733`
- Spell ID: `1271206`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Gaining Astral Power with Starfire][Thrash] has a $?c1[$s1][$s2]% chance to launch a Starsurge at a victim at $?c1[$s3][$s4]% effectiveness.
- Effect: $?c1[Gaining Astral Power with Starfire][Thrash] has a $?c1[$s1][$s2]% chance to launch a Starsurge at a victim at $?c1[$s3][$s4]% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94608` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stellar Command
- Node ID: `94596`
- Entry ID: `117190`
- Definition ID: `122202`
- Spell ID: `429668`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137013[Increases the damage of Fury of Elune by $s1% and the damage of Full Moon by $s2%.][Increases the damage of Lunar Beam by $s3% and Fury of Elune by $s1%.]
- Effect: $?a137013[Increases the damage of Fury of Elune by $s1% and the damage of Full Moon by $s2%.][Increases the damage of Lunar Beam by $s3% and Fury of Elune by $s1%.]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94598` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Atmospheric Exposure
- Node ID: `94607`
- Entry ID: `117204`
- Definition ID: `122216`
- Spell ID: `429532`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies damaged by $?a137013[Full Moon or Fury of Elune][Lunar Beam or Fury of Elune] take $430589s1% increased damage from you for $430589d.
- Effect: Enemies damaged by $?a137013[Full Moon or Fury of Elune][Lunar Beam or Fury of Elune] take $430589s1% increased damage from you for $430589d.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94588` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moondust
- Node ID: `94597`
- Entry ID: `117192`
- Definition ID: `122204`
- Spell ID: `429538`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies affected by Moonfire are slowed by $164812s8%.
- Effect: Enemies affected by Moonfire are slowed by $164812s8%.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94594` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elune's Grace
- Node ID: `94597`
- Entry ID: `123304`
- Definition ID: `128177`
- Spell ID: `443046`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Using Wild Charge while in Bear Form or Moonkin Form incurs a $s1 sec shorter cooldown.
- Effect: Using Wild Charge while in Bear Form or Moonkin Form incurs a $s1 sec shorter cooldown.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94594` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Penumbral Swell
- Node ID: `109719`
- Entry ID: `135977`
- Definition ID: `140732`
- Spell ID: `1271261`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Lunar Eclipse increases Arcane damage by an additional $s1%][
Lunar Beam increases Arcane damage you deal by $204066s6% while it is active].
- Effect: $?c1[Lunar Eclipse increases Arcane damage by an additional $s1%][
Lunar Beam increases Arcane damage you deal by $204066s6% while it is active].
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109720` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lunar Calling
- Node ID: `94590`
- Entry ID: `117183`
- Definition ID: `122195`
- Spell ID: `429523`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Starfire deals $s1% increased damage to its primary target.

Wrath no longer changes your Eclipse ability's mode to Solar Eclipse.][Thrash now deals Arcane damage and its damage is increased by $s2%.]
- Effect: $?a137013[Starfire deals $s1% increased damage to its primary target.

Wrath no longer changes your Eclipse ability's mode to Solar Eclipse.][Thrash now deals Arcane damage and its damage is increased by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94596` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### The Light of Elune
- Node ID: `94585`
- Entry ID: `117176`
- Definition ID: `122188`
- Spell ID: `428655`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Moonfire damage has a chance to call down a Fury of Elune to follow your target for ${$s2/1000} sec.

$@spellicon202770 $@spellname202770
Calls down a beam of pure celestial energy, dealing $<dmg> Astral damage over ${$s2/1000} sec within its area.

|cFFFFFFFFGenerates $?a137010[${$202770m4/$202770t4*$s2/10000} Rage][${$202770m3/$202770t3*$s2/10000} Astral Power] over its duration.|r
- Effect: Moonfire damage has a chance to call down a Fury of Elune to follow your target for ${$s2/1000} sec.

$@spellicon202770 $@spellname202770
Calls down a beam of pure celestial energy, dealing $<dmg> Astral damage over ${$s2/1000} sec within its area.

|cFFFFFFFFGenerates $?a137010[${$202770m4/$202770t4*$s2/10000} Rage][${$202770m3/$202770t3*$s2/10000} Astral Power] over its duration.|r
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94607` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Astral Insight
- Node ID: `94585`
- Entry ID: `117772`
- Definition ID: `122784`
- Spell ID: `429536`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137013[Incarnation: Chosen of Elune][Incarnation: Guardian of Ursoc] increases Arcane damage from spells and abilities by $102560s6% while active.

Increases the duration and number of spells cast by Convoke the Spirits by $s1%.
- Effect: $?a137013[Incarnation: Chosen of Elune][Incarnation: Guardian of Ursoc] increases Arcane damage from spells and abilities by $102560s6% while active.

Increases the duration and number of spells cast by Convoke the Spirits by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94607` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arcane Affinity
- Node ID: `94586`
- Entry ID: `117178`
- Definition ID: `122190`
- Spell ID: `429540`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: All Arcane damage from your spells and abilities is increased by $s1%.
- Effect: All Arcane damage from your spells and abilities is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94597` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lunation
- Node ID: `94586`
- Entry ID: `117177`
- Definition ID: `122189`
- Spell ID: `429539`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137013[Your Arcane abilities reduce the cooldown of Fury of Elune by ${$s1/-1000}.1 sec and the cooldown of New Moon, Half Moon, and Full Moon by ${$s2/-1000}.1 sec.][Lunar Beam's cooldown is reduced by ${-$s3/1000} sec.]
- Effect: $?a137013[Your Arcane abilities reduce the cooldown of Fury of Elune by ${$s1/-1000}.1 sec and the cooldown of New Moon, Half Moon, and Full Moon by ${$s2/-1000}.1 sec.][Lunar Beam's cooldown is reduced by ${-$s3/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94597` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bask in Moonlight
- Node ID: `109718`
- Entry ID: `135976`
- Definition ID: `140731`
- Spell ID: `1271305`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Starsurge damage increased by $s1%. 
Starfall damage increased by $s2%.]?s400254[Raze][Maul] $?c3[damage increased by $s3%. Lunar Beam's damage dealt to its primary target increased by $s4%.][]
- Effect: $?c1[Starsurge damage increased by $s1%. 
Starfall damage increased by $s2%.]?s400254[Raze][Maul] $?c3[damage increased by $s3%. Lunar Beam's damage dealt to its primary target increased by $s4%.][]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109719` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### The Eternal Moon
- Node ID: `94587`
- Entry ID: `117179`
- Definition ID: `122191`
- Spell ID: `424113`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Further increases the power of Boundless Moonlight.

$?a137010[$@spellicon204066 $@spellname204066
Lunar Beam increases Mastery by an additional ${$s5*$mas}%, deals $s6% increased damage, and lasts ${$s3/1000} sec longer.

$@spellicon202770 $@spellname202770
The flash of energy now generates  ${$428682s3/10} Rage and its damage is increased by $s1%.][$@spellicon202770 $@spellname202770
The flash of energy now generates ${$428682s2/10} Astral Power and its damage is increased by $s1%.

$@spellicon274283 $@spellname274283
New Moon and Half Moon now also call down $s2 Minor $LMoon:Moons;.]
- Effect: Further increases the power of Boundless Moonlight.

$?a137010[$@spellicon204066 $@spellname204066
Lunar Beam increases Mastery by an additional ${$s5*$mas}%, deals $s6% increased damage, and lasts ${$s3/1000} sec longer.

$@spellicon202770 $@spellname202770
The flash of energy now generates  ${$428682s3/10} Rage and its damage is increased by $s1%.][$@spellicon202770 $@spellname202770
The flash of energy now generates ${$428682s2/10} Astral Power and its damage is increased by $s1%.

$@spellicon274283 $@spellname274283
New Moon and Half Moon now also call down $s2 Minor $LMoon:Moons;.]
- Point cost per purchased rank: `1` × Hero pool (Elune's Chosen) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94585` (type `2`), node `94586` (type `2`), node `94590` (type `2`), node `109718` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
