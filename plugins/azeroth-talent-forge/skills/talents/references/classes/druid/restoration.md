# Restoration

Reviewed build: `12.1.0.69404`
Spec ID: `105`
Role: `1`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Rejuvenation
- Node ID: `82217`
- Entry ID: `103295`
- Definition ID: `108300`
- Spell ID: `774`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals the target for $o1 over $d.$?s155675[

You can apply Rejuvenation twice to the same target.][]$?s33891[

|C0033AA11Tree of Life: Healing increased by $5420s5% and Mana cost reduced by $5420s4%.|R][]
- Effect: Heals the target for $o1 over $d.$?s155675[

You can apply Rejuvenation twice to the same target.][]$?s33891[

|C0033AA11Tree of Life: Healing increased by $5420s5% and Mana cost reduced by $5420s4%.|R][]
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
### Hunt Beneath the Open Skies
- Node ID: `94629`
- Entry ID: `117231`
- Definition ID: `122243`
- Spell ID: `439868`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage and healing while in Cat Form increased by $s1%.

Moonfire and Sunfire damage increased by $s4%.
- Effect: Damage and healing while in Cat Form increased by $s1%.

Moonfire and Sunfire damage increased by $s4%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94626` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wildstalker's Power
- Node ID: `94621`
- Entry ID: `117221`
- Definition ID: `122233`
- Spell ID: `439926`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Rip and Ferocious Bite damage increased by $s1%.

Rejuvenation$?a137012[, Efflorescence, and Lifebloom][] healing increased by $s3%.
- Effect: Rip and Ferocious Bite damage increased by $s1%.

Rejuvenation$?a137012[, Efflorescence, and Lifebloom][] healing increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94626` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wild Growth
- Node ID: `82205`
- Entry ID: `103283`
- Definition ID: `108288`
- Spell ID: `48438`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals up to $s2 injured allies within $A1 yards of the target for $o1 over $d. Healing starts high and declines over the duration.$?s33891[

|C0033AA11Tree of Life: Affects $33891s3 additional $ltarget:targets;.|R][]
- Effect: Heals up to $s2 injured allies within $A1 yards of the target for $o1 over $d. Healing starts high and declines over the duration.$?s33891[

|C0033AA11Tree of Life: Affects $33891s3 additional $ltarget:targets;.|R][]
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82217` (type `2`)
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
### Green Thumb
- Node ID: `109717`
- Entry ID: `135975`
- Definition ID: `140730`
- Spell ID: `1270565`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The rate at which $?c2[Bloodseeker Vines][Symbiotic Blooms] grow is increased by $?c2[$s1][$s2]%.
- Effect: The rate at which $?c2[Bloodseeker Vines][Symbiotic Blooms] grow is increased by $?c2[$s1][$s2]%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94626` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Strategic Infusion
- Node ID: `94623`
- Entry ID: `117223`
- Definition ID: `122235`
- Spell ID: `439890`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137011[Tiger's Fury and attacking from Prowl increase][Attacking from Prowl increases] the chance for Shred, Rake, and $?s202028[Brutal Slash][Swipe] to critically strike by $439891s1% for $439891d.

Your periodic heals have a $s1% increased chance to critically heal.
- Effect: $?a137011[Tiger's Fury and attacking from Prowl increase][Attacking from Prowl increases] the chance for Shred, Rake, and $?s202028[Brutal Slash][Swipe] to critically strike by $439891s1% for $439891d.

Your periodic heals have a $s1% increased chance to critically heal.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94626` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bond with Nature
- Node ID: `94625`
- Entry ID: `117225`
- Definition ID: `122237`
- Spell ID: `439929`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing you receive is increased by $s1%.
- Effect: Healing you receive is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94621` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Harmonious Constitution
- Node ID: `94625`
- Entry ID: `119854`
- Definition ID: `124754`
- Spell ID: `440116`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your Regrowth's healing to yourself is increased by $s1%.
- Effect: Your Regrowth's healing to yourself is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94621` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lethal Preservation
- Node ID: `94624`
- Entry ID: `117224`
- Definition ID: `122236`
- Spell ID: `455461`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you remove an effect with Soothe or $?s88423[Nature's Cure][Remove Corruption], gain a combo point and heal for $s1% of your maximum health. If you are at full health an injured party or raid member will be healed instead.
- Effect: When you remove an effect with Soothe or $?s88423[Nature's Cure][Remove Corruption], gain a combo point and heal for $s1% of your maximum health. If you are at full health an injured party or raid member will be healed instead.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94629` (type `2`)
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
### Improved Nature's Cure
- Node ID: `104084`
- Entry ID: `128590`
- Definition ID: `133393`
- Spell ID: `392378`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Nature's Cure additionally removes all Curse and Poison effects.
- Effect: Nature's Cure additionally removes all Curse and Poison effects.
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1`
- Incoming edges: node `82217` (type `2`), node `82219` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bursting Growth
- Node ID: `109716`
- Entry ID: `135974`
- Definition ID: `140729`
- Spell ID: `440120`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Bloodseeker Vines expire or you use Ferocious Bite on their target they explode in thorns, dealing $440122s1 physical damage to nearby enemies. Damage reduced above 5 targets.

When Symbiotic Blooms expire or you cast Rejuvenation on their target flowers grow around their target, healing them and up to $440121s2 nearby allies for $440121s1.
- Effect: When Bloodseeker Vines expire or you use Ferocious Bite on their target they explode in thorns, dealing $440122s1 physical damage to nearby enemies. Damage reduced above 5 targets.

When Symbiotic Blooms expire or you cast Rejuvenation on their target flowers grow around their target, healing them and up to $440121s2 nearby allies for $440121s1.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109717` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Entangling Vortex
- Node ID: `94622`
- Entry ID: `117222`
- Definition ID: `122234`
- Spell ID: `439895`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies pulled into Ursol's Vortex are rooted in place for ${$s1/1000} sec. Damage may cancel the effect.
- Effect: Enemies pulled into Ursol's Vortex are rooted in place for ${$s1/1000} sec. Damage may cancel the effect.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94623` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flower Walk
- Node ID: `94622`
- Entry ID: `119855`
- Definition ID: `124755`
- Spell ID: `439901`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: During Barkskin your movement speed is increased by $s1% and every second flowers grow beneath your feet that heal up to $439902s2 nearby injured allies for $439902s1.
- Effect: During Barkskin your movement speed is increased by $s1% and every second flowers grow beneath your feet that heal up to $439902s2 nearby injured allies for $439902s1.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94623` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twin Sprouts
- Node ID: `94628`
- Entry ID: `117230`
- Definition ID: `122242`
- Spell ID: `440117`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Bloodseeker Vines or Symbiotic Blooms grow, they have a $s1% chance to cause another growth of the same type to immediately grow on a valid nearby target.
- Effect: When Bloodseeker Vines or Symbiotic Blooms grow, they have a $s1% chance to cause another growth of the same type to immediately grow on a valid nearby target.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94625` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Implant
- Node ID: `94628`
- Entry ID: `117229`
- Definition ID: `122241`
- Spell ID: `440118`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137011[When you gain or lose Tiger's Fury, your next single-target melee ability causes a Bloodseeker Vine to grow on the target for ${$s1/1000} sec.][Casting Swiftmend or Wild Growth causes a Symbiotic Bloom to grow on a target for ${$s2/1000} sec.]
- Effect: $?a137011[When you gain or lose Tiger's Fury, your next single-target melee ability causes a Bloodseeker Vine to grow on the target for ${$s1/1000} sec.][Casting Swiftmend or Wild Growth causes a Symbiotic Bloom to grow on a target for ${$s2/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94625` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Resilient Flourishing
- Node ID: `94631`
- Entry ID: `117234`
- Definition ID: `122246`
- Spell ID: `439880`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Bloodseeker Vines and Symbiotic Blooms last ${$s1/1000} additional sec.

When a target afflicted by Bloodseeker Vines dies, the vines jump to a valid nearby target for their remaining duration.
- Effect: Bloodseeker Vines and Symbiotic Blooms last ${$s1/1000} additional sec.

When a target afflicted by Bloodseeker Vines dies, the vines jump to a valid nearby target for their remaining duration.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94624` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Root Network
- Node ID: `94631`
- Entry ID: `117233`
- Definition ID: `122245`
- Spell ID: `439882`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Each active Bloodseeker Vine increases the damage your abilities deal by 2%.

Each active Symbiotic Bloom increases the healing of your spells by 2%.
- Effect: Each active Bloodseeker Vine increases the damage your abilities deal by 2%.

Each active Symbiotic Bloom increases the healing of your spells by 2%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94624` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Patient Custodian
- Node ID: `94630`
- Entry ID: `117232`
- Definition ID: `122244`
- Spell ID: `1270592`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?c2[Bleeds and other damage over time][heal over time] effects are $?c2[$s1][$s3]% more effective.
- Effect: Your $?c2[Bleeds and other damage over time][heal over time] effects are $?c2[$s1][$s3]% more effective.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94622` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rampancy
- Node ID: `109715`
- Entry ID: `135973`
- Definition ID: `140728`
- Spell ID: `1270586`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Bloodseeker Vines][Symbiotic Blooms] have a $?c2[$s1][$s2]% chance to trigger Bursting Growth every 2 sec at $?c2[$s3][$s4]% effectiveness.
- Effect: $?c2[Bloodseeker Vines][Symbiotic Blooms] have a $?c2[$s1][$s2]% chance to trigger Bursting Growth every 2 sec at $?c2[$s3][$s4]% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109716` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Vigorous Creepers
- Node ID: `94627`
- Entry ID: `117227`
- Definition ID: `122239`
- Spell ID: `440119`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Bloodseeker Vines increase the damage your abilities deal to affected enemies by $s1%.

Symbiotic Blooms increase the healing your spells do to affected targets by $s2%.
- Effect: Bloodseeker Vines increase the damage your abilities deal to affected enemies by $s1%.

Symbiotic Blooms increase the healing your spells do to affected targets by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Wildstalker) (ID `2989`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94628` (type `2`), node `94630` (type `2`), node `94631` (type `2`), node `109715` (type `2`)
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
