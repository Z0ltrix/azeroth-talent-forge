# Rogue class tree

Reviewed build: `12.1.0.69404`

This catalog contains shared class-tree facts. For budget schedules, see `overview.md`.

### Structural rank (no player-facing ability)
- Node ID: `99844`
- Entry ID: `123375`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99844`
- Entry ID: `123371`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99843`
- Entry ID: `123374`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99843`
- Entry ID: `123372`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99842`
- Entry ID: `123373`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99842`
- Entry ID: `123370`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
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
### Opportunity
- Node ID: `90683`
- Entry ID: `112571`
- Definition ID: `117576`
- Spell ID: `279876`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Sinister Strike has a $s1% chance to hit an additional time and grant Opportunity.

$@spellicon195627 $@spellname195627
Your next Pistol Shot costs $195627s1% less Energy and deals $195627s2% increased damage.
- Effect: Sinister Strike has a $s1% chance to hit an additional time and grant Opportunity.

$@spellicon195627 $@spellname195627
Your next Pistol Shot costs $195627s1% less Energy and deals $195627s2% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Find Weakness
- Node ID: `90690`
- Entry ID: `112578`
- Definition ID: `117583`
- Spell ID: `91023`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Stealth abilities allow you to see the flaws in enemies' defenses, causing your attacks to ignore $s1% armor for $316220d.
- Effect: Your Stealth abilities allow you to see the flaws in enemies' defenses, causing your attacks to ignore $s1% armor for $316220d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deadly Poison
- Node ID: `90783`
- Entry ID: `112676`
- Definition ID: `117681`
- Spell ID: `2823`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Coats your weapons with a Lethal Poison that lasts for $d. Each strike has a $h% chance to poison the enemy for ${$2818m1*$2818d/$2818t1} Nature damage over $2818d. Subsequent poison applications will instantly deal $113780s1 Nature damage.
- Effect: Coats your weapons with a Lethal Poison that lasts for $d. Each strike has a $h% chance to poison the enemy for ${$2818m1*$2818d/$2818t1} Nature damage over $2818d. Subsequent poison applications will instantly deal $113780s1 Nature damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
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
### Toxic Stiletto
- Node ID: `110325`
- Entry ID: `136883`
- Definition ID: `141646`
- Spell ID: `1267182`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shiv's Energy cost is reduced by $s1, its cooldown is reduced by ${-$s2/1000} sec, and its range is increased by $s3 yds.
- Effect: Shiv's Energy cost is reduced by $s1, its cooldown is reduced by ${-$s2/1000} sec, and its range is increased by $s3 yds.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90740` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fleet Footed
- Node ID: `90764`
- Entry ID: `112657`
- Definition ID: `117662`
- Spell ID: `378813`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Movement speed increased by $s1%.
- Effect: Movement speed increased by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90684` (type `2`), node `90740` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gouge
- Node ID: `90741`
- Entry ID: `112631`
- Definition ID: `117636`
- Spell ID: `1776`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gouges the eyes of an enemy target, incapacitating for $d. Damage may interrupt the effect.

Must be in front of your target.

|cFFFFFFFFAwards $s2 combo $lpoint:points;.|r
- Effect: Gouges the eyes of an enemy target, incapacitating for $d. Damage may interrupt the effect.

Must be in front of your target.

|cFFFFFFFFAwards $s2 combo $lpoint:points;.|r
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90684` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Airborne Irritant
- Node ID: `90741`
- Entry ID: `117740`
- Definition ID: `122752`
- Spell ID: `200733`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Blind has $s1% reduced cooldown, $s2% reduced duration, and applies to all nearby enemies.
- Effect: Blind has $s1% reduced cooldown, $s2% reduced duration, and applies to all nearby enemies.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90684` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thrill Seeking
- Node ID: `90695`
- Entry ID: `112583`
- Definition ID: `117588`
- Spell ID: `394931`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137036[Grappling Hook][Shadowstep] has $s1 additional charge.
- Effect: $?a137036[Grappling Hook][Shadowstep] has $s1 additional charge.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90684` (type `2`), node `90697` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadowrunner
- Node ID: `110324`
- Entry ID: `136882`
- Definition ID: `141645`
- Spell ID: `378807`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Stealth or Shadow Dance is active, you move $s1% faster.
- Effect: While Stealth or Shadow Dance is active, you move $s1% faster.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90697` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Motivated Murderer
- Node ID: `90628`
- Entry ID: `112513`
- Definition ID: `117518`
- Spell ID: `1247993`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your Energy regeneration by $s1%.
- Effect: Increases your Energy regeneration by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90783` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hit and Run
- Node ID: `90681`
- Entry ID: `112569`
- Definition ID: `117574`
- Spell ID: `196922`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Movement speed increased by $s1%.
- Effect: Movement speed increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Combat Stamina
- Node ID: `90681`
- Entry ID: `135734`
- Definition ID: `140489`
- Spell ID: `381877`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Stamina increased by $<stam>%.
- Effect: Stamina increased by $<stam>%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Backstab
- Node ID: `90739`
- Entry ID: `112629`
- Definition ID: `117634`
- Spell ID: `319949`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s200758[Gloomblade][Backstab] has $s2% increased critical strike chance.

While behind your target, Backstab critical strikes grant Find Weakness for $s1 sec.
- Effect: $?s200758[Gloomblade][Backstab] has $s2% increased critical strike chance.

While behind your target, Backstab critical strikes grant Find Weakness for $s1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90690` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Poisons
- Node ID: `90635`
- Entry ID: `112520`
- Definition ID: `117525`
- Spell ID: `381624`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the application chance of your weapon poisons by $s1%.
- Effect: Increases the application chance of your weapon poisons by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90783` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Adrenaline Rush
- Node ID: `90659`
- Entry ID: `112545`
- Definition ID: `117550`
- Spell ID: `13750`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your Energy regeneration rate by $s1%, your maximum Energy by $s6, and your attack speed by $s2% for $d.$?$s4>0[

Damage of combo point generating abilities and finishers increased by $s4%.][]
- Effect: Increases your Energy regeneration rate by $s1%, your maximum Energy by $s6, and your attack speed by $s2% for $d.$?$s4>0[

Damage of combo point generating abilities and finishers increased by $s4%.][]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadow Blades
- Node ID: `90726`
- Entry ID: `112614`
- Definition ID: `117619`
- Spell ID: `121471`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Draws upon surrounding shadows to empower your weapons, causing your attacks to deal $s1% additional damage as Shadow and causing your combo point generating abilities to generate double combo points for $d.
- Effect: Draws upon surrounding shadows to empower your weapons, causing your attacks to deal $s1% additional damage as Shadow and causing your combo point generating abilities to generate double combo points for $d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90690` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Retractable Hook
- Node ID: `90673`
- Entry ID: `112560`
- Definition ID: `117565`
- Spell ID: `256188`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Grappling Hook by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Grappling Hook by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blinding Powder
- Node ID: `90673`
- Entry ID: `135733`
- Definition ID: `140488`
- Spell ID: `256165`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Blind by $s1% and increases its range by $s2 yds.
- Effect: Reduces the cooldown of Blind by $s1% and increases its range by $s2 yds.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90683` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Shuriken Storm
- Node ID: `90710`
- Entry ID: `112598`
- Definition ID: `117603`
- Spell ID: `319951`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shuriken Storm has $s2% increased critical strike chance.

Shuriken Storm critical strikes grant Find Weakness for $s1 sec.
- Effect: Shuriken Storm has $s2% increased critical strike chance.

