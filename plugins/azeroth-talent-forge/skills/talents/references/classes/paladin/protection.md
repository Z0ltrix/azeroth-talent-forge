# Protection

Reviewed build: `12.1.0.69404`
Spec ID: `66`
Role: `0`

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
### Lay on Hands
- Node ID: `81597`
- Entry ID: `102583`
- Definition ID: `107588`
- Spell ID: `633`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals a friendly target for an amount equal to $s2% your maximum health.$?a387791[

Grants the target $387792s1% increased armor for $387792d.][]

Cannot be used on a target with Forbearance. Causes Forbearance for $25771d.
- Effect: Heals a friendly target for an amount equal to $s2% your maximum health.$?a387791[

Grants the target $387792s1% increased armor for $387792d.][]

Cannot be used on a target with Forbearance. Causes Forbearance for $25771d.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
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
- Node ID: `93188`
- Entry ID: `115480`
- Definition ID: `120492`
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
### Divine Steed
- Node ID: `81632`
- Entry ID: `102625`
- Definition ID: `107630`
- Spell ID: `190784`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Leap atop your Charger for $221883d, increasing movement speed by $221883s4%. Usable while indoors or in combat.
- Effect: Leap atop your Charger for $221883d, increasing movement speed by $221883s4%. Usable while indoors or in combat.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `81598` (type `2`), node `81600` (type `2`), node `109999` (type `2`)
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
### Rebuke
- Node ID: `81604`
- Entry ID: `102591`
- Definition ID: `107596`
- Spell ID: `96231`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Interrupts spellcasting and prevents any spell in that school from being cast for $d.
- Effect: Interrupts spellcasting and prevents any spell in that school from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `81603` (type `2`), node `92220` (type `2`), node `103855` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Toll
- Node ID: `110006`
- Entry ID: `136496`
- Definition ID: `141269`
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
- Source gates: source `node`; type `4`; currency `2801` spend gate `0` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `1`
- Incoming edges: node `81605` (type `2`), node `81631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unbound Freedom
- Node ID: `93187`
- Entry ID: `115479`
- Definition ID: `120491`
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
- Node ID: `93165`
- Entry ID: `115444`
- Definition ID: `120456`
- Spell ID: `403530`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Successfully interrupting an enemy with Rebuke$?s31935[ or Avenger's Shield][] casts an extra $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?s137029[Holy Shock][Crusader Strike].
- Effect: Successfully interrupting an enemy with Rebuke$?s31935[ or Avenger's Shield][] casts an extra $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?s137029[Holy Shock][Crusader Strike].
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81604` (type `2`), node `110092` (type `2`), node `110093` (type `2`)
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
- Node ID: `81479`
- Entry ID: `102443`
- Definition ID: `107448`
- Spell ID: `386738`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc386732
- Effect: $@spelldesc386732
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81496` (type `2`), node `109368` (type `2`), node `110006` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quickened Invocation
- Node ID: `81479`
- Entry ID: `115168`
- Definition ID: `120175`
- Spell ID: `379391`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Divine Toll's, Holy Armament's, and Holy Prism's][Divine Toll's] cooldown is reduced by ${-$s1/1000} sec.
- Effect: $?c1[Divine Toll's, Holy Armament's, and Holy Prism's][Divine Toll's] cooldown is reduced by ${-$s1/1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81496` (type `2`), node `109368` (type `2`), node `110006` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rite of Sanctification
- Node ID: `95233`
- Entry ID: `117881`
- Definition ID: `122893`
- Spell ID: `433568`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Imbue your weapon with the power of the Light, increasing your armor by $433550s2% and your primary stat by $433550s1%.

Lasts $433550d.
- Effect: Imbue your weapon with the power of the Light, increasing your armor by $433550s2% and your primary stat by $433550s1%.

Lasts $433550d.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95234` (type `2`), node `110257` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rite of Adjuration
- Node ID: `95233`
- Entry ID: `117880`
- Definition ID: `122892`
- Spell ID: `433583`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Imbue your weapon with the power of the Light, increasing your Stamina by $433584s1% and causing your Holy Power abilities to sometimes unleash a burst of healing around a target.

Lasts $433584d.
- Effect: Imbue your weapon with the power of the Light, increasing your Stamina by $433584s1% and causing your Holy Power abilities to sometimes unleash a burst of healing around a target.

Lasts $433584d.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95234` (type `2`), node `110257` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Solidarity
- Node ID: `95228`
- Entry ID: `117873`
- Definition ID: `122885`
- Spell ID: `432802`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If you bestow an Armament upon an ally, you also gain its benefits.

