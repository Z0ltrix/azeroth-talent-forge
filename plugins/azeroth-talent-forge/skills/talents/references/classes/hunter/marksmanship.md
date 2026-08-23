# Marksmanship

Reviewed build: `12.1.0.69404`
Spec ID: `254`
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
### Don't Look Back
- Node ID: `94989`
- Entry ID: `117586`
- Definition ID: `122598`
- Spell ID: `450373`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming Sentinel's Mark grants you an absorb shield equal to ${$s1}.1% of your maximum health.
- Effect: Consuming Sentinel's Mark grants you an absorb shield equal to ${$s1}.1% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moon's Blessing
- Node ID: `94973`
- Entry ID: `117570`
- Definition ID: `122582`
- Spell ID: `1253825`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] has a $s1% increased chance to summon your Sentinel Owl.

When your Sentinel Owl applies Sentinel's Mark, reduce the cooldown of $?c2[Aimed Shot][Wildfire Bomb] by $?c2[${$s2/1000}.1][${$s3/1000}.1] sec.
- Effect: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] has a $s1% increased chance to summon your Sentinel Owl.

When your Sentinel Owl applies Sentinel's Mark, reduce the cooldown of $?c2[Aimed Shot][Wildfire Bomb] by $?c2[${$s2/1000}.1][${$s3/1000}.1] sec.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sanctified Armaments
- Node ID: `94981`
- Entry ID: `117578`
- Definition ID: `122590`
- Spell ID: `1253831`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: An additional $?c2[$s1][$s2]% of $?c2[Rapid Fire][Raptor Strike]'s damage is dealt as Arcane damage over $1253836d.
- Effect: An additional $?c2[$s1][$s2]% of $?c2[Rapid Fire][Raptor Strike]'s damage is dealt as Arcane damage over $1253836d.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Moonlight Chakram
- Node ID: `109807`
- Entry ID: `136065`
- Definition ID: `140820`
- Spell ID: `1264902`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For $1264946d after casting $?c2[Trueshot][Takedown], $?c2[Trueshot][Takedown] is replaced with Moonlight Chakram.

$@spellicon1264949 $@spellname1264949
$@spelldesc1264949
- Effect: For $1264946d after casting $?c2[Trueshot][Takedown], $?c2[Trueshot][Takedown] is replaced with Moonlight Chakram.

$@spellicon1264949 $@spellname1264949
$@spelldesc1264949
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94976` (type `2`)
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
### Stargazer
- Node ID: `94958`
- Entry ID: `117555`
- Definition ID: `122567`
- Spell ID: `1253751`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] grants $1253750s1% increased critical strike damage for $1253750d. Multiple applications may overlap.
- Effect: $?c2[Consuming Precise Shots][Consuming Tip of the Spear] grants $1253750s1% increased critical strike damage for $1253750d. Multiple applications may overlap.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94989` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Open Fire
- Node ID: `94958`
- Entry ID: `135589`
- Definition ID: `140345`
- Spell ID: `1253807`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c2[Volley damage increased by $s1%][Fire damage dealt increased by $s2%].
- Effect: $?c2[Volley damage increased by $s1%][Fire damage dealt increased by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94989` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Can't Miss, Won't Miss
- Node ID: `94990`
- Entry ID: `117587`
- Definition ID: `122599`
- Spell ID: `1253830`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Precise Shots damage bonus][Tip of the Spear damage bonus] increased by $?c2[$s1][$s2]%.

$?c2[Trueshot][Takedown] duration increased by $?c2[${$s3/1000}][${$s4/1000}] sec.
- Effect: $?c2[Precise Shots damage bonus][Tip of the Spear damage bonus] increased by $?c2[$s1][$s2]%.

$?c2[Trueshot][Takedown] duration increased by $?c2[${$s3/1000}][${$s4/1000}] sec.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94973` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Invigorating Pulse
- Node ID: `94971`
- Entry ID: `117568`
- Definition ID: `122580`
- Spell ID: `450379`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Steady Shot][Kill Command] grants an additional $s1 Focus and its damage is increased by $s4%. 

Maximum Focus increased by $s2.
- Effect: $?c2[Steady Shot][Kill Command] grants an additional $s1 Focus and its damage is increased by $s4%. 