Shuriken Storm critical strikes grant Find Weakness for $s1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90690` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Path of Blood
- Node ID: `94536`
- Entry ID: `117106`
- Definition ID: `122118`
- Spell ID: `423054`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases maximum Energy by $s1.
- Effect: Increases maximum Energy by $s1.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90783` (type `2`)
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
### Master Poisoner
- Node ID: `90636`
- Entry ID: `112521`
- Definition ID: `117526`
- Spell ID: `378436`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the non-damaging effects of your weapon poisons by $s1%.
- Effect: Increases the non-damaging effects of your weapon poisons by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90764` (type `2`), node `110325` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elusiveness
- Node ID: `90742`
- Entry ID: `112632`
- Definition ID: `117637`
- Spell ID: `79008`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Evasion also reduces damage taken by $s2%, and Feint also reduces non-area-of-effect damage taken by $s1%.
- Effect: Evasion also reduces damage taken by $s2%, and Feint also reduces non-area-of-effect damage taken by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90695` (type `2`), node `90741` (type `2`), node `90764` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cheat Death
- Node ID: `90742`
- Entry ID: `114737`
- Definition ID: `119744`
- Spell ID: `31230`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Fatal attacks instead reduce you to $s2% of your maximum health. For $45182d afterward, you take $45182s1% reduced damage. Cannot trigger more often than once per $45181d.
- Effect: Fatal attacks instead reduce you to $s2% of your maximum health. For $45182d afterward, you take $45182s1% reduced damage. Cannot trigger more often than once per $45181d.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90695` (type `2`), node `90741` (type `2`), node `90764` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tricks of the Trade
- Node ID: `90686`
- Entry ID: `112574`
- Definition ID: `117579`
- Spell ID: `57934`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s221622[Increases the target's damage by $221622m1%, and redirects][Redirects] all threat you cause to the targeted party or raid member, beginning with your next damaging attack within the next $d and lasting $59628d.
- Effect: $?s221622[Increases the target's damage by $221622m1%, and redirects][Redirects] all threat you cause to the targeted party or raid member, beginning with your next damaging attack within the next $d and lasting $59628d.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `entry`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `90695` (type `2`), node `110324` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blackjack
- Node ID: `90686`
- Entry ID: `117143`
- Definition ID: `122155`
- Spell ID: `379005`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Enemies have $394119s1% reduced damage and healing for $394119d after Blind or Sap's effect on them ends.
- Effect: Enemies have $394119s1% reduced damage and healing for $394119d after Blind or Sap's effect on them ends.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90695` (type `2`), node `110324` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Premeditation
- Node ID: `90700`
- Entry ID: `112588`
- Definition ID: `117593`
- Spell ID: `343160`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After entering Stealth, your next combo point generating ability generates full combo points.
- Effect: After entering Stealth, your next combo point generating ability generates full combo points.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90739` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Crimson Tempest
- Node ID: `94557`
- Entry ID: `117139`
- Definition ID: `122151`
- Spell ID: `1247227`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Slash all enemies within $A1 yds dealing $s1 damage. Deals reduced damage beyond $s4 targets.

Copy the longest Garrote and Rupture on the enemies you hit onto up to $s2 other enemies. 

|cFFFFFFFFAwards $s3 combo $lpoint:points;.|r
- Effect: Slash all enemies within $A1 yds dealing $s1 damage. Deals reduced damage beyond $s4 targets.

Copy the longest Garrote and Rupture on the enemies you hit onto up to $s2 other enemies. 

|cFFFFFFFFAwards $s3 combo $lpoint:points;.|r
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90628` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expert Duelist
- Node ID: `90645`
- Entry ID: `112531`
- Definition ID: `117536`
- Spell ID: `1259498`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Between the Eyes increases your damage dealt by an additional $s1%.
- Effect: Between the Eyes increases your damage dealt by an additional $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90659` (type `2`), node `90681` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Canny Strikes
- Node ID: `90634`
- Entry ID: `112519`
- Definition ID: `117524`
- Spell ID: `1250359`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases Critical Strike chance by $s1%.
- Effect: Increases Critical Strike chance by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90628` (type `2`), node `94536` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Internal Bleeding
- Node ID: `90634`
- Entry ID: `134840`
- Definition ID: `139608`
- Spell ID: `381627`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Kidney Shot and Rupture also apply Internal Bleeding, dealing up to ${5*$381628o1} Bleed damage over $381628d, based on combo points spent.
- Effect: Kidney Shot and Rupture also apply Internal Bleeding, dealing up to ${5*$381628o1} Bleed damage over $381628d, based on combo points spent.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90628` (type `2`), node `94536` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quick Decisions
- Node ID: `90728`
- Entry ID: `112616`
- Definition ID: `117621`
- Spell ID: `382503`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadowstep's cooldown is reduced by $s3%, and its maximum range is increased by $s1%.
- Effect: Shadowstep's cooldown is reduced by $s3%, and its maximum range is increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90726` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ephemeral Bond
- Node ID: `90728`
- Entry ID: `136808`
- Definition ID: `141571`
- Spell ID: `426563`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Increases healing received by $s1%.
- Effect: Increases healing received by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90726` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Combat Potency
- Node ID: `90648`
- Entry ID: `112534`
- Definition ID: `117539`
- Spell ID: `61329`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your Energy regeneration rate by $s1%.
- Effect: Increases your Energy regeneration rate by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90659` (type `2`), node `90673` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Garrote
- Node ID: `90625`
- Entry ID: `112510`
- Definition ID: `117515`
- Spell ID: `381632`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Garrote deals $s1% increased damage and has no cooldown when used from Stealth and for $392401d after breaking Stealth.
- Effect: Garrote deals $s1% increased damage and has no cooldown when used from Stealth and for $392401d after breaking Stealth.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `94536` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Silent Storm
- Node ID: `94582`
- Entry ID: `117170`
- Definition ID: `122182`
- Spell ID: `385722`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gaining Stealth, Vanish, or Shadow Dance causes your next Shuriken Storm to have $385727s1% increased chance to critically strike.
- Effect: Gaining Stealth, Vanish, or Shadow Dance causes your next Shuriken Storm to have $385727s1% increased chance to critically strike.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90710` (type `2`)
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
### Improved Wound Poison
- Node ID: `90637`
- Entry ID: `112522`
- Definition ID: `117527`
- Spell ID: `319066`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Wound Poison can now stack $s1 additional times.
- Effect: Wound Poison can now stack $s1 additional times.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90636` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nimble Fingers
- Node ID: `90745`
- Entry ID: `112635`
- Definition ID: `117640`
- Spell ID: `378427`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Energy cost of Feint and Crimson Vial reduced by $s1.
- Effect: Energy cost of Feint and Crimson Vial reduced by $s1.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90636` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deadened Nerves
- Node ID: `110323`
- Entry ID: `136881`
- Definition ID: `141644`
- Spell ID: `231719`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Physical damage taken reduced by $s1%.
- Effect: Physical damage taken reduced by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90742` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quick Fingers
- Node ID: `90746`
- Entry ID: `112636`
- Definition ID: `117641`
- Spell ID: `1267210`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your Agility by $s1%.
- Effect: Increases your Agility by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90686` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Sprint
- Node ID: `90687`
- Entry ID: `112575`
- Definition ID: `117580`
- Spell ID: `231691`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Sprint by ${$m1/-1000} sec.
- Effect: Reduces the cooldown of Sprint by ${$m1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `90686` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thrown Precision
- Node ID: `90630`
- Entry ID: `112515`
- Definition ID: `117520`
- Spell ID: `381629`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fan of Knives has $s2% increased critical strike chance and its critical strikes always apply your weapon poisons.
- Effect: Fan of Knives has $s2% increased critical strike chance and its critical strikes always apply your weapon poisons.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `94557` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shrouded in Darkness
- Node ID: `90698`
- Entry ID: `112586`
- Definition ID: `117591`
- Spell ID: `382507`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shroud of Concealment increases the movement speed of allies by $s1% and leaving its area no longer cancels the effect.
- Effect: Shroud of Concealment increases the movement speed of allies by $s1% and leaving its area no longer cancels the effect.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90700` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deadly Pursuit
- Node ID: `90643`
- Entry ID: `112529`
- Definition ID: `117534`
- Spell ID: `1259612`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After spending $s1 combo points, if you spend no combo points for $1259613d, abilities affected by Restless Blades will cool down $1259614s1% faster for $1259614d or until you spend a combo point.
- Effect: After spending $s1 combo points, if you spend no combo points for $1259613d, abilities affected by Restless Blades will cool down $1259614s1% faster for $1259614d or until you spend a combo point.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90645` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shot in the Dark
- Node ID: `90701`
- Entry ID: `112589`
- Definition ID: `117594`
- Spell ID: `257505`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After using Vanish or Shadow Dance, your next Cheap Shot is free and ignores its cooldown.
- Effect: After using Vanish or Shadow Dance, your next Cheap Shot is free and ignores its cooldown.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90700` (type `2`), node `90728` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Exhilarating Execution
- Node ID: `90701`
- Entry ID: `136807`
- Definition ID: `141570`
- Spell ID: `428486`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your finishing moves heal you for $s1% of damage done. At full health gain shielding instead, absorbing up to $s2% of your maximum health.
- Effect: Your finishing moves heal you for $s1% of damage done. At full health gain shielding instead, absorbing up to $s2% of your maximum health.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90700` (type `2`), node `90728` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Precision Shot
- Node ID: `90755`
- Entry ID: `112647`
- Definition ID: `117652`
- Spell ID: `428377`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Between the Eyes and Pistol Shot have $s1 yd increased range and deal $s2% increased damage.
- Effect: Between the Eyes and Pistol Shot have $s1 yd increased range and deal $s2% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90645` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Seal Fate
- Node ID: `90757`
- Entry ID: `112649`
- Definition ID: `117654`
- Spell ID: `14190`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strikes with attacks that generate combo points grant an additional combo point per critical strike.
- Effect: Critical strikes with attacks that generate combo points grant an additional combo point per critical strike.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90634` (type `2`), node `94557` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Crescendo of Violence
- Node ID: `90661`
- Entry ID: `112547`
- Definition ID: `117552`
- Spell ID: `1259499`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your finishing moves deal $s1% increased damage.
- Effect: Your finishing moves deal $s1% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90648` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cloaked in Shadows
- Node ID: `90733`
- Entry ID: `112622`
- Definition ID: `117627`
- Spell ID: `382515`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vanish grants you a shield for $386165d, absorbing damage equal to $s1% of your maximum health.
- Effect: Vanish grants you a shield for $386165d, absorbing damage equal to $s1% of your maximum health.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90728` (type `2`), node `94582` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fade to Nothing
- Node ID: `90733`
- Entry ID: `112621`
- Definition ID: `117626`
- Spell ID: `382514`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Movement speed increased by $386237s1% and damage taken reduced by $386237s2% for $386237d after gaining Stealth, Vanish, or Shadow Dance.
- Effect: Movement speed increased by $386237s1% and damage taken reduced by $386237s2% for $386237d after gaining Stealth, Vanish, or Shadow Dance.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90728` (type `2`), node `94582` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Doomblade
- Node ID: `94556`
- Entry ID: `117137`
- Definition ID: `122149`
- Spell ID: `381673`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Mutilate deals an additional $s1% Bleed damage over ${$394021d+2} sec.
- Effect: Mutilate deals an additional $s1% Bleed damage over ${$394021d+2} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90625` (type `2`), node `90634` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deft Maneuvers
- Node ID: `90647`
- Entry ID: `112533`
- Definition ID: `117538`
- Spell ID: `381878`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blade Flurry's initial damage is increased by $s1% and generates $m2 $Lcombo point:combo points; per target struck, but its Energy cost is increased by $s3.
- Effect: Blade Flurry's initial damage is increased by $s1% and generates $m2 $Lcombo point:combo points; per target struck, but its Energy cost is increased by $s3.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90648` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Night Terrors
- Node ID: `90714`
- Entry ID: `112602`
- Definition ID: `117607`
- Spell ID: `277953`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shuriken Storm reduces enemies' movement speed by $206760s1% for $206760d.
- Effect: Shuriken Storm reduces enemies' movement speed by $206760s1% for $206760d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `94582` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Terrifying Pace
- Node ID: `90714`
- Entry ID: `136488`
- Definition ID: `141261`
- Spell ID: `428387`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Shuriken Storm increases your movement speed by $428389s1% for $428389d when striking $s1 or more enemies.
- Effect: Shuriken Storm increases your movement speed by $428389s1% for $428389d when striking $s1 or more enemies.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `94582` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Razor Wire
- Node ID: `90780`
- Entry ID: `112673`
- Definition ID: `117678`
- Spell ID: `1249802`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Garrote lasts ${$s1/1000} sec longer.
- Effect: Garrote lasts ${$s1/1000} sec longer.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `90625` (type `2`)
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
### Superior Mixture
- Node ID: `94567`
- Entry ID: `117151`
- Definition ID: `122163`
- Spell ID: `423701`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Crippling Poison reduces movement speed by an additional $s1%.
- Effect: Crippling Poison reduces movement speed by an additional $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90637` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Evasion
- Node ID: `90762`
- Entry ID: `112654`
- Definition ID: `117659`
- Spell ID: `5277`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your dodge chance by ${$s1/2}% for $d.$?a344363[ Dodging an attack while Evasion is active will trigger Mastery: Main Gauche.][]
- Effect: Increases your dodge chance by ${$s1/2}% for $d.$?a344363[ Dodging an attack while Evasion is active will trigger Mastery: Main Gauche.][]
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90637` (type `2`), node `90745` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Iron Stomach
- Node ID: `90744`
- Entry ID: `112634`
- Definition ID: `117639`
- Spell ID: `193546`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the healing you receive from Crimson Vial, healing potions, and healthstones by $s1%.
- Effect: Increases the healing you receive from Crimson Vial, healing potions, and healthstones by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90745` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Virulent Poisons
- Node ID: `90747`
- Entry ID: `112638`
- Definition ID: `117643`
- Spell ID: `381543`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the damage of your weapon poisons by $s1%.
- Effect: Increases the damage of your weapon poisons by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90745` (type `2`), node `90746` (type `2`), node `110323` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stillshroud
- Node ID: `94563`
- Entry ID: `117146`
- Definition ID: `122158`
- Spell ID: `423662`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shroud of Concealment has $s1% reduced cooldown.
- Effect: Shroud of Concealment has $s1% reduced cooldown.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90746` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Graceful Guile
- Node ID: `90754`
- Entry ID: `112646`
- Definition ID: `117651`
- Spell ID: `423647`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Feint has $m1 additional $Lcharge:charges;.
- Effect: Feint has $m1 additional $Lcharge:charges;.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90687` (type `2`), node `90746` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Featherfoot
- Node ID: `101714`
- Entry ID: `125615`
- Definition ID: `130447`
- Spell ID: `423683`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Sprint increases movement speed by an additional $s1% and has ${$s2/1000} sec increased duration.
- Effect: Sprint increases movement speed by an additional $s1% and has ${$s2/1000} sec increased duration.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90687` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bloody Mess
- Node ID: `90633`
- Entry ID: `112518`
- Definition ID: `117523`
- Spell ID: `381626`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Garrote and Rupture damage increased by $s1%.
- Effect: Garrote and Rupture damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90630` (type `2`), node `90757` (type `2`), node `94557` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Devious Stratagem
- Node ID: `90679`
- Entry ID: `112567`
- Definition ID: `117572`
- Spell ID: `394321`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Effect: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90643` (type `2`), node `90755` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Master of Shadows
- Node ID: `90727`
- Entry ID: `112615`
- Definition ID: `117620`
- Spell ID: `196976`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain ${$196980s1*$196980d/$196980t1+$196980s2} Energy over $196980d when you enter Stealth or activate Shadow Dance.
- Effect: Gain ${$196980s1*$196980d/$196980t1+$196980s2} Energy over $196980d when you enter Stealth or activate Shadow Dance.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90698` (type `2`), node `90701` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gloomblade
- Node ID: `90699`
- Entry ID: `112587`
- Definition ID: `117592`
- Spell ID: `200758`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Punctures your target with your shadow-infused blade for $s1 Shadow damage, bypassing armor.$?s319949[ Critical strikes apply Find Weakness for $319949s1 sec.][]

