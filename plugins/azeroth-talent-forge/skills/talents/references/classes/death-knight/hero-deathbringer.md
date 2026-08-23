# Deathbringer

Reviewed build: `12.1.0.69404`
Hero subtree ID: `33`
Description: Become the emissary of death. Aim for the soul of your enemies with attacks empowered by the Shadowlands, and remind them of the inevitable.

## Hero talents

### Reaper's Mark
- Node ID: `95062`
- Entry ID: `117659`
- Definition ID: `122671`
- Spell ID: `439843`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Viciously slice into the soul of your enemy, dealing $?a137008[$s1][$s4] Shadowfrost damage and applying Reaper's Mark.

Each time you deal Shadow or Frost damage, add a stack of Reaper's Mark. After $434765d or reaching $434765u stacks, the mark explodes, dealing $?a137008[$436304s1][$436304s2] damage per stack.

Reaper's Mark travels to an unmarked enemy nearby if the target dies.
- Effect: Viciously slice into the soul of your enemy, dealing $?a137008[$s1][$s4] Shadowfrost damage and applying Reaper's Mark.

Each time you deal Shadow or Frost damage, add a stack of Reaper's Mark. After $434765d or reaching $434765u stacks, the mark explodes, dealing $?a137008[$436304s1][$436304s2] damage per stack.

Reaper's Mark travels to an unmarked enemy nearby if the target dies.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wave of Souls
- Node ID: `95036`
- Entry ID: `117633`
- Definition ID: `122645`
- Spell ID: `439851`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaper's Mark sends forth bursts of Shadowfrost energy and back, dealing $?a137008[$435802s1][$435802s2] Shadowfrost damage both ways to all enemies caught in its path.

Wave of Souls critical strikes cause enemies to take $443404s1% increased Shadowfrost damage for $443404d, stacking up to 2 times, and it is always a critical strike on its way back.
- Effect: Reaper's Mark sends forth bursts of Shadowfrost energy and back, dealing $?a137008[$435802s1][$435802s2] Shadowfrost damage both ways to all enemies caught in its path.

Wave of Souls critical strikes cause enemies to take $443404s1% increased Shadowfrost damage for $443404d, stacking up to 2 times, and it is always a critical strike on its way back.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wither Away
- Node ID: `95058`
- Entry ID: `117655`
- Definition ID: `122667`
- Spell ID: `441894`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Blood Plague][Frost Fever] deals its damage $?a137008[$s5]?a134735[$s7][$s6]% faster, and the second scythe of Exterminate applies $?a137008[Blood Plague][Frost Fever].
- Effect: $?a137008[Blood Plague][Frost Fever] deals its damage $?a137008[$s5]?a134735[$s7][$s6]% faster, and the second scythe of Exterminate applies $?a137008[Blood Plague][Frost Fever].
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bind in Darkness
- Node ID: `95043`
- Entry ID: `117640`
- Definition ID: `122652`
- Spell ID: `440031`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Blood Boil deals $s3% increased damage][Rime empowered Howling Blast deals $s4% increased damage to its main target], and is now Shadowfrost.

Shadowfrost damage applies 2 stacks to Reaper's Mark and 4 stacks when it is a critical strike.
- Effect: $?a137008[Blood Boil deals $s3% increased damage][Rime empowered Howling Blast deals $s4% increased damage to its main target], and is now Shadowfrost.

Shadowfrost damage applies 2 stacks to Reaper's Mark and 4 stacks when it is a critical strike.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frigid Resolve
- Node ID: `109735`
- Entry ID: `135993`
- Definition ID: `140748`
- Spell ID: `1265859`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The effectiveness of Permafrost is increased by $?c1[$s1][$s2]%$?c1[ and Exterminate grants Permafrost equal to $s3% of the damage dealt.]?c2[.][]

$@spellicon207200$@spellname207200
$@spelldesc207200
- Effect: The effectiveness of Permafrost is increased by $?c1[$s1][$s2]%$?c1[ and Exterminate grants Permafrost equal to $s3% of the damage dealt.]?c2[.][]