Maximum Focus increased by $s2.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94981` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twilight Requiem
- Node ID: `110028`
- Entry ID: `136522`
- Definition ID: `141295`
- Spell ID: `1264904`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Moonlight Chakram expires, it summons an explosion of moonlight, dealing $1266096s1 Arcane damage to nearby enemies. Damage reduced beyond $s1 targets.
- Effect: When your Moonlight Chakram expires, it summons an explosion of moonlight, dealing $1266096s1 Arcane damage to nearby enemies. Damage reduced beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109807` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stalk and Strike
- Node ID: `110028`
- Entry ID: `136521`
- Definition ID: `141294`
- Spell ID: `1266069`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Throwing your Moonlight Chakram $?c2[grants you Lock and Load][reduces the cooldown of Wildfire Bomb by ${$s1/1000} sec].
- Effect: Throwing your Moonlight Chakram $?c2[grants you Lock and Load][reduces the cooldown of Wildfire Bomb by ${$s1/1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109807` (type `2`)
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
- Node ID: `102402`
- Entry ID: `126466`
- Definition ID: `131292`
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
### Arcane Talons
- Node ID: `94970`
- Entry ID: `117567`
- Definition ID: `122579`
- Spell ID: `1253846`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Sentinel's Mark further increases the damage of $?c2[Aimed Shot][Wildfire Bomb]$?a1273128[ and Rapid Fire][] by $?c2[$s1][$s2]%
- Effect: Sentinel's Mark further increases the damage of $?c2[Aimed Shot][Wildfire Bomb]$?a1273128[ and Rapid Fire][] by $?c2[$s1][$s2]%
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94958` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lunar Calling
- Node ID: `94965`
- Entry ID: `117562`
- Definition ID: `122574`
- Spell ID: `1253852`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Feathered Frenzy further increases your chance to summon your Sentinel Owl during Trueshot by $s1%][Takedown summons your Sentinel Owl and your chance to summon your Sentinel Owl is increased by an additional $s2% during Takedown].
- Effect: $?c2[Feathered Frenzy further increases your chance to summon your Sentinel Owl during Trueshot by $s1%][Takedown summons your Sentinel Owl and your chance to summon your Sentinel Owl is increased by an additional $s2% during Takedown].
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94990` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Conditioning
- Node ID: `94980`
- Entry ID: `117577`
- Definition ID: `122589`
- Spell ID: `1253887`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your movement speed is increased by $s1%.

Aspect of the Cheetah's cooldown is reduced by ${-$s2/1000} sec.
- Effect: Your movement speed is increased by $s1%.

Aspect of the Cheetah's cooldown is reduced by ${-$s2/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94971` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Scout's Vigil
- Node ID: `94980`
- Entry ID: `123870`
- Definition ID: `128708`
- Spell ID: `1253892`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Enemy detection radius reduced by $s1 yds.
- Effect: Enemy detection radius reduced by $s1 yds.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94971` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Radiant Edge
- Node ID: `109805`
- Entry ID: `136063`
- Definition ID: `140818`
- Spell ID: `1264903`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Moonlight Chakram deals $1264949s3% increased damage each time it bounces.
- Effect: Your Moonlight Chakram deals $1264949s3% increased damage each time it bounces.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `110028` (type `2`)
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
### Lunar Storm
- Node ID: `94978`
- Entry ID: `117575`
- Definition ID: `122587`
- Spell ID: `1253732`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Sentinel's Mark is consumed, it summons a barrage of $s1 lunar missiles, each dealing $1253733s1 Arcane damage to enemies within $s2 yds.
- Effect: When Sentinel's Mark is consumed, it summons a barrage of $s1 lunar missiles, each dealing $1253733s1 Arcane damage to enemies within $s2 yds.
- Point cost per purchased rank: `1` × Hero pool (Sentinel) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94965` (type `2`), node `94970` (type `2`), node `94980` (type `2`), node `109805` (type `2`)
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
### Intimidation
- Node ID: `103990`
- Entry ID: `128413`
- Definition ID: `133219`
- Spell ID: `474421`
- Tree ID: `774`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Spotting Eagle descends from the skies, stunning your target for $24394d.$?s321468[

Targets stunned by Intimidation deal $321469s1% less damage to you for $321469d after the effect ends.][]

This ability does not require line of sight when used against players.
- Effect: Your Spotting Eagle descends from the skies, stunning your target for $24394d.$?s321468[

Targets stunned by Intimidation deal $321469s1% less damage to you for $321469d after the effect ends.][]

This ability does not require line of sight when used against players.
- Point cost per purchased rank: `1` × Specialization pool (Beast Mastery, Marksmanship, Survival) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1`
- Incoming edges: node `102424` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
