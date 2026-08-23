# Soul Harvester

Reviewed build: `12.1.0.69404`
Hero subtree ID: `57`
Description: Few grasp the power hidden within souls, but many know the hunger demons share for spirits of the fallen. Soul Harvesters enter pacts with demons from the Twisting Nether, serving as their host and feeding them the souls of their foes in exchange for incredible power.

## Hero talents

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
