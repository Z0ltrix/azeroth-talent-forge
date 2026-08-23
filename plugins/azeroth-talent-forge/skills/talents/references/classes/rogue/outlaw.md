# Outlaw

Reviewed build: `12.1.0.69404`
Spec ID: `260`
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
### Blind
- Node ID: `90684`
- Entry ID: `112572`
- Definition ID: `117577`
- Spell ID: `2094`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blinds the target, causing it to wander disoriented for $d. Damage may interrupt the effect. Limit 1.
- Effect: Blinds the target, causing it to wander disoriented for $d. Damage may interrupt the effect. Limit 1.
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
