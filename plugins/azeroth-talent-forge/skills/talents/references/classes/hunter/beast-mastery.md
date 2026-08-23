# Beast Mastery

Reviewed build: `12.1.0.69404`
Spec ID: `253`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Black Arrow
- Node ID: `94987`
- Entry ID: `117584`
- Definition ID: `122596`
- Spell ID: `466932`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Kill Shot is replaced with Black Arrow.

$@spellicon466930 $@spellname466930
$@spelldesc466930
- Effect: Your Kill Shot is replaced with Black Arrow.

$@spellicon466930 $@spellname466930
$@spelldesc466930
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Black Arrow
- Node ID: `109961`
- Entry ID: `136446`
- Definition ID: `141219`
- Spell ID: `466930`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You attempt to finish off a wounded target, dealing $s1 Shadow damage and $468572o1 Shadow damage over $468572d. Only usable on enemies above $s3% health or below $s2% health.
- Effect: You attempt to finish off a wounded target, dealing $s1 Shadow damage and $468572o1 Shadow damage over $468572d. Only usable on enemies above $s3% health or below $s2% health.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sentinel
- Node ID: `94976`
- Entry ID: `117573`
- Definition ID: `122585`
- Spell ID: `1253599`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Consuming Tip of the Spear has a $s2% chance to summon the aid of a Sentinel Owl that descends from the skies and applies Sentinel's Mark to your target][Your Eagle is replaced with a Sentinel Owl that applies an enhanced Sentinel's Mark].

$@spellicon1253601$@spellname1253601
$@spellaura1253601
- Effect: $?c3[Consuming Tip of the Spear has a $s2% chance to summon the aid of a Sentinel Owl that descends from the skies and applies Sentinel's Mark to your target][Your Eagle is replaced with a Sentinel Owl that applies an enhanced Sentinel's Mark].

$@spellicon1253601$@spellname1253601
$@spellaura1253601
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Survival of the Fittest
- Node ID: `102422`
- Entry ID: `126488`
- Definition ID: `131314`
- Spell ID: `264735`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces all damage you and your pet take by $s1% for $d.
- Effect: Reduces all damage you and your pet take by $s1% for $d.
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bleak Arrows
- Node ID: `94961`
- Entry ID: `117558`
- Definition ID: `122570`
- Spell ID: `467749`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto shot now deals Shadow damage, allowing it to bypass armor.

Auto shot damage increased by $s3%.
- Effect: Your auto shot now deals Shadow damage, allowing it to bypass armor.

Auto shot damage increased by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94987` (type `2`), node `109961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Soul Drinker
- Node ID: `94968`
- Entry ID: `117565`
- Definition ID: `122577`
- Spell ID: `469638`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Kill Command has a $s1% chance and Barbed Shot has a $s2% chance to grant Deathblow.
][Aimed Shot's chance to grant Deathblow is increased by $s3%. Rapid Fire has a $s4% chance to grant Deathblow.]
$@spellicon378770 $@spellname378770
The cooldown of $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] is reset. Your next $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] can be used on any target, regardless of their current health.
- Effect: $?c1[Kill Command has a $s1% chance and Barbed Shot has a $s2% chance to grant Deathblow.
][Aimed Shot's chance to grant Deathblow is increased by $s3%. Rapid Fire has a $s4% chance to grant Deathblow.]
$@spellicon378770 $@spellname378770
The cooldown of $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] is reset. Your next $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] can be used on any target, regardless of their current health.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94987` (type `2`), node `109961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bleak Powder
- Node ID: `94974`
- Entry ID: `117571`
- Definition ID: `122583`
- Spell ID: `467911`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Black Arrow now explodes in a cloud of shadow and sulfur on impact, dealing $?c1[$472084s1][$467914s1] Shadow damage to all enemies within an $s2 yd cone behind the target. Damage reduced beyond $s2 targets.
- Effect: Black Arrow now explodes in a cloud of shadow and sulfur on impact, dealing $?c1[$472084s1][$467914s1] Shadow damage to all enemies within an $s2 yd cone behind the target. Damage reduced beyond $s2 targets.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94987` (type `2`), node `109961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Corpsecaller
- Node ID: `109801`
- Entry ID: `136059`
- Definition ID: `140814`
- Spell ID: `1264289`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[When summoning a Dire Beast, you have a $s1% chance to instead summon a Dark Hound that deals significantly increased damage.][Black Arrow's periodic damage has a small chance to rouse the dead, summoning a Dark Minion to fight alongside you for $1264345d.]
- Effect: $?c1[When summoning a Dire Beast, you have a $s1% chance to instead summon a Dark Hound that deals significantly increased damage.][Black Arrow's periodic damage has a small chance to rouse the dead, summoning a Dark Minion to fight alongside you for $1264345d.]
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94987` (type `2`), node `109961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ebon Bowstring
- Node ID: `94986`
- Entry ID: `117583`
- Definition ID: `122595`
- Spell ID: `467897`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Black Arrow has a $s1% chance to grant Deathblow.

$@spellicon378770 $@spellname378770
The cooldown of $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] is reset. Your next $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] can be used on any target, regardless of their current health.
- Effect: Casting Black Arrow has a $s1% chance to grant Deathblow.

