# Voidweaver

Reviewed build: `12.1.0.69404`
Hero subtree ID: `18`
Description: Voidweavers have dedicated themselves to studying the origins of Void magic, and have discovered a way to tear open a tenuous connection to the Void. This power is incredibly dangerous and volatile, consuming anything in its path.

## Hero talents

### Void Torrent
- Node ID: `94684`
- Entry ID: `117287`
- Definition ID: `122299`
- Spell ID: `263165`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Channel a torrent of void energy into the target, dealing $o Shadow damage over $d and tearing open an $@spellname447444.

$@spellicon447444 $@spellname447444
$@spelldesc447444

|cFFFFFFFFGenerates ${$289577s1*$289577s2/100} Insanity over the duration.|r
- Effect: Channel a torrent of void energy into the target, dealing $o Shadow damage over $d and tearing open an $@spellname447444.

$@spellicon447444 $@spellname447444
$@spelldesc447444

|cFFFFFFFFGenerates ${$289577s1*$289577s2/100} Insanity over the duration.|r
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `2`; minimum level `71`; grants `1` rank(s) | source `node`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Entropic Rift
- Node ID: `110008`
- Entry ID: `136498`
- Definition ID: `141271`
- Spell ID: `447444`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Tear open a rift][Mind Blast tears open an Entropic Rift] that follows the enemy for $450193d. Enemies caught in its path suffer $447448s1 Shadow damage every $459314t1 sec while within its reach.
- Effect: $?c3[Tear open a rift][Mind Blast tears open an Entropic Rift] that follows the enemy for $450193d. Enemies caught in its path suffer $447448s1 Shadow damage every $459314t1 sec while within its reach.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `node`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### No Escape
- Node ID: `94693`
- Entry ID: `117296`
- Definition ID: `122308`
- Spell ID: `451204`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Entropic Rift slows enemies by up to $s1%, increased the closer they are to its center.
- Effect: Entropic Rift slows enemies by up to $s1%, increased the closer they are to its center.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94684` (type `2`), node `110008` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Energy
- Node ID: `94693`
- Entry ID: `123845`
- Definition ID: `128683`
- Spell ID: `451018`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c3[Void Torrent can be used while moving. ][]While Entropic Rift is active, you move $s1% faster.
- Effect: $?c3[Void Torrent can be used while moving. ][]While Entropic Rift is active, you move $s1% faster.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94684` (type `2`), node `110008` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Void Blast
- Node ID: `94703`
- Entry ID: `117306`
- Definition ID: `122318`
- Spell ID: `450405`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Entropic Rift upgrades $?c3[Mind Blast][Smite] into Void Blast while it is active.

$?c1[$@spellname450215:
$@spelldesc450215][$@spellname450983:
$@spelldesc450983]
- Effect: Entropic Rift upgrades $?c3[Mind Blast][Smite] into Void Blast while it is active.

$?c1[$@spellname450215:
$@spelldesc450215][$@spellname450983:
$@spelldesc450983]
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94684` (type `2`), node `110008` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Inner Quietus
- Node ID: `94670`
- Entry ID: `117273`
- Definition ID: `122285`
- Spell ID: `448278`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Vampiric Touch and Shadow Word: Pain deal $s1% additional damage.][Power Word: Shield absorbs $s2% additional damage.]
- Effect: $?c3[Vampiric Touch and Shadow Word: Pain deal $s1% additional damage.][Power Word: Shield absorbs $s2% additional damage.]
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94684` (type `2`), node `110008` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voidheart
- Node ID: `109780`
- Entry ID: `136038`
- Definition ID: `140793`
- Spell ID: `449880`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Entropic Rift is active, your $?c3[Shadow damage is increased by $s1%] [Atonement healing is increased by $s2%].
- Effect: While Entropic Rift is active, your $?c3[Shadow damage is increased by $s1%] [Atonement healing is increased by $s2%].
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94684` (type `2`), node `110008` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Devour Matter
- Node ID: `94668`
- Entry ID: `117271`
- Definition ID: `122283`
- Spell ID: `451840`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Word: Death consumes absorb shields from your target, dealing $32379s1 extra damage to them and granting you $?c3[$s3 Insanity][$s2% mana] if a shield was present.
- Effect: Shadow Word: Death consumes absorb shields from your target, dealing $32379s1 extra damage to them and granting you $?c3[$s3 Insanity][$s2% mana] if a shield was present.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94693` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Void Empowerment
- Node ID: `94695`
- Entry ID: `125821`
- Definition ID: `128681`
- Spell ID: `450138`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summoning an Entropic Rift $?c1[extends the duration of your $s4 shortest Atonements by $s1 sec][grants you Shadowy Insight].
- Effect: Summoning an Entropic Rift $?c1[extends the duration of your $s4 shortest Atonements by $s1 sec][grants you Shadowy Insight].
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94703` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Darkening Horizon
- Node ID: `94695`
- Entry ID: `125982`
- Definition ID: `130813`
- Spell ID: `449912`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Void Blast increases the duration of Entropic Rift by $?c1[${$s1}.1][${$s3}.1] sec, up to a maximum of $s2 sec.
- Effect: Void Blast increases the duration of Entropic Rift by $?c1[${$s1}.1][${$s3}.1] sec, up to a maximum of $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94703` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voidwraith
- Node ID: `100212`
- Entry ID: `123841`
- Definition ID: `128679`
- Spell ID: `451234`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When Entropic Rift ends, a Voidwraith is summoned from the collapsed rift for $451235d.

