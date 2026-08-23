# Retribution

Reviewed build: `12.1.0.69404`
Spec ID: `70`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Light's Guidance
- Node ID: `95180`
- Entry ID: `117813`
- Definition ID: `122825`
- Spell ID: `427445`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137028[Divine Toll][Wake of Ashes] is replaced with $@spellname427453 for $427441d after it is cast.

$@spellicon427453 $@spellname427453:
$@spelldesc427453
|cFFFFFFFFCosts 5 Holy Power.
- Effect: $?a137028[Divine Toll][Wake of Ashes] is replaced with $@spellname427453 for $427441d after it is cast.

$@spellicon427453 $@spellname427453:
$@spelldesc427453
|cFFFFFFFFCosts 5 Holy Power.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dawnlight
- Node ID: `95099`
- Entry ID: `117696`
- Definition ID: `122708`
- Spell ID: `431377`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?c1[Holy Prism or Divine Toll]?c3[Wake of Ashes][] causes your next $s1 Holy Power spending abilities to apply Dawnlight on your target, dealing $431380o1 Radiant damage or $431381o1 healing over $431380d.

$431581s1% of Dawnlight's damage and healing radiates to nearby allies or enemies, reduced beyond $431581s2 targets.$?c1[

Dawnlight's healing does not transfer to Beacon of Light.][]
- Effect: Casting $?c1[Holy Prism or Divine Toll]?c3[Wake of Ashes][] causes your next $s1 Holy Power spending abilities to apply Dawnlight on your target, dealing $431380o1 Radiant damage or $431381o1 healing over $431380d.

$431581s1% of Dawnlight's damage and healing radiates to nearby allies or enemies, reduced beyond $431581s2 targets.$?c1[

Dawnlight's healing does not transfer to Beacon of Light.][]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hammer of Wrath
- Node ID: `81510`
- Entry ID: `133481`
- Definition ID: `138267`
- Spell ID: `1241288`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: During Avenging Wrath, Judgment is empowered into Hammer of Wrath.$?c3[

$@spellicon24275$@spellname24275
$@spelldesc24275][

$@spellicon1241413 $@spellname1241413
$@spelldesc1241413]
- Effect: During Avenging Wrath, Judgment is empowered into Hammer of Wrath.$?c3[

$@spellicon24275$@spellname24275
$@spelldesc24275][

$@spellicon1241413 $@spellname1241413
$@spelldesc1241413]
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Auras of the Resolute
- Node ID: `81600`
- Entry ID: `102587`
- Definition ID: `107592`
- Spell ID: `385633`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Learn Concentration Aura, Devotion Aura, and Crusader Aura:

$@spellicon317920$@spellname317920:
$@spelldesc317920

$@spellicon465 $@spellname465:
$@spelldesc465

$@spellicon32223 $@spellname32223:
$@spelldesc32223
- Effect: Learn Concentration Aura, Devotion Aura, and Crusader Aura:

$@spellicon317920$@spellname317920:
$@spelldesc317920

$@spellicon465 $@spellname465:
$@spelldesc465

$@spellicon32223 $@spellname32223:
$@spelldesc32223
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shake the Heavens
- Node ID: `95187`
- Entry ID: `117823`
- Definition ID: `122835`
- Spell ID: `431533`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After casting Hammer of Light, you call down an Empyrean Hammer on a nearby target every $431536T sec, for $431536d.
- Effect: After casting Hammer of Light, you call down an Empyrean Hammer on a nearby target every $431536T sec, for $431536d.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95180` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Hammer
- Node ID: `109747`
- Entry ID: `136005`
- Definition ID: `140760`
- Spell ID: `432929`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Divine Toll summons Divine Hammers that spin around you for $198034d.

$@spellicon198034$@spellname198034
$@spelldesc198034
- Effect: Divine Toll summons Divine Hammers that spin around you for $198034d.

$@spellicon198034$@spellname198034
$@spelldesc198034
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `95180` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Zealous Vindication
- Node ID: `95183`
- Entry ID: `117816`
- Definition ID: `122828`
- Spell ID: `431463`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hammer of Light instantly calls down $s1 Empyrean Hammers on your target when it is cast.
- Effect: Hammer of Light instantly calls down $s1 Empyrean Hammers on your target when it is cast.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95180` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wrathful Descent
- Node ID: `95177`
- Entry ID: `117810`
- Definition ID: `122822`
- Spell ID: `431551`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Empyrean Hammer critically strikes, $s2% of its damage is dealt to nearby enemies.

