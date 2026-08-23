# Affliction

Reviewed build: `12.1.0.69404`
Spec ID: `265`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

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
### Soul Leech
- Node ID: `71933`
- Entry ID: `91441`
- Definition ID: `96443`
- Spell ID: `1311653`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: All single-target damage done by you and your minions grants you and your pet shadowy shields that absorb $s1% of the damage dealt$?s219272[][ for $108366d], up to $s2% of maximum health.
- Effect: All single-target damage done by you and your minions grants you and your pet shadowy shields that absorb $s1% of the damage dealt$?s219272[][ for $108366d], up to $s2% of maximum health.
- Point cost per purchased rank: `1` × Specialization pool (Affliction, Demonology, Destruction) (ID `2801`; group)
- Source gates: source `node`; type `2`; minimum level `10`; grants `1` rank(s)
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
### Demonic Soul
- Node ID: `94851`
- Entry ID: `117448`
- Definition ID: `122460`
- Spell ID: `449614`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: A demonic entity now inhabits your soul, allowing you to detect if a Soul Shard has a Succulent Soul when it's generated.

Consuming a Succulent Soul unleashes your demonic soul, dealing $449801s1 Shadow damage to all enemies within $449801a1 yds of the target. Damage reduced beyond 8 targets.
- Effect: A demonic entity now inhabits your soul, allowing you to detect if a Soul Shard has a Succulent Soul when it's generated.