$@spellicon378770 $@spellname378770
The cooldown of $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] is reset. Your next $?a137015[Black Arrow]?a466932[Black Arrow][Kill Shot] can be used on any target, regardless of their current health.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Through the Eyes
- Node ID: `94986`
- Entry ID: `136742`
- Definition ID: `141514`
- Spell ID: `1277565`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a466932[Black Arrow][Kill Shot] damage increased by $s1%.
- Effect: $?a466932[Black Arrow][Kill Shot] damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Smoke Screen
- Node ID: `94959`
- Entry ID: `123779`
- Definition ID: `128617`
- Spell ID: `430709`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Exhilaration grants you $s1 sec of Survival of the Fittest.

Survival of the Fittest activates Exhilaration at $s2% effectiveness.
- Effect: Exhilaration grants you $s1 sec of Survival of the Fittest.

Survival of the Fittest activates Exhilaration at $s2% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94968` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Chains
- Node ID: `94960`
- Entry ID: `117557`
- Definition ID: `122569`
- Spell ID: `430712`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While in combat, Disengage will chain the closest target to the ground, causing them to move $442396s1% slower until they move $s1 yards away.
- Effect: While in combat, Disengage will chain the closest target to the ground, causing them to move $442396s1% slower until they move $s1 yards away.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94974` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadow Dagger
- Node ID: `94960`
- Entry ID: `128219`
- Definition ID: `133026`
- Spell ID: `467741`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: While in combat, Disengage releases a fan of shadow daggers, dealing $467745s1 Shadow damage per second and reducing affected target's movement speed by $467745s2% for $467745d.
- Effect: While in combat, Disengage releases a fan of shadow daggers, dealing $467745s1 Shadow damage per second and reducing affected target's movement speed by $467745s2% for $467745d.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94974` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wailing Dead
- Node ID: `109800`
- Entry ID: `136058`
- Definition ID: `140813`
- Spell ID: `1264290`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Bestial Wrath][Trueshot] summons a $?c1[Dark Hound][Dark Minion].

For $459808d after casting $?c1[Bestial Wrath][Trueshot], $?c1[Bestial Wrath][Trueshot] is replaced with Wailing Arrow.

$@spellicon392060 $@spellname392060
$@spelldesc392060
- Effect: $?c1[Bestial Wrath][Trueshot] summons a $?c1[Dark Hound][Dark Minion].

For $459808d after casting $?c1[Bestial Wrath][Trueshot], $?c1[Bestial Wrath][Trueshot] is replaced with Wailing Arrow.

