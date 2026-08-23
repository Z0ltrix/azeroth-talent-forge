# Holy

Reviewed build: `12.1.0.69404`
Spec ID: `65`
Role: `1`

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
### Improved Cleanse
- Node ID: `81508`
- Entry ID: `102477`
- Definition ID: `107482`
- Spell ID: `393024`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Cleanse additionally removes all Disease and Poison effects.
- Effect: Cleanse additionally removes all Disease and Poison effects.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
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
### Afterimage
- Node ID: `81613`
- Entry ID: `102601`
- Definition ID: `107606`
- Spell ID: `385414`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After you spend $s3 Holy Power, your next Word of Glory echoes onto a nearby ally at $s1% effectiveness.
- Effect: After you spend $s3 Holy Power, your next Word of Glory echoes onto a nearby ally at $s1% effectiveness.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `81508` (type `2`), node `103859` (type `2`), node `109999` (type `2`)
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
### Greater Judgment
- Node ID: `92220`
- Entry ID: `114292`
- Definition ID: `119297`
- Spell ID: `231644`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Judgment deems the target unworthy, preventing the next $<shield> damage dealt by the target.
- Effect: Judgment deems the target unworthy, preventing the next $<shield> damage dealt by the target.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
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
### Armory of Light
- Node ID: `110092`
- Entry ID: `136593`
- Definition ID: `141366`
- Spell ID: `1277443`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While holding a shield, you have a $s2% chance to block incoming spells, reducing their damage by $s3%. 

Without a shield, you have a $s4% chance to parry incoming melee attacks, reducing their damage by $s5%.
- Effect: While holding a shield, you have a $s2% chance to block incoming spells, reducing their damage by $s3%. 

Without a shield, you have a $s4% chance to parry incoming melee attacks, reducing their damage by $s5%.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `node`; type `1`
- Incoming edges: node `92220` (type `2`), node `103855` (type `2`)
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
- Node ID: `81496`
- Entry ID: `102465`
- Definition ID: `107470`
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
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1` | source `node`; type `4`
- Incoming edges: node `81605` (type `2`), node `81631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Holy Prism
- Node ID: `81496`
- Entry ID: `133480`
- Definition ID: `138266`
- Spell ID: `114165`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Fires a beam of light that scatters to strike a clump of targets. 

If the beam is aimed at an enemy target, it deals $114852s1 Holy damage and radiates ${$114852s2*$<healmod>} healing to 5 allies within $114852A2 yds.

If the beam is aimed at a friendly target, it heals for ${$114871s1*$<healmod>} and radiates $114871s2 Holy damage to 5 enemies within $114871A2 yds.

|cFFFFFFFFGenerates $s2 Holy Power.
- Effect: Fires a beam of light that scatters to strike a clump of targets. 

If the beam is aimed at an enemy target, it deals $114852s1 Holy damage and radiates ${$114852s2*$<healmod>} healing to 5 allies within $114852A2 yds.

If the beam is aimed at a friendly target, it heals for ${$114871s1*$<healmod>} and radiates $114871s2 Holy damage to 5 enemies within $114871A2 yds.

|cFFFFFFFFGenerates $s2 Holy Power.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1` | source `node`; type `4`
- Incoming edges: node `81605` (type `2`), node `81631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echoing Blessings
- Node ID: `93520`
- Entry ID: `115872`
- Definition ID: `120884`
- Spell ID: `387801`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blessing of Freedom increases the target's movement speed by $s3%. $?s204018[Blessing of Spellwarding][Blessing of Protection] and Blessing of Sacrifice reduce the target's damage taken by $s4%. These effects linger for $394454d after the Blessing ends.
- Effect: Blessing of Freedom increases the target's movement speed by $s3%. $?s204018[Blessing of Spellwarding][Blessing of Protection] and Blessing of Sacrifice reduce the target's damage taken by $s4%. These effects linger for $394454d after the Blessing ends.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unbound Freedom
- Node ID: `93520`
- Entry ID: `131438`
- Definition ID: `136239`
- Spell ID: `305394`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Blessing of Freedom increases movement speed by $m1%, and you gain Blessing of Freedom when cast on a friendly target.
- Effect: Blessing of Freedom increases movement speed by $m1%, and you gain Blessing of Freedom when cast on a friendly target.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81631` (type `2`)
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
- Node ID: `93180`
- Entry ID: `115466`
- Definition ID: `120478`
- Spell ID: `386738`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc386732
- Effect: $@spelldesc386732
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81496` (type `2`), node `110006` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quickened Invocation
- Node ID: `93180`
- Entry ID: `115465`
- Definition ID: `120477`
- Spell ID: `379391`
- Tree ID: `790`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Divine Toll's, Holy Armament's, and Holy Prism's][Divine Toll's] cooldown is reduced by ${-$s1/1000} sec.
- Effect: $?c1[Divine Toll's, Holy Armament's, and Holy Prism's][Divine Toll's] cooldown is reduced by ${-$s1/1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Holy, Protection, Retribution) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `81496` (type `2`), node `110006` (type `2`)
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
- Node ID: `93191`
- Entry ID: `115489`
- Definition ID: `120501`
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
- Node ID: `93191`
- Entry ID: `128246`
- Definition ID: `133053`
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
- Node ID: `103852`
- Entry ID: `128242`
- Definition ID: `133049`
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
