# Holy

Reviewed build: `12.1.0.69404`
Spec ID: `257`
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
### Holy Fire
- Node ID: `108730`
- Entry ID: `134283`
- Definition ID: `139056`
- Spell ID: `14914`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consumes the enemy in Holy flames that cause $s1 Holy damage and an additional $o2 Holy damage over $d.$?a231687[ Stacks up to $u times.][]
- Effect: Consumes the enemy in Holy flames that cause $s1 Holy damage and an additional $o2 Holy damage over $d.$?a231687[ Stacks up to $u times.][]
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `group`; type `1`
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
### Halo
- Node ID: `108724`
- Entry ID: `134273`
- Definition ID: `139046`
- Spell ID: `120517`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Creates a ring of Holy energy around you that quickly expands to a $s2 yd radius, healing allies for $120692s1 and dealing $<holyhalodamage> Holy damage to enemies.

Healing reduced beyond $s1 targets.
- Effect: Creates a ring of Holy energy around you that quickly expands to a $s2 yd radius, healing allies for $120692s1 and dealing $<holyhalodamage> Holy damage to enemies.

Healing reduced beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; node)
- Source gates: source `node`; type `1` | source `node`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Holy Nova
- Node ID: `82718`
- Entry ID: `103870`
- Definition ID: `108875`
- Spell ID: `132157`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: An explosion of holy light around you deals up to $s1 Holy damage to enemies and up to $281265s1 healing to allies within $A1 yds, reduced if there are more than $s3 targets.
- Effect: An explosion of holy light around you deals up to $s1 Holy damage to enemies and up to $281265s1 healing to allies within $A1 yds, reduced if there are more than $s3 targets.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `82717` (type `2`)
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
### Perfected Form
- Node ID: `94677`
- Entry ID: `117280`
- Definition ID: `122292`
- Spell ID: `453917`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137031[Your healing done is increased by $s3% while Apotheosis is active.][Your damage dealt is increased by $s1% while Voidform is active.]
- Effect: $?a137031[Your healing done is increased by $s3% while Apotheosis is active.][Your damage dealt is increased by $s1% while Voidform is active.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94697` (type `2`), node `108724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Power Surge
- Node ID: `94681`
- Entry ID: `117284`
- Definition ID: `122296`
- Spell ID: `453109`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Halo also causes you to create a Halo around you at $s1% effectiveness every $453112t sec for $453112d.
- Effect: Casting Halo also causes you to create a Halo around you at $s1% effectiveness every $453112t sec for $453112d.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94697` (type `2`), node `108724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Manifested Power
- Node ID: `94699`
- Entry ID: `117302`
- Definition ID: `122314`
- Spell ID: `453783`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Creating a Halo $?a137033[upgrades your next Mind Flay to Mind Flay: Insanity.

$@spellicon391403 $@spellname391403
$@spelldesc391403][grants Surge of Light.

$@spellicon109186 $@spellname109186
$@spelldesc109186]
- Effect: Creating a Halo $?a137033[upgrades your next Mind Flay to Mind Flay: Insanity.

$@spellicon391403 $@spellname391403
$@spelldesc391403][grants Surge of Light.

$@spellicon109186 $@spellname109186
$@spelldesc109186]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94697` (type `2`), node `108724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Focused Outburst
- Node ID: `109777`
- Entry ID: `136035`
- Definition ID: `140790`
- Spell ID: `1272320`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Prayer of Healing mana cost reduced by $s1% and its cast time is reduced by $s2%.][Void Volley deals $s3% increased damage and Shadow Word: Madness casts during Voidform unleash a Void Volley at your target at $s4% effectiveness.]
- Effect: $?c2[Prayer of Healing mana cost reduced by $s1% and its cast time is reduced by $s2%.][Void Volley deals $s3% increased damage and Shadow Word: Madness casts during Voidform unleash a Void Volley at your target at $s4% effectiveness.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94697` (type `2`), node `108724` (type `2`)
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
### Shock Pulse
- Node ID: `94686`
- Entry ID: `117289`
- Definition ID: `122301`
- Spell ID: `453852`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Halo damage reduces enemy movement speed by $453848s1% for $453848d, stacking up to $453848U times.
- Effect: Halo damage reduces enemy movement speed by $453848s1% for $453848d, stacking up to $453848U times.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94677` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Incessant Screams
- Node ID: `94686`
- Entry ID: `125083`
- Definition ID: `129915`
- Spell ID: `453918`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Psychic Scream creates an image of you at your location. After $s1 sec, the image will let out a Psychic Scream.
- Effect: Psychic Scream creates an image of you at your location. After $s1 sec, the image will let out a Psychic Scream.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94677` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Energy Conservation
- Node ID: `94680`
- Entry ID: `117283`
- Definition ID: `122295`
- Spell ID: `1272308`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Power Surge lasts an additional ${$s1/1000} sec.
- Effect: Power Surge lasts an additional ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94681` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Empowered Surges
- Node ID: `94688`
- Entry ID: `117291`
- Definition ID: `122303`
- Spell ID: `453799`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137033[Increases the damage done by Mind Flay: Insanity by $s2%.

][Your spells affected by Surge of Light heal for $s1% more while Surge of Light is active.]
- Effect: $?a137033[Increases the damage done by Mind Flay: Insanity by $s2%.

][Your spells affected by Surge of Light heal for $s1% more while Surge of Light is active.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94699` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Word of Supremacy
- Node ID: `109776`
- Entry ID: `136034`
- Definition ID: `140789`
- Spell ID: `453726`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Power Word: Fortitude grants you an additional $s1% stamina.
- Effect: Power Word: Fortitude grants you an additional $s1% stamina.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109777` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Heightened Alteration
- Node ID: `109776`
- Entry ID: `136687`
- Definition ID: `141459`
- Spell ID: `453729`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137031[Increases the duration of Spirit of Redemption by ${$s1/1000} sec.][Increases the duration of Dispersion by ${$s2/1000} sec.]
- Effect: $?a137031[Increases the duration of Spirit of Redemption by ${$s1/1000} sec.][Increases the duration of Dispersion by ${$s2/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109777` (type `2`)
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
### Energy Compression
- Node ID: `94678`
- Entry ID: `117281`
- Definition ID: `122293`
- Spell ID: `449874`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Halo damage and healing is increased by $s1%.
- Effect: Halo damage and healing is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94686` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sustained Potency
- Node ID: `94678`
- Entry ID: `125085`
- Definition ID: `129917`
- Spell ID: `454001`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Creating a Halo extends the duration of $?a137031[Apotheosis][Voidform] by ${$s1/1000} sec. If $?a137031[Apotheosis][Voidform] is not active, up to $454002U seconds is stored.

While out of combat or affected by a loss of control effect, the duration of $?a137031[Apotheosis][Voidform] is paused for up to $s2 sec.
- Effect: Creating a Halo extends the duration of $?a137031[Apotheosis][Voidform] by ${$s1/1000} sec. If $?a137031[Apotheosis][Voidform] is not active, up to $454002U seconds is stored.

While out of combat or affected by a loss of control effect, the duration of $?a137031[Apotheosis][Voidform] is paused for up to $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94686` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Resonant Energy
- Node ID: `94676`
- Entry ID: `117279`
- Definition ID: `122291`
- Spell ID: `453845`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137033[Creating a Halo increases your spell damage by $453850s1% for $453850d, stacking up to $453850U times.][Creating a Halo increases your healing done by $453846s1% for $453846d, stacking up to $453846U times.]
- Effect: $?a137033[Creating a Halo increases your spell damage by $453850s1% for $453850d, stacking up to $453850U times.][Creating a Halo increases your healing done by $453846s1% for $453846d, stacking up to $453846U times.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94680` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Energy Cycle
- Node ID: `94685`
- Entry ID: `117288`
- Definition ID: `122300`
- Spell ID: `453828`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137031&?a1246517[Consuming Surge of Light reduces the cooldown of Holy Word: Serenity by ${$s1/-1000} sec.]?a137031&!a1246517[Consuming Surge of Light reduces the cooldown of Holy Word: Sanctify by ${$s1/-1000} sec.][Casting Mind Flay: Insanity has a $s2% chance to conjure Shadowy Apparitions.]
- Effect: $?a137031&?a1246517[Consuming Surge of Light reduces the cooldown of Holy Word: Serenity by ${$s1/-1000} sec.]?a137031&!a1246517[Consuming Surge of Light reduces the cooldown of Holy Word: Sanctify by ${$s1/-1000} sec.][Casting Mind Flay: Insanity has a $s2% chance to conjure Shadowy Apparitions.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94688` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Realized Potential
- Node ID: `109775`
- Entry ID: `136033`
- Definition ID: `140788`
- Spell ID: `1272326`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Flash Heal healing increased by $s1%. 

Healing spells and Smite have an additional $s2% chance to grant Surge of Light.][Shadow Word: Death damage increased by $s3% and its cooldown is reduced by ${$s4/-1000} sec.]
- Effect: $?c2[Flash Heal healing increased by $s1%. 

Healing spells and Smite have an additional $s2% chance to grant Surge of Light.][Shadow Word: Death damage increased by $s3% and its cooldown is reduced by ${$s4/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109776` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spiritwell
- Node ID: `109775`
- Entry ID: `136688`
- Definition ID: `141460`
- Spell ID: `1247178`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c2[Surge of Light can now be consumed by Prayer of Healing in addition to Flash Heal.

$@spellicon109186 $@spellname109186
$@spelldesc109186][Increases Shadowy Apparition damage by $s1%.]
- Effect: $?c2[Surge of Light can now be consumed by Prayer of Healing in addition to Flash Heal.

$@spellicon109186 $@spellname109186
$@spelldesc109186][Increases Shadowy Apparition damage by $s1%.]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109776` (type `2`)
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
### Divine Halo
- Node ID: `94702`
- Entry ID: `117305`
- Definition ID: `122317`
- Spell ID: `449806`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Halo now centers around you and returns to you after it reaches its maximum distance, healing allies and damaging enemies each time it passes through them.
- Effect: Halo now centers around you and returns to you after it reaches its maximum distance, healing allies and damaging enemies each time it passes through them.
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94676` (type `2`), node `94678` (type `2`), node `94685` (type `2`), node `109775` (type `2`)
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
