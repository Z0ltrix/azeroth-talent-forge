# Discipline

Reviewed build: `12.1.0.69404`
Spec ID: `256`
Role: `1`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Improved Flash Heal
- Node ID: `82717`
- Entry ID: `103869`
- Definition ID: `108874`
- Spell ID: `393870`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases healing done by Flash Heal$?c1[ and Shadow Mend][] by $s1%.
- Effect: Increases healing done by Flash Heal$?c1[ and Shadow Mend][] by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mind Blast
- Node ID: `82713`
- Entry ID: `103865`
- Definition ID: `108870`
- Spell ID: `8092`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blast the target's mind for $s1 Shadow damage.$?c1[ Costs a high amount of mana.][]$?s137033[

|cFFFFFFFFGenerates ${$s2/100} Insanity.|r][]
- Effect: Blast the target's mind for $s1 Shadow damage.$?c1[ Costs a high amount of mana.][]$?s137033[

|cFFFFFFFFGenerates ${$s2/100} Insanity.|r][]
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1` | source `node`; type `1` | source `node`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Guiding Light
- Node ID: `94683`
- Entry ID: `117286`
- Definition ID: `122298`
- Spell ID: `1248423`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137032[Penance][Prayer of Mending] gains an additional charge.
- Effect: $?a137032[Penance][Prayer of Mending] gains an additional charge.
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Preventive Measures
- Node ID: `94698`
- Entry ID: `117301`
- Definition ID: `122313`
- Spell ID: `440662`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137032[Power Word: Shield absorbs $s2% additional damage.

All damage dealt by Penance, Smite and Holy Nova increased by $s3%.][Increases the healing done by Prayer of Mending by $s1%.

All damage dealt by Smite, Holy Fire and Holy Nova increased by $s4%.]
- Effect: $?a137032[Power Word: Shield absorbs $s2% additional damage.

All damage dealt by Penance, Smite and Holy Nova increased by $s3%.][Increases the healing done by Prayer of Mending by $s1%.

All damage dealt by Smite, Holy Fire and Holy Nova increased by $s4%.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Preemptive Care
- Node ID: `94674`
- Entry ID: `117277`
- Definition ID: `122289`
- Spell ID: `440671`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137032[Increases the duration of Atonement by ${$s1/1000} sec.][Increases the duration of your Renew by $s2%.]
- Effect: $?a137032[Increases the duration of Atonement by ${$s1/1000} sec.][Increases the duration of your Renew by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Waste No Time
- Node ID: `94679`
- Entry ID: `117282`
- Definition ID: `122294`
- Spell ID: `440681`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of $?a137032[Power Word: Shield by ${$s2/-1000}.1 sec.][Prayer of Mending by ${$s1/-1000}.1 sec.]
- Effect: Reduces the cooldown of $?a137032[Power Word: Shield by ${$s2/-1000}.1 sec.][Prayer of Mending by ${$s1/-1000}.1 sec.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Words of the Wise
- Node ID: `109782`
- Entry ID: `136040`
- Definition ID: `140795`
- Spell ID: `1272352`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137031&?a1246517[Holy Word: Serenity healing increased by $s1%.]?c2[Holy Word: Serenity and Holy Word: Sanctify healing increased by $s1%.][Flash Heal, Shadow Mend, Plea, and Power Word: Radiance healing increased by $s2%.]
- Effect: $?a137031&?a1246517[Holy Word: Serenity healing increased by $s1%.]?c2[Holy Word: Serenity and Holy Word: Sanctify healing increased by $s1%.][Flash Heal, Shadow Mend, Plea, and Power Word: Radiance healing increased by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Purify
- Node ID: `82705`
- Entry ID: `103855`
- Definition ID: `108860`
- Spell ID: `390632`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Purify additionally removes all Disease effects.
- Effect: Purify additionally removes all Disease effects.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `109009` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Assured Safety
- Node ID: `94691`
- Entry ID: `117294`
- Definition ID: `122306`
- Spell ID: `440766`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137032[Power Word: Shield casts apply $s1 $Lstack:stacks; of Prayer of Mending to your target.

$@spellicon33076 $@spellname33076
$@spelldesc33076][Casting Prayer of Mending applies Power Word: Shield to your target.

$@spellicon1246768 $@spellname1246768
$@spelldesc1246768]
- Effect: $?a137032[Power Word: Shield casts apply $s1 $Lstack:stacks; of Prayer of Mending to your target.

$@spellicon33076 $@spellname33076
$@spelldesc33076][Casting Prayer of Mending applies Power Word: Shield to your target.

$@spellicon1246768 $@spellname1246768
$@spelldesc1246768]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94698` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Feathers
- Node ID: `94675`
- Entry ID: `117278`
- Definition ID: `122290`
- Spell ID: `440670`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Angelic Feathers increase movement speed by an additional $s2%.

