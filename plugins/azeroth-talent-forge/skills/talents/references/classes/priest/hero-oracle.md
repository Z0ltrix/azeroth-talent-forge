# Oracle

Reviewed build: `12.1.0.69404`
Hero subtree ID: `20`
Description: Oracles gain insight into the future and use it to protect and empower their allies. Their future sight grants Oracles the ability to bestow unique blessings and benefits upon their allies before they even know they are needed.

## Hero talents

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
