# Archon

Reviewed build: `12.1.0.69404`
Hero subtree ID: `19`
Description: Archons are highly devout and deeply connected to the Light and Shadow. Archons can be blessed from higher beings to enter into an ascended state, becoming an ultimate version of themselves.

## Hero talents

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