$@spellicon207200$@spellname207200
$@spelldesc207200
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95062` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Soul Rupture
- Node ID: `95061`
- Entry ID: `117658`
- Definition ID: `122670`
- Spell ID: `437161`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When Reaper's Mark explodes, it deals $?a137008[$s1][$s2]% of the damage dealt to nearby enemies.
- Effect: When Reaper's Mark explodes, it deals $?a137008[$s1][$s2]% of the damage dealt to nearby enemies.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95036` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Grim Reaper
- Node ID: `95034`
- Entry ID: `117631`
- Definition ID: `122643`
- Spell ID: `434905`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaper's Mark initial strike grants $?a137008][$s3 charges of Bone Shield][Killing Machine].

Reaper's Mark explosion deals up to $s1% increased damage based on your target's missing health.
- Effect: Reaper's Mark initial strike grants $?a137008][$s3 charges of Bone Shield][Killing Machine].

Reaper's Mark explosion deals up to $s1% increased damage based on your target's missing health.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95058` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pact of the Deathbringer
- Node ID: `95035`
- Entry ID: `117632`
- Definition ID: `122644`
- Spell ID: `440476`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you suffer a damaging effect equal to $s1% of your maximum health, you instantly cast Death Pact at $s3% effectiveness. May only occur every $s2 min.

When a Reaper's Mark explodes, the cooldowns of this effect and Death Pact are reduced by $s4 sec.
- Effect: When you suffer a damaging effect equal to $s1% of your maximum health, you instantly cast Death Pact at $s3% effectiveness. May only occur every $s2 min.

When a Reaper's Mark explodes, the cooldowns of this effect and Death Pact are reduced by $s4 sec.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95043` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rune Carved Plates
- Node ID: `95035`
- Entry ID: `123420`
- Definition ID: `128258`
- Spell ID: `440282`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Each Rune spent reduces the magic damage you take by ${$abs($440290s1/10)}.1% and each Rune generated reduces the physical damage you take by ${$abs($440289s1/10)}.1% for $440289d, up to $440290u times.
- Effect: Each Rune spent reduces the magic damage you take by ${$abs($440290s1/10)}.1% and each Rune generated reduces the physical damage you take by ${$abs($440289s1/10)}.1% for $440289d, up to $440290u times.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95043` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deathly Blows
- Node ID: `109734`
- Entry ID: `135992`
- Definition ID: `140747`
- Spell ID: `1265932`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Frost Strike damage is increased by $s1% and Glacial Advance damage is increased by $s2%.

Reaper's Mark grants $s4 charges of Bonegrinder if it is known.]?c1[Death Strike damage increased by $s3%.][]
- Effect: $?c2[Frost Strike damage is increased by $s1% and Glacial Advance damage is increased by $s2%.

Reaper's Mark grants $s4 charges of Bonegrinder if it is known.]?c1[Death Strike damage increased by $s3%.][]
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109735` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swift and Painful
- Node ID: `95032`
- Entry ID: `117629`
- Definition ID: `122641`
- Spell ID: `443560`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If no enemies are struck by Soul Rupture, you gain $469169s1% Strength for $469169d.

Wave of Souls is $s2% more effective on the main target of your Reaper's Mark.
- Effect: If no enemies are struck by Soul Rupture, you gain $469169s1% Strength for $469169d.

Wave of Souls is $s2% more effective on the main target of your Reaper's Mark.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95061` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dark Talons
- Node ID: `95057`
- Entry ID: `117654`
- Definition ID: `122666`
- Spell ID: `436687`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137008[Marrowrend and Heart Strike have][Consuming Killing Machine or Rime has] a $s1% chance to grant $s2 stacks of Icy Talons and increase its maximum stacks by the same amount for 6 sec.

Runic Power spending abilities count as Shadowfrost while Icy Talons is active.
- Effect: $?a137008[Marrowrend and Heart Strike have][Consuming Killing Machine or Rime has] a $s1% chance to grant $s2 stacks of Icy Talons and increase its maximum stacks by the same amount for 6 sec.

