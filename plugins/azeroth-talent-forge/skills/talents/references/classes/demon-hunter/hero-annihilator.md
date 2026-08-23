# Annihilator

Reviewed build: `12.1.0.69404`
Hero subtree ID: `124`
Description: An Annihilator draws upon the most fundamental forces of reality to erase from existence any enemies who would threaten the same. While their methods are often questioned, they are always needed when the fight arrives.

## Hero talents

### Voidfall
- Node ID: `109449`
- Entry ID: `135667`
- Definition ID: `140423`
- Spell ID: `1253304`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212613[Fracture][Consume] has a $s3% chance to grant $m1 $Lstack:stacks; of Voidfall.

Upon reaching $1256301u stacks of Voidfall, $?a212613[Soul Cleave][Reap] consumes a stack to reach into the Void and call down a meteor strike at your target's location, dealing $?a212613[$1256306s1 Shadowflame][$1256305s1 Cosmic] damage to all enemies within $1256306A yards. Damage reduced beyond $s2 targets.
- Effect: $?a212613[Fracture][Consume] has a $s3% chance to grant $m1 $Lstack:stacks; of Voidfall.

Upon reaching $1256301u stacks of Voidfall, $?a212613[Soul Cleave][Reap] consumes a stack to reach into the Void and call down a meteor strike at your target's location, dealing $?a212613[$1256306s1 Shadowflame][$1256305s1 Cosmic] damage to all enemies within $1256306A yards. Damage reduced beyond $s2 targets.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swift Erasure
- Node ID: `109454`
- Entry ID: `135672`
- Definition ID: `140428`
- Spell ID: `1253668`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each stack of Voidfall grants $s1% Haste.
- Effect: Each stack of Voidfall grants $s1% Haste.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109449` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Meteoric Rise
- Node ID: `109455`
- Entry ID: `135673`
- Definition ID: `140429`
- Spell ID: `1253377`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Fel Devastation][Void Ray] damage increased by $s1%.

$?c2[Fel Devastation][Fully channeling Void Ray] generates $?c2[$s4 Soul Fragments over its duration][$s3 $Lstack:stacks; of Voidfall].
- Effect: $?c2[Fel Devastation][Void Ray] damage increased by $s1%.

$?c2[Fel Devastation][Fully channeling Void Ray] generates $?c2[$s4 Soul Fragments over its duration][$s3 $Lstack:stacks; of Voidfall].
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109449` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Catastrophe
- Node ID: `109453`
- Entry ID: `135671`
- Definition ID: `140427`
- Spell ID: `1253769`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies struck by a Voidfall Meteor take an additional $?a212613[$s1%][$s2%] damage over $1256667d.
- Effect: Enemies struck by a Voidfall Meteor take an additional $?a212613[$s1%][$s2%] damage over $1256667d.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109449` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Phase Shift
- Node ID: `109452`
- Entry ID: `135670`
- Definition ID: `140426`
- Spell ID: `1256245`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each stack of Voidfall grants $s1% reduced damage taken.
- Effect: Each stack of Voidfall grants $s1% reduced damage taken.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109449` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Path to Oblivion
- Node ID: `109448`
- Entry ID: `135666`
- Definition ID: `140422`
- Spell ID: `1253399`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each stack of Voidfall grants $s1% increased movement speed.
- Effect: Each stack of Voidfall grants $s1% increased movement speed.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109454` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### State of Matter
- Node ID: `109448`
- Entry ID: `135659`
- Definition ID: `140415`
- Spell ID: `1253402`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a212613[Torment][Shift] has $m1 additional $Lcharge:charges;.
- Effect: $?a212613[Torment][Shift] has $m1 additional $Lcharge:charges;.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109454` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mass Acceleration
- Node ID: `109447`
- Entry ID: `135665`
- Definition ID: `140421`
- Spell ID: `1256295`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain $m1 $Lstack:stacks; of Voidfall $?a212613[and reset the cooldown of Spirit Bomb][and reset the cooldown of Reap] upon activating $?a212613[Metamorphosis][Void Metamorphosis].
- Effect: Gain $m1 $Lstack:stacks; of Voidfall $?a212613[and reset the cooldown of Spirit Bomb][and reset the cooldown of Reap] upon activating $?a212613[Metamorphosis][Void Metamorphosis].
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109455` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Doomsayer
- Node ID: `109450`
- Entry ID: `135668`
- Definition ID: `140424`
- Spell ID: `1253676`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating $?a212613[Infernal Strike][Void Ray] out of combat or within $?a1213636[${$1265768d*$s2} sec][$1265768d] of entering combat calls down $?a212613[$s3][$s1] Voidfall $LMeteor:Meteors;$?a212613[][ over its duration].
- Effect: Activating $?a212613[Infernal Strike][Void Ray] out of combat or within $?a1213636[${$1265768d*$s2} sec][$1265768d] of entering combat calls down $?a212613[$s3][$s1] Voidfall $LMeteor:Meteors;$?a212613[][ over its duration].
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109453` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Harness the Cosmos
- Node ID: `109450`
- Entry ID: `136810`
- Definition ID: `141573`
- Spell ID: `1279247`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Voidfall Meteor damage increased by $s1%.
- Effect: Voidfall Meteor damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109453` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Celestial Echoes
- Node ID: `109451`
- Entry ID: `135669`
- Definition ID: `140425`
- Spell ID: `1253415`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s263642[Fracture]?a212613[Shear][Consume] generates $?a212613[$s1][$s2] additional Fury and deals $?a212613[$s3%][$s4%] increased damage.
- Effect: $?s263642[Fracture]?a212613[Shear][Consume] generates $?a212613[$s1][$s2] additional Fury and deals $?a212613[$s3%][$s4%] increased damage.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109452` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Final Hour
- Node ID: `109445`
- Entry ID: `135663`
- Definition ID: `140419`
- Spell ID: `1253805`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Passive bonuses granted by each stack of Voidfall persist for $1256322d after being consumed.
- Effect: Passive bonuses granted by each stack of Voidfall persist for $1256322d after being consumed.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109448` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Meteoric Fall
- Node ID: `109446`
- Entry ID: `135664`
- Definition ID: `140420`
- Spell ID: `1253391`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While at $s1 stacks of Voidfall, $?c2[Spirit Bomb and Soul Cleave][Reap] consumes all $s1 to rapidly call down that many meteor strikes.
- Effect: While at $s1 stacks of Voidfall, $?c2[Spirit Bomb and Soul Cleave][Reap] consumes all $s1 to rapidly call down that many meteor strikes.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109447` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Matter
- Node ID: `109444`
- Entry ID: `135662`
- Definition ID: `140418`
- Spell ID: `1256307`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your first $?a212613[Spirit Bomb][Collapsing Star] after $?a212613[entering demon form][casting Void Metamorphosis] causes a $?a212613[Shadowflame][Cosmic] meteor shower to assault the area, dealing $?a212613[${$1264130s1*($s1)} Shadowflame][${$1264129s1*($s1)} Cosmic] damage over ${$s1/2} sec.
- Effect: Your first $?a212613[Spirit Bomb][Collapsing Star] after $?a212613[entering demon form][casting Void Metamorphosis] causes a $?a212613[Shadowflame][Cosmic] meteor shower to assault the area, dealing $?a212613[${$1264130s1*($s1)} Shadowflame][${$1264129s1*($s1)} Cosmic] damage over ${$s1/2} sec.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109450` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Otherworldly Focus
- Node ID: `109443`
- Entry ID: `135661`
- Definition ID: `140417`
- Spell ID: `1253817`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212613[Spirit Bomb][Collapsing Star] and Voidfall meteors deal $?a212613[$s1][$s3]% increased damage when striking a single target.

Each additional target reduces this bonus by $s2%.
- Effect: $?a212613[Spirit Bomb][Collapsing Star] and Voidfall meteors deal $?a212613[$s1][$s3]% increased damage when striking a single target.

Each additional target reduces this bonus by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109451` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### World Killer
- Node ID: `109442`
- Entry ID: `135660`
- Definition ID: `140416`
- Spell ID: `1256353`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The third Voidfall meteor strike called down in sequence is larger, has $s1% increased area, deals $s2% increased damage, and $?a212613[reduces the remaining cooldown of Metamorphosis by $s3 sec][generates $s4 Soul $LFragment:Fragments;].
- Effect: The third Voidfall meteor strike called down in sequence is larger, has $s1% increased area, deals $s2% increased damage, and $?a212613[reduces the remaining cooldown of Metamorphosis by $s3 sec][generates $s4 Soul $LFragment:Fragments;].
- Point cost per purchased rank: `1` × Hero pool (Annihilator) (ID `4185`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109443` (type `2`), node `109444` (type `2`), node `109445` (type `2`), node `109446` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
