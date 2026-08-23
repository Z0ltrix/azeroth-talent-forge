# Hellcaller

Reviewed build: `12.1.0.69404`
Hero subtree ID: `58`
Description: Amongst the satyr sects throughout Azeroth, Hellcallers are the most feared. Hellcaller warlocks have learned to weave together the vilest of shadow magic and entropic fel fire at the cost of corrupting their own soul.

## Hero talents

### Wither
- Node ID: `94840`
- Entry ID: `117437`
- Definition ID: `122449`
- Spell ID: `445465`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc445468
- Effect: $@spelldesc445468
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Xalan's Ferocity
- Node ID: `94853`
- Entry ID: `117450`
- Definition ID: `122462`
- Spell ID: `440044`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fire damage dealt by your spells and abilities is increased by $s1% and your Fire spells gain $s4% more critical strike chance from all sources.
- Effect: Fire damage dealt by your spells and abilities is increased by $s1% and your Fire spells gain $s4% more critical strike chance from all sources.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94840` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blackened Soul
- Node ID: `94837`
- Entry ID: `117434`
- Definition ID: `122446`
- Spell ID: `440043`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If the target is afflicted with your Wither, casting $?s1259790[Unstable Affliction][Chaos Bolt and Shadowburn] increase its stack count by $s1.

Each time Wither gains a stack it has a chance to collapse, consuming a stack every $445731t1 sec to deal $445736s1 Shadowflame damage to its host until 1 stack remains.
- Effect: If the target is afflicted with your Wither, casting $?s1259790[Unstable Affliction][Chaos Bolt and Shadowburn] increase its stack count by $s1.

Each time Wither gains a stack it has a chance to collapse, consuming a stack every $445731t1 sec to deal $445736s1 Shadowflame damage to its host until 1 stack remains.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94840` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Xalan's Cruelty
- Node ID: `94845`
- Entry ID: `117442`
- Definition ID: `122454`
- Spell ID: `440040`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow damage dealt by your spells and abilities is increased by $s3% and your Shadow spells gain $s1% more critical strike chance from all sources.
- Effect: Shadow damage dealt by your spells and abilities is increased by $s3% and your Shadow spells gain $s1% more critical strike chance from all sources.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94840` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Through the Felvine
- Node ID: `109836`
- Entry ID: `136095`
- Definition ID: `140850`
- Spell ID: `1266799`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the damage of $?a137043[Unstable Affliction by $s1][Chaos Bolt by $s4]% and $?a137043[Seed of Corruption by $s3][Rain of Fire by $s5]%.

This effect is doubled while Malevolence is active.
- Effect: Increases the damage of $?a137043[Unstable Affliction by $s1][Chaos Bolt by $s4]% and $?a137043[Seed of Corruption by $s3][Rain of Fire by $s5]%.

This effect is doubled while Malevolence is active.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94840` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Curse of the Satyr
- Node ID: `94822`
- Entry ID: `117419`
- Definition ID: `122431`
- Spell ID: `440057`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Curse of Weakness is empowered and transforms into Curse of the Satyr.

$@spellicon442804 $@spellname442804
$@spelldesc442804
- Effect: Curse of Weakness is empowered and transforms into Curse of the Satyr.