|cFFFFFFFFAwards $s2 combo $lpoint:points;.|r
- Effect: Punctures your target with your shadow-infused blade for $s1 Shadow damage, bypassing armor.$?s319949[ Critical strikes apply Find Weakness for $319949s1 sec.][]

|cFFFFFFFFAwards $s2 combo $lpoint:points;.|r
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90701` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fatal Flourish
- Node ID: `90662`
- Entry ID: `112548`
- Definition ID: `117553`
- Spell ID: `35551`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your off-hand attacks and Pistol Shots have a $s1% chance to generate $35546s1 Energy.
- Effect: Your off-hand attacks and Pistol Shots have a $s1% chance to generate $35546s1 Energy.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90659` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadow Focus
- Node ID: `90734`
- Entry ID: `112623`
- Definition ID: `117628`
- Spell ID: `108209`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Abilities deal $112942m1% more damage while Stealth or Shadow Dance is active.
- Effect: Abilities deal $112942m1% more damage while Stealth or Shadow Dance is active.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90701` (type `2`), node `90733` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deathmark
- Node ID: `90769`
- Entry ID: `112662`
- Definition ID: `117667`
- Spell ID: `360194`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Carve a deathmark into an enemy, dealing $o1 Bleed damage and restoring $s3 Energy to you over $d. Damage dealt to the target by your Garrote, Rupture, and Lethal Poisons is increased by $s2%.

Each time you apply a Lethal Poison to the target, apply it twice.
- Effect: Carve a deathmark into an enemy, dealing $o1 Bleed damage and restoring $s3 Energy to you over $d. Damage dealt to the target by your Garrote, Rupture, and Lethal Poisons is increased by $s2%.

Each time you apply a Lethal Poison to the target, apply it twice.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `node`; type `4`; currency `2800` spend gate `0` | source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `90757` (type `2`), node `94556` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Secret Technique
- Node ID: `90715`
- Entry ID: `112603`
- Definition ID: `117608`
- Spell ID: `1279444`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Secret Technique damage increased by $s1%.
- Effect: Secret Technique damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90733` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quick Draw
- Node ID: `90663`
- Entry ID: `112549`
- Definition ID: `117554`
- Spell ID: `196938`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Opportunity increases the damage of Pistol Shot by an additional $s1%. Each charge of Opportunity consumed by Pistol Shot generates $1254567s1 combo $Lpoint:points;.
- Effect: Opportunity increases the damage of Pistol Shot by an additional $s1%. Each charge of Opportunity consumed by Pistol Shot generates $1254567s1 combo $Lpoint:points;.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90647` (type `2`), node `90661` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Relentless Strikes
- Node ID: `90709`
- Entry ID: `112597`
- Definition ID: `117602`
- Spell ID: `58423`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your finishing moves generate $98440s2 Energy per combo point spent.
- Effect: Your finishing moves generate $98440s2 Energy per combo point spent.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90714` (type `2`), node `90733` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Caustic Spatter
- Node ID: `90779`
- Entry ID: `112672`
- Definition ID: `117677`
- Spell ID: `421975`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Envenom or Kingsbane apply Caustic Spatter for $421976d. Limit 1.

Caustic Spatter causes $421976s1% of your Nature damage dealt to splash onto other nearby enemies, reduced beyond $421976s2 targets.
- Effect: Envenom or Kingsbane apply Caustic Spatter for $421976d. Limit 1.

