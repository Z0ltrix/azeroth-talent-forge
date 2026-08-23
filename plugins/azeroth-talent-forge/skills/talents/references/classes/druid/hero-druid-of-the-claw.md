# Druid of the Claw

Reviewed build: `12.1.0.69404`
Hero subtree ID: `21`
Description: Druids of the Claw are masters of their mighty animal forms. When they transform into cats or bears, they become ferocious combatants and protectors of the wild.

## Hero talents

### Ravage
- Node ID: `94609`
- Entry ID: `117206`
- Definition ID: `122218`
- Spell ID: `441583`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto-attacks have a chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.

$?a137010[$@spellicon441605|cFFFFFFFF$@spellname441605|r
$@spelldesc441605]$?a137011[$@spellicon441591|cFFFFFFFF$@spellname441591|r
$@spelldesc441591]
- Effect: Your auto-attacks have a chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.

$?a137010[$@spellicon441605|cFFFFFFFF$@spellname441605|r
$@spelldesc441605]$?a137011[$@spellicon441591|cFFFFFFFF$@spellname441591|r
$@spelldesc441591]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fount of Strength
- Node ID: `94618`
- Entry ID: `117218`
- Definition ID: `122230`
- Spell ID: `441675`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your maximum Energy and Rage are increased by $s1.

Frenzied Regeneration also increases your maximum health by $s3%.
- Effect: Your maximum Energy and Rage are increased by $s1.

Frenzied Regeneration also increases your maximum health by $s3%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dreadful Wound
- Node ID: `94620`
- Entry ID: `117220`
- Definition ID: `122232`
- Spell ID: `441809`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ravage also inflicts a Bleed that causes $?a137011[$441812s1][$451177s1] damage over $441812d and saps its victims' strength, reducing damage they deal to you by $?a137011[$441812s2][$451177s2]%.

Dreadful Wound is not affected by Circle of Life and Death. $?a137011[If a Dreadful Wound benefiting from Tiger's Fury is re-applied, the new Dreadful Wound deals damage as if Tiger's Fury was active.][]
- Effect: Ravage also inflicts a Bleed that causes $?a137011[$441812s1][$451177s1] damage over $441812d and saps its victims' strength, reducing damage they deal to you by $?a137011[$441812s2][$451177s2]%.

