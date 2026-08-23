# Dark Ranger

Reviewed build: `12.1.0.69404`
Hero subtree ID: `44`
Description: Embrace hatred and strike from the shadows, assaulting your enemies with necrotic, shadow-empowered abilities. Enemies who fall from your abilities further empower your dark energies.

## Hero talents

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
