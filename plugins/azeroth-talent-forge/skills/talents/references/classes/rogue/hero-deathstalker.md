# Deathstalker

Reviewed build: `12.1.0.69404`
Hero subtree ID: `53`
Description: The harbingers of death, Deathstalkers strike from the shadows to bring a swift end to their targets.

## Hero talents

### Deathstalker's Mark
- Node ID: `95136`
- Entry ID: `117733`
- Definition ID: `122745`
- Spell ID: `457052`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Garrote][Shadowstrike] applies $s1 stacks of Deathstalker's Mark to your target, unless Deathstalker's Mark is already active. You learn Mark for Death.

When you spend $s2 or more combo points on attacks against a Marked target you consume an application of Deathstalker's Mark, dealing $457157s1 Plague damage.

$@spellicon1293340
$@spellname1293340
$@spelldesc1293340
- Effect: $?c1[Garrote][Shadowstrike] applies $s1 stacks of Deathstalker's Mark to your target, unless Deathstalker's Mark is already active. You learn Mark for Death.

When you spend $s2 or more combo points on attacks against a Marked target you consume an application of Deathstalker's Mark, dealing $457157s1 Plague damage.

$@spellicon1293340
$@spellname1293340
$@spelldesc1293340
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Clear the Witnesses
- Node ID: `95110`
- Entry ID: `117707`
- Definition ID: `122719`
- Spell ID: `1248793`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Fan of Knives][Shuriken Storm] damage increased by $s1%.
- Effect: $?c1[Fan of Knives][Shuriken Storm] damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95136` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hunt Them Down
- Node ID: `95132`
- Entry ID: `117729`
- Definition ID: `122741`
- Spell ID: `457054`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Auto-attacks against Marked targets deal an additional $457193s1 Plague damage.
- Effect: Auto-attacks against Marked targets deal an additional $457193s1 Plague damage.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95136` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Singular Focus
- Node ID: `95117`
- Entry ID: `117714`
- Definition ID: `122726`
- Spell ID: `457055`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage dealt to targets other than your Marked target deals $s1% Plague damage to your Marked target.
- Effect: Damage dealt to targets other than your Marked target deals $s1% Plague damage to your Marked target.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95136` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Precise Killer
- Node ID: `109762`
- Entry ID: `136020`
- Definition ID: `140775`
- Spell ID: `1272989`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strike damage bonus increased by $s2%.
- Effect: Critical strike damage bonus increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95136` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quietus Celeris
- Node ID: `109761`
- Entry ID: `136019`
- Definition ID: `140774`
- Spell ID: `1273017`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Deathstalker's Mark has a ${$s1/$s2*100}% chance to immediately consume a stack when applied.
- Effect: Deathstalker's Mark has a ${$s1/$s2*100}% chance to immediately consume a stack when applied.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109762` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unshakeable Drive
- Node ID: `95135`
- Entry ID: `117732`
- Definition ID: `122744`
- Spell ID: `1248774`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you consume an application of Deathstalker's Mark, the damage of your next $?c1[Ambush or Mutilate]?s200758[Gloomblade][Backstab] is increased by $1248775s1%$?c1[][ or Shadowstrike increased by $1248775s2%].
- Effect: When you consume an application of Deathstalker's Mark, the damage of your next $?c1[Ambush or Mutilate]?s200758[Gloomblade][Backstab] is increased by $1248775s1%$?c1[][ or Shadowstrike increased by $1248775s2%].
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95110` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Corrupt the Blood
- Node ID: `95108`
- Entry ID: `117705`
- Definition ID: `122717`
- Spell ID: `1248785`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Rupture][Deathstalker's Mark] damage increased by $?c1[$s1][$s2]%.
- Effect: $?c1[Rupture][Deathstalker's Mark] damage increased by $?c1[$s1][$s2]%.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95132` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lingering Darkness
- Node ID: `95109`
- Entry ID: `117706`
- Definition ID: `122718`
- Spell ID: `457056`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After $?c1[Deathmark][Shadow Blades] expires, gain $?c1[$457273s1][$457273s2]% increased $?c1[Nature][Shadow] damage for $457273d.
- Effect: After $?c1[Deathmark][Shadow Blades] expires, gain $?c1[$457273s1][$457273s2]% increased $?c1[Nature][Shadow] damage for $457273d.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95117` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Symbolic Victory
- Node ID: `95109`
- Entry ID: `126030`
- Definition ID: `130862`
- Spell ID: `457062`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137037 [Kingsbane][Shadow Dance] additionally increases the damage of your next $?a137037 [two Envenoms][Eviscerate or Black Powder] by $?a137037[$457167s1][$457167s2]%.
- Effect: $?a137037 [Kingsbane][Shadow Dance] additionally increases the damage of your next $?a137037 [two Envenoms][Eviscerate or Black Powder] by $?a137037[$457167s1][$457167s2]%.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95117` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ethereal Cloak
- Node ID: `95106`
- Entry ID: `117703`
- Definition ID: `122715`
- Spell ID: `457022`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Cloak of Shadows duration increased by ${$s1/1000} sec.
- Effect: Cloak of Shadows duration increased by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95135` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bait and Switch
- Node ID: `95106`
- Entry ID: `126029`
- Definition ID: `130861`
- Spell ID: `457034`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Evasion reduces magical damage taken by ${-$s1}%. 

Cloak of Shadows reduces physical damage taken by ${-$s2}%.
- Effect: Evasion reduces magical damage taken by ${-$s1}%. 

Cloak of Shadows reduces physical damage taken by ${-$s2}%.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95135` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Momentum of Despair
- Node ID: `95131`
- Entry ID: `117728`
- Definition ID: `122740`
- Spell ID: `457067`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If you have critically struck with $?c1[Fan of Knives][Shuriken Storm], increase the critical strike chance of $?c1[Fan of Knives][Shuriken Storm] and $?c1[Crimson Tempest][Black Powder] by $457115s1% and critical strike damage by $457115s2% for $457115d.
- Effect: If you have critically struck with $?c1[Fan of Knives][Shuriken Storm], increase the critical strike chance of $?c1[Fan of Knives][Shuriken Storm] and $?c1[Crimson Tempest][Black Powder] by $457115s1% and critical strike damage by $457115s2% for $457115d.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95108` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Follow the Blood
- Node ID: `95131`
- Entry ID: `126028`
- Definition ID: `130860`
- Spell ID: `457068`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c1[Fan of Knives][Shuriken Storm] and $?c1[Crimson Tempest][Black Powder] deal $?c1[$s1][$s3]% additional damage while $?c1[$s2 or more enemies are afflicted with Rupture][Find Weakness is active].
- Effect: $?c1[Fan of Knives][Shuriken Storm] and $?c1[Crimson Tempest][Black Powder] deal $?c1[$s1][$s3]% additional damage while $?c1[$s2 or more enemies are afflicted with Rupture][Find Weakness is active].
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95108` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadewalker
- Node ID: `95123`
- Entry ID: `117720`
- Definition ID: `122732`
- Spell ID: `457057`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each time you consume a stack of Deathstalker's Mark, reduce the cooldown of Shadowstep by ${$s1/-1000} sec.
- Effect: Each time you consume a stack of Deathstalker's Mark, reduce the cooldown of Shadowstep by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95109` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shroud of Night
- Node ID: `95123`
- Entry ID: `126027`
- Definition ID: `130859`
- Spell ID: `457063`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Shroud of Concealment duration increased by ${$s1/1000} sec.
- Effect: Shroud of Concealment duration increased by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95109` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mass Casualty
- Node ID: `109760`
- Entry ID: `136018`
- Definition ID: `140773`
- Spell ID: `1273035`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Deathstalker's Mark deals $?c1[$s1][$s2]% of its normal damage to all other enemies within 8 yds $?c1[that are afflicted by Rupture][when a stack is consumed by Black Powder].
- Effect: Deathstalker's Mark deals $?c1[$s1][$s2]% of its normal damage to all other enemies within 8 yds $?c1[that are afflicted by Rupture][when a stack is consumed by Black Powder].
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109761` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Darkest Night
- Node ID: `95142`
- Entry ID: `117739`
- Definition ID: `122751`
- Spell ID: `457058`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you consume the final Deathstalker's Mark from a target or your target dies, gain $457280s1 Energy and Darkest Night, causing your next $?c1[Envenom][Eviscerate] cast with 5 or more combo points to critically strike, deal $457280s2% additional damage, and apply $457280s3 stacks of Deathstalker's Mark to the target if no other Deathstalker's Mark is active.

$?c1[Envenom][Eviscerate] cast with Darkest Night does not consume a stack of active Deathstalker's Marks.
- Effect: When you consume the final Deathstalker's Mark from a target or your target dies, gain $457280s1 Energy and Darkest Night, causing your next $?c1[Envenom][Eviscerate] cast with 5 or more combo points to critically strike, deal $457280s2% additional damage, and apply $457280s3 stacks of Deathstalker's Mark to the target if no other Deathstalker's Mark is active.

$?c1[Envenom][Eviscerate] cast with Darkest Night does not consume a stack of active Deathstalker's Marks.
- Point cost per purchased rank: `1` × Hero pool (Deathstalker) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95106` (type `2`), node `95123` (type `2`), node `95131` (type `2`), node `109760` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
