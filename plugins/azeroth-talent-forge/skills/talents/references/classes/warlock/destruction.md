# Destruction

Reviewed build: `12.1.0.69404`
Spec ID: `267`
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
### Cloven Souls
- Node ID: `94849`
- Entry ID: `117446`
- Definition ID: `122458`
- Spell ID: `428517`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies damaged by your Overlord have their souls cloven, increasing damage taken by you and your pets by $434424s1% for $434424d.
- Effect: Enemies damaged by your Overlord have their souls cloven, increasing damage taken by you and your pets by $434424s1% for $434424d.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94855` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Touch of Rancora
- Node ID: `94856`
- Entry ID: `117453`
- Definition ID: `122465`
- Spell ID: `429893`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Demonic Art increases the damage of your next $?s137044[Hand of Gul'dan][Chaos Bolt, Rain of Fire, or Shadowburn] by $s1% and reduces its cast time by $s2%.

$?s137044[][Casting Chaos Bolt reduces the duration of Diabolic Ritual by $s3 additional sec.]
- Effect: Demonic Art increases the damage of your next $?s137044[Hand of Gul'dan][Chaos Bolt, Rain of Fire, or Shadowburn] by $s1% and reduces its cast time by $s2%.

$?s137044[][Casting Chaos Bolt reduces the duration of Diabolic Ritual by $s3 additional sec.]
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94855` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Secrets of the Coven
- Node ID: `94826`
- Entry ID: `117423`
- Definition ID: `122435`
- Spell ID: `428518`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Mother of Chaos empowers your next $?s137044[Shadow Bolt][Incinerate] to become Infernal Bolt.

$@spellicon434506 $@spellname434506
$@spelldesc434506
- Effect: Mother of Chaos empowers your next $?s137044[Shadow Bolt][Incinerate] to become Infernal Bolt.

$@spellicon434506 $@spellname434506
$@spelldesc434506
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94855` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Diabolic Oculi
- Node ID: `109833`
- Entry ID: `136092`
- Definition ID: `140847`
- Spell ID: `1268709`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You summon a Diabolic Oculus, up to $1269643u, each time the duration of Diabolic Ritual is reduced by one of your spells.

Diabolic Oculi explode when consuming Demonic Art, dealing $1269800s1 Fire damage to all enemies within $1269800a1 yds of the target. Damage reduced beyond $s1 targets.
- Effect: You summon a Diabolic Oculus, up to $1269643u, each time the duration of Diabolic Ritual is reduced by one of your spells.

Diabolic Oculi explode when consuming Demonic Art, dealing $1269800s1 Fire damage to all enemies within $1269800a1 yds of the target. Damage reduced beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94855` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Soul-Etched Circles
- Node ID: `94836`
- Entry ID: `117433`
- Definition ID: `122445`
- Spell ID: `428911`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You always gain the benefit of Soulburn when casting Demonic Circle: Teleport, increasing your movement speed by 50% and making you immune to snares and roots for 6 sec.
- Effect: You always gain the benefit of Soulburn when casting Demonic Circle: Teleport, increasing your movement speed by 50% and making you immune to snares and roots for 6 sec.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94849` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Annihilan's Bellow
- Node ID: `94836`
- Entry ID: `118837`
- Definition ID: `123737`
- Spell ID: `429072`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Howl of Terror cooldown is reduced by ${$s1/-1000} sec and range is increased by $s2 yds.
- Effect: Howl of Terror cooldown is reduced by ${$s1/-1000} sec and range is increased by $s2 yds.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94849` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cruelty of Kerxan
- Node ID: `94848`
- Entry ID: `117445`
- Definition ID: `122457`
- Spell ID: `429902`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137044[Summon Demonic Tyrant][Summon Infernal] grants Diabolic Ritual and reduces its duration by ${$s1/1000} sec.
- Effect: $?s137044[Summon Demonic Tyrant][Summon Infernal] grants Diabolic Ritual and reduces its duration by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94856` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Infernal Machine
- Node ID: `94848`
- Entry ID: `118838`
- Definition ID: `123738`
- Spell ID: `429917`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Spending Soul Shards on damaging spells while your $?s137044[Demonic Tyrant][Infernal] is active decreases the duration of Diabolic Ritual by ${$s1/1000} additional sec.
- Effect: Spending Soul Shards on damaging spells while your $?s137044[Demonic Tyrant][Infernal] is active decreases the duration of Diabolic Ritual by ${$s1/1000} additional sec.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94856` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Infernal Vitality
- Node ID: `94852`
- Entry ID: `117449`
- Definition ID: `122461`
- Spell ID: `429115`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unending Resolve heals you for ${$434559s1*($434559d/$434559t1)}% of your maximum health over $434559d.
- Effect: Unending Resolve heals you for ${$434559s1*($434559d/$434559t1)}% of your maximum health over $434559d.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94826` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Infernal Bulwark
- Node ID: `94852`
- Entry ID: `118839`
- Definition ID: `123739`
- Spell ID: `429130`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Unending Resolve grants Soul Leech equal to $434561s1% of your maximum health and increases the maximum amount Soul Leech can absorb by $434561s1% for $434561d.
- Effect: Unending Resolve grants Soul Leech equal to $434561s1% of your maximum health and increases the maximum amount Soul Leech can absorb by $434561s1% for $434561d.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94826` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Looks That Kill
- Node ID: `109832`
- Entry ID: `136091`
- Definition ID: `140846`
- Spell ID: `1268713`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Diabolic Oculi now cast Diabolic Gaze at your primary demon's target every 1 sec while active.