Caustic Spatter causes $421976s1% of your Nature damage dealt to splash onto other nearby enemies, reduced beyond $421976s2 targets.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90625` (type `2`), node `90780` (type `2`), node `94556` (type `2`)
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
### Numbing Poison
- Node ID: `90763`
- Entry ID: `112656`
- Definition ID: `117661`
- Spell ID: `5761`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Coats your weapons with a Non-Lethal Poison that lasts for $d. Each strike has a $5761h% chance of poisoning the enemy, clouding their mind and slowing their attack and casting speed by $5760s1% for $5760d.
- Effect: Coats your weapons with a Non-Lethal Poison that lasts for $d. Each strike has a $5761h% chance of poisoning the enemy, clouding their mind and slowing their attack and casting speed by $5760s1% for $5760d.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90762` (type `2`), node `94567` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Atrophic Poison
- Node ID: `90763`
- Entry ID: `112655`
- Definition ID: `117660`
- Spell ID: `381637`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Coats your weapons with a Non-Lethal Poison that lasts for $d. Each strike has a $h% chance of poisoning the enemy, reducing their damage by ${$392388s1*-1}.1% for $392388d.
- Effect: Coats your weapons with a Non-Lethal Poison that lasts for $d. Each strike has a $h% chance of poisoning the enemy, reducing their damage by ${$392388s1*-1}.1% for $392388d.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90762` (type `2`), node `94567` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deadly Precision
- Node ID: `90743`
- Entry ID: `112633`
- Definition ID: `117638`
- Spell ID: `381542`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the critical strike chance of your attacks that generate combo points by $s1%.
- Effect: Increases the critical strike chance of your attacks that generate combo points by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90744` (type `2`), node `90747` (type `2`), node `90762` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sanguine Vial
- Node ID: `110576`
- Entry ID: `137380`
- Definition ID: `142140`
- Spell ID: `1293135`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you deal the killing blow to a target that yields experience or honor, the cooldown of Crimson Vial is reduced by ${-$s2/1000} sec and your next use heals $1293149s1% of your health instantly.
- Effect: When you deal the killing blow to a target that yields experience or honor, the cooldown of Crimson Vial is reduced by ${-$s2/1000} sec and your next use heals $1293149s1% of your health instantly.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90747` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deep Cuts
- Node ID: `94562`
- Entry ID: `117145`
- Definition ID: `122157`
- Spell ID: `1267216`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your finishing moves deal $s1% increased damage.
- Effect: Your finishing moves deal $s1% increased damage.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90747` (type `2`), node `90754` (type `2`), node `94563` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unbreakable Stride
- Node ID: `94561`
- Entry ID: `117144`
- Definition ID: `122156`
- Spell ID: `400804`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the duration of movement slowing effects $s1%.
- Effect: Reduces the duration of movement slowing effects $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90754` (type `2`), node `101714` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ruthlessness
- Node ID: `90680`
- Entry ID: `112568`
- Definition ID: `117573`
- Spell ID: `14161`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your finishing moves have a $b1% chance per combo point spent to grant a combo point.
- Effect: Your finishing moves have a $b1% chance per combo point spent to grant a combo point.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90679` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Weaponmaster
- Node ID: `90737`
- Entry ID: `112627`
- Definition ID: `117632`
- Spell ID: `193537`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s200758[Gloomblade][Backstab] and Shadowstrike have a $s1% chance to create a Shadow Clone that repeats the attack for $s2% of normal damage as Shadow.
- Effect: $?s200758[Gloomblade][Backstab] and Shadowstrike have a $s1% chance to create a Shadow Clone that repeats the attack for $s2% of normal damage as Shadow.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90727` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sanguine Stratagem
- Node ID: `94554`
- Entry ID: `117133`
- Definition ID: `122145`
- Spell ID: `457512`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Effect: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90633` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blade Rush
- Node ID: `90649`
- Entry ID: `112535`
- Definition ID: `117540`
- Spell ID: `271877`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Charge to your target with your blades out, dealing ${$271881sw1*$271881s2/100} Physical damage to the target and $271881sw1 to all other nearby enemies. Damage reduced beyond $271881sw3 targets.

While Blade Flurry is active, damage to non-primary targets is increased by $s1%.

|cFFFFFFFFGenerates ${$271896s1*$271896d/$271896t1} Energy over $271896d.
- Effect: Charge to your target with your blades out, dealing ${$271881sw1*$271881s2/100} Physical damage to the target and $271881sw1 to all other nearby enemies. Damage reduced beyond $271881sw3 targets.

While Blade Flurry is active, damage to non-primary targets is increased by $s1%.

|cFFFFFFFFGenerates ${$271896s1*$271896d/$271896t1} Energy over $271896d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90679` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Planned Execution
- Node ID: `90703`
- Entry ID: `112591`
- Definition ID: `117596`
- Spell ID: `382508`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Dance increases the critical strike damage bonus of your abilities by $185313s9%.
- Effect: Shadow Dance increases the critical strike damage bonus of your abilities by $185313s9%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90727` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Warning Signs
- Node ID: `90703`
- Entry ID: `117172`
- Definition ID: `122184`
- Spell ID: `426555`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Shadow Dance increases attack speed by $185313s8%.
- Effect: Shadow Dance increases attack speed by $185313s8%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90727` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Intent to Kill
- Node ID: `109004`
- Entry ID: `134839`
- Definition ID: `139607`
- Spell ID: `381630`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadowstep's cooldown is reduced by $s1% when used on a target afflicted by your Garrote.
- Effect: Shadowstep's cooldown is reduced by $s1% when used on a target afflicted by your Garrote.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90633` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Iron Wire
- Node ID: `109004`
- Entry ID: `134838`
- Definition ID: `139606`
- Spell ID: `196861`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Garrotes applied from stealth or during the Improved Garrote window silence their target for $s2 sec.

Enemies silenced by Garrote deal $256148s1% reduced damage for $256148d.
- Effect: Garrotes applied from stealth or during the Improved Garrote window silence their target for $s2 sec.

Enemies silenced by Garrote deal $256148s1% reduced damage for $256148d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90633` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Loaded Dice
- Node ID: `90656`
- Entry ID: `112542`
- Definition ID: `117547`
- Spell ID: `256170`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Activating Adrenaline Rush improves the result of your next Roll the Bones by one level.
- Effect: Activating Adrenaline Rush improves the result of your next Roll the Bones by one level.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90662` (type `2`), node `90679` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fatal Concoction
- Node ID: `90772`
- Entry ID: `112665`
- Definition ID: `117670`
- Spell ID: `392384`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Increases the damage of your weapon poisons by $s1%.
- Effect: Increases the damage of your weapon poisons by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90633` (type `2`), node `90769` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `61227`, index `1`, operation `1`, curve `70436`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Double Dance
- Node ID: `101715`
- Entry ID: `125619`
- Definition ID: `130451`
- Spell ID: `394930`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Dance has $s1 additional charge.
- Effect: Shadow Dance has $s1 additional charge.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90699` (type `2`), node `90727` (type `2`), node `90734` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Finish the Job
- Node ID: `90626`
- Entry ID: `112511`
- Definition ID: `117516`
- Spell ID: `1249809`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: All damage you deal is increased by $1249810s1% while Deathmark is active.
- Effect: All damage you deal is increased by $1249810s1% while Deathmark is active.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90769` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Negotiable Contract
- Node ID: `90626`
- Entry ID: `137379`
- Definition ID: `142139`
- Spell ID: `1292996`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: If the target of your Deathmark dies, Deathmark jumps to a nearby enemy combatant for its remaining duration.
- Effect: If the target of your Deathmark dies, Deathmark jumps to a nearby enemy combatant for its remaining duration.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90769` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lethal Dose
- Node ID: `90624`
- Entry ID: `112509`
- Definition ID: `117514`
- Spell ID: `381640`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Your weapon poisons and Nature or Bleed damage over time abilities deal $s1% increased damage to targets for each of your lethal poison or damage over time effects on them.
- Effect: Your weapon poisons and Nature or Bleed damage over time abilities deal $s1% increased damage to targets for each of your lethal poison or damage over time effects on them.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90769` (type `2`), node `90779` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61194`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sleight of Hand
- Node ID: `90651`
- Entry ID: `112537`
- Definition ID: `117542`
- Spell ID: `381839`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Roll the Bones has a $s1% increased chance of granting more powerful results.
- Effect: Roll the Bones has a $s1% increased chance of granting more powerful results.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90662` (type `2`), node `90663` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadowed Finishers
- Node ID: `90723`
- Entry ID: `112611`
- Definition ID: `117616`
- Spell ID: `382511`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Eviscerate and Black Powder deal an additional $s1% damage as Shadow while Find Weakness is active.
- Effect: Eviscerate and Black Powder deal an additional $s1% damage as Shadow while Find Weakness is active.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90709` (type `2`), node `90715` (type `2`), node `90734` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Secret Stratagem
- Node ID: `90722`
- Entry ID: `112610`
- Definition ID: `117615`
- Spell ID: `394320`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Effect: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90709` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Between the Eyes
- Node ID: `90753`
- Entry ID: `112645`
- Definition ID: `117650`
- Spell ID: `235484`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strikes with Between the Eyes deal ${$s1/100+2}.1 times normal damage.
- Effect: Critical strikes with Between the Eyes deal ${$s1/100+2}.1 times normal damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90663` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flying Daggers
- Node ID: `109003`
- Entry ID: `134837`
- Definition ID: `139605`
- Spell ID: `381631`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fan of Knives has its radius increased to $?a196924[${$196924s1+$s4}][$s4] yds, deals $s5% more damage, and an additional $s1% when striking $s2 or more targets.
- Effect: Fan of Knives has its radius increased to $?a196924[${$196924s1+$s4}][$s4] yds, deals $s5% more damage, and an additional $s1% when striking $s2 or more targets.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90779` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Secondary Poisoning
- Node ID: `109003`
- Entry ID: `134836`
- Definition ID: `139604`
- Spell ID: `1250141`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you apply a Weapon Poison with a single-target attack, you have a $s1% chance to strike a nearby enemy for $1250216s1 Physical damage and apply the same Weapon Poison to them.
- Effect: When you apply a Weapon Poison with a single-target attack, you have a $s1% chance to strike a nearby enemy for $1250216s1 Physical damage and apply the same Weapon Poison to them.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90779` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thief's Versatility
- Node ID: `90671`
- Entry ID: `112558`
- Definition ID: `117563`
- Spell ID: `381619`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Versatility increased by $s1%.
- Effect: Versatility increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90663` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flickering Steel
- Node ID: `90671`
- Entry ID: `135731`
- Definition ID: `140486`
- Spell ID: `1259492`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Sinister Strike and Ambush deal $s1% increased damage. They also generate $1259493s1 Energy when they grant you Opportunity.
- Effect: Sinister Strike and Ambush deal $s1% increased damage. They also generate $1259493s1 Energy when they grant you Opportunity.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90663` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shuriken Tornado
- Node ID: `90717`
- Entry ID: `112605`
- Definition ID: `117610`
- Spell ID: `1264764`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shuriken Storm has a $s1% chance to create a Shadow Clone that repeats the attack for $s2% of normal damage as Shadow.
- Effect: Shuriken Storm has a $s1% chance to create a Shadow Clone that repeats the attack for $s2% of normal damage as Shadow.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90709` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Poison Bomb
- Node ID: `94555`
- Entry ID: `117135`
- Definition ID: `122147`
- Spell ID: `255544`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Envenom has a $<chance>% chance per combo point spent to smash a vial of poison at the target's location, creating a pool of acidic death that deals ${$255546s1*$s2} Nature damage over $255545d to all enemies within it.
- Effect: Envenom has a $<chance>% chance per combo point spent to smash a vial of poison at the target's location, creating a pool of acidic death that deals ${$255546s1*$s2} Nature damage over $255545d to all enemies within it.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90779` (type `2`)
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
### Danger Sense
- Node ID: `90760`
- Entry ID: `112652`
- Definition ID: `117657`
- Spell ID: `1267220`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You have a $s2% chance to partially evade any damage dealt to you, reducing the damage it deals by $s3%.
- Effect: You have a $s2% chance to partially evade any damage dealt to you, reducing the damage it deals by $s3%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90743` (type `2`), node `90763` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swift Slasher
- Node ID: `90752`
- Entry ID: `112644`
- Definition ID: `117649`
- Spell ID: `381988`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Slice and Dice grants additional attack speed equal to $s2% of your Haste.
- Effect: Slice and Dice grants additional attack speed equal to $s2% of your Haste.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90743` (type `2`), node `94562` (type `2`), node `110576` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Ambush
- Node ID: `90692`
- Entry ID: `112580`
- Definition ID: `117585`
- Spell ID: `381620`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s185438[Shadowstrike damage increased by $s2%][Ambush generates $s1 additional combo point].
- Effect: $?s185438[Shadowstrike damage increased by $s2%][Ambush generates $s1 additional combo point].
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `94561` (type `2`), node `94562` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tight Spender
- Node ID: `90692`
- Entry ID: `117152`
- Definition ID: `122164`
- Spell ID: `381621`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Energy cost of finishing moves reduced by $s1%.
- Effect: Energy cost of finishing moves reduced by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `94561` (type `2`), node `94562` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Audacity
- Node ID: `90641`
- Entry ID: `112527`
- Definition ID: `117532`
- Spell ID: `381845`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Using Pistol Shot with Opportunity has a $279876s1% chance to make your next Ambush usable without Stealth.

