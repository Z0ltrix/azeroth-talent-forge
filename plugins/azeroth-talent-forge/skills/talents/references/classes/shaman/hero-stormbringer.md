# Stormbringer

Reviewed build: `12.1.0.69404`
Hero subtree ID: `55`
Description: Stormbringers harness the power of the storm, enhancing their dominion over lightning and shaping it to their will. Summon a fierce Tempest to unleash chaos upon your foes awakening the storm, creating devastation in your path.

## Hero talents

### Tempest
- Node ID: `94892`
- Entry ID: `117489`
- Definition ID: `122501`
- Spell ID: `454009`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Each Maelstrom spent has a ${$s1/100}.2% chance to upgrade][Each Maelstrom Weapon spent has a ${$s2/100}.2% chance to upgrade] your next Lightning Bolt to Tempest.

$@spelltooltip452201
- Effect: $?s137040[Each Maelstrom spent has a ${$s1/100}.2% chance to upgrade][Each Maelstrom Weapon spent has a ${$s2/100}.2% chance to upgrade] your next Lightning Bolt to Tempest.

$@spelltooltip452201
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unlimited Power
- Node ID: `94886`
- Entry ID: `117483`
- Definition ID: `122495`
- Spell ID: `454391`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Spending $?s137040[Maelstrom][Maelstrom Weapon stacks] grants you $454394s1% haste for $454394d.

Multiple applications may overlap.
- Effect: Spending $?s137040[Maelstrom][Maelstrom Weapon stacks] grants you $454394s1% haste for $454394d.

Multiple applications may overlap.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormcaller
- Node ID: `94893`
- Entry ID: `117490`
- Definition ID: `122502`
- Spell ID: `454021`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the critical strike chance of your Nature damage spells by $s1% and the critical strike damage of your Nature spells by $s2%.
- Effect: Increases the critical strike chance of your Nature damage spells by $s1% and the critical strike damage of your Nature spells by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightning Conduit
- Node ID: `94863`
- Entry ID: `117460`
- Definition ID: `122472`
- Spell ID: `467778`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You have a chance to get struck by lightning, increasing your movement speed by $468226s2% for $468226d. The effectiveness is increased to $s3% in outdoor areas.

You call down a Thunderstorm when you Reincarnate.
- Effect: You have a chance to get struck by lightning, increasing your movement speed by $468226s2% for $468226d. The effectiveness is increased to $s3% in outdoor areas.