$@spellicon1269892 $@spellname1269892
$@spelldesc1269892
- Effect: Your Diabolic Oculi now cast Diabolic Gaze at your primary demon's target every 1 sec while active.

$@spellicon1269892 $@spellname1269892
$@spelldesc1269892
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109833` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flames of Xoroth
- Node ID: `94833`
- Entry ID: `117430`
- Definition ID: `122442`
- Spell ID: `429657`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fire damage increased by $s1% and damage dealt by your demons is increased by $s3%.
- Effect: Fire damage increased by $s1% and damage dealt by your demons is increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94836` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Abyssal Dominion
- Node ID: `94831`
- Entry ID: `117428`
- Definition ID: `122440`
- Spell ID: `429581`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137044[Summon Demonic Tyrant is empowered, dealing $s1% increased damage and increasing the damage of your demons by $s2% while active.][Summon Infernal becomes empowered, dealing $s3% increased damage. When your Summon Infernal ends, it fragments into two smaller Infernals at $s4% effectiveness that lasts $456310d.]
- Effect: $?s137044[Summon Demonic Tyrant is empowered, dealing $s1% increased damage and increasing the damage of your demons by $s2% while active.][Summon Infernal becomes empowered, dealing $s3% increased damage. When your Summon Infernal ends, it fragments into two smaller Infernals at $s4% effectiveness that lasts $456310d.]
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94848` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gloom of Nathreza
- Node ID: `94843`
- Entry ID: `117440`
- Definition ID: `122452`
- Spell ID: `429899`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137044[Hand of Gul'dan deals $s1% increased damage for each Soul Shard spent.][Enemies marked by your Havoc take $s2% increased damage from your single target spells.]
- Effect: $?s137044[Hand of Gul'dan deals $s1% increased damage for each Soul Shard spent.][Enemies marked by your Havoc take $s2% increased damage from your single target spells.]
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94852` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mind's Eyes
- Node ID: `109831`
- Entry ID: `136090`
- Definition ID: `140845`
- Spell ID: `1268716`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Diabolic Oculi observe the battlefield and collect information that is imparted to you upon being exploded, each Diabolic Oculi increasing your Intellect by $1269879s1% for $1269879d.
- Effect: Your Diabolic Oculi observe the battlefield and collect information that is imparted to you upon being exploded, each Diabolic Oculi increasing your Intellect by $1269879s1% for $1269879d.
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109832` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ruination
- Node ID: `94830`
- Entry ID: `117427`
- Definition ID: `122439`
- Spell ID: `428522`
- Tree ID: `720`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summoning a Pit Lord causes your next $?s137044[Hand of Gul'dan][Chaos Bolt] to become Ruination.

$@spellicon434635 $@spellname434635
$@spelldesc434635
- Effect: Summoning a Pit Lord causes your next $?s137044[Hand of Gul'dan][Chaos Bolt] to become Ruination.

$@spellicon434635 $@spellname434635
$@spelldesc434635
- Point cost per purchased rank: `1` × Hero pool (Diabolist) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94831` (type `2`), node `94833` (type `2`), node `94843` (type `2`), node `109831` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
