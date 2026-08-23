# Assassination

Reviewed build: `12.1.0.69404`
Spec ID: `259`
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
### Shiv
- Node ID: `90740`
- Entry ID: `112630`
- Definition ID: `117635`
- Spell ID: `5938`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Attack with your $?s319032[poisoned blades][off-hand], dealing $sw1 Physical damage, dispelling all enrage effects and applying a concentrated form of your $?a3408[Crippling Poison, reducing movement speed by $115196s1% for $115196d.]?a5761[Numbing Poison, reducing casting speed by $359078s1% for $359078d.][]$?(!a3408&!a5761)[active Non-Lethal poison.][]$?(a319032&a400783)[

Your Nature and Bleed ]?a319032[

Your Nature ]?a400783[

Your Bleed ][]$?(a400783|a319032)[damage done to the target is increased by $319504s1% for $319504d.][]$?a354124[ The target's healing received is reduced by $1291471S1% for $1291471d.][]

|cFFFFFFFFAwards $s3 combo $lpoint:points;.|r
- Effect: Attack with your $?s319032[poisoned blades][off-hand], dealing $sw1 Physical damage, dispelling all enrage effects and applying a concentrated form of your $?a3408[Crippling Poison, reducing movement speed by $115196s1% for $115196d.]?a5761[Numbing Poison, reducing casting speed by $359078s1% for $359078d.][]$?(!a3408&!a5761)[active Non-Lethal poison.][]$?(a319032&a400783)[

Your Nature and Bleed ]?a319032[

Your Nature ]?a400783[

Your Bleed ][]$?(a400783|a319032)[damage done to the target is increased by $319504s1% for $319504d.][]$?a354124[ The target's healing received is reduced by $1291471S1% for $1291471d.][]

|cFFFFFFFFAwards $s3 combo $lpoint:points;.|r
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chosen's Revelry
- Node ID: `95138`
- Entry ID: `117735`
- Definition ID: `122747`
- Spell ID: `1249201`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Flipping a Fatebound Coin restores $1249202s1 health.
- Effect: Flipping a Fatebound Coin restores $1249202s1 health.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95125` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tempted Fate
- Node ID: `95138`
- Entry ID: `125132`
- Definition ID: `129964`
- Spell ID: `454286`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: You have a $s2% chance to absorb $s1% of any damage taken.
- Effect: You have a $s2% chance to absorb $s1% of any damage taken.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95125` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mean Streak
- Node ID: `95122`
- Entry ID: `117719`
- Definition ID: `122731`
- Spell ID: `453428`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fatebound Coins flipped by $?a137036[Dispatch][Envenom] are $s1% more likely to match the same face as the last flip.
- Effect: Fatebound Coins flipped by $?a137036[Dispatch][Envenom] are $s1% more likely to match the same face as the last flip.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95125` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Inexorable March
- Node ID: `95130`
- Entry ID: `117727`
- Definition ID: `122739`
- Spell ID: `454432`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You cannot be slowed below $s1% of normal movement speed while your Fatebound Coin flips have an active streak of at least $s2 flips matching the same face.
- Effect: You cannot be slowed below $s1% of normal movement speed while your Fatebound Coin flips have an active streak of at least $s2 flips matching the same face.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95125` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death's Arrival
- Node ID: `95130`
- Entry ID: `125140`
- Definition ID: `129972`
- Spell ID: `454433`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137037[Shadowstep][Grappling Hook] may be used a second time within $457333d with no cooldown, but its total cooldown is increased by ${$s3/1000} sec.
- Effect: $?a137037[Shadowstep][Grappling Hook] may be used a second time within $457333d with no cooldown, but its total cooldown is increased by ${$s3/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95125` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sometimes Lucky
- Node ID: `109767`
- Entry ID: `136025`
- Definition ID: `140780`
- Spell ID: `1277030`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strike chance increased by $s1%.
- Effect: Critical strike chance increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95125` (type `2`)
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
### Deal Fate
- Node ID: `95107`
- Entry ID: `117704`
- Definition ID: `122716`
- Spell ID: `454419`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a383281[Sinister Strike and Ambush generate]?a137036[Sinister Strike generates][Mutilate, Ambush, and Fan of Knives have a $s1% chance to generate] $454421s1 additional combo point $?a383281[when they grant Opportunity]?a137036[when it grants Opportunity][when they trigger Seal Fate].
- Effect: $?a383281[Sinister Strike and Ambush generate]?a137036[Sinister Strike generates][Mutilate, Ambush, and Fan of Knives have a $s1% chance to generate] $454421s1 additional combo point $?a383281[when they grant Opportunity]?a137036[when it grants Opportunity][when they trigger Seal Fate].
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95138` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fate Intertwined
- Node ID: `95139`
- Entry ID: `117736`
- Definition ID: `122748`
- Spell ID: `1249215`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Caustic Spatter][Blade Flurry] causes an additional $?c1[$s1% of Nature][$s2% of attack] damage dealt to be dealt to affected enemies.
- Effect: $?c1[Caustic Spatter][Blade Flurry] causes an additional $?c1[$s1% of Nature][$s2% of attack] damage dealt to be dealt to affected enemies.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95122` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Edge Case
- Node ID: `95120`
- Entry ID: `117717`
- Definition ID: `122729`
- Spell ID: `453457`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating $?a137036[Adrenaline Rush][Deathmark] flips a Fatebound Coin and causes it to land on its edge, counting as both Heads and Tails.
- Effect: Activating $?a137036[Adrenaline Rush][Deathmark] flips a Fatebound Coin and causes it to land on its edge, counting as both Heads and Tails.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95130` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Controlled Chaos
- Node ID: `109768`
- Entry ID: `136026`
- Definition ID: `140781`
- Spell ID: `1276816`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After flipping a Fatebound Coin that ends a streak of $s1 or more, flip another that matches the same face.
- Effect: After flipping a Fatebound Coin that ends a streak of $s1 or more, flip another that matches the same face.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109767` (type `2`)
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
### Delivered Doom
- Node ID: `95119`
- Entry ID: `117716`
- Definition ID: `122728`
- Spell ID: `1249194`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Envenom deals][Dispatch and Between the Eyes deal] $s1% more damage when $?c1[it consumes][they consume] $s2 or more combo points.
- Effect: $?c1[Envenom deals][Dispatch and Between the Eyes deal] $s1% more damage when $?c1[it consumes][they consume] $s2 or more combo points.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95107` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overflowing Purse
- Node ID: `95114`
- Entry ID: `117711`
- Definition ID: `122723`
- Spell ID: `1249190`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Dispatch][Envenom] has a $?c2[$s2][$s3]% chance to flip $s1 Fatebound Coins.
- Effect: $?c2[Dispatch][Envenom] has a $?c2[$s2][$s3]% chance to flip $s1 Fatebound Coins.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95139` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Destiny Defined
- Node ID: `95114`
- Entry ID: `125139`
- Definition ID: `129971`
- Spell ID: `454435`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137037[Weapon poisons have $s1% increased application chance][Sinister Strike has $s2% increased chance to strike an additional time and grant Opportunity] and your Fatebound Coins flipped have an additional $s3% chance to match the same face as the last flip.
- Effect: $?a137037[Weapon poisons have $s1% increased application chance][Sinister Strike has $s2% increased chance to strike an additional time and grant Opportunity] and your Fatebound Coins flipped have an additional $s3% chance to match the same face as the last flip.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95139` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rush to the Inevitable
- Node ID: `95129`
- Entry ID: `117726`
- Definition ID: `122738`
- Spell ID: `1249204`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain $?c1[$s1][$s2] Energy every time you flip a Fatebound Coin. Gain $?c1[$s3][$s4] Energy for Coins that land on their edge.
- Effect: Gain $?c1[$s1][$s2] Energy every time you flip a Fatebound Coin. Gain $?c1[$s3][$s4] Energy for Coins that land on their edge.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95120` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ravenholdt Mint
- Node ID: `109766`
- Entry ID: `136024`
- Definition ID: `140779`
- Spell ID: `1276809`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Flipping Heads increases damage by an additional $s1%. Damage dealt by flipping Tails is increased by $s2%.
- Effect: Flipping Heads increases damage by an additional $s1%. Damage dealt by flipping Tails is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109768` (type `2`)
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
### Lucky Coin
- Node ID: `95127`
- Entry ID: `117724`
- Definition ID: `122736`
- Spell ID: `1248970`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 coin flips, keep a lucky coin that bends you towards your fate for $1248971d. Your Agility is increased by $1248971s1%, the damage and bonuses of Fatebound Coins are increased by $1248971s3%, and coin flips are $1248971s5% more likely to match the same face as the last flip.

Coin flips do not count toward finding a lucky coin while you have a lucky coin.
- Effect: Every $s1 coin flips, keep a lucky coin that bends you towards your fate for $1248971d. Your Agility is increased by $1248971s1%, the damage and bonuses of Fatebound Coins are increased by $1248971s3%, and coin flips are $1248971s5% more likely to match the same face as the last flip.

Coin flips do not count toward finding a lucky coin while you have a lucky coin.
- Point cost per purchased rank: `1` × Hero pool (Fatebound) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2962` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95114` (type `2`), node `95119` (type `2`), node `95129` (type `2`), node `109766` (type `2`)
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
