# Guardian

Reviewed build: `12.1.0.69404`
Spec ID: `104`
Role: `0`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Frenzied Regeneration
- Node ID: `82220`
- Entry ID: `103298`
- Definition ID: `108303`
- Spell ID: `22842`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals you for $o1% health over $d$?s301768[, and increases healing received by $301768s1%][].
- Effect: Heals you for $o1% health over $d$?s301768[, and increases healing received by $301768s1%][].
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Starfire
- Node ID: `91044`
- Entry ID: `112967`
- Definition ID: `117972`
- Spell ID: `197628`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Call down a burst of energy, causing $s1 Arcane damage to the target, and ${$m1*$194153m3/100} Arcane damage to all other enemies within $A1 yards. Deals reduced damage beyond $s3 targets.
- Effect: Call down a burst of energy, causing $s1 Arcane damage to the target, and ${$m1*$194153m3/100} Arcane damage to all other enemies within $A1 yards. Deals reduced damage beyond $s3 targets.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `node`; type `1` | source `node`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Starfire
- Node ID: `91046`
- Entry ID: `112969`
- Definition ID: `117974`
- Spell ID: `197628`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Call down a burst of energy, causing $s1 Arcane damage to the target, and ${$m1*$194153m3/100} Arcane damage to all other enemies within $A1 yards. Deals reduced damage beyond $s3 targets.
- Effect: Call down a burst of energy, causing $s1 Arcane damage to the target, and ${$m1*$194153m3/100} Arcane damage to all other enemies within $A1 yards. Deals reduced damage beyond $s3 targets.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `node`; type `1`
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
### Swipe
- Node ID: `82223`
- Entry ID: `103301`
- Definition ID: `108306`
- Spell ID: `213764`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Swipe nearby enemies, inflicting Physical damage. Damage varies by shapeshift form.$?s137011[

|cFFFFFFFFAwards $s1 combo $lpoint:points;.|r][]
- Effect: Swipe nearby enemies, inflicting Physical damage. Damage varies by shapeshift form.$?s137011[

|cFFFFFFFFAwards $s1 combo $lpoint:points;.|r][]
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82199` (type `2`), node `82220` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Starsurge
- Node ID: `82200`
- Entry ID: `103278`
- Definition ID: `108283`
- Spell ID: `197626`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Launch a surge of stellar energies at the target, dealing $s1 Astral damage.
- Effect: Launch a surge of stellar energies at the target, dealing $s1 Astral damage.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `91044` (type `2`)
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
### Verdant Heart
- Node ID: `82218`
- Entry ID: `103296`
- Definition ID: `108301`
- Spell ID: `301768`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Frenzied Regeneration and Barkskin increase all healing received by $s1%.
- Effect: Frenzied Regeneration and Barkskin increase all healing received by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82219` (type `2`), node `82220` (type `2`), node `82223` (type `2`)
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
### Skull Bash
- Node ID: `82242`
- Entry ID: `103322`
- Definition ID: `108327`
- Spell ID: `106839`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You charge and bash the target's skull, interrupting spellcasting and preventing any spell in that school from being cast for $93985d.
- Effect: You charge and bash the target's skull, interrupting spellcasting and preventing any spell in that school from being cast for $93985d.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1` | source `node`; type `1`
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
### Fount of Strength
- Node ID: `94618`
- Entry ID: `117218`
- Definition ID: `122230`
- Spell ID: `441675`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your maximum Energy and Rage are increased by $s1.

Frenzied Regeneration also increases your maximum health by $s3%.
- Effect: Your maximum Energy and Rage are increased by $s1.

Frenzied Regeneration also increases your maximum health by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dreadful Wound
- Node ID: `94620`
- Entry ID: `117220`
- Definition ID: `122232`
- Spell ID: `441809`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ravage also inflicts a Bleed that causes $?a137011[$441812s1][$451177s1] damage over $441812d and saps its victims' strength, reducing damage they deal to you by $?a137011[$441812s2][$451177s2]%.

Dreadful Wound is not affected by Circle of Life and Death. $?a137011[If a Dreadful Wound benefiting from Tiger's Fury is re-applied, the new Dreadful Wound deals damage as if Tiger's Fury was active.][]
- Effect: Ravage also inflicts a Bleed that causes $?a137011[$441812s1][$451177s1] damage over $441812d and saps its victims' strength, reducing damage they deal to you by $?a137011[$441812s2][$451177s2]%.

