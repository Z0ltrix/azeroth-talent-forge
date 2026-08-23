# Shadow

Reviewed build: `12.1.0.69404`
Spec ID: `258`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

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
### Halo
- Node ID: `94697`
- Entry ID: `117300`
- Definition ID: `122312`
- Spell ID: `120644`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Creates a ring of Shadow energy around you that quickly expands to a $s2 yd radius, healing allies for $120692s1 and dealing $<shadowhalodamage> Shadow damage to enemies. Healing reduced beyond $s1 targets.$?s137033[

|cFFFFFFFFGenerates ${$m5/100} Insanity.|r][]
- Effect: Creates a ring of Shadow energy around you that quickly expands to a $s2 yd radius, healing allies for $120692s1 and dealing $<shadowhalodamage> Shadow damage to enemies. Healing reduced beyond $s1 targets.$?s137033[

|cFFFFFFFFGenerates ${$m5/100} Insanity.|r][]
- Point cost per purchased rank: `1` × Hero pool (Archon) (ID `2986`; node)
- Source gates: source `node`; type `1` | source `node`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Psychic Scream
- Node ID: `82701`
- Entry ID: `103851`
- Definition ID: `108856`
- Spell ID: `8122`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lets out a psychic scream, causing all enemies within $A1 yards to flee, disorienting them for $d. Damage may interrupt the effect.
- Effect: Lets out a psychic scream, causing all enemies within $A1 yards to flee, disorienting them for $d. Damage may interrupt the effect.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `node`; type `2`; grants `1` rank(s)
- Incoming edges: node `82713` (type `2`), node `108730` (type `2`)
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
### Purify Disease
- Node ID: `82704`
- Entry ID: `103854`
- Definition ID: `108859`
- Spell ID: `213634`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Removes all Disease effects from a friendly target.
- Effect: Removes all Disease effects from a friendly target.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `109009` (type `2`)
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
- Node ID: `82680`
- Entry ID: `103828`
- Definition ID: `108833`
- Spell ID: `238100`
- Tree ID: `795`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Desperate Prayer by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Desperate Prayer by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Discipline, Holy, Shadow) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
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
