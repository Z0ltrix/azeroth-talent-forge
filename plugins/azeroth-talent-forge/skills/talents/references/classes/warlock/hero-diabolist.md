# Diabolist

Reviewed build: `12.1.0.69404`
Hero subtree ID: `59`
Description: The defeat of the Legion left many powerful demons unbound. Diabolists command greater demons once thought to be uncontrollable and wield abyssal powers from the Twisting Nether on the battlefield.

## Hero talents

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
