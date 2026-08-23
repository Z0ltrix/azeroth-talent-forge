# Enhancement

Reviewed build: `12.1.0.69404`
Spec ID: `263`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Lava Lash
- Node ID: `109389`
- Entry ID: `135593`
- Definition ID: `140349`
- Spell ID: `60103`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Charges your off-hand weapon with lava and burns your target, dealing $s1 Fire damage.

Damage is increased by $s2% if your offhand weapon is imbued with Flametongue Weapon. $?s334033[Lava Lash will spread Flame Shock from your target to $s3 nearby targets.][]$?s334046[

Lava Lash increases the damage of Flame Shock on its target by $334168s1% for $334168d.][]
- Effect: Charges your off-hand weapon with lava and burns your target, dealing $s1 Fire damage.

Damage is increased by $s2% if your offhand weapon is imbued with Flametongue Weapon. $?s334033[Lava Lash will spread Flame Shock from your target to $s3 nearby targets.][]$?s334046[

Lava Lash increases the damage of Flame Shock on its target by $334168s1% for $334168d.][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1`
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
