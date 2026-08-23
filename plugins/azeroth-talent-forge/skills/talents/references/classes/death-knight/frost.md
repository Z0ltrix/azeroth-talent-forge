# Frost

Reviewed build: `12.1.0.69404`
Spec ID: `251`
Role: `2`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Icebound Fortitude
- Node ID: `76081`
- Entry ID: `96210`
- Definition ID: `101212`
- Spell ID: `48792`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your blood freezes, granting immunity to Stun effects and reducing all damage you take by $s3% for $d.
- Effect: Your blood freezes, granting immunity to Stun effects and reducing all damage you take by $s3% for $d.
- Point cost per purchased rank: `1` × Specialization pool (Blood, Frost, Unholy) (ID `2801`; group)
- Source gates: source `node`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
### Vampiric Strike
- Node ID: `95051`
- Entry ID: `117648`
- Definition ID: `122660`
- Spell ID: `433901`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Death Coil$?a137007[, Epidemic][] and Death Strike have a $s1% chance to make your next $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] become Vampiric Strike.

Vampiric Strike heals you for $?a137008[$434422s2][$434422s3]% of your maximum health and grants you Essence of the Blood Queen, increasing your Haste by ${$433925s1/10}.1%, up to ${$433925s1*$433925u/10}.1% for $433925d.
- Effect: Your Death Coil$?a137007[, Epidemic][] and Death Strike have a $s1% chance to make your next $?a137008[Heart Strike]?s207311[Clawing Shadows][Scourge Strike] become Vampiric Strike.

