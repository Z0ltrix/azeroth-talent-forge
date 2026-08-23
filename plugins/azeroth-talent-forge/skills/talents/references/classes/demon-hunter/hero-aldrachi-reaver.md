# Aldrachi Reaver

Reviewed build: `12.1.0.69404`
Hero subtree ID: `35`
Description: The Aldrachi warriors were the ultimate glaivemasters and wielded their blades with deadly grace, consuming souls and imbuing their weapons with greater power.

## Hero talents

### Art of the Glaive
- Node ID: `94915`
- Entry ID: `117512`
- Definition ID: `122524`
- Spell ID: `442290`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming $?a212612[$s1][$s2] Soul Fragments or casting $?a212612[The Hunt][Sigil of Spite] converts your next Throw Glaive into Reaver's Glaive.

$@spellicon442294 $@spellname442294: 
$@spelldesc442294
- Effect: Consuming $?a212612[$s1][$s2] Soul Fragments or casting $?a212612[The Hunt][Sigil of Spite] converts your next Throw Glaive into Reaver's Glaive.

$@spellicon442294 $@spellname442294: 
$@spelldesc442294
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fury of the Aldrachi
- Node ID: `94898`
- Entry ID: `117495`
- Definition ID: `122519`
- Spell ID: `442718`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When enhanced by Reaver's Glaive, $?a212612[Blade Dance][Soul Cleave] casts $s2 additional glaive slashes to nearby targets. Deals reduced damage beyond $444806s2 targets.

If cast after $?a212612[Chaos Strike]?s263642[Fracture][Shear], cast $?a1236360[${($s2*($s1/100+1))+$1236360s1}][${$s2*($s1/100+1)}] slashes instead.
- Effect: When enhanced by Reaver's Glaive, $?a212612[Blade Dance][Soul Cleave] casts $s2 additional glaive slashes to nearby targets. Deals reduced damage beyond $444806s2 targets.

