# Subtlety

Reviewed build: `12.1.0.69404`
Spec ID: `261`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Hand of Fate
- Node ID: `95125`
- Entry ID: `117722`
- Definition ID: `122734`
- Spell ID: `452536`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Flip a Fatebound Coin each time a finishing move consumes $s1 or more combo points. Heads increases the damage of your attacks by ${$452923s4+$452923s1}%, lasting $452923d or until you flip Tails. Tails deals $452538s1 Cosmic damage to your target.

For each time the same face is flipped in a row, Heads increases damage by an additional $452923s1% and Tails increases its damage by $452917s1%.
- Effect: Flip a Fatebound Coin each time a finishing move consumes $s1 or more combo points. Heads increases the damage of your attacks by ${$452923s4+$452923s1}%, lasting $452923d or until you flip Tails. Tails deals $452538s1 Cosmic damage to your target.

For each time the same face is flipped in a row, Heads increases damage by an additional $452923s1% and Tails increases its damage by $452917s1%.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Cloak of Shadows
- Node ID: `90697`
- Entry ID: `112585`
- Definition ID: `117590`
- Spell ID: `31224`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Provides a moment of magic immunity, instantly removing all harmful spell effects. The cloak lingers, causing you to resist harmful spells for $d.
- Effect: Provides a moment of magic immunity, instantly removing all harmful spell effects. The cloak lingers, causing you to resist harmful spells for $d.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
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
### Unseen Blade
- Node ID: `95140`
- Entry ID: `117737`
- Definition ID: `122749`
- Spell ID: `441146`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137036[Sinister Strike]?s200758[Gloomblade][Backstab] and $?a137036[Ambush][Shadowstrike] now also strike with an Unseen Blade dealing $441144s1 damage. Targets struck are Fazed for $441224d.

Fazed enemies take $441224s1% more damage from you and cannot parry your attacks.

This effect may occur once every $459485d.
- Effect: $?a137036[Sinister Strike]?s200758[Gloomblade][Backstab] and $?a137036[Ambush][Shadowstrike] now also strike with an Unseen Blade dealing $441144s1 damage. Targets struck are Fazed for $441224d.

Fazed enemies take $441224s1% more damage from you and cannot parry your attacks.

This effect may occur once every $459485d.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Smoke
- Node ID: `95141`
- Entry ID: `117738`
- Definition ID: `122750`
- Spell ID: `441247`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You take $s1% reduced damage from Fazed targets.
- Effect: You take $s1% reduced damage from Fazed targets.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95140` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mirrors
- Node ID: `95141`
- Entry ID: `120130`
- Definition ID: `125030`
- Spell ID: `441250`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Feint reduces damage taken from area-of-effect attacks by an additional $s1%
- Effect: Feint reduces damage taken from area-of-effect attacks by an additional $s1%
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95140` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flawless Form
- Node ID: `95111`
- Entry ID: `117708`
- Definition ID: `122720`
- Spell ID: `441321`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unseen Blade and $?a137036[Killing Spree][Secret Technique] increase the damage of your finishing moves by $441326s1% for $441326d. Max $441326u stacks.
- Effect: Unseen Blade and $?a137036[Killing Spree][Secret Technique] increase the damage of your finishing moves by $441326s1% for $441326d. Max $441326u stacks.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95140` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Surprising Strikes
- Node ID: `95121`
- Entry ID: `117718`
- Definition ID: `122730`
- Spell ID: `441273`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Attacks that generate combo points deal $s1% increased critical strike damage to Fazed targets.
- Effect: Attacks that generate combo points deal $s1% increased critical strike damage to Fazed targets.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95140` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hoodwink
- Node ID: `109765`
- Entry ID: `136023`
- Definition ID: `140778`
- Spell ID: `1276626`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fazed increases damage taken by an additional $s1%.
- Effect: Fazed increases damage taken by an additional $s1%.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95140` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### So Tricky
- Node ID: `95134`
- Entry ID: `117731`
- Definition ID: `122743`
- Spell ID: `441403`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tricks of the Trade's threat redirect duration is increased to $m1 $Lhour:min;.
- Effect: Tricks of the Trade's threat redirect duration is increased to $m1 $Lhour:min;.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95121` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Don't Be Suspicious
- Node ID: `95134`
- Entry ID: `120133`
- Definition ID: `125033`
- Spell ID: `441415`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Blind and Shroud of Concealment have $s1% reduced cooldown.

Pick Pocket and Sap have $s2 yd increased range.
- Effect: Blind and Shroud of Concealment have $s1% reduced cooldown.

