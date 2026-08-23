# Pack Leader

Reviewed build: `12.1.0.69404`
Hero subtree ID: `43`
Description: Pack Leaders have formed a deep bond with their animal companions and nature itself, allowing the Hunter and their pack to hunt with a vicious coordination on the battlefield and summon aid from powerful beasts.

## Hero talents

### Howl of the Pack Leader
- Node ID: `94991`
- Entry ID: `117588`
- Definition ID: `122600`
- Spell ID: `471876`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While in combat, every $471877d your next Kill Command summons the aid of a Beast.

$@spellicon471881 Wyvern
A Wyvern descends from the skies, letting out a battle cry that increases the damage of you and your pets by ${$471881s1*$s3}% for $471881d.

$@spellicon471936 Boar
A Boar charges through your target $s2 $Ltime:times;, dealing $471938s1 damage to nearby enemies and an additional $471936s1 physical damage to its primary target. Damage reduced beyond $471938s2 targets.

$@spellicon471993 Bear
A Bear leaps into the fray, rending the flesh of your enemies, dealing $471999o1 damage over $471999d to up to $471999s2 nearby enemies.
- Effect: While in combat, every $471877d your next Kill Command summons the aid of a Beast.

$@spellicon471881 Wyvern
A Wyvern descends from the skies, letting out a battle cry that increases the damage of you and your pets by ${$471881s1*$s3}% for $471881d.

$@spellicon471936 Boar
A Boar charges through your target $s2 $Ltime:times;, dealing $471938s1 damage to nearby enemies and an additional $471936s1 physical damage to its primary target. Damage reduced beyond $471938s2 targets.

$@spellicon471993 Bear
A Bear leaps into the fray, rending the flesh of your enemies, dealing $471999o1 damage over $471999d to up to $471999s2 nearby enemies.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pack Mentality
- Node ID: `94985`
- Entry ID: `117582`
- Definition ID: `122594`
- Spell ID: `472358`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Howl of the Pack Leader increases the damage of your Kill Command by $s1%.

Summoning a Beast reduces the cooldown of $?c1[Barbed Shot][Wildfire Bomb] by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec.
- Effect: Howl of the Pack Leader increases the damage of your Kill Command by $s1%.

Summoning a Beast reduces the cooldown of $?c1[Barbed Shot][Wildfire Bomb] by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dire Summons
- Node ID: `94992`
- Entry ID: `117589`
- Definition ID: `122601`
- Spell ID: `472352`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Kill Command reduces the cooldown of Howl of the Pack Leader by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec.

$?s259387[Mongoose Bite]?a137017[Raptor Strike][Cobra Shot] reduces the cooldown of Howl of the Pack Leader by $?c1[${$s3/1000}.1][${$s4/1000}.1] sec.
- Effect: Kill Command reduces the cooldown of Howl of the Pack Leader by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec.

$?s259387[Mongoose Bite]?a137017[Raptor Strike][Cobra Shot] reduces the cooldown of Howl of the Pack Leader by $?c1[${$s3/1000}.1][${$s4/1000}.1] sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Better Together
- Node ID: `94962`
- Entry ID: `117559`
- Definition ID: `122571`
- Spell ID: `472357`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage dealt by your pet$?c1[s][] is increased by $?c1[$s1][$s2]%.

$?c1[Barbed Shot damage increased by $s4%][Raptor Strike damage increased by $s3%].
- Effect: Damage dealt by your pet$?c1[s][] is increased by $?c1[$s1][$s2]%.

$?c1[Barbed Shot damage increased by $s4%][Raptor Strike damage increased by $s3%].
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slicked Shoes
- Node ID: `94979`
- Entry ID: `117576`
- Definition ID: `122588`
- Spell ID: `472719`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Disengage removes a movement impairing effect, its cooldown is reduced by ${$s1/1000} sec.
- Effect: When Disengage removes a movement impairing effect, its cooldown is reduced by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Masterful Call
- Node ID: `94979`
- Entry ID: `123781`
- Definition ID: `128619`
- Spell ID: `1268705`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The duration of Master's Call is increased by ${$s1/1000} sec and it increases the movement speed of its target by $s2%.
- Effect: The duration of Master's Call is increased by ${$s1/1000} sec and it increases the movement speed of its target by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94991` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ursine Fury
- Node ID: `94972`
- Entry ID: `117569`
- Definition ID: `122581`
- Spell ID: `472476`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Bear is summoned, it is joined by $s1 Dire $LBeast:Beasts;.
- Effect: When your Bear is summoned, it is joined by $s1 Dire $LBeast:Beasts;.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94985` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sharpened Claws
- Node ID: `94972`
- Entry ID: `128358`
- Definition ID: `133164`
- Spell ID: `472524`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The damage of your Bear's Rend Flesh is increased by $s1%.
- Effect: The damage of your Bear's Rend Flesh is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94985` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fury of the Wyvern
- Node ID: `94984`
- Entry ID: `117581`
- Definition ID: `122593`
- Spell ID: `472550`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your pet's attacks increase your Wyvern's damage bonus by $471881s1%, up to $s1%.

