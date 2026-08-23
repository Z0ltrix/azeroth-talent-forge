# Totemic

Reviewed build: `12.1.0.69404`
Hero subtree ID: `54`
Description: Totemic shamans excel at unlocking the full power of their totems, strengthening their totems and gaining access to new ones. They also hone their imbuement skills to maintain their threat up close.

## Hero talents

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