Pick Pocket and Sap have $s2 yd increased range.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95121` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thousand Cuts
- Node ID: `95137`
- Entry ID: `117734`
- Definition ID: `122746`
- Spell ID: `441346`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Slice and Dice grants $s1% additional attack speed and gives your auto-attacks a chance to refresh your opportunity to strike with Unseen Blade.
- Effect: Slice and Dice grants $s1% additional attack speed and gives your auto-attacks a chance to refresh your opportunity to strike with Unseen Blade.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95111` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flickerstrike
- Node ID: `95137`
- Entry ID: `120131`
- Definition ID: `125031`
- Spell ID: `441359`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Taking damage from an area-of-effect attack while Feint is active or dodging while Evasion is active refreshes your opportunity to strike with Unseen Blade.

This effect may only occur once every $proccooldown sec.
- Effect: Taking damage from an area-of-effect attack while Feint is active or dodging while Evasion is active refreshes your opportunity to strike with Unseen Blade.

This effect may only occur once every $proccooldown sec.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95111` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flashing Steel
- Node ID: `109764`
- Entry ID: `136022`
- Definition ID: `140777`
- Spell ID: `1276630`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unseen Blade may now occur once every ${20-($s1/-1000)} sec and has $s2% chance to strike twice.
- Effect: Unseen Blade may now occur once every ${20-($s1/-1000)} sec and has $s2% chance to strike twice.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109765` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Devious Distractions
- Node ID: `95133`
- Entry ID: `117730`
- Definition ID: `122742`
- Spell ID: `441263`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137036[Killing Spree][Secret Technique] applies Fazed to any targets struck.
- Effect: $?a137036[Killing Spree][Secret Technique] applies Fazed to any targets struck.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95141` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Disorienting Strikes
- Node ID: `95118`
- Entry ID: `117715`
- Definition ID: `122727`
- Spell ID: `441274`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137036[Killing Spree][Secret Technique] has $s1% reduced cooldown and allows your next $s2 strikes of Unseen Blade to ignore its cooldown.
- Effect: $?a137036[Killing Spree][Secret Technique] has $s1% reduced cooldown and allows your next $s2 strikes of Unseen Blade to ignore its cooldown.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95134` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cloud Cover
- Node ID: `95116`
- Entry ID: `117713`
- Definition ID: `122725`
- Spell ID: `441429`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating $?a137036[Adrenaline Rush][Shadow Blades] creates a cloud of smoke for $441587d, allowing attacks from within the cloud to apply Fazed, stacking up to $441640m2 additional $Ltime:times;.

Effect persists for $?a137036[${$s1/1000}][${$s2/1000}] sec after leaving the cloud.
- Effect: Activating $?a137036[Adrenaline Rush][Shadow Blades] creates a cloud of smoke for $441587d, allowing attacks from within the cloud to apply Fazed, stacking up to $441640m2 additional $Ltime:times;.

Effect persists for $?a137036[${$s1/1000}][${$s2/1000}] sec after leaving the cloud.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95133` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### No Scruples
- Node ID: `95116`
- Entry ID: `120132`
- Definition ID: `125032`
- Spell ID: `441398`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Finishing moves have $s1% increased chance to critically strike Fazed targets.
- Effect: Finishing moves have $s1% increased chance to critically strike Fazed targets.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95133` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nimble Flurry
- Node ID: `95128`
- Entry ID: `117725`
- Definition ID: `122737`
- Spell ID: `441367`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137036[Blade Flurry damage is increased by $s1%][Your auto-attacks, Unseen Blade, and Coup de Grace also strike up to $s2 nearby enemies for $s3% of normal damage] while Flawless Form is active.
- Effect: $?a137036[Blade Flurry damage is increased by $s1%][Your auto-attacks, Unseen Blade, and Coup de Grace also strike up to $s2 nearby enemies for $s3% of normal damage] while Flawless Form is active.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95137` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Clever Combatant
- Node ID: `109763`
- Entry ID: `136021`
- Definition ID: `140776`
- Spell ID: `1276679`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Pistol Shot][Shuriken Storm] has $?c2[$s1][$s2]% increased critical strike chance and now triggers Unseen Blade when available.
- Effect: $?c2[Pistol Shot][Shuriken Storm] has $?c2[$s1][$s2]% increased critical strike chance and now triggers Unseen Blade when available.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109764` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Coup de Grace
- Node ID: `95115`
- Entry ID: `117712`
- Definition ID: `122724`
- Spell ID: `441423`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After $441786s1 strikes with Unseen Blade, your next $?a137036[Dispatch][Eviscerate] will be performed as a Coup de Grace, functioning as if it had consumed $s3 additional combo points, and granting you $s2 stacks of Flawless Form.
- Effect: After $441786s1 strikes with Unseen Blade, your next $?a137036[Dispatch][Eviscerate] will be performed as a Coup de Grace, functioning as if it had consumed $s3 additional combo points, and granting you $s2 stacks of Flawless Form.
- Point cost per purchased rank: `1` × Hero pool (Trickster) (ID `2988`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95116` (type `2`), node `95118` (type `2`), node `95128` (type `2`), node `109763` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
