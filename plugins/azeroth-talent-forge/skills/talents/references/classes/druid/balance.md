# Balance

Reviewed build: `12.1.0.69404`
Spec ID: `102`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Starfire
- Node ID: `82201`
- Entry ID: `103279`
- Definition ID: `108284`
- Spell ID: `194153`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Call down a burst of energy, causing $s1 Arcane damage to the target, and $?a429523[${($m1*$m3/100)/(1+$429523s1/100)}][${$m1*$m3/100}] Arcane damage to all other enemies within $A1 yards. Deals reduced damage beyond $s5 targets.

|cFFFFFFFFGenerates ${$m2/10} Astral Power.|r
- Effect: Call down a burst of energy, causing $s1 Arcane damage to the target, and $?a429523[${($m1*$m3/100)/(1+$429523s1/100)}][${$m1*$m3/100}] Arcane damage to all other enemies within $A1 yards. Deals reduced damage beyond $s5 targets.

|cFFFFFFFFGenerates ${$m2/10} Astral Power.|r
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Thriving Growth
- Node ID: `94626`
- Entry ID: `117226`
- Definition ID: `122238`
- Spell ID: `439528`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Rip and Rake damage has a chance to cause Bloodseeker Vines to grow on the victim, dealing $439531o1 Bleed damage over $439531d.

$?a137011[Wild Growth and Regrowth][Wild Growth, Regrowth, and Efflorescence] healing has a chance to cause Symbiotic Blooms to grow on the target, healing for $439530o1 over $439530d.

Multiple instances of these can overlap.
- Effect: Rip and Rake damage has a chance to cause Bloodseeker Vines to grow on the victim, dealing $439531o1 Bleed damage over $439531d.

$?a137011[Wild Growth and Regrowth][Wild Growth, Regrowth, and Efflorescence] healing has a chance to cause Symbiotic Blooms to grow on the target, healing for $439530o1 over $439530d.

Multiple instances of these can overlap.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Starsurge
- Node ID: `82202`
- Entry ID: `103280`
- Definition ID: `108285`
- Spell ID: `78674`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Launch a surge of stellar energies at the target, dealing $s1 Astral damage.
- Effect: Launch a surge of stellar energies at the target, dealing $s1 Astral damage.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82201` (type `2`)
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
### Remove Corruption
- Node ID: `82241`
- Entry ID: `103320`
- Definition ID: `108325`
- Spell ID: `2782`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Nullifies corrupting effects on the friendly target, removing all Curse and Poison effects.
- Effect: Nullifies corrupting effects on the friendly target, removing all Curse and Poison effects.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1` | source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `82217` (type `2`), node `82219` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moonkin Form
- Node ID: `82208`
- Entry ID: `103286`
- Definition ID: `108291`
- Spell ID: `24858`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shapeshift into $?s114301[Astral Form][Moonkin Form], increasing the damage of your spells by $s9% and your armor by $m3%, and granting protection from Polymorph effects.$?a231042[

While in this form, single-target attacks against you have a $h% chance to make your next Starfire instant.][]

The act of shapeshifting frees you from movement impairing effects.
- Effect: Shapeshift into $?s114301[Astral Form][Moonkin Form], increasing the damage of your spells by $s9% and your armor by $m3%, and granting protection from Polymorph effects.$?a231042[

While in this form, single-target attacks against you have a $h% chance to make your next Starfire instant.][]

