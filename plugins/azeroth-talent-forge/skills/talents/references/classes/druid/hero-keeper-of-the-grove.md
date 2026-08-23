# Keeper of the Grove

Reviewed build: `12.1.0.69404`
Hero subtree ID: `23`
Description: Keepers of the Grove take inspiration from Cenarius' mighty children to protect the balance of nature and safeguard the Dream. They channel the power of the Dream to strengthen their spells and summon empowered treants to protect their allies and crush their enemies.

## Hero talents

### Dream Surge
- Node ID: `94600`
- Entry ID: `117195`
- Definition ID: `122207`
- Spell ID: `433831`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Force of Nature grants $s1 charges of Dream Burst, causing your next Wrath or Starfire to explode on the target, dealing ${$433850s1*(1+$393014s3/100)} Nature damage to nearby enemies. Damage reduced above $433850s2 targets.][When Grove Guardians are summoned, they grow Dream Petals on your target, healing up to $s2 nearby allies for $434141s1.]
- Effect: $?a137013[Force of Nature grants $s1 charges of Dream Burst, causing your next Wrath or Starfire to explode on the target, dealing ${$433850s1*(1+$393014s3/100)} Nature damage to nearby enemies. Damage reduced above $433850s2 targets.][When Grove Guardians are summoned, they grow Dream Petals on your target, healing up to $s2 nearby allies for $434141s1.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Treants of the Moon
- Node ID: `94599`
- Entry ID: `117194`
- Definition ID: `122206`
- Spell ID: `428544`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?a137013[Force of Nature treants][Grove Guardians] cast Moonfire on nearby targets about once every $s1 sec.
- Effect: Your $?a137013[Force of Nature treants][Grove Guardians] cast Moonfire on nearby targets about once every $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expansiveness
- Node ID: `94602`
- Entry ID: `117197`
- Definition ID: `122209`
- Spell ID: `429399`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your maximum mana is increased by $s2%$?a137013[ and your maximum Astral Power is increased by ${$s1/10}][].
- Effect: Your maximum mana is increased by $s2%$?a137013[ and your maximum Astral Power is increased by ${$s1/10}][].
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sylvan Beckoning
- Node ID: `109714`
- Entry ID: `135972`
- Definition ID: `140727`
- Spell ID: `1264614`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Entering an Eclipse summons a Dryad to assist you for $1264618d, casting Starsurge dealing $1264677s1 Astral damage and Starfall at $s2% effectiveness.][Your periodic heals have a chance to empower your next Swiftmend to summon a Dryad to assist you, casting Tranquility at $s1% effectiveness and Regrowth to heal $1264664s1 damage onto your lowest health ally.]
- Effect: $?c1[Entering an Eclipse summons a Dryad to assist you for $1264618d, casting Starsurge dealing $1264677s1 Astral damage and Starfall at $s2% effectiveness.][Your periodic heals have a chance to empower your next Swiftmend to summon a Dryad to assist you, casting Tranquility at $s1% effectiveness and Regrowth to heal $1264664s1 damage onto your lowest health ally.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Protective Growth
- Node ID: `94593`
- Entry ID: `117186`
- Definition ID: `122198`
- Spell ID: `433748`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Regrowth protects you, reducing damage you take by $s1% while your Regrowth is on you.
- Effect: Your Regrowth protects you, reducing damage you take by $s1% while your Regrowth is on you.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94600` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dryad's Dance
- Node ID: `109713`
- Entry ID: `135971`
- Definition ID: `140726`
- Spell ID: `1264776`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c4[Dryads cause Swiftmend to cool down $1264618s3% faster.][Dryads cause most of your Astral power generation to be increased by $1264618s4%.]
- Effect: $?c4[Dryads cause Swiftmend to cool down $1264618s3% faster.][Dryads cause most of your Astral power generation to be increased by $1264618s4%.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109714` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Power of Nature
- Node ID: `94605`
- Entry ID: `117201`
- Definition ID: `122213`
- Spell ID: `428859`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Your Force of Nature treants no longer taunt and deal $449001s1% increased melee damage.][Your Grove Guardians increase the healing of your Rejuvenation, Efflorescence, and Lifebloom by $428866s1% while active.]
- Effect: $?a137013[Your Force of Nature treants no longer taunt and deal $449001s1% increased melee damage.][Your Grove Guardians increase the healing of your Rejuvenation, Efflorescence, and Lifebloom by $428866s1% while active.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94599` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Durability of Nature
- Node ID: `94605`
- Entry ID: `117200`
- Definition ID: `122212`
- Spell ID: `429227`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Your Force of Nature treants have $s1% increased health.][Grove Guardians last $s2% longer.]
- Effect: $?c1[Your Force of Nature treants have $s1% increased health.][Grove Guardians last $s2% longer.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94599` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cenarius' Might
- Node ID: `94604`
- Entry ID: `117199`
- Definition ID: `122211`
- Spell ID: `455797`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Entering Eclipse increases your haste by $455801s1% for $455801d][Swiftmend healing is increased by $s2%].
- Effect: $?a137013[Entering Eclipse increases your haste by $455801s1% for $455801d][Swiftmend healing is increased by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94602` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Grove's Inspiration
- Node ID: `94595`
- Entry ID: `117189`
- Definition ID: `122201`
- Spell ID: `429402`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Wrath and Starfire damage increased by $s1%. 

Regrowth$?a137013[ and Wild Growth][, Wild Growth, and Swiftmend] healing increased by $s2%.
- Effect: Wrath and Starfire damage increased by $s1%. 

Regrowth$?a137013[ and Wild Growth][, Wild Growth, and Swiftmend] healing increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94593` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Potent Enchantments
- Node ID: `94595`
- Entry ID: `117188`
- Definition ID: `122200`
- Spell ID: `429420`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Orbital Strike damage increased by $s3%, and damage of Stellar Flares it applies increased by $s2%.

Whirling Stars increases the haste you gain during ][]$?c1&s394013[Incarnation: Chosen of Elune]?c1[Celestial Alignment][]$?c1[ by an additional $s4%.][Reforestation grants Tree of Life for $s5 additional sec.]
- Effect: $?c1[Orbital Strike damage increased by $s3%, and damage of Stellar Flares it applies increased by $s2%.

Whirling Stars increases the haste you gain during ][]$?c1&s394013[Incarnation: Chosen of Elune]?c1[Celestial Alignment][]$?c1[ by an additional $s4%.][Reforestation grants Tree of Life for $s5 additional sec.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94593` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spirit of the Thicket
- Node ID: `109712`
- Entry ID: `135970`
- Definition ID: `140725`
- Spell ID: `1264899`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c4[Ironbark summons a Dryad to channel a beam of pure nature onto your target, healing them for $1264905o1 over $1264905d.][Your Starfall damage is increased by $s1% and your Starsurge damage is increased by $s2%.]
- Effect: $?c4[Ironbark summons a Dryad to channel a beam of pure nature onto your target, healing them for $1264905o1 over $1264905d.][Your Starfall damage is increased by $s1% and your Starsurge damage is increased by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109713` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bounteous Bloom
- Node ID: `94591`
- Entry ID: `117184`
- Definition ID: `122196`
- Spell ID: `429215`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Force of Nature Treants last ${$s2/1000} sec longer.][Your Grove Guardians' healing is increased by $s1%.]
- Effect: $?a137013[Force of Nature Treants last ${$s2/1000} sec longer.][Your Grove Guardians' healing is increased by $s1%.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94605` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Early Spring
- Node ID: `94591`
- Entry ID: `117895`
- Definition ID: `122907`
- Spell ID: `428937`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137013[Force of Nature cooldown reduced by ${$s1/-1000} sec.][Swiftmend and Wild Growth cooldowns reduced by ${$s2/-1000} sec.]
- Effect: $?a137013[Force of Nature cooldown reduced by ${$s1/-1000} sec.][Swiftmend and Wild Growth cooldowns reduced by ${$s2/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94605` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Power of the Dream
- Node ID: `94592`
- Entry ID: `117185`
- Definition ID: `122197`
- Spell ID: `434220`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Force of Nature grants an additional stack of Dream Burst.][Dream Surge heals $s2 additional $Lally:allies;.]
- Effect: $?a137013[Force of Nature grants an additional stack of Dream Burst.][Dream Surge heals $s2 additional $Lally:allies;.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94604` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Control of the Dream
- Node ID: `94592`
- Entry ID: `117894`
- Definition ID: `122906`
- Spell ID: `434249`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Time elapsed while your major abilities are available to be used or at maximum charges is subtracted from that ability's cooldown after the next time you use it, up to $s1 seconds.

Affects $?a137012[Nature's Swiftness, Incarnation: Tree of Life,][Force of Nature,] $?a137012[]?a394013[Incarnation: Chosen of Elune, ][Celestial Alignment, ]and Convoke the Spirits.
- Effect: Time elapsed while your major abilities are available to be used or at maximum charges is subtracted from that ability's cooldown after the next time you use it, up to $s1 seconds.

Affects $?a137012[Nature's Swiftness, Incarnation: Tree of Life,][Force of Nature,] $?a137012[]?a394013[Incarnation: Chosen of Elune, ][Celestial Alignment, ]and Convoke the Spirits.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94604` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blooming Infusion
- Node ID: `94601`
- Entry ID: `117196`
- Definition ID: `122208`
- Spell ID: `429433`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 Regrowths you cast makes your next Wrath, Starfire, or Entangling Roots instant and increases damage it deals by $429474s2%.

Every $s1 Starsurges $?a137013[or Starfalls ][]you cast makes your next Regrowth or Entangling roots instant.
- Effect: Every $s1 Regrowths you cast makes your next Wrath, Starfire, or Entangling Roots instant and increases damage it deals by $429474s2%.

Every $s1 Starsurges $?a137013[or Starfalls ][]you cast makes your next Regrowth or Entangling roots instant.
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94595` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Harmony of the Grove
- Node ID: `94606`
- Entry ID: `117203`
- Definition ID: `122215`
- Spell ID: `428731`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137013[Each of your Force of Nature treants increases damage your spells deal by $428735s1% while active.][Each of your Grove Guardians increases your healing done by $428737s1% while active.]
- Effect: $?a137013[Each of your Force of Nature treants increases damage your spells deal by $428735s1% while active.][Each of your Grove Guardians increases your healing done by $428737s1% while active.]
- Point cost per purchased rank: `1` × Hero pool (Keeper of the Grove) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94591` (type `2`), node `94592` (type `2`), node `94601` (type `2`), node `109712` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