Casting $?c1[Kill Command][Wildfire Bomb] extends the duration of your Wyvern by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec, up to $?c1[$s4][$s5] additional sec.
- Effect: Your pet's attacks increase your Wyvern's damage bonus by $471881s1%, up to $s1%.

Casting $?c1[Kill Command][Wildfire Bomb] extends the duration of your Wyvern by $?c1[${$s2/1000}.1][${$s3/1000}.1] sec, up to $?c1[$s4][$s5] additional sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94992` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hogstrider
- Node ID: `94988`
- Entry ID: `117585`
- Definition ID: `122597`
- Spell ID: `472639`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[When your Boar deals damage, the damage of your next Cobra Shot is increased by $472640s1%.

Each additional enemy damaged by your Boar causes Cobra Shot to strike $472640s3 additional $Ltarget:targets;, up to $472640u][Each time your Boar deals damage, the damage of your next Boomstick is increased by $472640s2%, up to ${$472640s2*$472640u}%].
- Effect: $?c1[When your Boar deals damage, the damage of your next Cobra Shot is increased by $472640s1%.

Each additional enemy damaged by your Boar causes Cobra Shot to strike $472640s3 additional $Ltarget:targets;, up to $472640u][Each time your Boar deals damage, the damage of your next Boomstick is increased by $472640s2%, up to ${$472640s2*$472640u}%].
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94962` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lethal Barbs
- Node ID: `109803`
- Entry ID: `136061`
- Definition ID: `140816`
- Spell ID: `1264781`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your $?c1[auto shot][auto attacks] have a very high chance to grant$?c1[s][] $1264783s1 Focus to you and your pet.

$?c1[Auto shot][Auto attack] damage increased by $?c1[$s2][$s3]%.
- Effect: Your $?c1[auto shot][auto attacks] have a very high chance to grant$?c1[s][] $1264783s1 Focus to you and your pet.

$?c1[Auto shot][Auto attack] damage increased by $?c1[$s2][$s3]%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94979` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### No Mercy
- Node ID: `94969`
- Entry ID: `117566`
- Definition ID: `122578`
- Spell ID: `472660`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Bleed effects deal $?c1[$s1][$s2]% increased damage.
- Effect: Your Bleed effects deal $?c1[$s1][$s2]% increased damage.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94972` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shell Cover
- Node ID: `94967`
- Entry ID: `117564`
- Definition ID: `122576`
- Spell ID: `472707`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Survival of the Fittest now summons a Turtle to aid you, further increasing its damage reduction effect by ${-$s1}%.
- Effect: Survival of the Fittest now summons a Turtle to aid you, further increasing its damage reduction effect by ${-$s1}%.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94984` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hoof and Blade
- Node ID: `109804`
- Entry ID: `136062`
- Definition ID: `140817`
- Spell ID: `1264797`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Hogstrider further increases the damage of Cobra Shot by $s1% and it now strikes up to $s3 additional targets][Hogstrider further increases the damage of Boomstick by $s2%].
- Effect: $?c1[Hogstrider further increases the damage of Cobra Shot by $s1% and it now strikes up to $s3 additional targets][Hogstrider further increases the damage of Boomstick by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wyvern's Gaze
- Node ID: `109804`
- Entry ID: `136236`
- Definition ID: `141009`
- Spell ID: `1264792`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The damage bonus from your Wyvern now lasts an additional ${$s2/1000}.1 sec.
- Effect: The damage bonus from your Wyvern now lasts an additional ${$s2/1000}.1 sec.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sharpened Fangs
- Node ID: `109802`
- Entry ID: `136060`
- Definition ID: `140815`
- Spell ID: `1264775`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your mastery is increased by $s1%.$?c3[

Wildfire Bomb deals an additional $s2% increased damage to its primary target.][]
- Effect: Your mastery is increased by $s1%.$?c3[

Wildfire Bomb deals an additional $s2% increased damage to its primary target.][]
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109803` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stampede!
- Node ID: `94966`
- Entry ID: `117563`
- Definition ID: `122575`
- Spell ID: `472741`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?c1[Bestial Wrath][Takedown] grants Howl of the Pack Leader and causes your next Kill Command to rouse the nearby wildlife into a Stampede, charging your target and dealing ${$201594s1* $s1} Physical damage over $201430d.
- Effect: Casting $?c1[Bestial Wrath][Takedown] grants Howl of the Pack Leader and causes your next Kill Command to rouse the nearby wildlife into a Stampede, charging your target and dealing ${$201594s1* $s1} Physical damage over $201430d.
- Point cost per purchased rank: `1` × Hero pool (Pack Leader) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94967` (type `2`), node `94969` (type `2`), node `109802` (type `2`), node `109804` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
