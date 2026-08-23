# Trickster

Reviewed build: `12.1.0.69404`
Hero subtree ID: `51`
Description: Dirty tricks and flashing blades are on display when a Trickster enters a fight. Tricksters distract opponents with misdirection or a sword's flourish, then slash them with a blade they never saw coming.

## Hero talents

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
