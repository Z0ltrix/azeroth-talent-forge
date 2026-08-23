# Demonology

Reviewed build: `12.1.0.69404`
Spec ID: `266`
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