Dreadful Wound is not affected by Circle of Life and Death. $?a137011[If a Dreadful Wound benefiting from Tiger's Fury is re-applied, the new Dreadful Wound deals damage as if Tiger's Fury was active.][]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bestial Strength
- Node ID: `94611`
- Entry ID: `117208`
- Definition ID: `122220`
- Spell ID: `441841`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137011[Ferocious Bite and Rampant Ferocity damage increased by $s1% and Primal Wrath's direct damage increased by $s2%.][Maul and Raze damage increased by $s3%.]
- Effect: $?a137011[Ferocious Bite and Rampant Ferocity damage increased by $s1% and Primal Wrath's direct damage increased by $s2%.][Maul and Raze damage increased by $s3%.]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Limb from Limb
- Node ID: `109722`
- Entry ID: `135980`
- Definition ID: `140735`
- Spell ID: `1271540`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your auto-attacks are 30% more likely to make your next $?c2[Ferocious Bite]?s400254[Raze][Maul] become Ravage.
- Effect: Your auto-attacks are 30% more likely to make your next $?c2[Ferocious Bite]?s400254[Raze][Maul] become Ravage.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94609` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wildshape Mastery
- Node ID: `94610`
- Entry ID: `117207`
- Definition ID: `122219`
- Spell ID: `441678`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ironfur and Frenzied Regeneration persist in Cat Form.$?!c3[

When transforming from Bear to Cat Form, you retain $441685s1% of your Bear Form armor and health for $441685d.][]

For $441686d after entering Bear Form, you heal for $441686s1% of damage taken over $441688d.
- Effect: Ironfur and Frenzied Regeneration persist in Cat Form.$?!c3[

When transforming from Bear to Cat Form, you retain $441685s1% of your Bear Form armor and health for $441685d.][]

For $441686d after entering Bear Form, you heal for $441686s1% of damage taken over $441688d.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94618` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pack's Endurance
- Node ID: `94615`
- Entry ID: `117215`
- Definition ID: `122227`
- Spell ID: `441844`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stampeding Roar's duration is increased by $s1%.
- Effect: Stampeding Roar's duration is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94611` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ruthless Aggression
- Node ID: `109723`
- Entry ID: `135981`
- Definition ID: `140736`
- Spell ID: `441814`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ravage increases your auto-attack speed by $441817s1% for $441817d.
- Effect: Ravage increases your auto-attack speed by $441817s1% for $441817d.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109722` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Killing Strikes
- Node ID: `109723`
- Entry ID: `136624`
- Definition ID: `141396`
- Spell ID: `441824`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Ravage increases your Agility by $441825s1% and the armor granted by Ironfur by $441825s2% for $441825d.

Your first $?a137011[Tiger's Fury][Mangle] after entering combat makes your next $?a137011[Ferocious Bite][Maul] become Ravage.
- Effect: Ravage increases your Agility by $441825s1% and the armor granted by Ironfur by $441825s2% for $441825d.

Your first $?a137011[Tiger's Fury][Mangle] after entering combat makes your next $?a137011[Ferocious Bite][Maul] become Ravage.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109722` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Exacerbating Wounds
- Node ID: `94619`
- Entry ID: `117219`
- Definition ID: `122231`
- Spell ID: `1271839`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Dreadful Wounds increase the damage afflicted enemies take from your Bleed damage over time effects by $?c2[$s2][$s3]%.
- Effect: Your Dreadful Wounds increase the damage afflicted enemies take from your Bleed damage over time effects by $?c2[$s2][$s3]%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94620` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Strike for the Heart
- Node ID: `94614`
- Entry ID: `117214`
- Definition ID: `122226`
- Spell ID: `441845`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Shred, Swipe, and Rake damage increased by $s1% and their critical strike chance is increased by $s3%.][Mangle damage increased by $s4% and its critical strike chance is increased by $s5%.]

$?c3[Mangle heals you for $458724s1% of maximum health.][]
- Effect: $?c2[Shred, Swipe, and Rake damage increased by $s1% and their critical strike chance is increased by $s3%.][Mangle damage increased by $s4% and its critical strike chance is increased by $s5%.]

$?c3[Mangle heals you for $458724s1% of maximum health.][]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94615` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tear Down the Mighty
- Node ID: `94614`
- Entry ID: `117213`
- Definition ID: `122225`
- Spell ID: `441846`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?c2[Damage dealt by Chomp and ][]$?(c2&!s1243807)[Feral Frenzy]?c2[Frantic Frenzy][]$?c2[ increased by $s2%][The cooldown of Sundering Roar is reduced by ${$s1/-1000} sec].
- Effect: $?c2[Damage dealt by Chomp and ][]$?(c2&!s1243807)[Feral Frenzy]?c2[Frantic Frenzy][]$?c2[ increased by $s2%][The cooldown of Sundering Roar is reduced by ${$s1/-1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94615` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Empowered Shapeshifting
- Node ID: `94612`
- Entry ID: `117210`
- Definition ID: `122222`
- Spell ID: `441689`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Frenzied Regeneration can be cast in Cat Form for $s2 Energy.

Bear Form reduces magic damage you take by ${-$s4}%.

Shred and $?s202028[Brutal Slash][Swipe] damage increased by $s5%. Mangle damage increased by $s6%.
- Effect: Frenzied Regeneration can be cast in Cat Form for $s2 Energy.

Bear Form reduces magic damage you take by ${-$s4}%.

Shred and $?s202028[Brutal Slash][Swipe] damage increased by $s5%. Mangle damage increased by $s6%.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wildpower Surge
- Node ID: `94612`
- Entry ID: `117209`
- Definition ID: `122221`
- Spell ID: `441691`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?s202028[Shred and Brutal Slash]?a137011[Shred and Swipe][]$?a137011[ grant Ursine Potential. When you have $441695s1 stacks, the next time you transform into Bear Form, your next Mangle deals $441698s1% increased damage or your next Swipe deals $441698s2% increased damage. Either generates ${$442562s1/10} extra Rage.][Mangle grants Feline Potential. When you have $441701s1 stacks, the next time you transform into Cat Form, gain $441704s1 combo points and your next Ferocious Bite or Rip deals $441702s1% increased damage for its full duration.]
- Effect: $?s202028[Shred and Brutal Slash]?a137011[Shred and Swipe][]$?a137011[ grant Ursine Potential. When you have $441695s1 stacks, the next time you transform into Bear Form, your next Mangle deals $441698s1% increased damage or your next Swipe deals $441698s2% increased damage. Either generates ${$442562s1/10} extra Rage.][Mangle grants Feline Potential. When you have $441701s1 stacks, the next time you transform into Cat Form, gain $441704s1 combo points and your next Ferocious Bite or Rip deals $441702s1% increased damage for its full duration.]
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aggravate Wounds
- Node ID: `94616`
- Entry ID: `117216`
- Definition ID: `122228`
- Spell ID: `441829`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $?a137010[Maul, Raze, Mangle,  Thrash, or Swipe]$?a137011[attack with an Energy cost that] you cast extends the duration of your Dreadful Wounds by $?a137010[${$s1/1000}.1][${$s2/1000}.1] sec, up to $s3 additional sec.
- Effect: Every $?a137010[Maul, Raze, Mangle,  Thrash, or Swipe]$?a137011[attack with an Energy cost that] you cast extends the duration of your Dreadful Wounds by $?a137010[${$s1/1000}.1][${$s2/1000}.1] sec, up to $s3 additional sec.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94619` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twin Claw
- Node ID: `109721`
- Entry ID: `135979`
- Definition ID: `140734`
- Spell ID: `1271635`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You have a $?c2[$s1][$s2]% chance to follow up any single target melee ability$?c3[ or Raze][] with a Twin Claw, dealing $?c2[$1271636s1][$1271657s1] Physical damage and generating $?c2[$1271636s2 Energy][${$1271657s2/10} Rage].
- Effect: You have a $?c2[$s1][$s2]% chance to follow up any single target melee ability$?c3[ or Raze][] with a Twin Claw, dealing $?c2[$1271636s1][$1271657s1] Physical damage and generating $?c2[$1271636s2 Energy][${$1271657s2/10} Rage].
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109723` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Claw Rampage
- Node ID: `94613`
- Entry ID: `117211`
- Definition ID: `122223`
- Spell ID: `441835`
- Tree ID: `793`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: During Berserk, $?c3[Mangle, Thrash][Shred], and $?s202028[Brutal Slash][Swipe] have a $s1% chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.
- Effect: During Berserk, $?c3[Mangle, Thrash][Shred], and $?s202028[Brutal Slash][Swipe] have a $s1% chance to make your next $?a137010[Maul][Ferocious Bite] become Ravage.
- Point cost per purchased rank: `1` × Hero pool (Druid of the Claw) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94612` (type `2`), node `94614` (type `2`), node `94616` (type `2`), node `109721` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