The act of shapeshifting frees you from movement impairing effects.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82201` (type `2`), node `91044` (type `2`)
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
### Light of the Sun
- Node ID: `104083`
- Entry ID: `128588`
- Definition ID: `133391`
- Spell ID: `202918`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the remaining cooldown on Solar Beam by $m1 sec when it interrupts the primary target.
- Effect: Reduces the remaining cooldown on Solar Beam by $m1 sec when it interrupts the primary target.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `104085` (type `2`)
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
### Dream Surge
- Node ID: `94600`
- Entry ID: `117195`
- Definition ID: `122207`
- Spell ID: `433831`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Force of Nature grants $s1 charges of Dream Burst, causing your next Wrath or Starfire to explode on the target, dealing ${$433850s1*(1+$393014s3/100)} Nature damage to nearby enemies. Damage reduced above $433850s2 targets.][When Grove Guardians are summoned, they grow Dream Petals on your target, healing up to $s2 nearby allies for $434141s1.]
- Effect: $?a137013[Force of Nature grants $s1 charges of Dream Burst, causing your next Wrath or Starfire to explode on the target, dealing ${$433850s1*(1+$393014s3/100)} Nature damage to nearby enemies. Damage reduced above $433850s2 targets.][When Grove Guardians are summoned, they grow Dream Petals on your target, healing up to $s2 nearby allies for $434141s1.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Treants of the Moon
- Node ID: `94599`
- Entry ID: `117194`
- Definition ID: `122206`
- Spell ID: `428544`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?a137013[Force of Nature treants][Grove Guardians] cast Moonfire on nearby targets about once every $s1 sec.
- Effect: Your $?a137013[Force of Nature treants][Grove Guardians] cast Moonfire on nearby targets about once every $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ravage
- Node ID: `94609`
- Entry ID: `117206`
- Definition ID: `122218`
- Spell ID: `441583`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto-attacks have a chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.

$?a137010[$@spellicon441605|cFFFFFFFF$@spellname441605|r
$@spelldesc441605]$?a137011[$@spellicon441591|cFFFFFFFF$@spellname441591|r
$@spelldesc441591]
- Effect: Your auto-attacks have a chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.

$?a137010[$@spellicon441605|cFFFFFFFF$@spellname441605|r
$@spelldesc441605]$?a137011[$@spellicon441591|cFFFFFFFF$@spellname441591|r
$@spelldesc441591]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expansiveness
- Node ID: `94602`
- Entry ID: `117197`
- Definition ID: `122209`
- Spell ID: `429399`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your maximum mana is increased by $s2%$?a137013[ and your maximum Astral Power is increased by ${$s1/10}][].
- Effect: Your maximum mana is increased by $s2%$?a137013[ and your maximum Astral Power is increased by ${$s1/10}][].
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sylvan Beckoning
- Node ID: `109714`
- Entry ID: `135972`
- Definition ID: `140727`
- Spell ID: `1264614`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Entering an Eclipse summons a Dryad to assist you for $1264618d, casting Starsurge dealing $1264677s1 Astral damage and Starfall at $s2% effectiveness.][Your periodic heals have a chance to empower your next Swiftmend to summon a Dryad to assist you, casting Tranquility at $s1% effectiveness and Regrowth to heal $1264664s1 damage onto your lowest health ally.]
- Effect: $?c1[Entering an Eclipse summons a Dryad to assist you for $1264618d, casting Starsurge dealing $1264677s1 Astral damage and Starfall at $s2% effectiveness.][Your periodic heals have a chance to empower your next Swiftmend to summon a Dryad to assist you, casting Tranquility at $s1% effectiveness and Regrowth to heal $1264664s1 damage onto your lowest health ally.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Protective Growth
- Node ID: `94593`
- Entry ID: `117186`
- Definition ID: `122198`
- Spell ID: `433748`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Regrowth protects you, reducing damage you take by $s1% while your Regrowth is on you.
- Effect: Your Regrowth protects you, reducing damage you take by $s1% while your Regrowth is on you.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dryad's Dance
- Node ID: `109713`
- Entry ID: `135971`
- Definition ID: `140726`
- Spell ID: `1264776`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c4[Dryads cause Swiftmend to cool down $1264618s3% faster.][Dryads cause most of your Astral power generation to be increased by $1264618s4%.]
- Effect: $?c4[Dryads cause Swiftmend to cool down $1264618s3% faster.][Dryads cause most of your Astral power generation to be increased by $1264618s4%.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109714` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Power of Nature
- Node ID: `94605`
- Entry ID: `117201`
- Definition ID: `122213`
- Spell ID: `428859`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Your Force of Nature treants no longer taunt and deal $449001s1% increased melee damage.][Your Grove Guardians increase the healing of your Rejuvenation, Efflorescence, and Lifebloom by $428866s1% while active.]
- Effect: $?a137013[Your Force of Nature treants no longer taunt and deal $449001s1% increased melee damage.][Your Grove Guardians increase the healing of your Rejuvenation, Efflorescence, and Lifebloom by $428866s1% while active.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94599` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Durability of Nature
- Node ID: `94605`
- Entry ID: `117200`
- Definition ID: `122212`
- Spell ID: `429227`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Your Force of Nature treants have $s1% increased health.][Grove Guardians last $s2% longer.]
- Effect: $?c1[Your Force of Nature treants have $s1% increased health.][Grove Guardians last $s2% longer.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94599` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cenarius' Might
- Node ID: `94604`
- Entry ID: `117199`
- Definition ID: `122211`
- Spell ID: `455797`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Entering Eclipse increases your haste by $455801s1% for $455801d][Swiftmend healing is increased by $s2%].
- Effect: $?a137013[Entering Eclipse increases your haste by $455801s1% for $455801d][Swiftmend healing is increased by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94602` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Grove's Inspiration
- Node ID: `94595`
- Entry ID: `117189`
- Definition ID: `122201`
- Spell ID: `429402`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Wrath and Starfire damage increased by $s1%. 

Regrowth$?a137013[ and Wild Growth][, Wild Growth, and Swiftmend] healing increased by $s2%.
- Effect: Wrath and Starfire damage increased by $s1%. 

Regrowth$?a137013[ and Wild Growth][, Wild Growth, and Swiftmend] healing increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94593` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Potent Enchantments
- Node ID: `94595`
- Entry ID: `117188`
- Definition ID: `122200`
- Spell ID: `429420`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Orbital Strike damage increased by $s3%, and damage of Stellar Flares it applies increased by $s2%.

Whirling Stars increases the haste you gain during ][]$?c1&s394013[Incarnation: Chosen of Elune]?c1[Celestial Alignment][]$?c1[ by an additional $s4%.][Reforestation grants Tree of Life for $s5 additional sec.]
- Effect: $?c1[Orbital Strike damage increased by $s3%, and damage of Stellar Flares it applies increased by $s2%.

Whirling Stars increases the haste you gain during ][]$?c1&s394013[Incarnation: Chosen of Elune]?c1[Celestial Alignment][]$?c1[ by an additional $s4%.][Reforestation grants Tree of Life for $s5 additional sec.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94593` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spirit of the Thicket
- Node ID: `109712`
- Entry ID: `135970`
- Definition ID: `140725`
- Spell ID: `1264899`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c4[Ironbark summons a Dryad to channel a beam of pure nature onto your target, healing them for $1264905o1 over $1264905d.][Your Starfall damage is increased by $s1% and your Starsurge damage is increased by $s2%.]
- Effect: $?c4[Ironbark summons a Dryad to channel a beam of pure nature onto your target, healing them for $1264905o1 over $1264905d.][Your Starfall damage is increased by $s1% and your Starsurge damage is increased by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109713` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bounteous Bloom
- Node ID: `94591`
- Entry ID: `117184`
- Definition ID: `122196`
- Spell ID: `429215`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Force of Nature Treants last ${$s2/1000} sec longer.][Your Grove Guardians' healing is increased by $s1%.]
- Effect: $?a137013[Force of Nature Treants last ${$s2/1000} sec longer.][Your Grove Guardians' healing is increased by $s1%.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94605` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Early Spring
- Node ID: `94591`
- Entry ID: `117895`
- Definition ID: `122907`
- Spell ID: `428937`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137013[Force of Nature cooldown reduced by ${$s1/-1000} sec.][Swiftmend and Wild Growth cooldowns reduced by ${$s2/-1000} sec.]
- Effect: $?a137013[Force of Nature cooldown reduced by ${$s1/-1000} sec.][Swiftmend and Wild Growth cooldowns reduced by ${$s2/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94605` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Power of the Dream
- Node ID: `94592`
- Entry ID: `117185`
- Definition ID: `122197`
- Spell ID: `434220`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Force of Nature grants an additional stack of Dream Burst.][Dream Surge heals $s2 additional $Lally:allies;.]
- Effect: $?a137013[Force of Nature grants an additional stack of Dream Burst.][Dream Surge heals $s2 additional $Lally:allies;.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94604` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Control of the Dream
- Node ID: `94592`
- Entry ID: `117894`
- Definition ID: `122906`
- Spell ID: `434249`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Time elapsed while your major abilities are available to be used or at maximum charges is subtracted from that ability's cooldown after the next time you use it, up to $s1 seconds.

Affects $?a137012[Nature's Swiftness, Incarnation: Tree of Life,][Force of Nature,] $?a137012[]?a394013[Incarnation: Chosen of Elune, ][Celestial Alignment, ]and Convoke the Spirits.
- Effect: Time elapsed while your major abilities are available to be used or at maximum charges is subtracted from that ability's cooldown after the next time you use it, up to $s1 seconds.

Affects $?a137012[Nature's Swiftness, Incarnation: Tree of Life,][Force of Nature,] $?a137012[]?a394013[Incarnation: Chosen of Elune, ][Celestial Alignment, ]and Convoke the Spirits.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94604` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blooming Infusion
- Node ID: `94601`
- Entry ID: `117196`
- Definition ID: `122208`
- Spell ID: `429433`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 Regrowths you cast makes your next Wrath, Starfire, or Entangling Roots instant and increases damage it deals by $429474s2%.

Every $s1 Starsurges $?a137013[or Starfalls ][]you cast makes your next Regrowth or Entangling roots instant.
- Effect: Every $s1 Regrowths you cast makes your next Wrath, Starfire, or Entangling Roots instant and increases damage it deals by $429474s2%.

Every $s1 Starsurges $?a137013[or Starfalls ][]you cast makes your next Regrowth or Entangling roots instant.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94595` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Harmony of the Grove
- Node ID: `94606`
- Entry ID: `117203`
- Definition ID: `122215`
- Spell ID: `428731`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Each of your Force of Nature treants increases damage your spells deal by $428735s1% while active.][Each of your Grove Guardians increases your healing done by $428737s1% while active.]
- Effect: $?a137013[Each of your Force of Nature treants increases damage your spells deal by $428735s1% while active.][Each of your Grove Guardians increases your healing done by $428737s1% while active.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94591` (type `2`), node `94592` (type `2`), node `94601` (type `2`), node `109712` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
