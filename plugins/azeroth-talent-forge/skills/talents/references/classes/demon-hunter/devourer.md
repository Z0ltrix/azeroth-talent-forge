# Devourer

Reviewed build: `12.1.0.69404`
Spec ID: `1480`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

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
### Voidsurge
- Node ID: `110112`
- Entry ID: `136613`
- Definition ID: `141386`
- Spell ID: `452402`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[][Void ]Metamorphosis now also $?a212612[causes Demon Blades to generate $162264s10 additional Fury][greatly empowers Voidblade and Hungering Slash].

While demon form is active, the first cast of each empowered ability induces a $?a212612[Demonsurge][Voidsurge], causing you to explode with $?a212612[Fel][Void] energy, dealing $?a212612[$452416s1 Chaos][$1246160s1 Cosmic] damage to nearby enemies. Deals reduced damage beyond $452416s3 targets.
- Effect: $?a212612[][Void ]Metamorphosis now also $?a212612[causes Demon Blades to generate $162264s10 additional Fury][greatly empowers Voidblade and Hungering Slash].

While demon form is active, the first cast of each empowered ability induces a $?a212612[Demonsurge][Voidsurge], causing you to explode with $?a212612[Fel][Void] energy, dealing $?a212612[$452416s1 Chaos][$1246160s1 Cosmic] damage to nearby enemies. Deals reduced damage beyond $452416s3 targets.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voidblade
- Node ID: `108723`
- Entry ID: `134272`
- Definition ID: `139045`
- Spell ID: `1245412`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash your glaives and charge to your target, dealing $1245414s2 Cosmic damage.$?a1246562[

|CFFffffffGenerates $1245414s3 Fury.|R][]
- Effect: Unleash your glaives and charge to your target, dealing $1245414s2 Cosmic damage.$?a1246562[

|CFFffffffGenerates $1245414s3 Fury.|R][]
- Point cost per purchased rank: `1` × Specialization pool (Devourer, Havoc, Vengeance) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wave of Debilitation
- Node ID: `110114`
- Entry ID: `136621`
- Definition ID: `141394`
- Spell ID: `452403`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Chaos][Void] Nova slows enemies by $453263s1% and reduces attack and cast speed by $453263s2% for $453263d after its stun fades.
- Effect: $?c1[Chaos][Void] Nova slows enemies by $453263s1% and reduces attack and cast speed by $453263s2% for $453263d after its stun fades.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110112` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pursuit of Angriness
- Node ID: `110114`
- Entry ID: `136619`
- Definition ID: `141392`
- Spell ID: `452404`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Movement speed increased by $s1% per $s2 Fury.
- Effect: Movement speed increased by $s1% per $s2 Fury.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110112` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Focused Hatred
- Node ID: `110113`
- Entry ID: `136612`
- Definition ID: `141385`
- Spell ID: `452405`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Demonsurge][Voidsurge] deals $s1% increased damage when it strikes a single target.

Each additional target reduces this bonus by $s2%.
- Effect: $?a212612[Demonsurge][Voidsurge] deals $s1% increased damage when it strikes a single target.

Each additional target reduces this bonus by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110112` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Set Fire to the Pain
- Node ID: `110117`
- Entry ID: `136620`
- Definition ID: `141393`
- Spell ID: `452406`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $s2% of all non-Fire damage taken is instead taken as Fire damage over $453286d.

Fire damage taken reduced by $S3%.
- Effect: $s2% of all non-Fire damage taken is instead taken as Fire damage over $453286d.

Fire damage taken reduced by $S3%.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110112` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Soul Rending
- Node ID: `110117`
- Entry ID: `136618`
- Definition ID: `141391`
- Spell ID: `452407`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Leech granted by Soul Rending increased by $s1% and an additional $s2% while $?a212612[][Void ]Metamorphosis is active.
- Effect: Leech granted by Soul Rending increased by $s1% and an additional $s2% while $?a212612[][Void ]Metamorphosis is active.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110112` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blind Focus
- Node ID: `110105`
- Entry ID: `136607`
- Definition ID: `141380`
- Spell ID: `1272364`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Fire][Cosmic] damage increased by $?a212612[$s1][$s3]%.

Effect is doubled while in demon form.
- Effect: $?a212612[Fire][Cosmic] damage increased by $?a212612[$s1][$s3]%.

Effect is doubled while in demon form.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110112` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Burning Blades
- Node ID: `110111`
- Entry ID: `136610`
- Definition ID: `141383`
- Spell ID: `452408`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Your blades burn with Fel energy, causing the damage from Chaos Strike, Throw Glaive, Blade Dance's First Blood, and auto-attacks to burn for an additional $s1% damage as Fire over $453177d][Your blades burn with Cosmic energy, causing your Voidblade, Hungering Slash, and Throw Glaive to deal an additional $s2% damage as Cosmic damage.