If you bestow an Armament upon yourself, a nearby ally also gains its benefits.
- Effect: If you bestow an Armament upon an ally, you also gain its benefits.

If you bestow an Armament upon yourself, a nearby ally also gains its benefits.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95234` (type `2`), node `110257` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Guidance
- Node ID: `95235`
- Entry ID: `117884`
- Definition ID: `122896`
- Spell ID: `433106`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For each Holy Power ability cast, your next Consecration deals $?a137029[$<holy>][$<prot>] damage immediately, split across all enemies.

Up to $s3 nearby $Lally is:allies are each; healed for $?a137029[$s5][$s4]% of the damage amount.
- Effect: For each Holy Power ability cast, your next Consecration deals $?a137029[$<holy>][$<prot>] damage immediately, split across all enemies.

Up to $s3 nearby $Lally is:allies are each; healed for $?a137029[$s5][$s4]% of the damage amount.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95234` (type `2`), node `110257` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blessed Assurance
- Node ID: `95235`
- Entry ID: `117883`
- Definition ID: `122895`
- Spell ID: `433015`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Casting a Holy Power ability increases the damage and healing of your next $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?s137029[Holy Shock][Crusader Strike] by $433019s1%.
- Effect: Casting a Holy Power ability increases the damage and healing of your next $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?s137029[Holy Shock][Crusader Strike] by $433019s1%.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95234` (type `2`), node `110257` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Masterwork
- Node ID: `109742`
- Entry ID: `136000`
- Definition ID: `140755`
- Spell ID: `1271387`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After casting a Holy Armament, your next $s1 $Lcast:casts; of $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?a137029[Holy Shock or Crusader Strike][Crusader Strike] bestow a Lesser Armament of the same kind on a nearby ally.
- Effect: After casting a Holy Armament, your next $s1 $Lcast:casts; of $?s204019[Blessed Hammer]?s53595[Hammer of the Righteous]?a137029[Holy Shock or Crusader Strike][Crusader Strike] bestow a Lesser Armament of the same kind on a nearby ally.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95234` (type `2`), node `110257` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sacred Strength
- Node ID: `93192`
- Entry ID: `115490`
- Definition ID: `120502`
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
- Node ID: `93192`
- Entry ID: `128244`
- Definition ID: `133051`
- Spell ID: `223817`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Holy Power spending abilities have a $s1% chance to make your next Holy Power spending ability free and deal $223819s2% increased damage and healing.
- Effect: Holy Power spending abilities have a $s1% chance to make your next Holy Power spending ability free and deal $223819s2% increased damage and healing.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81614` (type `2`), node `81616` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Divine Inspiration
- Node ID: `95231`
- Entry ID: `117877`
- Definition ID: `122889`
- Spell ID: `432964`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your spells and abilities have a chance to manifest a Holy Armament for a nearby ally.
- Effect: Your spells and abilities have a chance to manifest a Holy Armament for a nearby ally.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95228` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Forewarning
- Node ID: `95231`
- Entry ID: `117876`
- Definition ID: `122888`
- Spell ID: `432804`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: The cooldown of Holy Armaments is reduced by $s1%.
- Effect: The cooldown of Holy Armaments is reduced by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95228` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Authoritative Rebuke
- Node ID: `95232`
- Entry ID: `117879`
- Definition ID: `122891`
- Spell ID: `469886`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Successfully $?c1[dispelling a harmful effect][interrupting an enemy spellcast] reduces $?c1[Cleanse's cooldown by ${$s3/1000}.1 sec][Rebuke's cooldown by ${$s1/1000}.1 sec]. Effect increased by $s2% while wielding a Holy Armament.
- Effect: Successfully $?c1[dispelling a harmful effect][interrupting an enemy spellcast] reduces $?c1[Cleanse's cooldown by ${$s3/1000}.1 sec][Rebuke's cooldown by ${$s1/1000}.1 sec]. Effect increased by $s2% while wielding a Holy Armament.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95235` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tempered in Battle
- Node ID: `95232`
- Entry ID: `117878`
- Definition ID: `122890`
- Spell ID: `469701`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you or an ally wielding a Holy Bulwark are healed above maximum health, transfer $s1% of the overhealing to your ally.

When you or an ally wielding a Sacred Weapon drop below $432502s4% health, redistribute your health immediately and every $469703t sec for $469703d. May only occur once per cast.
- Effect: When you or an ally wielding a Holy Bulwark are healed above maximum health, transfer $s1% of the overhealing to your ally.