$@spellicon392060 $@spellname392060
$@spelldesc392060
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109801` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blighted Quiver
- Node ID: `94983`
- Entry ID: `128238`
- Definition ID: `133045`
- Spell ID: `1264291`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: You fire $s1 additional Black Arrows during Withering Fire's barrage.

$?a137016[Trick Shots damage bonus increased by $s3%. Aspect of the Hydra's damage bonus increased by $s4%][Beast Cleave and Kill Cleave damage increased by $s5%].
- Effect: You fire $s1 additional Black Arrows during Withering Fire's barrage.

$?a137016[Trick Shots damage bonus increased by $s3%. Aspect of the Hydra's damage bonus increased by $s4%][Beast Cleave and Kill Cleave damage increased by $s5%].
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94986` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Banshee's Mark
- Node ID: `94957`
- Entry ID: `117554`
- Definition ID: `122566`
- Spell ID: `467902`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Black Arrow and Bleak Powder critical strike damage increased by $s1%.
- Effect: Black Arrow and Bleak Powder critical strike damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94959` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### The Bell Tolls
- Node ID: `94957`
- Entry ID: `136231`
- Definition ID: `141004`
- Spell ID: `467644`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[All pet damage increased by $s2%][Critical strike chance increased by $s1%].

$?c1[Dire Beast damage increased by $s3%][Dark Minion damage increased by $s4%].
- Effect: $?c1[All pet damage increased by $s2%][Critical strike chance increased by $s1%].

$?c1[Dire Beast damage increased by $s3%][Dark Minion damage increased by $s4%].
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94959` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Umbral Reach
- Node ID: `94982`
- Entry ID: `132888`
- Definition ID: `137674`
- Spell ID: `1235397`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Bleak Powder now applies Black Arrow's periodic effect to all enemies it damages.

If Bleak Powder damages $s2 or more enemies, gain $?c1[Beast Cleave][Trick Shots] if talented.
- Effect: Bleak Powder now applies Black Arrow's periodic effect to all enemies it damages.

If Bleak Powder damages $s2 or more enemies, gain $?c1[Beast Cleave][Trick Shots] if talented.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94960` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pact of the Hollow
- Node ID: `109799`
- Entry ID: `136057`
- Definition ID: `140812`
- Spell ID: `1264690`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Kill Command causes your Dark Hound to Shadow Thrash, dealing $1264485s1 Shadow damage to up to $s2 nearby enemies][Aimed Shot causes your Dark Minion to fire a Blighted Arrow, dealing $1264364s1 Shadow damage to up to $s1 nearby enemies].
- Effect: $?c1[Kill Command causes your Dark Hound to Shadow Thrash, dealing $1264485s1 Shadow damage to up to $s2 nearby enemies][Aimed Shot causes your Dark Minion to fire a Blighted Arrow, dealing $1264364s1 Shadow damage to up to $s1 nearby enemies].
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109800` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Counter Shot
- Node ID: `102292`
- Entry ID: `126352`
- Definition ID: `131178`
- Spell ID: `147362`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Interrupts spellcasting, preventing any spell in that school from being cast for $d.
- Effect: Interrupts spellcasting, preventing any spell in that school from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `109485` (type `2`), node `110157` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Withering Fire
- Node ID: `94993`
- Entry ID: `117590`
- Definition ID: `122602`
- Spell ID: `466990`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Bestial Wrath][Trueshot] causes you to surrender to darkness, granting you Withering Fire for $?c1[$466991d][the duration of Trueshot] and Deathblow.

$@spellicon466991 $@spellname466991
Casting Black Arrow fires a barrage of $s3 additional Black Arrows at nearby targets at $s4% effectiveness, prioritizing enemies that aren't affected by Black Arrow's damage over time effect.
- Effect: $?c1[Bestial Wrath][Trueshot] causes you to surrender to darkness, granting you Withering Fire for $?c1[$466991d][the duration of Trueshot] and Deathblow.

$@spellicon466991 $@spellname466991
Casting Black Arrow fires a barrage of $s3 additional Black Arrows at nearby targets at $s4% effectiveness, prioritizing enemies that aren't affected by Black Arrow's damage over time effect.
- Point cost per purchased rank: `1` × Hero pool (Dark Ranger) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94957` (type `2`), node `94982` (type `2`), node `94983` (type `2`), node `109799` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Intimidation
- Node ID: `102397`
- Entry ID: `126461`
- Definition ID: `131287`
- Spell ID: `19577`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Commands your pet to intimidate the target stunning your target for $24394d$?a1258509[ and nearby enemies for ${$1258508d}.1 sec][].
- Effect: Commands your pet to intimidate the target stunning your target for $24394d$?a1258509[ and nearby enemies for ${$1258508d}.1 sec][].
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1`
- Incoming edges: node `102424` (type `2`)
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