Reap damage increased by $s3%].
- Effect: $?a212612[Your blades burn with Fel energy, causing the damage from Chaos Strike, Throw Glaive, Blade Dance's First Blood, and auto-attacks to burn for an additional $s1% damage as Fire over $453177d][Your blades burn with Cosmic energy, causing your Voidblade, Hungering Slash, and Throw Glaive to deal an additional $s2% damage as Cosmic damage.

Reap damage increased by $s3%].
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110114` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Violent Transformation
- Node ID: `110115`
- Entry ID: `136622`
- Definition ID: `141395`
- Spell ID: `452409`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[When you activate Metamorphosis, reset the cooldown of Immolation Aura][Entering Void Metamorphosis resets the cooldown of Voidblade and The Hunt.

The Hunt deals $s2% increased damage and resets the cooldown of Soul Immolation].
- Effect: $?a212612[When you activate Metamorphosis, reset the cooldown of Immolation Aura][Entering Void Metamorphosis resets the cooldown of Voidblade and The Hunt.

The Hunt deals $s2% increased damage and resets the cooldown of Soul Immolation].
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110113` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Enduring Torment
- Node ID: `110106`
- Entry ID: `136615`
- Definition ID: `141388`
- Spell ID: `452410`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The effects of your demon form persist outside of it in a weakened state, increasing $?a212612[Chaos Strike and Blade Dance damage by $453314s2%, and Haste by $453314s1%][Mastery: Monster Within's effectiveness by $453314s4%].
- Effect: The effects of your demon form persist outside of it in a weakened state, increasing $?a212612[Chaos Strike and Blade Dance damage by $453314s2%, and Haste by $453314s1%][Mastery: Monster Within's effectiveness by $453314s4%].
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110117` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Undying Embers
- Node ID: `110108`
- Entry ID: `136609`
- Definition ID: `141382`
- Spell ID: `1272405`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Immolation Aura][Soul Immolation] has a $?a212612[$s1][$s2]% chance to reignite after it expires, reapplying its effect.
- Effect: $?a212612[Immolation Aura][Soul Immolation] has a $?a212612[$s1][$s2]% chance to reignite after it expires, reapplying its effect.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110105` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Untethered Fury
- Node ID: `110109`
- Entry ID: `136606`
- Definition ID: `141379`
- Spell ID: `452411`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Maximum Fury increased by $?a212612[$s1][$s2].$?c3[

Void Ray damage increased by $s3%.][]
- Effect: Maximum Fury increased by $?a212612[$s1][$s2].$?c3[

Void Ray damage increased by $s3%.][]
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110111` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Student of Suffering
- Node ID: `110107`
- Entry ID: `136616`
- Definition ID: `141389`
- Spell ID: `452412`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Eye Beam][Void Ray] applies Student of Suffering to you, increasing Mastery by ${$453239s1*$mas}.1% and granting $453236s1 Fury every $453239t2 sec, for $453239d.
- Effect: $?a212612[Eye Beam][Void Ray] applies Student of Suffering to you, increasing Mastery by ${$453239s1*$mas}.1% and granting $453236s1 Fury every $453239t2 sec, for $453239d.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110115` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flamebound
- Node ID: `110107`
- Entry ID: `136614`
- Definition ID: `141387`
- Spell ID: `452413`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a212612[Immolation Aura][Hungering Slash] has $s1 yd increased radius and $s2% increased critical strike damage bonus.
- Effect: $?a212612[Immolation Aura][Hungering Slash] has $s1 yd increased radius and $s2% increased critical strike damage bonus.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110115` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Monster Rising
- Node ID: `110104`
- Entry ID: `136608`
- Definition ID: `141381`
- Spell ID: `452414`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[Agility][Intellect] increased by $?a212612[$452550s1][$452550s2]% while not in demon form.$?c3[

Collapsing Star damage increased by $s2%.][]
- Effect: $?a212612[Agility][Intellect] increased by $?a212612[$452550s1][$452550s2]% while not in demon form.$?c3[

Collapsing Star damage increased by $s2%.][]
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110106` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Volatile Instinct
- Node ID: `110110`
- Entry ID: `136611`
- Definition ID: `141384`
- Spell ID: `1272453`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Entering demon form $?a212612[immediately induces a Demonsurge][causes your next Voidsurge to repeat after a short delay].
- Effect: Entering demon form $?a212612[immediately induces a Demonsurge][causes your next Voidsurge to repeat after a short delay].
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110108` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Void Nova
- Node ID: `107347`
- Entry ID: `132289`
- Definition ID: `137090`
- Spell ID: `1234195`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash an eruption of void energy, dealing $s2 Cosmic damage and stunning your target and all nearby enemies for $d.
- Effect: Unleash an eruption of void energy, dealing $s2 Cosmic damage and stunning your target and all nearby enemies for $d.
- Point cost per purchased rank: `1` × Specialization pool (Devourer, Havoc, Vengeance) (ID `2801`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Demonic Intensity
- Node ID: `110116`
- Entry ID: `136617`
- Definition ID: `141390`
- Spell ID: `452415`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating $?a212612[][Void ]Metamorphosis greatly empowers $?a212612[Eye Beam, Immolation Aura][The Hunt].

$?a212612[Demonsurge][Voidsurge] damage is increased by $?a212612[${$452416s2}][${$1246160s2}]% for each time it previously triggered while your demon form is active.
- Effect: Activating $?a212612[][Void ]Metamorphosis greatly empowers $?a212612[Eye Beam, Immolation Aura][The Hunt].

$?a212612[Demonsurge][Voidsurge] damage is increased by $?a212612[${$452416s2}][${$1246160s2}]% for each time it previously triggered while your demon form is active.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110104` (type `2`), node `110107` (type `2`), node `110109` (type `2`), node `110110` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Demonsurge
- Node ID: `94917`
- Entry ID: `117514`
- Definition ID: `122526`
- Spell ID: `452402`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a212612[][Void ]Metamorphosis now also $?a212612[causes Demon Blades to generate $162264s10 additional Fury][greatly empowers Voidblade and Hungering Slash].

While demon form is active, the first cast of each empowered ability induces a $?a212612[Demonsurge][Voidsurge], causing you to explode with $?a212612[Fel][Void] energy, dealing $?a212612[$452416s1 Chaos][$1246160s1 Cosmic] damage to nearby enemies. Deals reduced damage beyond $452416s3 targets.
- Effect: $?a212612[][Void ]Metamorphosis now also $?a212612[causes Demon Blades to generate $162264s10 additional Fury][greatly empowers Voidblade and Hungering Slash].

While demon form is active, the first cast of each empowered ability induces a $?a212612[Demonsurge][Voidsurge], causing you to explode with $?a212612[Fel][Void] energy, dealing $?a212612[$452416s1 Chaos][$1246160s1 Cosmic] damage to nearby enemies. Deals reduced damage beyond $452416s3 targets.
- Point cost per purchased rank: `1` × Hero pool (Fel-Scarred, Void-Scarred) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `0`
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
### Guile
- Node ID: `107346`
- Entry ID: `132288`
- Definition ID: `137089`
- Spell ID: `1223171`
- Tree ID: `854`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cast range of Voidblade, Consume Magic, and Disrupt are increased by $s1 yds.
- Effect: The cast range of Voidblade, Consume Magic, and Disrupt are increased by $s1 yds.
- Point cost per purchased rank: `1` × Specialization pool (Devourer, Havoc, Vengeance) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1`
- Incoming edges: node `90936` (type `2`), node `90939` (type `2`), node `91004` (type `2`)
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