You call down a Thunderstorm when you Reincarnate.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Electroshock
- Node ID: `94863`
- Entry ID: `128226`
- Definition ID: `133033`
- Spell ID: `454022`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Tempest increases your movement speed by $454025s1% for $454025d.
- Effect: Tempest increases your movement speed by $454025s1% for $454025d.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormwell
- Node ID: `109729`
- Entry ID: `135987`
- Definition ID: `140742`
- Spell ID: `1264762`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Storm Elemental lasts ${$s1/1000} sec longer, and Stormkeeper generates $s2 Maelstrom.][Windfury Weapon damage increased by $s3%.

When Crash Lightning hits a single enemy, it activates Windfury Weapon.]
- Effect: $?c1[Storm Elemental lasts ${$s1/1000} sec longer, and Stormkeeper generates $s2 Maelstrom.][Windfury Weapon damage increased by $s3%.

When Crash Lightning hits a single enemy, it activates Windfury Weapon.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Swell
- Node ID: `94873`
- Entry ID: `117470`
- Definition ID: `122482`
- Spell ID: `455088`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tempest grants ${$455089s1*$mas}% Mastery for $455089d.
- Effect: Tempest grants ${$455089s1*$mas}% Mastery for $455089d.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94886` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Supercharge
- Node ID: `94873`
- Entry ID: `128225`
- Definition ID: `133032`
- Spell ID: `455110`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?s137040[Lightning Bolt, Tempest, and Chain Lightning Elemental Overloads deal $s1% additional damage.][Lightning Bolt, Tempest, and Chain Lightning have a $s2% chance to refund $s3 Maelstrom Weapon stacks.]
- Effect: $?s137040[Lightning Bolt, Tempest, and Chain Lightning Elemental Overloads deal $s1% additional damage.][Lightning Bolt, Tempest, and Chain Lightning have a $s2% chance to refund $s3 Maelstrom Weapon stacks.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94886` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arc Discharge
- Node ID: `94885`
- Entry ID: `117482`
- Definition ID: `122494`
- Spell ID: `455096`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Casting Tempest grants a charge of Stormkeeper.][Tempest causes your next Chain Lightning to be instant cast, deal $455097s2% increased damage, and cast an additional time.

Can accumulate up to $470532U charges.]
- Effect: $?s137040[Casting Tempest grants a charge of Stormkeeper.][Tempest causes your next Chain Lightning to be instant cast, deal $455097s2% increased damage, and cast an additional time.

Can accumulate up to $470532U charges.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94893` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rolling Thunder
- Node ID: `94889`
- Entry ID: `117486`
- Definition ID: `122498`
- Spell ID: `454026`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Reduces the cooldown of Stormkeeper by ${$s1/-1000} sec.][Doom Winds summons a Nature Feral Spirit for ${$s2/1000} sec.

$@spellicon469314$@spellname469314
An Elemental Spirit infused with Nature magic, granting the summoner with $224125s1% increased Nature damage and $224125s3% Physical damage for ${$s2/1000} sec.]
- Effect: $?s137040[Reduces the cooldown of Stormkeeper by ${$s1/-1000} sec.][Doom Winds summons a Nature Feral Spirit for ${$s2/1000} sec.

$@spellicon469314$@spellname469314
An Elemental Spirit infused with Nature magic, granting the summoner with $224125s1% increased Nature damage and $224125s3% Physical damage for ${$s2/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94863` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Natural Gift
- Node ID: `109728`
- Entry ID: `135986`
- Definition ID: `140741`
- Spell ID: `1264691`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Nature damage is increased by $s1%
- Effect: Nature damage is increased by $s1%
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109729` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voltaic Surge
- Node ID: `94870`
- Entry ID: `117467`
- Definition ID: `122479`
- Spell ID: `454919`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Earthquake][Crash Lightning] and Chain Lightning damage increased by $s1%.
- Effect: $?s137040[Earthquake][Crash Lightning] and Chain Lightning damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94873` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Conductive Energy
- Node ID: `94868`
- Entry ID: `117465`
- Definition ID: `122477`
- Spell ID: `455123`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Lightning Rod targets now also take $s2% of the damage that Tempest deals, and Tempest also applies Lightning Rod effect.][Gain the effects of the Lightning Rod talent:

$@spellicon210689 $@spellname210689
$@spelldesc210689]
- Effect: $?s137040[Lightning Rod targets now also take $s2% of the damage that Tempest deals, and Tempest also applies Lightning Rod effect.][Gain the effects of the Lightning Rod talent:

$@spellicon210689 $@spellname210689
$@spelldesc210689]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94885` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nature's Protection
- Node ID: `94880`
- Entry ID: `117477`
- Definition ID: `122489`
- Spell ID: `454027`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lightning Shield reduces the damage you take by $s1%.
- Effect: Lightning Shield reduces the damage you take by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94889` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Surging Currents
- Node ID: `94880`
- Entry ID: `125617`
- Definition ID: `130449`
- Spell ID: `454372`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Casting Tempest grants Surging Currents, increasing the effectiveness of your next Chain Heal or Healing Surge by $454376s1%, up to ${$454376s1*$454376u}%.
- Effect: Casting Tempest grants Surging Currents, increasing the effectiveness of your next Chain Heal or Healing Surge by $454376s1%, up to ${$454376s1*$454376u}%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94889` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Descending Skies
- Node ID: `109727`
- Entry ID: `135985`
- Definition ID: `140740`
- Spell ID: `1264688`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting ][]Ascendance upgrades your next Lightning Bolt to Tempest.
- Effect: $?c1[Casting ][]Ascendance upgrades your next Lightning Bolt to Tempest.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109728` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Awakening Storms
- Node ID: `94867`
- Entry ID: `117464`
- Definition ID: `122476`
- Spell ID: `455129`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137040[Each Maelstrom spent has an additional ${$s3/100}.2% chance to upgrade your next Lightning Bolt to Tempest.][Stormstrike has a small chance to upgrade your next Lightning Bolt to Tempest.]
- Effect: $?a137040[Each Maelstrom spent has an additional ${$s3/100}.2% chance to upgrade your next Lightning Bolt to Tempest.][Stormstrike has a small chance to upgrade your next Lightning Bolt to Tempest.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94868` (type `2`), node `94870` (type `2`), node `94880` (type `2`), node `109727` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
