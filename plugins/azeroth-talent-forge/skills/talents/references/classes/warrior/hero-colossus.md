# Colossus

Reviewed build: `12.1.0.69404`
Hero subtree ID: `62`
Description: A veteran of countless battles who can shrug off attacks that would fell others while using their expertise to deliver their most powerful strikes and destroy their enemies.

## Hero talents

### Demolish
- Node ID: `94818`
- Entry ID: `117415`
- Definition ID: `122427`
- Spell ID: `436358`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash a series of precise and powerful strikes against your target, dealing ${$440884s1+$440886s1+$440888s1} damage to it, and $440888s1 damage to enemies within $440888A1 yds of it. Deals reduced damage beyond $s1 targets.

While channeling Demolish, you take $s4% less damage and are immune to stuns, knockbacks, and forced movement effects.

You can block, parry, dodge, and use certain defensive abilities while channeling Demolish.
- Effect: Unleash a series of precise and powerful strikes against your target, dealing ${$440884s1+$440886s1+$440888s1} damage to it, and $440888s1 damage to enemies within $440888A1 yds of it. Deals reduced damage beyond $s1 targets.

While channeling Demolish, you take $s4% less damage and are immune to stuns, knockbacks, and forced movement effects.

You can block, parry, dodge, and use certain defensive abilities while channeling Demolish.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Martial Expert
- Node ID: `94812`
- Entry ID: `117409`
- Definition ID: `122421`
- Spell ID: `429638`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strike damage of your abilities is increased by $s1% and the amount of damage blocked by your critical blocks is increased by $s2%.
- Effect: Critical strike damage of your abilities is increased by $s1% and the amount of damage blocked by your critical blocks is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Colossal Might
- Node ID: `94819`
- Entry ID: `117416`
- Definition ID: `122428`
- Spell ID: `429634`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Colossal Might increases damage dealt by your next Demolish by $440989s1%, stacking up to $440989u times.

$?c1[Mortal Strike][Shield Slam] grants a stack of Colossal Might and $?c1[Cleave][Revenge] grants a stack of Colossal Might when it strikes $s1 or more targets.
- Effect: Colossal Might increases damage dealt by your next Demolish by $440989s1%, stacking up to $440989u times.

$?c1[Mortal Strike][Shield Slam] grants a stack of Colossal Might and $?c1[Cleave][Revenge] grants a stack of Colossal Might when it strikes $s1 or more targets.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Boneshaker
- Node ID: `94789`
- Entry ID: `117386`
- Definition ID: `122398`
- Spell ID: `429639`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shockwave's stun duration is increased by ${$s1/1000} sec and reduces the movement speed of affected enemies by $458480s1% for $458480d after the stun ends.
- Effect: Shockwave's stun duration is increased by ${$s1/1000} sec and reduces the movement speed of affected enemies by $458480s1% for $458480d after the stun ends.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthquaker
- Node ID: `94789`
- Entry ID: `119858`
- Definition ID: `124758`
- Spell ID: `440992`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Shockwave also knocks enemies into the air and its cooldown is reduced by ${$s1/-1000} sec.
- Effect: Shockwave also knocks enemies into the air and its cooldown is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Decimator
- Node ID: `109814`
- Entry ID: `136073`
- Definition ID: `140828`
- Spell ID: `1270704`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Demolish's final strike applies Deep Wounds to all targets at $s1% effectiveness.
- Effect: Demolish's final strike applies Deep Wounds to all targets at $s1% effectiveness.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94818` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### One Against Many
- Node ID: `94799`
- Entry ID: `117396`
- Definition ID: `122408`
- Spell ID: `429637`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shockwave$?c1[, Cleave,][] and $?c1[Whirlwind][Revenge] deal $s1% more damage per target affected up to $s2.
- Effect: Shockwave$?c1[, Cleave,][] and $?c1[Whirlwind][Revenge] deal $s1% more damage per target affected up to $s2.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94812` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arterial Bleed
- Node ID: `94799`
- Entry ID: `119856`
- Definition ID: `124756`
- Spell ID: `440995`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Colossal Might increases the damage of your Rend and Deep Wounds by $440989s2% per stack.
- Effect: Colossal Might increases the damage of your Rend and Deep Wounds by $440989s2% per stack.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94812` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tide of Battle
- Node ID: `94811`
- Entry ID: `117408`
- Definition ID: `122420`
- Spell ID: `429641`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Colossal Might increases the damage of your $?c1[Overpower][Revenge] and Execute by $?c1[$440989s3][$440989s4]% per stack.
- Effect: Colossal Might increases the damage of your $?c1[Overpower][Revenge] and Execute by $?c1[$440989s3][$440989s4]% per stack.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94819` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### No Stranger to Pain
- Node ID: `94815`
- Entry ID: `117412`
- Definition ID: `122424`
- Spell ID: `429644`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Damage prevented by each use of Ignore Pain is increased by $s1%.
- Effect: Damage prevented by each use of Ignore Pain is increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94789` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Veteran Vitality
- Node ID: `94815`
- Entry ID: `119857`
- Definition ID: `124757`
- Spell ID: `440993`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When your health is brought below 35%, you gain a Second Wind, healing you for ${$441387s1*$441387t1*$441387d}% of your max health over $441387d.