If cast after $?a212612[Chaos Strike]?s263642[Fracture][Shear], cast $?a1236360[${($s2*($s1/100+1))+$1236360s1}][${$s2*($s1/100+1)}] slashes instead.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94915` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Evasive Action
- Node ID: `94911`
- Entry ID: `117508`
- Definition ID: `122520`
- Spell ID: `444926`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vengeful Retreat can be cast a second time within $444929d.
- Effect: Vengeful Retreat can be cast a second time within $444929d.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94915` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unhindered Assault
- Node ID: `94911`
- Entry ID: `123047`
- Definition ID: `127928`
- Spell ID: `444931`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Vengeful Retreat resets the cooldown of Felblade.
- Effect: Vengeful Retreat resets the cooldown of Felblade.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94915` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reaver's Mark
- Node ID: `94903`
- Entry ID: `117500`
- Definition ID: `122512`
- Spell ID: `442679`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When enhanced by Reaver's Glaive, $?a212612[Chaos Strike]?s263642[Fracture][Shear] applies Reaver's Mark, which causes the target to take $442624s1% increased damage for $442624d. Max $442624u stacks.

Applies $m2 additional $Lstack:stacks; of Reaver's Mark If cast after $?a212612[Blade Dance][Soul Cleave].
- Effect: When enhanced by Reaver's Glaive, $?a212612[Chaos Strike]?s263642[Fracture][Shear] applies Reaver's Mark, which causes the target to take $442624s1% increased damage for $442624d. Max $442624u stacks.

Applies $m2 additional $Lstack:stacks; of Reaver's Mark If cast after $?a212612[Blade Dance][Soul Cleave].
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94915` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Broken Spirit
- Node ID: `109771`
- Entry ID: `136029`
- Definition ID: `140784`
- Spell ID: `1272143`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212613[Sigil of Spite][The Hunt] shatters $?a212613[$s1 additional][$s2] Soul $LFragment:Fragments;. $?a212613[Soul Cleave has][Blade Dance and Chaos Strike have] a $?a212613[$s3][$s4]% chance to shatter a Soul Fragment.
- Effect: $?a212613[Sigil of Spite][The Hunt] shatters $?a212613[$s1 additional][$s2] Soul $LFragment:Fragments;. $?a212613[Soul Cleave has][Blade Dance and Chaos Strike have] a $?a212613[$s3][$s4]% chance to shatter a Soul Fragment.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94915` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aldrachi Tactics
- Node ID: `94914`
- Entry ID: `117511`
- Definition ID: `122523`
- Spell ID: `442683`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The second enhanced ability in a pattern shatters an additional Soul Fragment.
- Effect: The second enhanced ability in a pattern shatters an additional Soul Fragment.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94898` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Army Unto Oneself
- Node ID: `94896`
- Entry ID: `117493`
- Definition ID: `122505`
- Spell ID: `442714`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Felblade surrounds you with a Blade Ward, reducing damage taken by $442715s1% for $442715d.
- Effect: Felblade surrounds you with a Blade Ward, reducing damage taken by $442715s1% for $442715d.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94911` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Incorruptible Spirit
- Node ID: `94896`
- Entry ID: `123046`
- Definition ID: `127927`
- Spell ID: `442736`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Each Soul Fragment you consume shields you for an additional $s1% of the amount healed.
- Effect: Each Soul Fragment you consume shields you for an additional $s1% of the amount healed.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94911` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wounded Quarry
- Node ID: `94897`
- Entry ID: `117494`
- Definition ID: `122506`
- Spell ID: `442806`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Expose weaknesses in the target of your $@spellname442624, causing your Physical damage to any enemy to also deal $s1% of the damage dealt to your marked target as Chaos, and sometimes shatter a Soul Fragment.
- Effect: Expose weaknesses in the target of your $@spellname442624, causing your Physical damage to any enemy to also deal $s1% of the damage dealt to your marked target as Chaos, and sometimes shatter a Soul Fragment.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94903` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Keen Edge
- Node ID: `109770`
- Entry ID: `136028`
- Definition ID: `140783`
- Spell ID: `1272138`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaver's Glaive damage is increased by $s1% and other Physical-only damage is increased by $s2%.
- Effect: Reaver's Glaive damage is increased by $s1% and other Physical-only damage is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109771` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Incisive Blade
- Node ID: `94895`
- Entry ID: `117492`
- Definition ID: `122504`
- Spell ID: `442492`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Chaos Strike][Soul Cleave] deals $s1% increased damage.
- Effect: $?a212612[Chaos Strike][Soul Cleave] deals $s1% increased damage.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94914` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Keen Engagement
- Node ID: `94910`
- Entry ID: `117507`
- Definition ID: `122507`
- Spell ID: `442497`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaver's Glaive generates $s1 Fury.
- Effect: Reaver's Glaive generates $s1 Fury.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94896` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Preemptive Strike
- Node ID: `94910`
- Entry ID: `122422`
- Definition ID: `127322`
- Spell ID: `444997`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Throw Glaive deals $444979s1 Physical damage to enemies near its initial target.
- Effect: Throw Glaive deals $444979s1 Physical damage to enemies near its initial target.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94896` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bladecraft
- Node ID: `94906`
- Entry ID: `117503`
- Definition ID: `122515`
- Spell ID: `1272153`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fury of the Aldrachi further empowers $?a212613[Soul Cleave][Blade Dance] when cast after $?a212613[Fracture][Chaos Strike], increasing slashes to ${$442718s2*($442718s1/100+1)+$s1}.

Reaver's Mark now stacks up to $442624u times and further empowers $?a212613[Fracture][Chaos Strike] when cast after $?a212613[Soul Cleave][Blade Dance], applying an additional stack.
- Effect: Fury of the Aldrachi further empowers $?a212613[Soul Cleave][Blade Dance] when cast after $?a212613[Fracture][Chaos Strike], increasing slashes to ${$442718s2*($442718s1/100+1)+$s1}.

Reaver's Mark now stacks up to $442624u times and further empowers $?a212613[Fracture][Chaos Strike] when cast after $?a212613[Soul Cleave][Blade Dance], applying an additional stack.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94897` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Warblade's Hunger
- Node ID: `109769`
- Entry ID: `136027`
- Definition ID: `140782`
- Spell ID: `442502`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming a Soul Fragment causes your next $?a212612[Chaos Strike]?s263642[Fracture][Shear] to deal $442507s1 additional Physical damage.$?a212612[

Felblade consumes up to $s2 nearby Soul Fragments.][]
- Effect: Consuming a Soul Fragment causes your next $?a212612[Chaos Strike]?s263642[Fracture][Shear] to deal $442507s1 additional Physical damage.$?a212612[

Felblade consumes up to $s2 nearby Soul Fragments.][]
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109770` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thrill of the Fight
- Node ID: `94919`
- Entry ID: `117516`
- Definition ID: `122528`
- Spell ID: `442686`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After consuming both enhancements, gain Thrill of the Fight, increasing the damage of your next Reaver's Glaive by $442695s1% and increasing Haste by $442688s1% for $442688d.
- Effect: After consuming both enhancements, gain Thrill of the Fight, increasing the damage of your next Reaver's Glaive by $442695s1% and increasing Haste by $442688s1% for $442688d.
- Point cost per purchased rank: `1` × Hero pool (Aldrachi Reaver) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94895` (type `2`), node `94906` (type `2`), node `94910` (type `2`), node `109769` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