Dreadful Wound is not affected by Circle of Life and Death. $?a137011[If a Dreadful Wound benefiting from Tiger's Fury is re-applied, the new Dreadful Wound deals damage as if Tiger's Fury was active.][]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bestial Strength
- Node ID: `94611`
- Entry ID: `117208`
- Definition ID: `122220`
- Spell ID: `441841`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137011[Ferocious Bite and Rampant Ferocity damage increased by $s1% and Primal Wrath's direct damage increased by $s2%.][Maul and Raze damage increased by $s3%.]
- Effect: $?a137011[Ferocious Bite and Rampant Ferocity damage increased by $s1% and Primal Wrath's direct damage increased by $s2%.][Maul and Raze damage increased by $s3%.]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Limb from Limb
- Node ID: `109722`
- Entry ID: `135980`
- Definition ID: `140735`
- Spell ID: `1271540`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto-attacks are 30% more likely to make your next $?c2[Ferocious Bite]?s400254[Raze][Maul] become Ravage.
- Effect: Your auto-attacks are 30% more likely to make your next $?c2[Ferocious Bite]?s400254[Raze][Maul] become Ravage.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wildshape Mastery
- Node ID: `94610`
- Entry ID: `117207`
- Definition ID: `122219`
- Spell ID: `441678`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ironfur and Frenzied Regeneration persist in Cat Form.$?!c3[

When transforming from Bear to Cat Form, you retain $441685s1% of your Bear Form armor and health for $441685d.][]

For $441686d after entering Bear Form, you heal for $441686s1% of damage taken over $441688d.
- Effect: Ironfur and Frenzied Regeneration persist in Cat Form.$?!c3[

When transforming from Bear to Cat Form, you retain $441685s1% of your Bear Form armor and health for $441685d.][]

For $441686d after entering Bear Form, you heal for $441686s1% of damage taken over $441688d.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94618` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pack's Endurance
- Node ID: `94615`
- Entry ID: `117215`
- Definition ID: `122227`
- Spell ID: `441844`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stampeding Roar's duration is increased by $s1%.
- Effect: Stampeding Roar's duration is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94611` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ruthless Aggression
- Node ID: `109723`
- Entry ID: `135981`
- Definition ID: `140736`
- Spell ID: `441814`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ravage increases your auto-attack speed by $441817s1% for $441817d.
- Effect: Ravage increases your auto-attack speed by $441817s1% for $441817d.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109722` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Killing Strikes
- Node ID: `109723`
- Entry ID: `136624`
- Definition ID: `141396`
- Spell ID: `441824`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Ravage increases your Agility by $441825s1% and the armor granted by Ironfur by $441825s2% for $441825d.

Your first $?a137011[Tiger's Fury][Mangle] after entering combat makes your next $?a137011[Ferocious Bite][Maul] become Ravage.
- Effect: Ravage increases your Agility by $441825s1% and the armor granted by Ironfur by $441825s2% for $441825d.

Your first $?a137011[Tiger's Fury][Mangle] after entering combat makes your next $?a137011[Ferocious Bite][Maul] become Ravage.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109722` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Exacerbating Wounds
- Node ID: `94619`
- Entry ID: `117219`
- Definition ID: `122231`
- Spell ID: `1271839`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Dreadful Wounds increase the damage afflicted enemies take from your Bleed damage over time effects by $?c2[$s2][$s3]%.
- Effect: Your Dreadful Wounds increase the damage afflicted enemies take from your Bleed damage over time effects by $?c2[$s2][$s3]%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94620` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Strike for the Heart
- Node ID: `94614`
- Entry ID: `117214`
- Definition ID: `122226`
- Spell ID: `441845`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Shred, Swipe, and Rake damage increased by $s1% and their critical strike chance is increased by $s3%.][Mangle damage increased by $s4% and its critical strike chance is increased by $s5%.]

$?c3[Mangle heals you for $458724s1% of maximum health.][]
- Effect: $?c2[Shred, Swipe, and Rake damage increased by $s1% and their critical strike chance is increased by $s3%.][Mangle damage increased by $s4% and its critical strike chance is increased by $s5%.]

$?c3[Mangle heals you for $458724s1% of maximum health.][]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94615` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tear Down the Mighty
- Node ID: `94614`
- Entry ID: `117213`
- Definition ID: `122225`
- Spell ID: `441846`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c2[Damage dealt by Chomp and ][]$?(c2&!s1243807)[Feral Frenzy]?c2[Frantic Frenzy][]$?c2[ increased by $s2%][The cooldown of Sundering Roar is reduced by ${$s1/-1000} sec].
- Effect: $?c2[Damage dealt by Chomp and ][]$?(c2&!s1243807)[Feral Frenzy]?c2[Frantic Frenzy][]$?c2[ increased by $s2%][The cooldown of Sundering Roar is reduced by ${$s1/-1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94615` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Empowered Shapeshifting
- Node ID: `94612`
- Entry ID: `117210`
- Definition ID: `122222`
- Spell ID: `441689`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Frenzied Regeneration can be cast in Cat Form for $s2 Energy.

Bear Form reduces magic damage you take by ${-$s4}%.

Shred and $?s202028[Brutal Slash][Swipe] damage increased by $s5%. Mangle damage increased by $s6%.
- Effect: Frenzied Regeneration can be cast in Cat Form for $s2 Energy.

Bear Form reduces magic damage you take by ${-$s4}%.

Shred and $?s202028[Brutal Slash][Swipe] damage increased by $s5%. Mangle damage increased by $s6%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wildpower Surge
- Node ID: `94612`
- Entry ID: `117209`
- Definition ID: `122221`
- Spell ID: `441691`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?s202028[Shred and Brutal Slash]?a137011[Shred and Swipe][]$?a137011[ grant Ursine Potential. When you have $441695s1 stacks, the next time you transform into Bear Form, your next Mangle deals $441698s1% increased damage or your next Swipe deals $441698s2% increased damage. Either generates ${$442562s1/10} extra Rage.][Mangle grants Feline Potential. When you have $441701s1 stacks, the next time you transform into Cat Form, gain $441704s1 combo points and your next Ferocious Bite or Rip deals $441702s1% increased damage for its full duration.]
- Effect: $?s202028[Shred and Brutal Slash]?a137011[Shred and Swipe][]$?a137011[ grant Ursine Potential. When you have $441695s1 stacks, the next time you transform into Bear Form, your next Mangle deals $441698s1% increased damage or your next Swipe deals $441698s2% increased damage. Either generates ${$442562s1/10} extra Rage.][Mangle grants Feline Potential. When you have $441701s1 stacks, the next time you transform into Cat Form, gain $441704s1 combo points and your next Ferocious Bite or Rip deals $441702s1% increased damage for its full duration.]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aggravate Wounds
- Node ID: `94616`
- Entry ID: `117216`
- Definition ID: `122228`
- Spell ID: `441829`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $?a137010[Maul, Raze, Mangle,  Thrash, or Swipe]$?a137011[attack with an Energy cost that] you cast extends the duration of your Dreadful Wounds by $?a137010[${$s1/1000}.1][${$s2/1000}.1] sec, up to $s3 additional sec.
- Effect: Every $?a137010[Maul, Raze, Mangle,  Thrash, or Swipe]$?a137011[attack with an Energy cost that] you cast extends the duration of your Dreadful Wounds by $?a137010[${$s1/1000}.1][${$s2/1000}.1] sec, up to $s3 additional sec.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94619` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twin Claw
- Node ID: `109721`
- Entry ID: `135979`
- Definition ID: `140734`
- Spell ID: `1271635`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You have a $?c2[$s1][$s2]% chance to follow up any single target melee ability$?c3[ or Raze][] with a Twin Claw, dealing $?c2[$1271636s1][$1271657s1] Physical damage and generating $?c2[$1271636s2 Energy][${$1271657s2/10} Rage].
- Effect: You have a $?c2[$s1][$s2]% chance to follow up any single target melee ability$?c3[ or Raze][] with a Twin Claw, dealing $?c2[$1271636s1][$1271657s1] Physical damage and generating $?c2[$1271636s2 Energy][${$1271657s2/10} Rage].
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109723` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Claw Rampage
- Node ID: `94613`
- Entry ID: `117211`
- Definition ID: `122223`
- Spell ID: `441835`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: During Berserk, $?c3[Mangle, Thrash][Shred], and $?s202028[Brutal Slash][Swipe] have a $s1% chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.
- Effect: During Berserk, $?c3[Mangle, Thrash][Shred], and $?s202028[Brutal Slash][Swipe] have a $s1% chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94612` (type `2`), node `94614` (type `2`), node `94616` (type `2`), node `109721` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