When an ally walks through your Angelic Feather, you are also granted $s1% of its effect.
- Effect: Your Angelic Feathers increase movement speed by an additional $s2%.

When an ally walks through your Angelic Feather, you are also granted $s1% of its effect.
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94674` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Save the Day
- Node ID: `94675`
- Entry ID: `119331`
- Definition ID: `124231`
- Spell ID: `440669`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: For $458650d after casting Leap of Faith you may cast it a second time for free, ignoring its cooldown.
- Effect: For $458650d after casting Leap of Faith you may cast it a second time for free, ignoring its cooldown.
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94674` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Foreseen Circumstances
- Node ID: `94689`
- Entry ID: `117292`
- Definition ID: `122304`
- Spell ID: `440738`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137032[Pain Suppression reduces damage taken by an additional $s1%.][Guardian Spirit lasts an additional ${$s2/1000} sec.]
- Effect: $?a137032[Pain Suppression reduces damage taken by an additional $s1%.][Guardian Spirit lasts an additional ${$s2/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94679` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Prophet's Insight
- Node ID: `109783`
- Entry ID: `136041`
- Definition ID: `140796`
- Spell ID: `1272359`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Reduces the cooldown of your Holy Words by ${$s1/-1000} sec.][Atonement healing from Holy spells is increased by $s4%.]
- Effect: $?c2[Reduces the cooldown of your Holy Words by ${$s1/-1000} sec.][Atonement healing from Holy spells is increased by $s4%.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109782` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Prophet's Will
- Node ID: `94690`
- Entry ID: `117293`
- Definition ID: `122305`
- Spell ID: `433905`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Your Flash Heal, Shadow Mend, and Power Word: Shield are $s1%][Your Flash Heal and Holy Word: Serenity are $s1%] more effective when cast on yourself.
- Effect: $?c1[Your Flash Heal, Shadow Mend, and Power Word: Shield are $s1%][Your Flash Heal and Holy Word: Serenity are $s1%] more effective when cast on yourself.
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94691` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Desperate Measures
- Node ID: `94690`
- Entry ID: `126068`
- Definition ID: `130900`
- Spell ID: `458718`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Desperate Prayer lasts an additional ${$s1/1000} sec.

Angelic Bulwark's absorption effect is increased by $s2% of your maximum health.
- Effect: Desperate Prayer lasts an additional ${$s1/1000} sec.

Angelic Bulwark's absorption effect is increased by $s2% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94691` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Prompt Prognosis
- Node ID: `94673`
- Entry ID: `117276`
- Definition ID: `122288`
- Spell ID: `1246799`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137032[The first bolt of each Penance cast damages or heals for $s1% more.][$@spelldesc1246798]
- Effect: $?a137032[The first bolt of each Penance cast damages or heals for $s1% more.][$@spelldesc1246798]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94675` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Piety
- Node ID: `94700`
- Entry ID: `117303`
- Definition ID: `122315`
- Spell ID: `1246802`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $s1% of overhealing done is redistributed to up to $s2 nearby injured allies.
- Effect: $s1% of overhealing done is redistributed to up to $s2 nearby injured allies.
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94689` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unfolding Vision
- Node ID: `109781`
- Entry ID: `136039`
- Definition ID: `140794`
- Spell ID: `1272363`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[When Prayer of Mending expires without healing, it jumps to a nearby injured ally and loses $s1 $Lstack:stacks; instead.][When Power Word: Shield or Void Shield expires with absorption remaining, it jumps to a nearby injured ally instead. Can only happen once per shield.]
- Effect: $?c2[When Prayer of Mending expires without healing, it jumps to a nearby injured ally and loses $s1 $Lstack:stacks; instead.][When Power Word: Shield or Void Shield expires with absorption remaining, it jumps to a nearby injured ally instead. Can only happen once per shield.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109783` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twinsight
- Node ID: `94687`
- Entry ID: `117290`
- Definition ID: `122302`
- Spell ID: `440742`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137031[An additional $s1 stacks of Prayer of Mending is placed on a second ally within $A2 yards when casting Prayer of Mending.][$s3 additional Penance bolts are fired at an enemy within $A2 yards when healing an ally with Penance, or fired at an ally within $A2 yards when damaging an enemy with Penance.]
- Effect: $?a137031[An additional $s1 stacks of Prayer of Mending is placed on a second ally within $A2 yards when casting Prayer of Mending.][$s3 additional Penance bolts are fired at an enemy within $A2 yards when healing an ally with Penance, or fired at an ally within $A2 yards when damaging an enemy with Penance.]
- Point cost per purchased rank: `1` × Hero pool (Oracle) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94673` (type `2`), node `94690` (type `2`), node `94700` (type `2`), node `109781` (type `2`)
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
### Angel's Mercy
- Node ID: `82682`
- Entry ID: `103831`
- Definition ID: `108836`
- Spell ID: `238100`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Desperate Prayer by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Desperate Prayer by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `109012` (type `2`)
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