Enemies hit by this effect deal $431625s3% reduced damage to you for $431625d.
- Effect: When Empyrean Hammer critically strikes, $s2% of its damage is dealt to nearby enemies.

Enemies hit by this effect deal $431625s3% reduced damage to you for $431625d.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95180` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Morning Star
- Node ID: `95073`
- Entry ID: `117670`
- Definition ID: `122682`
- Spell ID: `431482`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every ${$t1}.1 sec, your next Dawnlight's damage or healing is increased by $431539s1%, stacking up to $431539u times.

Morning Star stacks twice as fast while out of combat.
- Effect: Every ${$t1}.1 sec, your next Dawnlight's damage or healing is increased by $431539s1%, stacking up to $431539u times.

Morning Star stacks twice as fast while out of combat.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95099` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gleaming Rays
- Node ID: `95073`
- Entry ID: `117778`
- Definition ID: `122790`
- Spell ID: `431480`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your Holy Power spenders deal $s1% additional damage and healing.
- Effect: Your Holy Power spenders deal $s1% additional damage and healing.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95099` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Eternal Flame
- Node ID: `95095`
- Entry ID: `117692`
- Definition ID: `122704`
- Spell ID: `156322`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals an ally for $s2 and an additional $o1 over $d.

Healing increased by $?c1[$s3][$s4]% when cast on self.
- Effect: Heals an ally for $s2 and an additional $o1 over $d.

Healing increased by $?c1[$s3][$s4]% when cast on self.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95099` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Luminosity
- Node ID: `95080`
- Entry ID: `117677`
- Definition ID: `122689`
- Spell ID: `431402`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Critical Strike chance of Holy Shock and Light of Dawn increased by $s1%.]?c3[Critical Strike chance of Hammer of Wrath and Divine Storm increased by $s2%.][]
- Effect: $?c1[Critical Strike chance of Holy Shock and Light of Dawn increased by $s1%.]?c3[Critical Strike chance of Hammer of Wrath and Divine Storm increased by $s2%.][]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95099` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Endless Gleam
- Node ID: `109748`
- Entry ID: `136006`
- Definition ID: `140761`
- Spell ID: `1263787`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Dawnlight's duration is increased by ${$s1/1000}.1 sec when it heals an ally with full health.][Dawnlight's duration is increased by ${$s2/1000}.1 sec whenever struck by Divine Storm or Templar's Verdict.

When 2 Dawnlights are struck by Divine Storm, their durations are extended by an additional ${$s3/1000}.1 sec.]
- Effect: $?c1[Dawnlight's duration is increased by ${$s1/1000}.1 sec when it heals an ally with full health.][Dawnlight's duration is increased by ${$s2/1000}.1 sec whenever struck by Divine Storm or Templar's Verdict.

When 2 Dawnlights are struck by Divine Storm, their durations are extended by an additional ${$s3/1000}.1 sec.]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95099` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Higher Calling
- Node ID: `95178`
- Entry ID: `117811`
- Definition ID: `122823`
- Spell ID: `431687`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137028[Crusader Strike, Hammer of Wrath and Judgment][Crusader Strike, Hammer of Wrath and Blade of Justice] extend the duration of Shake the Heavens by $s1 sec.
- Effect: $?a137028[Crusader Strike, Hammer of Wrath and Judgment][Crusader Strike, Hammer of Wrath and Blade of Justice] extend the duration of Shake the Heavens by $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95187` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sacrosanct Crusade
- Node ID: `95179`
- Entry ID: `117812`
- Definition ID: `122824`
- Spell ID: `431730`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137028[Divine Toll][Wake of Ashes] surrounds you with a Holy barrier for $?a137028[$s1][$s4]% of your maximum health.

Hammer of Light heals you for $?a137028[$s2][$s5]% of your maximum health, increased by $?a137028[$s3][$s6]% for each additional target hit. Any overhealing done with this effect gets converted into a Holy barrier instead.
- Effect: $?a137028[Divine Toll][Wake of Ashes] surrounds you with a Holy barrier for $?a137028[$s1][$s4]% of your maximum health.

Hammer of Light heals you for $?a137028[$s2][$s5]% of your maximum health, increased by $?a137028[$s3][$s6]% for each additional target hit. Any overhealing done with this effect gets converted into a Holy barrier instead.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95183` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bonds of Fellowship
- Node ID: `95181`
- Entry ID: `117814`
- Definition ID: `122826`
- Spell ID: `432992`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You receive 20% less damage from Blessing of Sacrifice and each time its target takes damage, you gain 4% movement speed up to a maximum of 40%.
- Effect: You receive 20% less damage from Blessing of Sacrifice and each time its target takes damage, you gain 4% movement speed up to a maximum of 40%.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95177` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unrelenting Charger
- Node ID: `95181`
- Entry ID: `117858`
- Definition ID: `122870`
- Spell ID: `432990`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Divine Steed lasts ${$s1/1000} sec longer and increases your movement speed by an additional $442221s1% for the first $442221d.
- Effect: Divine Steed lasts ${$s1/1000} sec longer and increases your movement speed by an additional $442221s1% for the first $442221d.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95177` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Light's Judicator
- Node ID: `109746`
- Entry ID: `136004`
- Definition ID: `140759`
- Spell ID: `1261525`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empyrean Hammer deals $s1% increased critical strike damage and its critical strikes have $h% chance to grant an additional stack of Light's Deliverance.
- Effect: Empyrean Hammer deals $s1% increased critical strike damage and its critical strikes have $h% chance to grant an additional stack of Light's Deliverance.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109747` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cleanse Toxins
- Node ID: `81507`
- Entry ID: `102476`
- Definition ID: `107481`
- Spell ID: `213644`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Cleanses a friendly target, removing all Poison and Disease effects.
- Effect: Cleanses a friendly target, removing all Poison and Disease effects.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `81597` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Illumine
- Node ID: `95098`
- Entry ID: `117695`
- Definition ID: `122707`
- Spell ID: `431423`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Dawnlight reduces the movement speed of enemies by $431380s3% and increases the movement speed of allies by $431381s3%.
- Effect: Dawnlight reduces the movement speed of enemies by $431380s3% and increases the movement speed of allies by $431381s3%.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95073` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Will of the Dawn
- Node ID: `95098`
- Entry ID: `117777`
- Definition ID: `122789`
- Spell ID: `431406`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Movement speed increased by $431462s1% while above $s1% health.

When your health is brought below $s3%, your movement speed is increased by $431752s1% for $431752d. Cannot occur more than once every $456779d.
- Effect: Movement speed increased by $431462s1% while above $s1% health.

When your health is brought below $s3%, your movement speed is increased by $431752s1% for $431752d. Cannot occur more than once every $456779d.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95073` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blessing of An'she
- Node ID: `95071`
- Entry ID: `117668`
- Definition ID: `122680`
- Spell ID: `445200`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[The healing and damage of Holy Shock is increased by $s1%.]?c3[Your damage and healing over time effects have a chance to increase the damage of your next Judgment by $445206s1%.][]
- Effect: $?c1[The healing and damage of Holy Shock is increased by $s1%.]?c3[Your damage and healing over time effects have a chance to increase the damage of your next Judgment by $445206s1%.][]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95095` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lingering Radiance
- Node ID: `95071`
- Entry ID: `117779`
- Definition ID: `122791`
- Spell ID: `431407`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Dawnlight leaves an Eternal Flame for ${$s1/1000} sec on allies or a Greater Judgment on enemies when it expires or is extended.
- Effect: Dawnlight leaves an Eternal Flame for ${$s1/1000} sec on allies or a Greater Judgment on enemies when it expires or is extended.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95095` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sun Sear
- Node ID: `95072`
- Entry ID: `117669`
- Definition ID: `122681`
- Spell ID: `431413`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Holy Shock and Light of Dawn critical strikes cause the target to be healed for an additional $431415o1 over $431415d.]?c3[Hammer of Wrath and Divine Storm critical strikes cause the target to burn for an additional $431414o1 Radiant damage over $431414d.][]
- Effect: $?c1[Holy Shock and Light of Dawn critical strikes cause the target to be healed for an additional $431415o1 over $431415d.]?c3[Hammer of Wrath and Divine Storm critical strikes cause the target to burn for an additional $431414o1 Radiant damage over $431414d.][]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95080` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Solar Grace
- Node ID: `109750`
- Entry ID: `136008`
- Definition ID: `140763`
- Spell ID: `431404`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Haste is increased by $s1%.
- Effect: Haste is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109748` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Endless Wrath
- Node ID: `95185`
- Entry ID: `117820`
- Definition ID: `122832`
- Spell ID: `432615`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empyrean Hammer has a $s1% increased chance to critically strike.
- Effect: Empyrean Hammer has a $s1% increased chance to critically strike.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95179` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sanctification
- Node ID: `95185`
- Entry ID: `117819`
- Definition ID: `122831`
- Spell ID: `432977`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Casting Judgment increases the damage of Empyrean Hammer by $433671s1% for $433671d.

Multiple applications may overlap.
- Effect: Casting Judgment increases the damage of Empyrean Hammer by $433671s1% for $433671d.

Multiple applications may overlap.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95179` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hammerfall
- Node ID: `95184`
- Entry ID: `117818`
- Definition ID: `122830`
- Spell ID: `432463`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137028[Shield of the Righteous and Word of Glory]?s383328[Final Verdict][Templar's Verdict]$?a137027[ and Divine Storm][] calls down an Empyrean Hammer on a nearby enemy.

While Shake the Heavens is active, this effect calls down an additional Empyrean Hammer.
- Effect: $?a137028[Shield of the Righteous and Word of Glory]?s383328[Final Verdict][Templar's Verdict]$?a137027[ and Divine Storm][] calls down an Empyrean Hammer on a nearby enemy.

While Shake the Heavens is active, this effect calls down an additional Empyrean Hammer.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95178` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Afterimage
- Node ID: `93189`
- Entry ID: `115482`
- Definition ID: `120494`
- Spell ID: `385414`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After you spend $s3 Holy Power, your next Word of Glory echoes onto a nearby ally at $s1% effectiveness.
- Effect: After you spend $s3 Holy Power, your next Word of Glory echoes onto a nearby ally at $s1% effectiveness.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `81507` (type `2`), node `103859` (type `2`), node `109999` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Healing Hands
- Node ID: `93189`
- Entry ID: `115481`
- Definition ID: `120493`
- Spell ID: `326734`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The cooldown of Lay on Hands is reduced up to $s1%, based on the target's missing health.

Word of Glory's healing is increased by up to $m3% on yourself, based on your missing health.
- Effect: The cooldown of Lay on Hands is reduced up to $s1%, based on the target's missing health.

Word of Glory's healing is increased by up to $m3% on yourself, based on your missing health.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `81507` (type `2`), node `103859` (type `2`), node `109999` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Undisputed Ruling
- Node ID: `95186`
- Entry ID: `117822`
- Definition ID: `122834`
- Spell ID: `432626`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hammer of Light $?a137028[grants Shield of the Righteous, erupts a Consecration beneath its target][applies Judgment to its targets], and increases your Haste by $432629s1% for $432629d.
- Effect: Hammer of Light $?a137028[grants Shield of the Righteous, erupts a Consecration beneath its target][applies Judgment to its targets], and increases your Haste by $432629s1% for $432629d.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95181` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Exaction
- Node ID: `109745`
- Entry ID: `136003`
- Definition ID: `140758`
- Spell ID: `1260429`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Divine Toll casts $s1 additional $ltime:times; on your target at $s2% effectiveness.
- Effect: Divine Toll casts $s1 additional $ltime:times; on your target at $s2% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `109746` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Seal of the Templar
- Node ID: `109745`
- Entry ID: `136184`
- Definition ID: `140957`
- Spell ID: `1263252`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137028[Judgment]?s383328[Final Verdict][Templar's Verdict] damage increased by $?a137028[$s2%][$s1%].
- Effect: $?a137028[Judgment]?s383328[Final Verdict][Templar's Verdict] damage increased by $?a137028[$s2%][$s1%].
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `109746` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Greater Judgment
- Node ID: `81603`
- Entry ID: `102590`
- Definition ID: `107595`
- Spell ID: `231663`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Judgment causes the target to take $s1% increased damage from your next Holy Power ability.

Multiple applications may overlap.
- Effect: Judgment causes the target to take $s1% increased damage from your next Holy Power ability.

Multiple applications may overlap.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `81510` (type `2`), node `81598` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aurora
- Node ID: `95069`
- Entry ID: `117666`
- Definition ID: `122678`
- Spell ID: `439760`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After you cast $?c1[Holy Prism or Divine Toll]?c3[Wake of Ashes][], gain Divine Purpose.

$?c1[$@spellicon223819 $@spellname223819
$@spellaura223819]?c3[$@spellicon408458 $@spellname408458
$@spellaura408458][]
- Effect: After you cast $?c1[Holy Prism or Divine Toll]?c3[Wake of Ashes][], gain Divine Purpose.

$?c1[$@spellicon223819 $@spellname223819
$@spellaura223819]?c3[$@spellicon408458 $@spellname408458
$@spellaura408458][]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95098` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Walk Into Light
- Node ID: `95094`
- Entry ID: `117691`
- Definition ID: `122703`
- Spell ID: `1263782`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[You have a $s1% chance to gain Blessing of An'she and generate $s2 Holy Power after casting Avenging Wrath.

During Avenging Wrath, Hammer of Wrath casts Blade of Justice at $s3% effectiveness.][Infusion of Light occurs $s4% more often during Avenging Wrath.]
- Effect: $?c3[You have a $s1% chance to gain Blessing of An'she and generate $s2 Holy Power after casting Avenging Wrath.

During Avenging Wrath, Hammer of Wrath casts Blade of Justice at $s3% effectiveness.][Infusion of Light occurs $s4% more often during Avenging Wrath.]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95071` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Second Sunrise
- Node ID: `95086`
- Entry ID: `117683`
- Definition ID: `122695`
- Spell ID: `431474`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Light of Dawn and Holy Shock have a $s1% chance to cast again at $s2% effectiveness.]?c3[Divine Storm and Hammer of Wrath have a $s1% chance to cast again at $s2% effectiveness.][]
- Effect: $?c1[Light of Dawn and Holy Shock have a $s1% chance to cast again at $s2% effectiveness.]?c3[Divine Storm and Hammer of Wrath have a $s1% chance to cast again at $s2% effectiveness.][]
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95072` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Born in Sunlight
- Node ID: `109749`
- Entry ID: `136007`
- Definition ID: `140762`
- Spell ID: `1263920`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Dawnlight's critical strike chance is increased by $1264050s1% during Avenging Wrath.
- Effect: Dawnlight's critical strike chance is increased by $1264050s1% during Avenging Wrath.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109750` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shield of Vengeance
- Node ID: `109867`
- Entry ID: `136127`
- Definition ID: `140882`
- Spell ID: `1261562`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Divine Protection reduces damage taken by an additional $s2% and casts Shield of Vengeance.

$@spellicon184662$@spellname184662
$@spelldesc184662
- Effect: Divine Protection reduces damage taken by an additional $s2% and casts Shield of Vengeance.

$@spellicon184662$@spellname184662
$@spelldesc184662
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `93189` (type `2`), node `110012` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rebuke
- Node ID: `110093`
- Entry ID: `136594`
- Definition ID: `141367`
- Spell ID: `96231`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Interrupts spellcasting and prevents any spell in that school from being cast for $d.
- Effect: Interrupts spellcasting and prevents any spell in that school from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `81603` (type `2`), node `103855` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Light's Deliverance
- Node ID: `95182`
- Entry ID: `117815`
- Definition ID: `122827`
- Spell ID: `425518`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You gain a stack of Light's Deliverance when you call down an Empyrean Hammer.

While $?a137028[Divine Toll][Wake of Ashes] and Hammer of Light are unavailable, you consume $433674U stacks of Light's Deliverance, empowering yourself to cast Hammer of Light an additional time for free.
- Effect: You gain a stack of Light's Deliverance when you call down an Empyrean Hammer.

While $?a137028[Divine Toll][Wake of Ashes] and Hammer of Light are unavailable, you consume $433674U stacks of Light's Deliverance, empowering yourself to cast Hammer of Light an additional time for free.
- Point cost per purchased rank: `1` × Hero pool (Templar) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95184` (type `2`), node `95185` (type `2`), node `95186` (type `2`), node `109745` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sun's Avatar
- Node ID: `95105`
- Entry ID: `117702`
- Definition ID: `122714`
- Spell ID: `431425`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You link to your Dawnlights within $s8 yds, causing $431911s1 Radiant damage to enemies or $431939s1 healing to allies that pass through the beams, reduced beyond $?c3[$s9][$s6] targets.
- Effect: You link to your Dawnlights within $s8 yds, causing $431911s1 Radiant damage to enemies or $431939s1 healing to allies that pass through the beams, reduced beyond $?c3[$s9][$s6] targets.
- Point cost per purchased rank: `1` × Hero pool (Herald of the Sun) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95069` (type `2`), node `95086` (type `2`), node `95094` (type `2`), node `109749` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Toll
- Node ID: `109368`
- Entry ID: `135564`
- Definition ID: `140320`
- Spell ID: `375576`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Instantly cast $?a137029[Holy Shock at $375609s2% effectiveness]?a137028[Avenger's Shield]?a137027[Judgment][Holy Shock, Avenger's Shield, or Judgment] on up to $s1 targets within $A2 yds.$?c3[

Divine Toll's Judgment deals $s6% increased damage.][]$?c2[

Generates $s5 Holy Power per target hit.][]
- Effect: Instantly cast $?a137029[Holy Shock at $375609s2% effectiveness]?a137028[Avenger's Shield]?a137027[Judgment][Holy Shock, Avenger's Shield, or Judgment] on up to $s1 targets within $A2 yds.$?c3[

Divine Toll's Judgment deals $s6% increased damage.][]$?c2[

Generates $s5 Holy Power per target hit.][]
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `group`; type `1` | source `node`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `81605` (type `2`), node `81631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unbound Freedom
- Node ID: `93174`
- Entry ID: `115454`
- Definition ID: `120466`
- Spell ID: `305394`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blessing of Freedom increases movement speed by $m1%, and you gain Blessing of Freedom when cast on a friendly target.
- Effect: Blessing of Freedom increases movement speed by $m1%, and you gain Blessing of Freedom when cast on a friendly target.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Punishment
- Node ID: `110091`
- Entry ID: `136592`
- Definition ID: `141365`
- Spell ID: `403530`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Successfully interrupting an enemy with Rebuke$?s31935[ or Avenger's Shield][] casts an extra $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?s137029[Holy Shock][Crusader Strike].
- Effect: Successfully interrupting an enemy with Rebuke$?s31935[ or Avenger's Shield][] casts an extra $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?s137029[Holy Shock][Crusader Strike].
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `110093` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Holy Armaments
- Node ID: `95234`
- Entry ID: `117882`
- Definition ID: `122894`
- Spell ID: `432459`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Will the Light to coalesce and become manifest as a Holy Armament, wielded by your friendly target.|n|n$@spellicon432496 $@spellname432496: $@spelldesc432496|n|n$@spellicon432502 $@spellname432502: $@spelldesc432502
- Effect: Will the Light to coalesce and become manifest as a Holy Armament, wielded by your friendly target.|n|n$@spellicon432496 $@spellname432496: $@spelldesc432496|n|n$@spellicon432502 $@spellname432502: $@spelldesc432502
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `node`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Holy Armaments
- Node ID: `110257`
- Entry ID: `136795`
- Definition ID: `141558`
- Spell ID: `1289728`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Will the Light to coalesce and become manifest as a Holy Armament, wielded by your friendly target.|n|n$@spellicon432496 $@spellname432496: $@spelldesc432496|n|n$@spellicon432502 $@spellname432502: $@spelldesc432502
- Effect: Will the Light to coalesce and become manifest as a Holy Armament, wielded by your friendly target.|n|n$@spellicon432496 $@spellname432496: $@spelldesc432496|n|n$@spellicon432502 $@spellname432502: $@spelldesc432502
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `node`; type `4` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Resonance
- Node ID: `93181`
- Entry ID: `115468`
- Definition ID: `120480`
- Spell ID: `384027`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc384028
- Effect: $@spelldesc384028
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81496` (type `2`), node `109368` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quickened Invocation
- Node ID: `93181`
- Entry ID: `115467`
- Definition ID: `120479`
- Spell ID: `379391`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Divine Toll's, Holy Armament's, and Holy Prism's][Divine Toll's] cooldown is reduced by ${-$s1/1000} sec.
- Effect: $?c1[Divine Toll's, Holy Armament's, and Holy Prism's][Divine Toll's] cooldown is reduced by ${-$s1/1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81496` (type `2`), node `109368` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sacred Strength
- Node ID: `81618`
- Entry ID: `102608`
- Definition ID: `107613`
- Spell ID: `469337`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Holy Power spending abilities have $s1% increased damage and healing.
- Effect: Holy Power spending abilities have $s1% increased damage and healing.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81614` (type `2`), node `81616` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Purpose
- Node ID: `81618`
- Entry ID: `128243`
- Definition ID: `133050`
- Spell ID: `408459`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Holy Power spending abilities have a $s1% chance to make your next Holy Power spending ability free and deal $408458s2% increased damage and healing.
- Effect: Holy Power spending abilities have a $s1% chance to make your next Holy Power spending ability free and deal $408458s2% increased damage and healing.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81614` (type `2`), node `81616` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightforged Blessing
- Node ID: `93008`
- Entry ID: `115239`
- Definition ID: `120251`
- Spell ID: `403479`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Divine Storm heals you and up to $s2 nearby allies for $403460s1.
- Effect: Divine Storm heals you and up to $s2 nearby allies for $403460s1.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81609` (type `2`), node `93168` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