$@spellicon442804 $@spellname442804
$@spelldesc442804
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94853` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aura of Enfeeblement
- Node ID: `94822`
- Entry ID: `123309`
- Definition ID: `128179`
- Spell ID: `440059`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: While Unending Resolve is active, enemies within $449587a1 yds are affected by Curse of Tongues and Curse of Weakness at $s1% effectiveness.
- Effect: While Unending Resolve is active, enemies within $449587a1 yds are affected by Curse of Tongues and Curse of Weakness at $s1% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94853` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hatefury Rituals
- Node ID: `94854`
- Entry ID: `117451`
- Definition ID: `122463`
- Spell ID: `440048`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Wither deals $s1% increased periodic damage but its duration is $s2% shorter.
- Effect: Wither deals $s1% increased periodic damage but its duration is $s2% shorter.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94837` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bleakheart Tactics
- Node ID: `94854`
- Entry ID: `123310`
- Definition ID: `128180`
- Spell ID: `440051`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Wither damage increased $s1%. When Wither gains a stack from Blackened Soul, it has a chance to gain an additional stack.
- Effect: Wither damage increased $s1%. When Wither gains a stack from Blackened Soul, it has a chance to gain an additional stack.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94837` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Zevrim's Resilience
- Node ID: `94835`
- Entry ID: `117432`
- Definition ID: `122444`
- Spell ID: `440065`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Dark Pact heals you for $108416s5 every $108416t5 sec while active.
- Effect: Dark Pact heals you for $108416s5 every $108416t5 sec while active.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94845` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Illhoof's Design
- Node ID: `94835`
- Entry ID: `123308`
- Definition ID: `128178`
- Spell ID: `440070`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Sacrifice $s1% of your maximum health. Soul Leech now absorbs an additional $s2% of your maximum health.
- Effect: Sacrifice $s1% of your maximum health. Soul Leech now absorbs an additional $s2% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94845` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Devil Fruit
- Node ID: `109835`
- Entry ID: `136094`
- Definition ID: `140849`
- Spell ID: `1266805`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Periodic damage dealt by Wither has a chance to grant Malevolence for $s1 sec.
- Effect: Periodic damage dealt by Wither has a chance to grant Malevolence for $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109836` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mark of Xavius
- Node ID: `94834`
- Entry ID: `117431`
- Definition ID: `122443`
- Spell ID: `440046`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s980[Agony damage increased by $s1%.][Wither damage increased by $s2%.]

Blackened Soul deals $s3% increased damage per stack of Wither.
- Effect: $?s980[Agony damage increased by $s1%.][Wither damage increased by $s2%.]

Blackened Soul deals $s3% increased damage per stack of Wither.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94822` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Seeds of Their Demise
- Node ID: `94829`
- Entry ID: `117426`
- Definition ID: `122438`
- Spell ID: `440055`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After Wither reaches $s1 stacks or when its host reaches $s2% health, Wither deals $445736s1 Shadowflame damage to its host every $445731t1 sec until 1 stack remains.

When Blackened Soul deals damage, you have a chance to gain $?s137046[$s3 stacks of Flashpoint][Shard Instability].
- Effect: After Wither reaches $s1 stacks or when its host reaches $s2% health, Wither deals $445736s1 Shadowflame damage to its host every $445731t1 sec until 1 stack remains.

When Blackened Soul deals damage, you have a chance to gain $?s137046[$s3 stacks of Flashpoint][Shard Instability].
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94854` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mark of Peroth'arn
- Node ID: `94844`
- Entry ID: `117441`
- Definition ID: `122453`
- Spell ID: `440045`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damaging critical strikes dealt by Wither deal ${200+$s1}% damage instead of the usual 200%.

Damaging critical strikes dealt by Blackened Soul deal ${200+$s2}% damage instead of the usual 200%.
- Effect: Damaging critical strikes dealt by Wither deal ${200+$s1}% damage instead of the usual 200%.

Damaging critical strikes dealt by Blackened Soul deal ${200+$s2}% damage instead of the usual 200%.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94835` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Alzzin's Iniquity
- Node ID: `109834`
- Entry ID: `136093`
- Definition ID: `140848`
- Spell ID: `1266803`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Malevolence grants an additional $s1% Haste and when cast increases the stack count of active Withers by an additional $s2 stacks.
- Effect: Malevolence grants an additional $s1% Haste and when cast increases the stack count of active Withers by an additional $s2 stacks.
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109835` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Malevolence
- Node ID: `94842`
- Entry ID: `117439`
- Definition ID: `122451`
- Spell ID: `430014`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc442726
- Effect: $@spelldesc442726
- Point cost per purchased rank: `1` × Hero pool (Hellcaller) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94829` (type `2`), node `94834` (type `2`), node `94844` (type `2`), node `109834` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