This effect cannot occur more than once every $proccooldown sec.
- Effect: When your health is brought below 35%, you gain a Second Wind, healing you for ${$441387s1*$441387t1*$441387d}% of your max health over $441387d.

This effect cannot occur more than once every $proccooldown sec.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94789` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cut to the Bone
- Node ID: `109813`
- Entry ID: `136072`
- Definition ID: `140827`
- Spell ID: `1270709`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike][Shield Slam] critical strikes increase your Rend and Deep Wounds damage by $1270840s1% for $1270840d.
- Effect: $?c1[Mortal Strike][Shield Slam] critical strikes increase your Rend and Deep Wounds damage by $1270840s1% for $1270840d.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109814` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Practiced Strikes
- Node ID: `94796`
- Entry ID: `117393`
- Definition ID: `122405`
- Spell ID: `429647`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike and Slam damage increased by $s1%.

Cleave and Whirlwind damage increased by $s2%][Shield Slam damage increased by $s3%.

Revenge and Thunder Clap damage increased by $s4%].$?c3[

Shield Slam generates an additional ${$s5/10} Rage.][]
- Effect: $?c1[Mortal Strike and Slam damage increased by $s1%.

Cleave and Whirlwind damage increased by $s2%][Shield Slam damage increased by $s3%.

Revenge and Thunder Clap damage increased by $s4%].$?c3[

Shield Slam generates an additional ${$s5/10} Rage.][]
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94799` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Precise Might
- Node ID: `94794`
- Entry ID: `117391`
- Definition ID: `122403`
- Spell ID: `431548`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mortal Strike][Shield Slam] critical strikes grant an additional stack of Colossal Might.
- Effect: $?c1[Mortal Strike][Shield Slam] critical strikes grant an additional stack of Colossal Might.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94811` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mountain of Muscle and Scars
- Node ID: `94806`
- Entry ID: `117403`
- Definition ID: `122415`
- Spell ID: `429642`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You deal $s1% more damage and take $s4% less damage.

Size increased by $s5%.
- Effect: You deal $s1% more damage and take $s4% less damage.

Size increased by $s5%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94815` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Celeritous Conclusion
- Node ID: `109812`
- Entry ID: `136071`
- Definition ID: `140826`
- Spell ID: `1270710`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Demolish's final strike grants $1270843s1% Haste for $1270843d and increases the critical strike chance of your next $?c1[Mortal Strike][Shield Slam] by $1270846s1%.
- Effect: Demolish's final strike grants $1270843s1% Haste for $1270843d and increases the critical strike chance of your next $?c1[Mortal Strike][Shield Slam] by $1270846s1%.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109813` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Dominance of the Colossus
- Node ID: `94793`
- Entry ID: `117390`
- Definition ID: `122402`
- Spell ID: `429636`
- Tree ID: `850`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enemies affected by Demolish take up to ${$447513s2*$447513u*0.1}% more damage from you and deal up to ${$447513s1*$447513u*-0.1}% less damage to you for $447513d based on the number of stacks of Colossal Might consumed by Demolish.

Colossal Might stacks up to 10 times.
- Effect: Enemies affected by Demolish take up to ${$447513s2*$447513u*0.1}% more damage from you and deal up to ${$447513s1*$447513u*-0.1}% less damage to you for $447513d based on the number of stacks of Colossal Might consumed by Demolish.

Colossal Might stacks up to 10 times.
- Point cost per purchased rank: `1` × Hero pool (Colossus) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94794` (type `2`), node `94796` (type `2`), node `94806` (type `2`), node `109812` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
