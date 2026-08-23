# Fatebound

Reviewed build: `12.1.0.69404`
Hero subtree ID: `52`
Description: The Fatebound eagerly act as the Hand of Fate, sowing chaos into well-laid plans. Guided by the whims of a flipped Fatebound Coin, they deliver the ending their enemies are destined for; the ending they deserve.

## Hero talents

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