Consuming a Succulent Soul unleashes your demonic soul, dealing $449801s1 Shadow damage to all enemies within $449801a1 yds of the target. Damage reduced beyond 8 targets.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Necrolyte Teachings
- Node ID: `94825`
- Entry ID: `117422`
- Definition ID: `122434`
- Spell ID: `449620`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137043[Shadow Bolt and Drain Soul damage increased by $s2%. Nightfall increases the damage of Shadow Bolt and Drain Soul by an additional $s1%.][Shadow Bolt damage increased by $s2%. Power Siphon increases the damage of Demonbolt by an additional $s3%.]
- Effect: $?s137043[Shadow Bolt and Drain Soul damage increased by $s2%. Nightfall increases the damage of Shadow Bolt and Drain Soul by an additional $s1%.][Shadow Bolt damage increased by $s2%. Power Siphon increases the damage of Demonbolt by an additional $s3%.]
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94851` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Soul Anathema
- Node ID: `94847`
- Entry ID: `117444`
- Definition ID: `122456`
- Spell ID: `449624`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleashing your demonic soul bestows a fiendish entity unto the soul of its targets, dealing $450538o1 Shadow damage over $450538d.

If this effect is reapplied, any remaining damage will be added to the new Soul Anathema.
- Effect: Unleashing your demonic soul bestows a fiendish entity unto the soul of its targets, dealing $450538o1 Shadow damage over $450538d.

If this effect is reapplied, any remaining damage will be added to the new Soul Anathema.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94851` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Demoniac's Fervor
- Node ID: `94832`
- Entry ID: `117429`
- Definition ID: `122441`
- Spell ID: `449629`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your demonic soul deals $s1% increased damage to $?s137043[targets affected by your Unstable Affliction.][the main target of Hand of Gul'dan.]
- Effect: Your demonic soul deals $s1% increased damage to $?s137043[targets affected by your Unstable Affliction.][the main target of Hand of Gul'dan.]
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94851` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Manifested Avarice
- Node ID: `109839`
- Entry ID: `136098`
- Definition ID: `140853`
- Spell ID: `1268884`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each Succulent Soul consumed has an increasing chance to unleash the Demonic Soul within you, enabling it to assault your enemies for $1269042d.

$@spellicon1269049 $@spellname1269049
$@spelldesc1269049
- Effect: Each Succulent Soul consumed has an increasing chance to unleash the Demonic Soul within you, enabling it to assault your enemies for $1269042d.

$@spellicon1269049 $@spellname1269049
$@spelldesc1269049
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94851` (type `2`)
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
### Gorebound Fortitude
- Node ID: `94850`
- Entry ID: `117447`
- Definition ID: `122459`
- Spell ID: `449701`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You always gain the benefit of Soulburn when consuming a Healthstone, increasing its healing by 30% and increasing your maximum health by 20% for 12 sec.
- Effect: You always gain the benefit of Soulburn when consuming a Healthstone, increasing its healing by 30% and increasing your maximum health by 20% for 12 sec.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94825` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Friends In Dark Places
- Node ID: `94850`
- Entry ID: `123840`
- Definition ID: `128678`
- Spell ID: `449703`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Dark Pact now shields you for an additional $s1% of the sacrificed health.
- Effect: Dark Pact now shields you for an additional $s1% of the sacrificed health.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94825` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shared Fate
- Node ID: `94823`
- Entry ID: `117420`
- Definition ID: `122432`
- Spell ID: `449704`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you kill a target, its tortured soul is flung into a nearby enemy for $450591d. This effect inflicts $450593s1 Shadow damage to enemies within $450593a1 yds every $450591t1 sec.

Deals reduced damage beyond $s1 targets.
- Effect: When you kill a target, its tortured soul is flung into a nearby enemy for $450591d. This effect inflicts $450593s1 Shadow damage to enemies within $450593a1 yds every $450591t1 sec.

Deals reduced damage beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94847` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Feast of Souls
- Node ID: `94823`
- Entry ID: `123839`
- Definition ID: `128677`
- Spell ID: `449706`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you kill a target, you have a chance to generate a Soul Shard that is guaranteed to be a Succulent Soul.
- Effect: When you kill a target, you have a chance to generate a Soul Shard that is guaranteed to be a Succulent Soul.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94847` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Eternal Servitude
- Node ID: `94824`
- Entry ID: `117421`
- Definition ID: `122433`
- Spell ID: `449707`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fel Domination cooldown is reduced by ${$s1/-1000} sec.
- Effect: Fel Domination cooldown is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94832` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gorefiend's Resolve
- Node ID: `94824`
- Entry ID: `123838`
- Definition ID: `128676`
- Spell ID: `389623`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Targets resurrected with Soulstone resurrect with $s1% additional health and $s2% additional mana.
- Effect: Targets resurrected with Soulstone resurrect with $s1% additional health and $s2% additional mana.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94832` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shared Vessel
- Node ID: `109838`
- Entry ID: `136097`
- Definition ID: `140852`
- Spell ID: `1268889`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your Mastery by $s1%.

This effect is doubled while the demonic entity is aiding you in combat.
- Effect: Increases your Mastery by $s1%.

This effect is doubled while the demonic entity is aiding you in combat.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109839` (type `2`)
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
### Wicked Reaping
- Node ID: `94821`
- Entry ID: `117418`
- Definition ID: `122430`
- Spell ID: `449631`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage dealt by your demonic soul is increased by $s1%.

Consuming $?s137043[Nightfall][Demonic Core] feeds the demonic entity within you, causing it to appear and deal $?s137043[$449826s1][${$449826s1*($s2/100)}] Shadow damage to your target.
- Effect: Damage dealt by your demonic soul is increased by $s1%.

Consuming $?s137043[Nightfall][Demonic Core] feeds the demonic entity within you, causing it to appear and deal $?s137043[$449826s1][${$449826s1*($s2/100)}] Shadow damage to your target.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94850` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quietus
- Node ID: `94846`
- Entry ID: `117443`
- Definition ID: `122455`
- Spell ID: `449634`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Soul Anathema damage increased by $s1% and is dealt $s2% faster.

Consuming $?s137043[Nightfall][Demonic Core] activates Shared Fate or Feast of Souls.
- Effect: Soul Anathema damage increased by $s1% and is dealt $s2% faster.

Consuming $?s137043[Nightfall][Demonic Core] activates Shared Fate or Feast of Souls.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94823` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sataiel's Volition
- Node ID: `94838`
- Entry ID: `117435`
- Definition ID: `122447`
- Spell ID: `449637`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137043[Corruption deals damage $s1% faster and Haunt grants Nightfall.][Wild Imp damage increased by $s2% and Wild Imps that are imploded have an additional $s3% chance to grant a Demonic Core.]
- Effect: $?s137043[Corruption deals damage $s1% faster and Haunt grants Nightfall.][Wild Imp damage increased by $s2% and Wild Imps that are imploded have an additional $s3% chance to grant a Demonic Core.]
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94824` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Eternal Hunger
- Node ID: `109837`
- Entry ID: `136096`
- Definition ID: `140851`
- Spell ID: `1268903`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the duration of Manifested Avarice by ${$s1/1000} sec and increases the damage of Soul Swipe by $s2%.
- Effect: Increases the duration of Manifested Avarice by ${$s1/1000} sec and increases the damage of Soul Swipe by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109838` (type `2`)
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
### Shadow of Death
- Node ID: `94857`
- Entry ID: `117454`
- Definition ID: `122466`
- Spell ID: `449638`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?s137043[Dark Harvest spell is empowered by the demonic entity within you, causing it to grant ${$s2} Soul Shard that each contain a Succulent Soul every 1 sec while channeled.][Summon Demonic Tyrant spell is empowered by the demonic entity within you, causing it to grant ${$449858s1/10} Soul Shards that each contain a Succulent Soul.]
- Effect: Your $?s137043[Dark Harvest spell is empowered by the demonic entity within you, causing it to grant ${$s2} Soul Shard that each contain a Succulent Soul every 1 sec while channeled.][Summon Demonic Tyrant spell is empowered by the demonic entity within you, causing it to grant ${$449858s1/10} Soul Shards that each contain a Succulent Soul.]
- Point cost per purchased rank: `1` × Hero pool (Soul Harvester) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94821` (type `2`), node `94838` (type `2`), node `94846` (type `2`), node `109837` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Diabolic Ritual
- Node ID: `94855`
- Entry ID: `117452`
- Definition ID: `122464`
- Spell ID: `428514`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137044[Spending a Soul Shard on a damaging spell grants Diabolic Ritual for $431944d. While Diabolic Ritual is active, each Soul Shard spent on a damaging spell reduces its duration by $s1 sec.][Casting Chaos Bolt, Rain of Fire, or Shadowburn grants Diabolic Ritual for $431944d. If Diabolic Ritual is already active, its duration is reduced by $s2 sec instead.]

When Diabolic Ritual expires you gain Demonic Art, causing your next $?s137044[Hand of Gul'dan][Chaos Bolt, Rain of Fire, or Shadowburn] to summon an Overlord, Mother of Chaos, or Pit Lord that unleashes a devastating attack against your enemies.
- Effect: $?s137044[Spending a Soul Shard on a damaging spell grants Diabolic Ritual for $431944d. While Diabolic Ritual is active, each Soul Shard spent on a damaging spell reduces its duration by $s1 sec.][Casting Chaos Bolt, Rain of Fire, or Shadowburn grants Diabolic Ritual for $431944d. If Diabolic Ritual is already active, its duration is reduced by $s2 sec instead.]

When Diabolic Ritual expires you gain Demonic Art, causing your next $?s137044[Hand of Gul'dan][Chaos Bolt, Rain of Fire, or Shadowburn] to summon an Overlord, Mother of Chaos, or Pit Lord that unleashes a devastating attack against your enemies.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
