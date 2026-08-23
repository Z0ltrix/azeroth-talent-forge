# Farseer

Reviewed build: `12.1.0.69404`
Hero subtree ID: `56`
Description: Harness your spiritual magic, improving your spell casting capabilities and empowering you to call upon the spirits of your ancestors to aid you and your allies in combat.

## Hero talents

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