$@spellicon451235$@spellname451235
$@spelldesc451235
- Effect: When Entropic Rift ends, a Voidwraith is summoned from the collapsed rift for $451235d.

$@spellicon451235$@spellname451235
$@spelldesc451235
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94670` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Touch of the Void
- Node ID: `109779`
- Entry ID: `136037`
- Definition ID: `140792`
- Spell ID: `1266856`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Voidheart now persists for $s1 sec after Entropic Rift ends.
- Effect: Voidheart now persists for $s1 sec after Entropic Rift ends.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109780` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quickened Pulse
- Node ID: `94692`
- Entry ID: `117295`
- Definition ID: `122307`
- Spell ID: `1266845`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Word: Pain and Entropic Rift deal damage ${100*(1/(1+$m1/100)-1)}% more often.
- Effect: Shadow Word: Pain and Entropic Rift deal damage ${100*(1/(1+$m1/100)-1)}% more often.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94668` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Void Infusion
- Node ID: `94669`
- Entry ID: `117272`
- Definition ID: `122284`
- Spell ID: `450612`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[While Entropic Rift is active, Atonement healing with Void Blast and Penance is $s2% more effective.][Void Blast generates ${$s1/100} additional Insanity.]
- Effect: $?c1[While Entropic Rift is active, Atonement healing with Void Blast and Penance is $s2% more effective.][Void Blast generates ${$s1/100} additional Insanity.]
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94695` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Void Leech
- Node ID: `94696`
- Entry ID: `117299`
- Definition ID: `122311`
- Spell ID: `451311`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $t1 sec siphon an amount equal to $s1% of your health from an ally within $s3 yds if they are higher health than you.
- Effect: Every $t1 sec siphon an amount equal to $s1% of your health from an ally within $s3 yds if they are higher health than you.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `100212` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Embrace the Shadow
- Node ID: `94696`
- Entry ID: `123844`
- Definition ID: `128682`
- Spell ID: `451569`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: You absorb $s3% of all magic damage taken. Absorbing Shadow damage heals you for $s2% of the amount absorbed.
- Effect: You absorb $s3% of all magic damage taken. Absorbing Shadow damage heals you for $s2% of the amount absorbed.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `100212` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overwhelming Shadows
- Node ID: `109778`
- Entry ID: `136036`
- Definition ID: `140791`
- Spell ID: `1266883`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Void Torrent deals $s1% increased damage.][Mind Blast deals $s2% increased damage.]
- Effect: $?c3[Void Torrent deals $s1% increased damage.][Mind Blast deals $s2% increased damage.]
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109779` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Collapsing Void
- Node ID: `94694`
- Entry ID: `117297`
- Definition ID: `122309`
- Spell ID: `448403`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each time $?c3[you cast Shadow Word: Madness][Penance damages or heals], Entropic Rift is empowered, increasing its damage and size by $?c1[$s4][$s3]%.

After Entropic Rift ends it collapses, dealing $448405s1 Shadow damage split amongst enemy targets within $448405a1 yds.
- Effect: Each time $?c3[you cast Shadow Word: Madness][Penance damages or heals], Entropic Rift is empowered, increasing its damage and size by $?c1[$s4][$s3]%.

After Entropic Rift ends it collapses, dealing $448405s1 Shadow damage split amongst enemy targets within $448405a1 yds.
- Point cost per purchased rank: `1` × Hero pool (Voidweaver) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94669` (type `2`), node `94692` (type `2`), node `94696` (type `2`), node `109778` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
