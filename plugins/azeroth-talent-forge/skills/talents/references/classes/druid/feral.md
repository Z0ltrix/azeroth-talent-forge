# Feral

Reviewed build: `12.1.0.69404`
Spec ID: `103`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Rake
- Node ID: `82199`
- Entry ID: `103277`
- Definition ID: `108282`
- Spell ID: `1822`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Rake the target for $s1 Bleed damage and an additional $155722o1 Bleed damage over $155722d.$?s48484[ Reduces the target's movement speed by $58180s1% for $58180d.][]$?a231052[ 

While stealthed, Rake will also stun the target for $163505d and deal $s4% increased damage.][]$?a405834[ 

While stealthed, Rake will also stun the target for $163505d and deal $s4% increased damage.][]

|cFFFFFFFFAwards $s2 combo $lpoint:points;.|r
- Effect: Rake the target for $s1 Bleed damage and an additional $155722o1 Bleed damage over $155722d.$?s48484[ Reduces the target's movement speed by $58180s1% for $58180d.][]$?a231052[ 

While stealthed, Rake will also stun the target for $163505d and deal $s4% increased damage.][]$?a405834[ 

While stealthed, Rake will also stun the target for $163505d and deal $s4% increased damage.][]

|cFFFFFFFFAwards $s2 combo $lpoint:points;.|r
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
### Rip
- Node ID: `82222`
- Entry ID: `103300`
- Definition ID: `108305`
- Spell ID: `1079`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Finishing move that causes Bleed damage over time. Lasts longer per combo point.

   1 point  : ${$o1*2/6} over ${$d*2/6} sec
   2 points: ${$o1*3/6} over ${$d*3/6} sec
   3 points: ${$o1*4/6} over ${$d*4/6} sec
   4 points: ${$o1*5/6} over ${$d*5/6} sec
   5 points: ${$o1*6/6} over ${$d*6/6} sec
- Effect: Finishing move that causes Bleed damage over time. Lasts longer per combo point.

   1 point  : ${$o1*2/6} over ${$d*2/6} sec
   2 points: ${$o1*3/6} over ${$d*3/6} sec
   3 points: ${$o1*4/6} over ${$d*4/6} sec
   4 points: ${$o1*5/6} over ${$d*5/6} sec
   5 points: ${$o1*6/6} over ${$d*6/6} sec
- Point cost per purchased rank: `1` × Specialization pool (Balance, Feral, Guardian, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82199` (type `2`)
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
