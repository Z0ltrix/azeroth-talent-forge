# Rider of the Apocalypse

Reviewed build: `12.1.0.69404`
Hero subtree ID: `32`
Description: Riders of the Apoclypse call forth the power of the legendary Four Horsemen. They can call upon the Horsemen for aid and tap into the powers of death, famine and disease.

## Hero talents

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