Vampiric Strike heals you for $?a137008[$434422s2][$434422s3]% of your maximum health and grants you Essence of the Blood Queen, increasing your Haste by ${$433925s1/10}.1%, up to ${$433925s1*$433925u/10}.1% for $433925d.
- Point cost per purchased rank: `1` × Hero pool (San'layn) (ID `2988`; group)
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
### Rider's Champion
- Node ID: `95066`
- Entry ID: `117663`
- Definition ID: `122675`
- Spell ID: `444005`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Spending Runes has a chance to call forth the aid of a Horsemen for $454390d.

|cFFFFFFFFMograine|R
Casts Death and Decay at his location that follows his position and extends the duration of your diseases by ${$s2/1000}.1 sec whenever it deals damage.

|cFFFFFFFFWhitemane|R
Casts Undeath on your target dealing $444633s1 Shadowfrost damage per stack every $444633t sec, for $444633d. Each time Undeath deals damage it gains a stack. Cannot be refreshed.

|cFFFFFFFFTrollbane|R
Casts Chains of Ice on your target slowing their movement speed by $444834s1% and increasing the damage they take from you by 5% for 8 sec.

|cFFFFFFFFNazgrim|R
While Nazgrim is active you gain Apocalyptic Conquest, increasing your Strength by $444763s1%.
- Effect: Spending Runes has a chance to call forth the aid of a Horsemen for $454390d.

|cFFFFFFFFMograine|R
Casts Death and Decay at his location that follows his position and extends the duration of your diseases by ${$s2/1000}.1 sec whenever it deals damage.

|cFFFFFFFFWhitemane|R
Casts Undeath on your target dealing $444633s1 Shadowfrost damage per stack every $444633t sec, for $444633d. Each time Undeath deals damage it gains a stack. Cannot be refreshed.

|cFFFFFFFFTrollbane|R
Casts Chains of Ice on your target slowing their movement speed by $444834s1% and increasing the damage they take from you by 5% for 8 sec.

|cFFFFFFFFNazgrim|R
While Nazgrim is active you gain Apocalyptic Conquest, increasing your Strength by $444763s1%.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### On a Paler Horse
- Node ID: `95060`
- Entry ID: `117657`
- Definition ID: `122669`
- Spell ID: `444008`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While outdoors you are able to mount your Acherus Deathcharger in combat.
- Effect: While outdoors you are able to mount your Acherus Deathcharger in combat.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Death Charge
- Node ID: `95060`
- Entry ID: `123412`
- Definition ID: `128250`
- Spell ID: `444010`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Call upon your Death Charger to break free of movement impairment effects.

For $444347d, while upon your Death Charger your movement speed is increased by $444347s5%, you cannot be slowed below $444347s10% of normal speed, and you are immune to forced movement effects and knockbacks.
- Effect: Call upon your Death Charger to break free of movement impairment effects.

For $444347d, while upon your Death Charger your movement speed is increased by $444347s5%, you cannot be slowed below $444347s10% of normal speed, and you are immune to forced movement effects and knockbacks.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mograine's Might
- Node ID: `95067`
- Entry ID: `117664`
- Definition ID: `122676`
- Spell ID: `444047`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your damage is increased by $444505s1% and you gain $?c3[the benefits of your Death and Decay]?c2[$444505s4% critical strike chance][] while inside Mograine's Death and Decay.
- Effect: Your damage is increased by $444505s1% and you gain $?c3[the benefits of your Death and Decay]?c2[$444505s4% critical strike chance][] while inside Mograine's Death and Decay.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Horsemen's Aid
- Node ID: `95037`
- Entry ID: `117634`
- Definition ID: `122646`
- Spell ID: `444074`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While at your aid, the Horsemen will occasionally cast Anti-Magic Shell on you and themselves at $s1% effectiveness.

You may only benefit from this effect every $451777d.
- Effect: While at your aid, the Horsemen will occasionally cast Anti-Magic Shell on you and themselves at $s1% effectiveness.

You may only benefit from this effect every $451777d.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pact of the Apocalypse
- Node ID: `95037`
- Entry ID: `123410`
- Definition ID: `128248`
- Spell ID: `444083`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you take damage, $s1% of the damage is redirected to each active horsemen.
- Effect: When you take damage, $s1% of the damage is redirected to each active horsemen.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ride or Die!
- Node ID: `109741`
- Entry ID: `135999`
- Definition ID: `140754`
- Spell ID: `1265959`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Pillar of Frost summons forth Trollbane for $s1 sec.][Dark Transformation summons forth Whitemane for $s2 sec.]
- Effect: $?c2[Pillar of Frost summons forth Trollbane for $s1 sec.][Dark Transformation summons forth Whitemane for $s2 sec.]
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Whitemane's Famine
- Node ID: `95047`
- Entry ID: `117644`
- Definition ID: `122656`
- Spell ID: `444033`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When $?a137006[Obliterate or Frostscythe]?s207311[Clawing Shadows][Scourge Strike] damages an enemy affected by Undeath it gains $s1 $Lstack:stacks; and infects another nearby enemy.
- Effect: When $?a137006[Obliterate or Frostscythe]?s207311[Clawing Shadows][Scourge Strike] damages an enemy affected by Undeath it gains $s1 $Lstack:stacks; and infects another nearby enemy.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95060` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nazgrim's Conquest
- Node ID: `95059`
- Entry ID: `117656`
- Definition ID: `122668`
- Spell ID: `444052`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If an enemy dies while Nazgrim is active, the strength of Apocalyptic Conquest is increased by $s1%.

Additionally, each Rune you spend increase its value by $s2%.
- Effect: If an enemy dies while Nazgrim is active, the strength of Apocalyptic Conquest is increased by $s1%.

Additionally, each Rune you spend increase its value by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95067` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Trollbane's Icy Fury
- Node ID: `95063`
- Entry ID: `117660`
- Definition ID: `122672`
- Spell ID: `444097`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137006[Obliterate and Frostscythe]?s207311[Clawing Shadows][Scourge Strike] $?a137006[shatter][shatters] Trollbane's Chains of Ice when hit, dealing $444834s2 Shadowfrost damage to nearby enemies, and slowing them by $444834s1% for $444834d. Deals reduced damage beyond $s1 targets.
- Effect: $?a137006[Obliterate and Frostscythe]?s207311[Clawing Shadows][Scourge Strike] $?a137006[shatter][shatters] Trollbane's Chains of Ice when hit, dealing $444834s2 Shadowfrost damage to nearby enemies, and slowing them by $444834s1% for $444834d. Deals reduced damage beyond $s1 targets.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95037` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Let Terror Reign
- Node ID: `109740`
- Entry ID: `135998`
- Definition ID: `140753`
- Spell ID: `1265949`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Casting Obliterate or Frostscythe orders Trollbane to cast his Obliterate or Frostscythe alongside you at $s1% effectiveness.][Casting Death Coil or Epidemic orders Whitemane to cast her Death Coil or Epidemic alongside you at $s2% effectiveness.]
- Effect: $?c2[Casting Obliterate or Frostscythe orders Trollbane to cast his Obliterate or Frostscythe alongside you at $s1% effectiveness.][Casting Death Coil or Epidemic orders Whitemane to cast her Death Coil or Epidemic alongside you at $s2% effectiveness.]
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109741` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hungering Thirst
- Node ID: `95044`
- Entry ID: `117641`
- Definition ID: `122653`
- Spell ID: `444037`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The damage of your diseases and $?a137006[Frost Strike][Death Coil] are increased by $s1%.
- Effect: The damage of your diseases and $?a137006[Frost Strike][Death Coil] are increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95047` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fury of the Horsemen
- Node ID: `95042`
- Entry ID: `117639`
- Definition ID: `122651`
- Spell ID: `444069`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 Runic Power you spend extends the duration of the Horsemen's aid in combat by $s3 sec, up to $s2 sec.
- Effect: Every $s1 Runic Power you spend extends the duration of the Horsemen's aid in combat by $s3 sec, up to $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95059` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### A Feast of Souls
- Node ID: `95042`
- Entry ID: `123411`
- Definition ID: `128249`
- Spell ID: `444072`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: While you have $s1 or more Horsemen aiding you, your $?c2[Runic Power spending abilities deal $440861s1%]?c3[Death Coil deals $440861s1% and Epidemic deals $440861s3%][] increased damage.
- Effect: While you have $s1 or more Horsemen aiding you, your $?c2[Runic Power spending abilities deal $440861s1%]?c3[Death Coil deals $440861s1% and Epidemic deals $440861s3%][] increased damage.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95059` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mawsworn Menace
- Node ID: `95054`
- Entry ID: `117651`
- Definition ID: `122663`
- Spell ID: `444099`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137006[Obliterate deals $s4]?s207311[Clawing Shadows deals $s3][Scourge Strike deals $s3]% increased damage and $?s152280[the cooldown of your Defile is reduced by ${$s2/-1000}]?a137006[your Remorseless Winter lasts ${$s5/1000} sec longer][the cooldown of your Death and Decay is reduced by ${$s1/-1000} sec].
- Effect: $?a137006[Obliterate deals $s4]?s207311[Clawing Shadows deals $s3][Scourge Strike deals $s3]% increased damage and $?s152280[the cooldown of your Defile is reduced by ${$s2/-1000}]?a137006[your Remorseless Winter lasts ${$s5/1000} sec longer][the cooldown of your Death and Decay is reduced by ${$s1/-1000} sec].
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `95063` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unholy Armaments
- Node ID: `109739`
- Entry ID: `135997`
- Definition ID: `140752`
- Spell ID: `1265971`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The abilities that Horsemen cast deal $s1% increased damage.$?c3[

Your Ghoul and skeletal archer deals $s3% and Lesser Ghouls deal $s5% increased damage][].
- Effect: The abilities that Horsemen cast deal $s1% increased damage.$?c3[

Your Ghoul and skeletal archer deals $s3% and Lesser Ghouls deal $s5% increased damage][].
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109740` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Apocalypse Now
- Node ID: `95041`
- Entry ID: `117638`
- Definition ID: `122650`
- Spell ID: `444040`
- Tree ID: `750`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Army of the Dead and Frostwyrm's Fury call upon all 4 Horsemen to aid you for ${$s2/1000} sec.
- Effect: Army of the Dead and Frostwyrm's Fury call upon all 4 Horsemen to aid you for ${$s2/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Rider of the Apocalypse) (ID `2987`; group)
- Source gates: source `group`; type `1`; currency `2960` spend gate `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `95042` (type `2`), node `95044` (type `2`), node `95054` (type `2`), node `109739` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
