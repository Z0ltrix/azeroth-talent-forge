# Templar

Reviewed build: `12.1.0.69404`
Hero subtree ID: `48`
Description: Templars stop at nothing to bring justice to the wicked. They call down hammers of Light and unleash devastating combinations of physical and holy attacks to vanquish their enemies.

## Hero talents

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