When you or an ally wielding a Sacred Weapon drop below $432502s4% health, redistribute your health immediately and every $469703t sec for $469703d. May only occur once per cast.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95235` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Laying Down Arms
- Node ID: `95236`
- Entry ID: `117885`
- Definition ID: `122897`
- Spell ID: `432866`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When an Armament fades from you, the cooldown of Lay on Hands is reduced by ${$s1/1000}.1 sec and you gain $?a137028[Shining Light][Infusion of Light].
- Effect: When an Armament fades from you, the cooldown of Lay on Hands is reduced by ${$s1/1000}.1 sec and you gain $?a137028[Shining Light][Infusion of Light].
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95233` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hammer and Anvil
- Node ID: `109743`
- Entry ID: `136001`
- Definition ID: `140756`
- Spell ID: `433718`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Judgment critical strikes cause a shockwave around the target, $?c1[healing to up to $s3 injuried allies for $433722s1][dealing $433717s1 damage to enemies within $433717a1 yards. Damage reduced above $s4 targets].
- Effect: Judgment critical strikes cause a shockwave around the target, $?c1[healing to up to $s3 injuried allies for $433722s1][dealing $433717s1 damage to enemies within $433717a1 yards. Damage reduced above $s4 targets].
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109742` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightforged Blessing
- Node ID: `103850`
- Entry ID: `128240`
- Definition ID: `133047`
- Spell ID: `406468`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s2812[Denounce][Shield of the Righteous] heals you and up to $s3 nearby allies for $403460s1.
- Effect: $?s2812[Denounce][Shield of the Righteous] heals you and up to $s3 nearby allies for $403460s1.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81609` (type `2`), node `93168` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightforged Blessing
- Node ID: `103853`
- Entry ID: `128245`
- Definition ID: `133052`
- Spell ID: `406468`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s2812[Denounce][Shield of the Righteous] heals you and up to $s3 nearby allies for $403460s1.
- Effect: $?s2812[Denounce][Shield of the Righteous] heals you and up to $s3 nearby allies for $403460s1.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `81609` (type `2`), node `93168` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Valiance
- Node ID: `95229`
- Entry ID: `117874`
- Definition ID: `122886`
- Spell ID: `432919`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming $?a137028[Shining Light][Infusion of Light] reduces the cooldown of Holy Armaments by ${$s1/1000}.1 sec.
- Effect: Consuming $?a137028[Shining Light][Infusion of Light] reduces the cooldown of Holy Armaments by ${$s1/1000}.1 sec.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95231` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shared Resolve
- Node ID: `95237`
- Entry ID: `117886`
- Definition ID: `122898`
- Spell ID: `432821`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The effect of your active Aura is increased by $432496s1% on targets with your Armaments.
- Effect: The effect of your active Aura is increased by $432496s1% on targets with your Armaments.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95236` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reflection of Radiance
- Node ID: `95238`
- Entry ID: `117887`
- Definition ID: `122899`
- Spell ID: `1271466`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your Holy Bulwark absorbs damage or your Sacred Weapon deals damage or healing, you have a chance to gain $?c2[Grand Crusader][Awakening].
- Effect: When your Holy Bulwark absorbs damage or your Sacred Weapon deals damage or healing, you have a chance to gain $?c2[Grand Crusader][Awakening].
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95232` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Resounding Strike
- Node ID: `109744`
- Entry ID: `136002`
- Definition ID: `140757`
- Spell ID: `1271553`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Holy Armaments activate][Divine Toll activates] Hammer and Anvil at $s1% effectiveness.
- Effect: $?c1[Holy Armaments activate][Divine Toll activates] Hammer and Anvil at $s1% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109743` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blessing of the Forge
- Node ID: `95230`
- Entry ID: `117875`
- Definition ID: `122887`
- Spell ID: `433011`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Avenging Wrath summons an additional Sacred Weapon, and during Avenging Wrath your Sacred Weapon casts spells on your target and echoes the effects of your Holy Power abilities.
- Effect: Avenging Wrath summons an additional Sacred Weapon, and during Avenging Wrath your Sacred Weapon casts spells on your target and echoes the effects of your Holy Power abilities.
- Point cost per purchased rank: `1` × Hero pool (Lightsmith) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95229` (type `2`), node `95237` (type `2`), node `95238` (type `2`), node `109744` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
