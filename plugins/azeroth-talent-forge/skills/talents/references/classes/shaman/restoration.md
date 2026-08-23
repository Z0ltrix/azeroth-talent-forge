# Restoration

Reviewed build: `12.1.0.69404`
Spec ID: `264`
Role: `1`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Chain Heal
- Node ID: `103588`
- Entry ID: `127861`
- Definition ID: `132670`
- Spell ID: `1064`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals the friendly target for $s1, then jumps up to $?a236502[${$s3*(($236502s2/100)+1)}][$s3] yards to heal the $<jumps> most injured nearby allies. Healing is reduced by $s2% with each jump.
- Effect: Heals the friendly target for $s1, then jumps up to $?a236502[${$s3*(($236502s2/100)+1)}][$s3] yards to heal the $<jumps> most injured nearby allies. Healing is reduced by $s2% with each jump.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Totemic Rebound
- Node ID: `94890`
- Entry ID: `117487`
- Definition ID: `122499`
- Spell ID: `445025`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Lightning Bolt, Chain Lightning and Elemental Blast has a chance to unleash a Surging Bolt at your Surging Totem, increasing the totem's damage by $458269s1%, and then redirecting the bolt to your target for $458267s1 Nature damage. The damage bonus effect can stack.][Chain Heal now jumps to a nearby totem within $458357A3 yards once it reaches its last target, causing the totem to cast Chain Heal on an injured ally within $458357r yards for $458357s1. Jumps to $s1 nearby targets within $458357A3 yards.]
- Effect: $?a137041[Lightning Bolt, Chain Lightning and Elemental Blast has a chance to unleash a Surging Bolt at your Surging Totem, increasing the totem's damage by $458269s1%, and then redirecting the bolt to your target for $458267s1 Nature damage. The damage bonus effect can stack.][Chain Heal now jumps to a nearby totem within $458357A3 yards once it reaches its last target, causing the totem to cast Chain Heal on an injured ally within $458357r yards for $458357s1. Jumps to $s1 nearby targets within $458357A3 yards.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Amplification Core
- Node ID: `94874`
- Entry ID: `117471`
- Definition ID: `122483`
- Spell ID: `445029`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Surging Totem is active, your damage and healing done is increased by $456369s1%.
- Effect: While Surging Totem is active, your damage and healing done is increased by $456369s1%.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Oversurge
- Node ID: `94874`
- Entry ID: `125823`
- Definition ID: `130654`
- Spell ID: `445030`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Surging Totem $?a462110[heals for $s1% more][deals $s2% more damage] while Ascendance or Healing Tide Totem is active.
- Effect: Surging Totem $?a462110[heals for $s1% more][deals $s2% more damage] while Ascendance or Healing Tide Totem is active.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lively Totems
- Node ID: `94882`
- Entry ID: `117479`
- Definition ID: `122491`
- Spell ID: `445034`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Lava Lash has a chance to summon a Searing Totem to hurl Searing Bolts that deal $3606s1 Fire damage to a nearby enemy. Lasts $458101d.

Lava Lash and Voltaic Blaze cause your Searing Totems to shoot a Searing Volley at up to $s3 nearby enemies for $458147s1 Fire damage.][When you summon a Healing Tide Totem, Healing Stream Totem, or Spirit Link Totem you cast a free instant Chain Heal at $458221s2% effectiveness.]
- Effect: $?a137041[Lava Lash has a chance to summon a Searing Totem to hurl Searing Bolts that deal $3606s1 Fire damage to a nearby enemy. Lasts $458101d.

Lava Lash and Voltaic Blaze cause your Searing Totems to shoot a Searing Volley at up to $s3 nearby enemies for $458147s1 Fire damage.][When you summon a Healing Tide Totem, Healing Stream Totem, or Spirit Link Totem you cast a free instant Chain Heal at $458221s2% effectiveness.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Momentum
- Node ID: `109726`
- Entry ID: `135984`
- Definition ID: `140739`
- Spell ID: `1260644`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Lava Lash damage increased by $s2%.

Each stack of Maelstrom Weapon consumed increases the duration of an active Hot Hand by ${$s1/1000}.2 sec.][Reduces the cooldown of Healing Stream Totem by ${$s3/-1000} sec.]
- Effect: $?c2[Lava Lash damage increased by $s2%.

Each stack of Maelstrom Weapon consumed increases the duration of an active Hot Hand by ${$s1/1000}.2 sec.][Reduces the cooldown of Healing Stream Totem by ${$s3/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
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
### Oversized Totems
- Node ID: `94859`
- Entry ID: `117456`
- Definition ID: `122468`
- Spell ID: `445026`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the size and radius of your totems by $458016s2%, and the health of your totems by $458016s1%.
- Effect: Increases the size and radius of your totems by $458016s2%, and the health of your totems by $458016s1%.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94890` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swift Recall
- Node ID: `94859`
- Entry ID: `125825`
- Definition ID: `130656`
- Spell ID: `445027`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Successfully removing a harmful effect with Tremor Totem or Poison Cleansing Totem, or controlling an enemy with Capacitor Totem or Earthgrab Totem reduces the cooldown of the totem used by $/1000;s1 sec.

Cannot occur more than once every $457676d per totem.
- Effect: Successfully removing a harmful effect with Tremor Totem or Poison Cleansing Totem, or controlling an enemy with Capacitor Totem or Earthgrab Totem reduces the cooldown of the totem used by $/1000;s1 sec.

Cannot occur more than once every $457676d per totem.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94890` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wind Barrier
- Node ID: `94891`
- Entry ID: `117488`
- Definition ID: `122500`
- Spell ID: `445031`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If you have a totem active, your totem grants you a shield absorbing ${$mhp*$s1/100} damage for $457387d every $457390d.
- Effect: If you have a totem active, your totem grants you a shield absorbing ${$mhp*$s1/100} damage for $457387d every $457390d.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94874` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Splitstream
- Node ID: `94872`
- Entry ID: `117469`
- Definition ID: `122481`
- Spell ID: `445035`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[While Hot Hand is active Lava Lash shatters the earth, causing a Sundering at $s1% effectiveness.][Your Healing Stream Totems heals an additional ally at $s3% effectiveness.

Healing Tide Totem healing increased by $s2%.]
- Effect: $?a137041[While Hot Hand is active Lava Lash shatters the earth, causing a Sundering at $s1% effectiveness.][Your Healing Stream Totems heals an additional ally at $s3% effectiveness.

Healing Tide Totem healing increased by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94882` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Attunement
- Node ID: `109725`
- Entry ID: `135983`
- Definition ID: `140738`
- Spell ID: `1263288`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Mastery increased by $s1%.
- Effect: Mastery increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109726` (type `2`)
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
### Imbuement Mastery
- Node ID: `94871`
- Entry ID: `117468`
- Definition ID: `122480`
- Spell ID: `445028`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Increases the chance for Windfury Weapon to trigger by $s1% and increases its damage by $s2%.

When Flametongue Weapon triggers from Windfury Weapon attacks, it has a chance to gather a whirl of flame around the target, dealing $s5% of its damage to all nearby enemies.][Increases the duration of your Earthliving effect by ${$s3/1000} sec.]
- Effect: $?a137041[Increases the chance for Windfury Weapon to trigger by $s1% and increases its damage by $s2%.

When Flametongue Weapon triggers from Windfury Weapon attacks, it has a chance to gather a whirl of flame around the target, dealing $s5% of its damage to all nearby enemies.][Increases the duration of your Earthliving effect by ${$s3/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94859` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pulse Capacitor
- Node ID: `94866`
- Entry ID: `117463`
- Definition ID: `122475`
- Spell ID: `445032`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Increases the damage of Surging Totem by $s1%.][Increases the healing done by Surging Totem by $s2%.]
- Effect: $?a137041[Increases the damage of Surging Totem by $s1%.][Increases the healing done by Surging Totem by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94891` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Supportive Imbuements
- Node ID: `94866`
- Entry ID: `125824`
- Definition ID: `130655`
- Spell ID: `445033`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137041[Increases the critical strike chance of Flametongue Weapon by $s1%, and its critical strike damage by $s2%.][Learn a new weapon imbue, Tidecaller's Guard.

$@spellicon457481 $@spellname457481
$@spelldesc457481 ]
- Effect: $?a137041[Increases the critical strike chance of Flametongue Weapon by $s1%, and its critical strike damage by $s2%.][Learn a new weapon imbue, Tidecaller's Guard.

$@spellicon457481 $@spellname457481
$@spelldesc457481 ]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94891` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Coordination
- Node ID: `94881`
- Entry ID: `117478`
- Definition ID: `122490`
- Spell ID: `445036`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Increases the critical strike chance of your Searing Totem's attacks by $s1%, and its critical strike damage by $s2%.][Chain Heals from Lively Totem and Totemic Rebound are $s3% more effective.]
- Effect: $?a137041[Increases the critical strike chance of your Searing Totem's attacks by $s1%, and its critical strike damage by $s2%.][Chain Heals from Lively Totem and Totemic Rebound are $s3% more effective.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94872` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthsurge
- Node ID: `94881`
- Entry ID: `125822`
- Definition ID: `130653`
- Spell ID: `455590`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137041[Casting Sundering within $s2 yards of your Surging Totem causes it to create a Tremor at $s1% effectiveness at the target area.][Allies affected by your Earthliving effect receive $s3% increased healing from you.]
- Effect: $?a137041[Casting Sundering within $s2 yards of your Surging Totem causes it to create a Tremor at $s1% effectiveness at the target area.][Allies affected by your Earthliving effect receive $s3% increased healing from you.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94872` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primal Catalyst
- Node ID: `109724`
- Entry ID: `135982`
- Definition ID: `140737`
- Spell ID: `1260874`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[After casting Surging Totem, your next Lava Lash casts again at $s1% effectiveness.][Healing Stream Totem and Healing Tide Totem healing has a $s2% chance to apply Earthliving to allies it heals.]
- Effect: $?c2[After casting Surging Totem, your next Lava Lash casts again at $s1% effectiveness.][Healing Stream Totem and Healing Tide Totem healing has a $s2% chance to apply Earthliving to allies it heals.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109725` (type `2`)
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
### Whirling Elements
- Node ID: `94879`
- Entry ID: `117476`
- Definition ID: `122488`
- Spell ID: `445024`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Elemental motes orbit around your Surging Totem. Your abilities consume the motes for enhanced effects. 

$?a137041[|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406

|cFFFFFFFFFire:|r $@spelldesc453405][|cFFFFFFFFWater:|r $@spelldesc453407

|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406]
- Effect: Elemental motes orbit around your Surging Totem. Your abilities consume the motes for enhanced effects. 

$?a137041[|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406

|cFFFFFFFFFire:|r $@spelldesc453405][|cFFFFFFFFWater:|r $@spelldesc453407

|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94866` (type `2`), node `94871` (type `2`), node `94881` (type `2`), node `109724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Purify Spirit
- Node ID: `81073`
- Entry ID: `101964`
- Definition ID: `106962`
- Spell ID: `383016`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Purify Spirit additionally removes all Curse effects.
- Effect: Purify Spirit additionally removes all Curse effects.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
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