Chance to trigger this effect matches the chance for Sinister Strike to grant Opportunity.

Ambush damage increased by $s2%.
- Effect: Using Pistol Shot with Opportunity has a $279876s1% chance to make your next Ambush usable without Stealth.

Chance to trigger this effect matches the chance for Sinister Strike to grant Opportunity.

Ambush damage increased by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90680` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Umbral Edge
- Node ID: `90738`
- Entry ID: `112628`
- Definition ID: `117633`
- Spell ID: `1281468`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Clones deal $s1% increased damage.

Cheap Shot creates a Shadow Clone to Shadowstrike the target for $s2% of normal damage as Shadow.

Kidney Shot creates a Shadow Clone to Eviscerate the target for $s2% of normal damage as Shadow.
- Effect: Shadow Clones deal $s1% increased damage.

Cheap Shot creates a Shadow Clone to Shadowstrike the target for $s2% of normal damage as Shadow.

Kidney Shot creates a Shadow Clone to Eviscerate the target for $s2% of normal damage as Shadow.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90703` (type `2`), node `90737` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Heavy Hitter
- Node ID: `90678`
- Entry ID: `112566`
- Definition ID: `117571`
- Spell ID: `381885`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Attacks that generate combo points deal $s1% increased damage.
- Effect: Attacks that generate combo points deal $s1% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90649` (type `2`), node `90656` (type `2`), node `90680` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `92467`, index `1`, operation `1`, curve `92466`, index `2`, operation `1`, curve `92465`, index `3`, operation `1`, curve `92464`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Amplifying Poison
- Node ID: `90771`
- Entry ID: `112664`
- Definition ID: `117669`
- Spell ID: `381664`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Coats your weapons with a Lethal Poison that lasts for $d. Each strike has a $h% chance to poison the enemy, dealing $383414s1 Nature damage and applying Amplifying Poison for $383414d. Envenom can consume $s2 stacks of Amplifying Poison to deal $s1% increased damage. Max $383414u stacks.
- Effect: Coats your weapons with a Lethal Poison that lasts for $d. Each strike has a $h% chance to poison the enemy, dealing $383414s1 Nature damage and applying Amplifying Poison for $383414d. Envenom can consume $s2 stacks of Amplifying Poison to deal $s1% increased damage. Max $383414u stacks.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90772` (type `2`), node `94554` (type `2`), node `109004` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deepening Shadows
- Node ID: `90735`
- Entry ID: `112625`
- Definition ID: `117630`
- Spell ID: `185314`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Dance duration is increased by $1271702s3% of your Haste stat.

Current bonus duration: ${$s1/1000}.2 sec
- Effect: Shadow Dance duration is increased by $1271702s3% of your Haste stat.

Current bonus duration: ${$s1/1000}.2 sec
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90703` (type `2`), node `101715` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Adrenaline Rush
- Node ID: `90654`
- Entry ID: `112540`
- Definition ID: `117545`
- Spell ID: `395422`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Generate full combo points when you gain Adrenaline Rush.
- Effect: Generate full combo points when you gain Adrenaline Rush.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90662` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Goremaw's Bite
- Node ID: `90724`
- Entry ID: `112612`
- Definition ID: `117617`
- Spell ID: `426591`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lash out at your target and $s1 additional nearby enemies, inflicting $426592s1 Shadow damage and causing them to Bleed for $426593o1 damage over $426593d.

$1309274s2% of all damage from Finishing Moves is repeated as Shadow, split evenly among affected enemies.
- Effect: Lash out at your target and $s1 additional nearby enemies, inflicting $426592s1 Shadow damage and causing them to Bleed for $426593o1 damage over $426593d.

