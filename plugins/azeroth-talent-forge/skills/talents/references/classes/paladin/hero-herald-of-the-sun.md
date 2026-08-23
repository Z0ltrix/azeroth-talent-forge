# Herald of the Sun

Reviewed build: `12.1.0.69404`
Hero subtree ID: `50`
Description: Heralds of the Sun develop a deep bond to the sun and solar energy, using it to burn enemies and cauterize their allies' wounds. They can manifest potent solar rays while fully connected to the Light.

## Hero talents

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