Runic Power spending abilities count as Shadowfrost while Icy Talons is active.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95034` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reaper's Onslaught
- Node ID: `95057`
- Entry ID: `128266`
- Definition ID: `133073`
- Spell ID: `469870`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Reaper's Mark by ${$s1/-1000} sec, but the amount of $?a137008[Marrowrends][Obliterates and Frostscythes] empowered by Exterminate is reduced by $s2.
- Effect: Reduces the cooldown of Reaper's Mark by ${$s1/-1000} sec, but the amount of $?a137008[Marrowrends][Obliterates and Frostscythes] empowered by Exterminate is reduced by $s2.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95034` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death's Messenger
- Node ID: `95049`
- Entry ID: `117646`
- Definition ID: `122658`
- Spell ID: `437122`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldowns of Lichborne and Raise Dead by ${$s1/-1000} sec.
- Effect: Reduces the cooldowns of Lichborne and Raise Dead by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95035` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expelling Shield
- Node ID: `95049`
- Entry ID: `128234`
- Definition ID: `133041`
- Spell ID: `439948`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When an enemy deals direct damage to your Anti-Magic Shell, their cast speed is reduced by $440739s1% for $440739d.
- Effect: When an enemy deals direct damage to your Anti-Magic Shell, their cast speed is reduced by $440739s1% for $440739d.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95035` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echoing Fury
- Node ID: `109733`
- Entry ID: `135991`
- Definition ID: `140746`
- Spell ID: `1265855`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reaper's Mark deals $s7% increased damage.

Casting $?c1?[Dancing Rune Weapon][Reaper's Mark] grants $?c1?[$s4][$s1] $Lstack:stacks; of Exterminate with $?c1?[$s5][$s2]% first scythe and $?c1?[$s6][$s3]% second scythe effectiveness.
- Effect: Reaper's Mark deals $s7% increased damage.

Casting $?c1?[Dancing Rune Weapon][Reaper's Mark] grants $?c1?[$s4][$s1] $Lstack:stacks; of Exterminate with $?c1?[$s5][$s2]% first scythe and $?c1?[$s6][$s3]% second scythe effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109734` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Exterminate
- Node ID: `95068`
- Entry ID: `117665`
- Definition ID: `122677`
- Spell ID: `441378`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: After Reaper's Mark explodes, your next $s3 $?a137008[$LMarrowrend:Marrowrends;][$LObliterate:Obliterates; or $LFrostscythe:Frostscythes;] cost $s4 $LRune:Runes; and summon $s1 $Lscythe:scythes; to strike your enemies.

The first scythe strikes your target for $?a137008[$441424s1][$441424s2] Shadowfrost damage $?c2[and has a $s6% chance to grant Killing Machine,][and] the second scythe strikes all enemies around your target for $?a137008[$441426s1][$441426s2] Shadowfrost damage$?(a441894&a137008)[ and applies Blood Plague]?(a441894&$a137006)[ and applies Frost Fever][]. Deals reduced damage beyond $s5 targets.
- Effect: After Reaper's Mark explodes, your next $s3 $?a137008[$LMarrowrend:Marrowrends;][$LObliterate:Obliterates; or $LFrostscythe:Frostscythes;] cost $s4 $LRune:Runes; and summon $s1 $Lscythe:scythes; to strike your enemies.

The first scythe strikes your target for $?a137008[$441424s1][$441424s2] Shadowfrost damage $?c2[and has a $s6% chance to grant Killing Machine,][and] the second scythe strikes all enemies around your target for $?a137008[$441426s1][$441426s2] Shadowfrost damage$?(a441894&a137008)[ and applies Blood Plague]?(a441894&$a137006)[ and applies Frost Fever][]. Deals reduced damage beyond $s5 targets.
- Point cost per purchased rank: `1` × Hero pool (Deathbringer) (ID `2986`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95032` (type `2`), node `95049` (type `2`), node `95057` (type `2`), node `109733` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