$1309274s2% of all damage from Finishing Moves is repeated as Shadow, split evenly among affected enemies.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90723` (type `2`), node `101715` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Venomous Wounds
- Node ID: `90768`
- Entry ID: `112661`
- Definition ID: `117666`
- Spell ID: `79134`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You regain $s1 Energy each time your Garrote or Rupture deal Bleed damage to a target affected by your weapon poisons. Energy gain is reduced for bleeds beyond the first.

If an enemy dies while afflicted by your Rupture, you regain energy based on its remaining duration.
- Effect: You regain $s1 Energy each time your Garrote or Rupture deal Bleed damage to a target affected by your weapon poisons. Energy gain is reduced for bleeds beyond the first.

If an enemy dies while afflicted by your Rupture, you regain energy based on its remaining duration.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90624` (type `2`), node `90626` (type `2`), node `90772` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Veiltouched
- Node ID: `90713`
- Entry ID: `112601`
- Definition ID: `117606`
- Spell ID: `382017`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your abilities deal $s1% increased magic damage.
- Effect: Your abilities deal $s1% increased magic damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90722` (type `2`), node `90723` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ace Up Your Sleeve
- Node ID: `90668`
- Entry ID: `112555`
- Definition ID: `117560`
- Spell ID: `381828`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Between the Eyes has a $s1% chance per combo point spent to grant $394120s1 combo points and reset its own cooldown.
- Effect: Between the Eyes has a $s1% chance per combo point spent to grant $394120s1 combo points and reset its own cooldown.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90651` (type `2`), node `90671` (type `2`), node `90753` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `92463`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Systemic Failure
- Node ID: `90777`
- Entry ID: `112670`
- Definition ID: `117675`
- Spell ID: `381652`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Garrote increases the damage of Ambush and Mutilate on the target by $s1%.
- Effect: Garrote increases the damage of Ambush and Mutilate on the target by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90624` (type `2`), node `94555` (type `2`), node `109003` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Replicating Shadows
- Node ID: `90716`
- Entry ID: `112604`
- Definition ID: `117609`
- Spell ID: `382506`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow Clones deal $s1% increased damage and your effects that have a chance to create them have $s2% additional chance to occur.
- Effect: Shadow Clones deal $s1% increased damage and your effects that have a chance to create them have $s2% additional chance to occur.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90717` (type `2`), node `90722` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dancing Steel
- Node ID: `90669`
- Entry ID: `112556`
- Definition ID: `117561`
- Spell ID: `272026`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blade Flurry strikes $s3 additional enemies and its duration is increased by ${$s2/1000} sec.
- Effect: Blade Flurry strikes $s3 additional enemies and its duration is increased by ${$s2/1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `90671` (type `2`)
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
### Leeching Poison
- Node ID: `90758`
- Entry ID: `112650`
- Definition ID: `117655`
- Spell ID: `280716`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Adds a Leeching effect to your Lethal poisons, granting you ${$108211s1}.1% Leech.
- Effect: Adds a Leeching effect to your Lethal poisons, granting you ${$108211s1}.1% Leech.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90760` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lethality
- Node ID: `90749`
- Entry ID: `112640`
- Definition ID: `117645`
- Spell ID: `382238`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Critical strike chance increased by $s1%. Critical strike damage bonus of your attacks that generate combo points increased by $s2%.
- Effect: Critical strike chance increased by $s1%. Critical strike damage bonus of your attacks that generate combo points increased by $s2%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90752` (type `2`), node `90760` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61220`, index `1`, operation `0`, curve `61219`, index `2`, operation `0`, curve `71206`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Recuperator
- Node ID: `90640`
- Entry ID: `112526`
- Definition ID: `117531`
- Spell ID: `378996`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Slice and Dice heals you for up to $s1% of your maximum health per $426605t sec.
- Effect: Slice and Dice heals you for up to $s1% of your maximum health per $426605t sec.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90752` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Alacrity
- Node ID: `90751`
- Entry ID: `112643`
- Definition ID: `117648`
- Spell ID: `193539`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Haste increased by ${$s1/10}.1%.
- Effect: Haste increased by ${$s1/10}.1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90692` (type `2`), node `90752` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61221`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Soothing Darkness
- Node ID: `90691`
- Entry ID: `112579`
- Definition ID: `117584`
- Spell ID: `393970`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You are healed for ${$393971s1*($393971d/$393971t)}% of your maximum health over $393971d after activating Vanish.
- Effect: You are healed for ${$393971s1*($393971d/$393971t)}% of your maximum health over $393971d after activating Vanish.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90692` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Find an Opening
- Node ID: `90677`
- Entry ID: `112565`
- Definition ID: `117570`
- Spell ID: `1259457`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your chance for Sinister Strike to strike twice and grant Opportunity is increased by $s1%
- Effect: Your chance for Sinister Strike to strike twice and grant Opportunity is increased by $s1%
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90641` (type `2`), node `90678` (type `2`), node `90680` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Find Weakness
- Node ID: `90704`
- Entry ID: `112592`
- Definition ID: `117597`
- Spell ID: `382512`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Find Weakness causes your attacks to ignore an additional $s1% armor.
- Effect: Find Weakness causes your attacks to ignore an additional $s1% armor.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90735` (type `2`), node `90738` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dashing Scoundrel
- Node ID: `90786`
- Entry ID: `112679`
- Definition ID: `117684`
- Spell ID: `381797`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Envenom's effect also increases the critical strike chance of your weapon poisons by $s1%. Your Energy generation is increased by $s2% for each lethal poison on your weapons.
- Effect: Envenom's effect also increases the critical strike chance of your weapon poisons by $s1%. Your Energy generation is increased by $s2% for each lethal poison on your weapons.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90771` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Acrobatic Strikes
- Node ID: `90664`
- Entry ID: `112551`
- Definition ID: `117556`
- Spell ID: `455143`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Auto-attacks increase auto-attack damage by $455144s1% and movement speed by $455144s2% for $455144d, stacking up to $455144u times.
- Effect: Auto-attacks increase auto-attack damage by $455144s1% and movement speed by $455144s2% for $455144d, stacking up to $455144u times.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90654` (type `2`), node `90678` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Perforated Veins
- Node ID: `90707`
- Entry ID: `112595`
- Definition ID: `117600`
- Spell ID: `382518`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s200758[Gloomblade][Backstab], Shuriken Storm, and Shadowstrike have $1264521s3% increased damage while Find Weakness is active.
- Effect: $?s200758[Gloomblade][Backstab], Shuriken Storm, and Shadowstrike have $1264521s3% increased damage while Find Weakness is active.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90724` (type `2`), node `90735` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Kingsbane
- Node ID: `90770`
- Entry ID: `112663`
- Definition ID: `117668`
- Spell ID: `385627`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Release a powerful poison from your weapons and inject it into your target, dealing $s2 Nature damage instantly and an additional $o4 Nature damage over $d. 

Each time you apply a Lethal Poison to a target affected by Kingsbane, Kingsbane damage increases by $394095s1%, up to ${$394095s1*$394095u}%.

|cFFFFFFFFAwards $s6 combo $lpoint:points;.|r
- Effect: Release a powerful poison from your weapons and inject it into your target, dealing $s2 Nature damage instantly and an additional $o4 Nature damage over $d. 

Each time you apply a Lethal Poison to a target affected by Kingsbane, Kingsbane damage increases by $394095s1%, up to ${$394095s1*$394095u}%.

|cFFFFFFFFAwards $s6 combo $lpoint:points;.|r
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `node`; type `4`; currency `2800` spend gate `0` | source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `90768` (type `2`), node `90771` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Heightened Rush
- Node ID: `90655`
- Entry ID: `112541`
- Definition ID: `117546`
- Spell ID: `1259465`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Adrenaline Rush's duration is increased by ${$s1/1000} sec.
- Effect: Adrenaline Rush's duration is increased by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90654` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Menacing Rush
- Node ID: `90655`
- Entry ID: `135732`
- Definition ID: `140487`
- Spell ID: `1256630`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Adrenaline Rush magnifies your precision and power, increasing the damage your combo point generating abilities and finishers deal by $s1%.
- Effect: Adrenaline Rush magnifies your precision and power, increasing the damage your combo point generating abilities and finishers deal by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90654` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lingering Shadow
- Node ID: `90731`
- Entry ID: `112619`
- Definition ID: `117624`
- Spell ID: `382524`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After Shadow Dance ends, $?s200758[Gloomblade][Backstab] and Shuriken Storm deal an additional $s1% damage as Shadow, fading by ${$s1/$s3}.1% per sec.
- Effect: After Shadow Dance ends, $?s200758[Gloomblade][Backstab] and Shuriken Storm deal an additional $s1% damage as Shadow, fading by ${$s1/$s3}.1% per sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rapid Injection
- Node ID: `90766`
- Entry ID: `112659`
- Definition ID: `117664`
- Spell ID: `455072`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Envenom's effect increases the damage of Envenom by $s1%.
- Effect: Envenom's effect increases the damage of Envenom by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90768` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `90135`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Zero In
- Node ID: `90670`
- Entry ID: `112557`
- Definition ID: `117562`
- Spell ID: `1259485`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto-attack critical strikes increase the damage and critical strike chance of your next Between the Eyes by $1259486s1%, stacking up to $1259486u times.
- Effect: Your auto-attack critical strikes increase the damage and critical strike chance of your next Between the Eyes by $1259486s1%, stacking up to $1259486u times.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90654` (type `2`), node `90668` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deeper Daggers
- Node ID: `90721`
- Entry ID: `112609`
- Definition ID: `117614`
- Spell ID: `382517`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shadow damage increased by $383405s1%.
- Effect: Shadow damage increased by $383405s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90713` (type `2`), node `90724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shrouded Suffocation
- Node ID: `90776`
- Entry ID: `112669`
- Definition ID: `117674`
- Spell ID: `385478`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Garrote damage increased by $s1%. Garrote generates $s2 additional combo points when used from Stealth.
- Effect: Garrote damage increased by $s1%. Garrote generates $s2 additional combo points when used from Stealth.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90768` (type `2`), node `90777` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Blindside
- Node ID: `90622`
- Entry ID: `112507`
- Definition ID: `117512`
- Spell ID: `328085`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ambush and Mutilate have a $s1% chance to make your next Ambush free and usable without Stealth. Chance increased to $s2% if the target is under $s3% health.
- Effect: Ambush and Mutilate have a $s1% chance to make your next Ambush free and usable without Stealth. Chance increased to $s2% if the target is under $s3% health.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90777` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Potent Powder
- Node ID: `90718`
- Entry ID: `112606`
- Definition ID: `117611`
- Spell ID: `1265952`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Black Powder deals increased damage equal to $s1% of your Mastery when it spends $s2 or more combo points.
- Effect: Black Powder deals increased damage equal to $s1% of your Mastery when it spends $s2 or more combo points.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90713` (type `2`), node `90716` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Grand Melee
- Node ID: `90667`
- Entry ID: `112554`
- Definition ID: `117559`
- Spell ID: `1259469`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blade Flurry causes your attacks to hit nearby enemies for an additional $s1% of their normal damage.
- Effect: Blade Flurry causes your attacks to hit nearby enemies for an additional $s1% of their normal damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90668` (type `2`), node `90669` (type `2`), node `90671` (type `2`)
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
### Vigor
- Node ID: `90759`
- Entry ID: `112651`
- Definition ID: `117656`
- Spell ID: `14983`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Increases your maximum Energy by $s1 and Energy regeneration by $s2%.
- Effect: Increases your maximum Energy by $s1 and Energy regeneration by $s2%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90758` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `69540`, index `1`, operation `0`, curve `69539`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Supercharger
- Node ID: `90639`
- Entry ID: `112525`
- Definition ID: `117530`
- Spell ID: `470347`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: $?a137035[Shadow Dance]?a137036[Adrenaline Rush][Kingsbane] supercharges $m1 combo $Lpoint:points;.

Damaging finishing moves consume a supercharged combo point to function as if they spent $m2 additional combo $Lpoint:points;.
- Effect: $?a137035[Shadow Dance]?a137036[Adrenaline Rush][Kingsbane] supercharges $m1 combo $Lpoint:points;.

Damaging finishing moves consume a supercharged combo point to function as if they spent $m2 additional combo $Lpoint:points;.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `90640` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `79574`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Subterfuge
- Node ID: `90688`
- Entry ID: `112576`
- Definition ID: `117581`
- Spell ID: `108208`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Abilities requiring Stealth can be used for $?a137035[${$s4/1000}][${$s2/1000}] sec after Stealth breaks.

Combat benefits requiring Stealth persist for an additional $?a137035[${$s4/1000}][${$s2/1000}] sec after Stealth breaks.
- Effect: Abilities requiring Stealth can be used for $?a137035[${$s4/1000}][${$s2/1000}] sec after Stealth breaks.

Combat benefits requiring Stealth persist for an additional $?a137035[${$s4/1000}][${$s2/1000}] sec after Stealth breaks.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90691` (type `2`)
- Effect-point records: index `1`, operation `0`, curve `76845`, index `2`, operation `0`, curve `76843`, index `0`, operation `0`, curve `76844`, index `3`, operation `0`, curve `79583`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Summarily Dispatched
- Node ID: `90676`
- Entry ID: `112563`
- Definition ID: `117568`
- Spell ID: `381990`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Dispatch deals $s1% increased damage and costs $s3 less Energy. This damage bonus is increased by $315341s4% while your damage is enhanced by your Between the Eyes.
- Effect: Dispatch deals $s1% increased damage and costs $s3 less Energy. This damage bonus is increased by $315341s4% while your damage is enhanced by your Between the Eyes.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90664` (type `2`), node `90677` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `92462`, index `1`, operation `1`, curve `92461`, index `2`, operation `1`, curve `92460`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death Perception
- Node ID: `90706`
- Entry ID: `112594`
- Definition ID: `117599`
- Spell ID: `469642`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Find Weakness increases the damage of finishing moves by $s1%.

Shadow Dance increases the damage of finishing moves by $s2%.

Shadow Blades increases the damage of finishing moves by $s3%.
- Effect: Find Weakness increases the damage of finishing moves by $s1%.

Shadow Dance increases the damage of finishing moves by $s2%.

Shadow Blades increases the damage of finishing moves by $s3%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90704` (type `2`), node `90707` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61208`, index `2`, operation `0`, curve `79855`, index `1`, operation `0`, curve `79856`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Zoldyck Recipe
- Node ID: `90785`
- Entry ID: `112678`
- Definition ID: `117683`
- Spell ID: `381798`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Your Bleed, weapon poison, and other Nature damage is increased by $s1% against targets below $s2% health.
- Effect: Your Bleed, weapon poison, and other Nature damage is increased by $s1% against targets below $s2% health.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90770` (type `2`), node `90786` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61229`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Regicide's Reward
- Node ID: `94552`
- Entry ID: `117130`
- Definition ID: `122142`
- Spell ID: `1250325`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Kingsbane ends, gain $1250331s1% haste for every $s1 stacks of increased Kingsbane damage that you had, decreasing by $1250331s1% every $1250331t2 sec.
- Effect: When Kingsbane ends, gain $1250331s1% haste for every $s1 stacks of increased Kingsbane damage that you had, decreasing by $1250331s1% every $1250331t2 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90770` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dragon-Bone Dice
- Node ID: `90653`
- Entry ID: `112539`
- Definition ID: `117544`
- Spell ID: `1259481`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The bonuses granted by your Roll the Bones are stronger.

Bonuses to chance for Sinister Strike to strike twice are $s1% greater.
Bonuses to Sinister Strike and Ambush damage are $s2% greater.
Bonuses to Restless Blades cooldown reduction are $s3% greater.
Jackpot's bonus to critical strike chance is $s4% greater.
- Effect: The bonuses granted by your Roll the Bones are stronger.

Bonuses to chance for Sinister Strike to strike twice are $s1% greater.
Bonuses to Sinister Strike and Ambush damage are $s2% greater.
Bonuses to Restless Blades cooldown reduction are $s3% greater.
Jackpot's bonus to critical strike chance is $s4% greater.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90655` (type `2`), node `90664` (type `2`), node `90670` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Shadow
- Node ID: `90732`
- Entry ID: `112620`
- Definition ID: `117625`
- Spell ID: `245687`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Shadow Dance increases all ability damage by $s2%, and Shadowstrike and Shuriken Storm damage by an additional $s1%.
- Effect: Shadow Dance increases all ability damage by $s2%, and Shadowstrike and Shuriken Storm damage by an additional $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90707` (type `2`), node `90721` (type `2`), node `90731` (type `2`)
- Effect-point records: index `1`, operation `0`, curve `61216`, index `0`, operation `0`, curve `61217`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Inspiring Strike
- Node ID: `90767`
- Entry ID: `112660`
- Definition ID: `117665`
- Spell ID: `1250036`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Applying Envenom while Envenom is already active causes it to increase all damage you deal by $s1% in addition to increasing your poison application chance.
- Effect: Applying Envenom while Envenom is already active causes it to increase all damage you deal by $s1% in addition to increasing your poison application chance.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90766` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Poisoner's Drive
- Node ID: `90767`
- Entry ID: `134835`
- Definition ID: `139603`
- Spell ID: `1250318`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Applying Envenom while Envenom is already active restores $1250319s1 combo point.
- Effect: Applying Envenom while Envenom is already active restores $1250319s1 combo point.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90766` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Avulsion
- Node ID: `90774`
- Entry ID: `112667`
- Definition ID: `117672`
- Spell ID: `1250358`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Rupture damage increased by $s1%.
- Effect: Rupture damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90766` (type `2`), node `90776` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fan the Hammer
- Node ID: `90666`
- Entry ID: `112553`
- Definition ID: `117558`
- Spell ID: `381846`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: When you gain Opportunity, gain $m1 additional $Lcharge:charges;. Max ${$s2+1} charges.

Pistol Shot consumes $m1 additional $Lcharge:charges; of Opportunity to fire $m1 additional $Lbullet:bullets;. Additional shots deal $s3% reduced damage.
- Effect: When you gain Opportunity, gain $m1 additional $Lcharge:charges;. Max ${$s2+1} charges.

Pistol Shot consumes $m1 additional $Lcharge:charges; of Opportunity to fire $m1 additional $Lbullet:bullets;. Additional shots deal $s3% reduced damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90667` (type `2`), node `90670` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61201`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Finality
- Node ID: `90720`
- Entry ID: `112608`
- Definition ID: `117613`
- Spell ID: `382525`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Eviscerate and Black Powder have $s1% increased critical strike damage bonus.
- Effect: Eviscerate and Black Powder have $s1% increased critical strike damage bonus.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90718` (type `2`), node `90721` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61210`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Scent of Blood
- Node ID: `90775`
- Entry ID: `112668`
- Definition ID: `117673`
- Spell ID: `381799`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Each enemy afflicted by your Rupture increases your Agility by $S1%, up to a maximum of $394080u%.
- Effect: Each enemy afflicted by your Rupture increases your Agility by $S1%, up to a maximum of $394080u%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90622` (type `2`), node `90776` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `61228`
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
### Thistle Tea
- Node ID: `90756`
- Entry ID: `112648`
- Definition ID: `117653`
- Spell ID: `469779`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc381623
- Effect: $@spelldesc381623
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90759` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thistle Tea
- Node ID: `90756`
- Entry ID: `137464`
- Definition ID: `142224`
- Spell ID: `1298826`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Restore $s1 Energy.
- Effect: Restore $s1 Energy.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90759` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cold Blooded Killer
- Node ID: `90748`
- Entry ID: `112639`
- Definition ID: `117644`
- Spell ID: `382245`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critically striking with an attack that generates combo points increases the critical strike chance of your next finishing move by $1264297s1%.
- Effect: Critically striking with an attack that generates combo points increases the critical strike chance of your next finishing move by $1264297s1%.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90749` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echoing Reprimand
- Node ID: `90638`
- Entry ID: `112524`
- Definition ID: `117529`
- Spell ID: `470669`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After consuming a supercharged combo point, your next $?s200758[Gloomblade]?a137035[Backstab]?a137036[Sinister Strike][Mutilate] also strikes the target with an Echoing Reprimand dealing $470672s1 Physical damage.
- Effect: After consuming a supercharged combo point, your next $?s200758[Gloomblade]?a137035[Backstab]?a137036[Sinister Strike][Mutilate] also strikes the target with an Echoing Reprimand dealing $470672s1 Physical damage.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `90639` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Forced Induction
- Node ID: `90638`
- Entry ID: `112523`
- Definition ID: `117528`
- Spell ID: `470668`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Increase the bonus granted when a damaging finishing move consumes a supercharged combo point by $s1.
- Effect: Increase the bonus granted when a damaging finishing move consumes a supercharged combo point by $s1.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `90639` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deeper Stratagem
- Node ID: `90750`
- Entry ID: `112642`
- Definition ID: `117647`
- Spell ID: `193531`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Effect: Gain $s1 additional max combo point.

Your finishing moves that consume more than $s3 combo points have increased effects, and your finishing moves deal $s4% increased damage.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90751` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Without a Trace
- Node ID: `101713`
- Entry ID: `125614`
- Definition ID: `130446`
- Spell ID: `382513`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Vanish has $s1 additional $lcharge:charges;.
- Effect: Vanish has $s1 additional $lcharge:charges;.
- Point cost per purchased rank: `1` × Specialization pool (Assassination, Outlaw, Subtlety) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `90688` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hidden Opportunity
- Node ID: `90675`
- Entry ID: `112562`
- Definition ID: `117567`
- Spell ID: `383281`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ambush has a chance to grant Opportunity. Chance to trigger this effect is $s1% of the chance for Sinister Strike to grant Opportunity.

Energy cost of Ambush reduced by $s2.
- Effect: Ambush has a chance to grant Opportunity. Chance to trigger this effect is $s1% of the chance for Sinister Strike to grant Opportunity.

Energy cost of Ambush reduced by $s2.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90676` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### The Rotten
- Node ID: `90705`
- Entry ID: `112593`
- Definition ID: `117598`
- Spell ID: `382015`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After activating Shadow Dance, your next $@switch<$s1>[attack][$s1 attacks] that $@switch<$s1>[generates][generate] combo points $@switch<$s1>[deals][deal] $394203s3% increased damage.
- Effect: After activating Shadow Dance, your next $@switch<$s1>[attack][$s1 attacks] that $@switch<$s1>[generates][generate] combo points $@switch<$s1>[deals][deal] $394203s3% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90706` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unstable Toxin
- Node ID: `90784`
- Entry ID: `112677`
- Definition ID: `117682`
- Spell ID: `1298812`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Envenom's damage is increased by $s1%, but its duration is reduced by ${$s2/-1000} sec.
- Effect: Envenom's damage is increased by $s1%, but its duration is reduced by ${$s2/-1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90785` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Killing Spree
- Node ID: `94565`
- Entry ID: `117148`
- Definition ID: `122160`
- Spell ID: `51690`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Finishing move that unleashes a barrage of gunfire, striking random enemies within $r yards for Physical damage. Number of strikes increased per combo point.

Restores $1235074m2 combo $Lpoint:points; every ${$t1}.2 sec. Each combo point spent above $?s193531&s394321[7]?s193531|s394321[6][5] increases damage by $s4%.

   1 point  : ${$<dmg>*2} over ${$424556d}.2 sec
   2 points: ${$<dmg>*3} over ${$424556d*2}.2 sec
   3 points: ${$<dmg>*4} over ${$424556d*3}.2 sec
   4 points: ${$<dmg>*5} over ${$424556d*4}.2 sec
   5 points: ${$<dmg>*6} over ${$424556d*5}.2 sec$?s193531|((s394320|s394321)&!s193531)[
   6 points: ${$<dmg>*7} over ${$424556d*6}.2 sec][]$?s193531&(s394320|s394321)[
   7 points: ${$<dmg>*8} over ${$424556d*7}.2 sec][]
- Effect: Finishing move that unleashes a barrage of gunfire, striking random enemies within $r yards for Physical damage. Number of strikes increased per combo point.

Restores $1235074m2 combo $Lpoint:points; every ${$t1}.2 sec. Each combo point spent above $?s193531&s394321[7]?s193531|s394321[6][5] increases damage by $s4%.

   1 point  : ${$<dmg>*2} over ${$424556d}.2 sec
   2 points: ${$<dmg>*3} over ${$424556d*2}.2 sec
   3 points: ${$<dmg>*4} over ${$424556d*3}.2 sec
   4 points: ${$<dmg>*5} over ${$424556d*4}.2 sec
   5 points: ${$<dmg>*6} over ${$424556d*5}.2 sec$?s193531|((s394320|s394321)&!s193531)[
   6 points: ${$<dmg>*7} over ${$424556d*6}.2 sec][]$?s193531&(s394320|s394321)[
   7 points: ${$<dmg>*8} over ${$424556d*7}.2 sec][]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90653` (type `2`), node `90676` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shadowcraft
- Node ID: `94580`
- Entry ID: `117168`
- Definition ID: `122180`
- Spell ID: `426594`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Shadow Dance is active, your Shadow Techniques triggers $s3% more frequently and generates $m2 additional combo $Lpoint:points;.
- Effect: While Shadow Dance is active, your Shadow Techniques triggers $s3% more frequently and generates $m2 additional combo $Lpoint:points;.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90706` (type `2`), node `90732` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Keep It Rolling
- Node ID: `90652`
- Entry ID: `112538`
- Definition ID: `117543`
- Spell ID: `381989`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increase the remaining duration of your active Roll the Bones combat enhancement by ${$s1/1000} sec.
- Effect: Increase the remaining duration of your active Roll the Bones combat enhancement by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90653` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Danse Macabre
- Node ID: `90730`
- Entry ID: `112618`
- Definition ID: `117623`
- Spell ID: `382528`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Shadow Dance is active, each different attack that generates or spends combo points lashes out at the target, dealing $1264397s1 Shadow damage.
- Effect: While Shadow Dance is active, each different attack that generates or spends combo points lashes out at the target, dealing $1264397s1 Shadow damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90732` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dragon-Tempered Blades
- Node ID: `94553`
- Entry ID: `117131`
- Definition ID: `122143`
- Spell ID: `381801`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You may apply $s1 additional Lethal and Non-Lethal Poison to your weapons, but they have $s2% less application chance.
- Effect: You may apply $s1 additional Lethal and Non-Lethal Poison to your weapons, but they have $s2% less application chance.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90767` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fast Action
- Node ID: `90644`
- Entry ID: `112530`
- Definition ID: `117535`
- Spell ID: `1259480`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cooldown of Between the Eyes is reduced by ${-$s1/1000} sec.

Between the Eyes increases your damage dealt by an additional $s2%.
- Effect: The cooldown of Between the Eyes is reduced by ${-$s1/1000} sec.

Between the Eyes increases your damage dealt by an additional $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90653` (type `2`), node `90666` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### The First Dance
- Node ID: `94581`
- Entry ID: `117169`
- Definition ID: `122181`
- Spell ID: `382505`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Remaining out of combat for $470677d increases the duration of your next Shadow Dance by ${$470678s1/1000} sec.
- Effect: Remaining out of combat for $470677d increases the duration of your next Shadow Dance by ${$470678s1/1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90720` (type `2`), node `90732` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Brew
- Node ID: `90719`
- Entry ID: `112607`
- Definition ID: `117612`
- Spell ID: `382504`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your weapon poisons have $s8% increased application chance and now deal damage as Shadow instead of Nature.

Shadow damage increased by $s2%.
- Effect: Your weapon poisons have $s8% increased application chance and now deal damage as Shadow instead of Nature.

Shadow damage increased by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90720` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sudden Demise
- Node ID: `94551`
- Entry ID: `117129`
- Definition ID: `122141`
- Spell ID: `423136`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Bleed damage increased by $s1%.

Targets below $s3% health instantly bleed out and take fatal damage when the remaining Bleed damage you would deal to them exceeds $s2% of their remaining health.
- Effect: Bleed damage increased by $s1%.

Targets below $s3% health instantly bleed out and take fatal damage when the remaining Bleed damage you would deal to them exceeds $s2% of their remaining health.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90775` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Preparation
- Node ID: `90665`
- Entry ID: `112552`
- Definition ID: `117557`
- Spell ID: `1277933`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Immediately reset the cooldowns of Adrenaline Rush, Between the Eyes, Blade Flurry, Blade Rush, and Killing Spree.
- Effect: Immediately reset the cooldowns of Adrenaline Rush, Between the Eyes, Blade Flurry, Blade Rush, and Killing Spree.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `90666` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancient Arts
- Node ID: `110432`
- Entry ID: `137064`
- Definition ID: `141827`
- Spell ID: `1268932`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damaging attacks that expend Shadow Techniques to generate combo points have a $s1% chance per stack expended to create a Shadow Clone that repeats the attack for $s2% of normal damage as Shadow.
- Effect: Damaging attacks that expend Shadow Techniques to generate combo points have a $s1% chance per stack expended to create a Shadow Clone that repeats the attack for $s2% of normal damage as Shadow.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancient Arts
- Node ID: `110432`
- Entry ID: `137063`
- Definition ID: `141826`
- Spell ID: `1268936`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `200`
- Description: Shadow damage increased by $s2%.

Shadow Clones have a $s1% chance to trigger Shadow Techniques' effect.
- Effect: Shadow damage increased by $s2%.

Shadow Clones have a $s1% chance to trigger Shadow Techniques' effect.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Effect-point records: index `0`, operation `1`, curve `98749`, index `1`, operation `1`, curve `98748`, index `2`, operation `1`, curve `98747`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancient Arts
- Node ID: `110432`
- Entry ID: `137062`
- Definition ID: `141825`
- Spell ID: `1268939`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: After attacks that generate combo points, if $s1 or more stacks of Shadow Techniques remain, your next damaging finishing move will expend them to generate combo points up to your max.
- Effect: After attacks that generate combo points, if $s1 or more stacks of Shadow Techniques remain, your next damaging finishing move will expend them to generate combo points up to your max.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Implacable
- Node ID: `110433`
- Entry ID: `137067`
- Definition ID: `141831`
- Spell ID: `1265385`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Nothing will save your target from you. Envenom damage increased by $s1%. Envenom restores $s2 Energy per combo point spent.
- Effect: Nothing will save your target from you. Envenom damage increased by $s1%. Envenom restores $s2 Energy per combo point spent.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Implacable
- Node ID: `110433`
- Entry ID: `137066`
- Definition ID: `141830`
- Spell ID: `1265386`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `200`
- Description: Your Nature and Bleed ability damage is increased by $s1%.
- Effect: Your Nature and Bleed ability damage is increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Effect-point records: index `0`, operation `1`, curve `98756`, index `1`, operation `1`, curve `98755`, index `2`, operation `1`, curve `98754`, index `3`, operation `1`, curve `98753`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Implacable
- Node ID: `110433`
- Entry ID: `137065`
- Definition ID: `141829`
- Spell ID: `1265387`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: After striking with Kingsbane, rapidly strike that target $1265787s1 times over $1265787d for $1265795s1 Physical and $1265794s1 Nature damage. Each strike applies the Lethal Poisons on your weapons and generates a combo point.
- Effect: After striking with Kingsbane, rapidly strike that target $1265787s1 times over $1265787d for $1265795s1 Physical and $1265794s1 Nature damage. Each strike applies the Lethal Poisons on your weapons and generates a combo point.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gravedigger
- Node ID: `110434`
- Entry ID: `137070`
- Definition ID: `141834`
- Spell ID: `1265861`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Between the Eyes has a $s1% chance to apply 2 stacks of its bonus to your damage dealt.
- Effect: Between the Eyes has a $s1% chance to apply 2 stacks of its bonus to your damage dealt.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gravedigger
- Node ID: `110434`
- Entry ID: `137069`
- Definition ID: `141833`
- Spell ID: `1265862`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `200`
- Description: When you spend $s1 or more combo points on Dispatch, immediately strike your target with an underhanded Scoundrel Strike for $s3 Physical damage.
- Effect: When you spend $s1 or more combo points on Dispatch, immediately strike your target with an underhanded Scoundrel Strike for $s3 Physical damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Effect-point records: index `1`, operation `0`, curve `98757`, index `2`, operation `1`, curve `98819`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gravedigger
- Node ID: `110434`
- Entry ID: `137068`
- Definition ID: `141832`
- Spell ID: `1265863`
- Tree ID: `852`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: When you Dispatch you have a $s1% chance per combo point spent to hide a bullet up your sleeve. When you've hidden $s2 bullets, your next Between the Eyes consumes them and costs no Energy, generates $1279356s1 combo points, and immediately resets its own cooldown.
- Effect: When you Dispatch you have a $s1% chance per combo point spent to hide a bullet up your sleeve. When you've hidden $s2 bullets, your next Between the Eyes consumes them and costs no Energy, generates $1279356s1 combo points, and immediately resets its own cooldown.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
