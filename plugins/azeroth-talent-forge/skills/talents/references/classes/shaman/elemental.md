# Elemental

Reviewed build: `12.1.0.69404`
Spec ID: `262`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Lava Burst
- Node ID: `103598`
- Entry ID: `127873`
- Definition ID: `132682`
- Spell ID: `51505`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hurls molten lava at the target, dealing $285452s1 Fire damage. Lava Burst will always critically strike if the target is affected by Flame Shock and its damage is increased by your critical strike chance.$?a343725[

|cFFFFFFFFGenerates $343725s3 Maelstrom.|r][]
- Effect: Hurls molten lava at the target, dealing $285452s1 Fire damage. Lava Burst will always critically strike if the target is affected by Flame Shock and its damage is increased by your critical strike chance.$?a343725[

|cFFFFFFFFGenerates $343725s3 Maelstrom.|r][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1` | source `node`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Call of the Ancestors
- Node ID: `94888`
- Entry ID: `117485`
- Definition ID: `122497`
- Spell ID: `443450`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137040[Stormkeeper calls an Ancestor to your side for $445624d.][Unleash Life calls an Ancestor to your side for $s1 sec.]

Whenever you cast a healing or damaging spell, the Ancestor will cast a similar spell.
- Effect: $?a137040[Stormkeeper calls an Ancestor to your side for $445624d.][Unleash Life calls an Ancestor to your side for $s1 sec.]

Whenever you cast a healing or damaging spell, the Ancestor will cast a similar spell.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Surging Totem
- Node ID: `94877`
- Entry ID: `117474`
- Definition ID: `122486`
- Spell ID: `444995`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enhancement Summons a totem at the target location that creates Tremor immediately and every 6 sec for (122.382% of Attack Power) Flamestrike damage. Damage reduced beyond 5 targets. Lasts 25 sec. Restoration maintains Healing Rain with 10% increased effectiveness Replaces Rain.
- Effect: Enhancement Summons a totem at the target location that creates Tremor immediately and every 6 sec for (122.382% of Attack Power) Flamestrike damage. Damage reduced beyond 5 targets. Lasts 25 sec. Restoration maintains Healing Rain with 10% increased effectiveness Replaces Rain.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `wowhead`; build: `12.1.0.69404`
### Latent Wisdom
- Node ID: `94862`
- Entry ID: `117459`
- Definition ID: `122471`
- Spell ID: `443449`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Ancestors' spells are $s1% more powerful.
- Effect: Your Ancestors' spells are $s1% more powerful.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancient Fellowship
- Node ID: `94862`
- Entry ID: `123632`
- Definition ID: `128470`
- Spell ID: `443423`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Ancestors have a $s1% chance to call another Ancestor for $445624d when they depart.
- Effect: Ancestors have a $s1% chance to call another Ancestor for $445624d when they depart.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Reverb
- Node ID: `94869`
- Entry ID: `117466`
- Definition ID: `122478`
- Spell ID: `443418`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lava Burst gains an additional charge and deals $s2% increased damage.$?a137039[

Riptide gains an additional charge and heals for $s3% more.][]
- Effect: Lava Burst gains an additional charge and deals $s2% increased damage.$?a137039[

Riptide gains an additional charge and heals for $s3% more.][]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Heed My Call
- Node ID: `94884`
- Entry ID: `117481`
- Definition ID: `122493`
- Spell ID: `443444`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ancestors last an additional ${$s1/1000} sec.
- Effect: Ancestors last an additional ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Routine Communication
- Node ID: `94884`
- Entry ID: `123630`
- Definition ID: `128468`
- Spell ID: `443445`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137040[Lightning Bolt, Lava Burst, Flame Shock, Voltaic Blaze, and Chain Lightning have a $s2][Riptide has a $s1]% chance to call an Ancestor to your side for $445624d.
- Effect: $?a137040[Lightning Bolt, Lava Burst, Flame Shock, Voltaic Blaze, and Chain Lightning have a $s2][Riptide has a $s1]% chance to call an Ancestor to your side for $445624d.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Influence
- Node ID: `109732`
- Entry ID: `135990`
- Definition ID: `140745`
- Spell ID: `1270446`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Intellect is increased by ${$s1}.1% for each Ancestor active.
- Effect: Your Intellect is increased by ${$s1}.1% for each Ancestor active.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Offering from Beyond
- Node ID: `94887`
- Entry ID: `117484`
- Definition ID: `122496`
- Spell ID: `443451`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When an Ancestor is called, they reduce the cooldown of $?a137040[Stormkeeper by ${$s1/-1000} sec.][Riptide by ${$s2/-1000} sec.]
- Effect: When an Ancestor is called, they reduce the cooldown of $?a137040[Stormkeeper by ${$s1/-1000} sec.][Riptide by ${$s2/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94862` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primordial Capacity
- Node ID: `94860`
- Entry ID: `117457`
- Definition ID: `122469`
- Spell ID: `443448`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your maximum $?a137040[Maelstrom by $s1.][mana by $s2%.

Tidal Waves can now stack up to ${$s3+$s4} times.]
- Effect: Increases your maximum $?a137040[Maelstrom by $s1.][mana by $s2%.

Tidal Waves can now stack up to ${$s3+$s4} times.]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94884` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spiritwalker's Momentum
- Node ID: `94861`
- Entry ID: `117458`
- Definition ID: `122470`
- Spell ID: `443425`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Using spells with a cast time increases the duration of Spiritwalker's Grace and Spiritwalker's Aegis by ${$s1/1000} sec, up to a maximum of ${$s2/1000} sec.
- Effect: Using spells with a cast time increases the duration of Spiritwalker's Grace and Spiritwalker's Aegis by ${$s1/1000} sec, up to a maximum of ${$s2/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94869` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Windspeaker
- Node ID: `109731`
- Entry ID: `135989`
- Definition ID: `140744`
- Spell ID: `1270447`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cast times of $?c1[Healing Surge, Chain Heal and][Healing Wave, Chain Heal, and] Lava Burst are reduced by $s1%.
- Effect: The cast times of $?c1[Healing Surge, Chain Heal and][Healing Wave, Chain Heal, and] Lava Burst are reduced by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109732` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Natural Harmony
- Node ID: `94858`
- Entry ID: `117455`
- Definition ID: `122467`
- Spell ID: `443442`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Nature's Guardian by ${$s1/-1000} sec and causes it to heal for an additional $s2% of your maximum health.
- Effect: Reduces the cooldown of Nature's Guardian by ${$s1/-1000} sec and causes it to heal for an additional $s2% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94887` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthen Communion
- Node ID: `94858`
- Entry ID: `123631`
- Definition ID: `128469`
- Spell ID: `443441`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Earth Shield has an additional $s1 charges and heals you for $s3% more.
- Effect: Earth Shield has an additional $s1 charges and heals you for $s3% more.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94887` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Maelstrom Supremacy
- Node ID: `94883`
- Entry ID: `117480`
- Definition ID: `122492`
- Spell ID: `443447`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137040[Increases the damage of Earth Shock, Elemental Blast, and Earthquake by $s1%.

Increases the healing of Healing Surge and Chain Heal by $s2%.][Increases the healing done by Healing Wave, Downpour, and Chain Heal by $s2%.]
- Effect: $?a137040[Increases the damage of Earth Shock, Elemental Blast, and Earthquake by $s1%.

Increases the healing of Healing Surge and Chain Heal by $s2%.][Increases the healing done by Healing Wave, Downpour, and Chain Heal by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94860` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Final Calling
- Node ID: `94875`
- Entry ID: `117472`
- Definition ID: `122484`
- Spell ID: `443446`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When an Ancestor departs, they cast $?a137040[Elemental Blast at a nearby enemy.][Hydrobubble on a nearby injured ally.

$@spellicon444490 |cFFFFFFFF$@spellname444490|r
$@spelldesc444490]
- Effect: When an Ancestor departs, they cast $?a137040[Elemental Blast at a nearby enemy.][Hydrobubble on a nearby injured ally.

$@spellicon444490 |cFFFFFFFF$@spellname444490|r
$@spelldesc444490]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94861` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mystic Knowledge
- Node ID: `109730`
- Entry ID: `135988`
- Definition ID: `140743`
- Spell ID: `1270450`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[For $1270453d after casting Nature's Swiftness or Ancestral Swiftness, the recharge rate of Riptide is increased by $1270453s1%.

][]Increases the chance for Lava Surge to occur by $s1%.
- Effect: $?c3[For $1270453d after casting Nature's Swiftness or Ancestral Swiftness, the recharge rate of Riptide is increased by $1270453s1%.

][]Increases the chance for Lava Surge to occur by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109731` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Swiftness
- Node ID: `94894`
- Entry ID: `117491`
- Definition ID: `122503`
- Spell ID: `448861`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc443454
- Effect: $@spelldesc443454
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94858` (type `2`), node `94875` (type `2`), node `94883` (type `2`), node `109730` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cleanse Spirit
- Node ID: `103608`
- Entry ID: `127884`
- Definition ID: `132693`
- Spell ID: `51886`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Removes all Curse effects from a friendly target.
- Effect: Removes all Curse effects from a friendly target.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `103579` (type `2`), node `103622` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
