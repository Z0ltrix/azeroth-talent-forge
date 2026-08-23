# Shaman class tree

Reviewed build: `12.1.0.69404`

This catalog contains shared class-tree facts. For budget schedules, see `overview.md`.

### Structural rank (no player-facing ability)
- Node ID: `99845`
- Entry ID: `123377`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99845`
- Entry ID: `123376`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99847`
- Entry ID: `123381`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99847`
- Entry ID: `123379`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99846`
- Entry ID: `123380`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Structural rank (no player-facing ability)
- Node ID: `99846`
- Entry ID: `123378`
- Definition ID: `0`
- Spell ID: `0`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Structural status: no spell ID or player-facing text exists in the exact-build source; this record is retained only for codec/topology correctness.
- Point cost per purchased rank: no cost record in the exact-build source
- Source gates: source `node`; type `1` | source `group`; type `1`; minimum level `71`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `structural`; build: `12.1.0.69404`
### Chain Heal
- Node ID: `103588`
- Entry ID: `127861`
- Definition ID: `132670`
- Spell ID: `1064`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Heals the friendly target for $s1, then jumps up to $?a236502[${$s3*(($236502s2/100)+1)}][$s3] yards to heal the $<jumps> most injured nearby allies. Healing is reduced by $s2% with each jump.
- Effect: Heals the friendly target for $s1, then jumps up to $?a236502[${$s3*(($236502s2/100)+1)}][$s3] yards to heal the $<jumps> most injured nearby allies. Healing is reduced by $s2% with each jump.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lava Burst
- Node ID: `103598`
- Entry ID: `127873`
- Definition ID: `132682`
- Spell ID: `51505`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hurls molten lava at the target, dealing $285452s1 Fire damage. Lava Burst will always critically strike if the target is affected by Flame Shock and its damage is increased by your critical strike chance.$?a343725[

|cFFFFFFFFGenerates $343725s3 Maelstrom.|r][]
- Effect: Hurls molten lava at the target, dealing $285452s1 Fire damage. Lava Burst will always critically strike if the target is affected by Flame Shock and its damage is increased by your critical strike chance.$?a343725[

|cFFFFFFFFGenerates $343725s3 Maelstrom.|r][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1` | source `node`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lava Lash
- Node ID: `109389`
- Entry ID: `135593`
- Definition ID: `140349`
- Spell ID: `60103`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Charges your off-hand weapon with lava and burns your target, dealing $s1 Fire damage.

Damage is increased by $s2% if your offhand weapon is imbued with Flametongue Weapon. $?s334033[Lava Lash will spread Flame Shock from your target to $s3 nearby targets.][]$?s334046[

Lava Lash increases the damage of Flame Shock on its target by $334168s1% for $334168d.][]
- Effect: Charges your off-hand weapon with lava and burns your target, dealing $s1 Fire damage.

Damage is increased by $s2% if your offhand weapon is imbued with Flametongue Weapon. $?s334033[Lava Lash will spread Flame Shock from your target to $s3 nearby targets.][]$?s334046[

Lava Lash increases the damage of Flame Shock on its target by $334168s1% for $334168d.][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `node`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chain Lightning
- Node ID: `103583`
- Entry ID: `127856`
- Definition ID: `132665`
- Spell ID: `188443`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hurls a lightning bolt at the enemy, dealing $s1 Nature damage and then jumping to additional nearby enemies. Affects $x1 total targets$?a383303[

|cFFFFFFFFConsumes Maelstrom Weapon for increased cast speed and damage.|r]?a187880[

|cFFFFFFFFConsumes Maelstrom Weapon for increased cast speed.|r][]$?a343725[

|cFFFFFFFFGenerates $343725s5 Maelstrom per target hit.|r][]
- Effect: Hurls a lightning bolt at the enemy, dealing $s1 Nature damage and then jumping to additional nearby enemies. Affects $x1 total targets$?a383303[

|cFFFFFFFFConsumes Maelstrom Weapon for increased cast speed and damage.|r]?a187880[

|cFFFFFFFFConsumes Maelstrom Weapon for increased cast speed.|r][]$?a343725[

|cFFFFFFFFGenerates $343725s5 Maelstrom per target hit.|r][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Call of the Ancestors
- Node ID: `94888`
- Entry ID: `117485`
- Definition ID: `122497`
- Spell ID: `443450`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137040[Stormkeeper calls an Ancestor to your side for $445624d.][Unleash Life calls an Ancestor to your side for $s1 sec.]

Whenever you cast a healing or damaging spell, the Ancestor will cast a similar spell.
- Effect: $?a137040[Stormkeeper calls an Ancestor to your side for $445624d.][Unleash Life calls an Ancestor to your side for $s1 sec.]

Whenever you cast a healing or damaging spell, the Ancestor will cast a similar spell.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Maelstrom Weapon
- Node ID: `80941`
- Entry ID: `101804`
- Definition ID: `106862`
- Spell ID: `187880`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you deal damage with a melee weapon, you have a chance to generate Maelstrom Weapon, stacking up to $344179u times. 

Each stack of Maelstrom Weapon reduces the cast time of your next Lightning Bolt or Chain Lightning by $s5% and increases its damage by $s3%.
- Effect: When you deal damage with a melee weapon, you have a chance to generate Maelstrom Weapon, stacking up to $344179u times. 

Each stack of Maelstrom Weapon reduces the cast time of your next Lightning Bolt or Chain Lightning by $s5% and increases its damage by $s3%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earth Shock
- Node ID: `80984`
- Entry ID: `101854`
- Definition ID: `106811`
- Spell ID: `8042`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Instantly shocks the target with concussive force, causing $s1 Nature damage.$?a190493[

Earth Shock will consume all stacks of Fulmination to deal extra Nature damage to your target.][]
- Effect: Instantly shocks the target with concussive force, causing $s1 Nature damage.$?a190493[

Earth Shock will consume all stacks of Fulmination to deal extra Nature damage to your target.][]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Blast
- Node ID: `80984`
- Entry ID: `127924`
- Definition ID: `132733`
- Spell ID: `117014`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Harnesses the raw power of the elements, dealing $s1 Elemental damage and increasing your Critical Strike or Haste by $118522s1% or Mastery by ${$173184s1*$168534bc1}% for $118522d.
- Effect: Harnesses the raw power of the elements, dealing $s1 Elemental damage and increasing your Critical Strike or Haste by $118522s1% or Mastery by ${$173184s1*$168534bc1}% for $118522d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Riptide
- Node ID: `81027`
- Entry ID: `101905`
- Definition ID: `106805`
- Spell ID: `61295`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Restorative waters wash over a friendly target, healing them for $s1 and an additional $o2 over $d.
- Effect: Restorative waters wash over a friendly target, healing them for $s1 and an additional $o2 over $d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Surging Totem
- Node ID: `94877`
- Entry ID: `117474`
- Definition ID: `122486`
- Spell ID: `444995`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Enhancement Summons a totem at the target location that creates Tremor immediately and every 6 sec for (122.382% of Attack Power) Flamestrike damage. Damage reduced beyond 5 targets. Lasts 25 sec. Restoration maintains Healing Rain with 10% increased effectiveness Replaces Rain.
- Effect: Enhancement Summons a totem at the target location that creates Tremor immediately and every 6 sec for (122.382% of Attack Power) Flamestrike damage. Damage reduced beyond 5 targets. Lasts 25 sec. Restoration maintains Healing Rain with 10% increased effectiveness Replaces Rain.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `wowhead`; build: `12.1.0.69404`
### Latent Wisdom
- Node ID: `94862`
- Entry ID: `117459`
- Definition ID: `122471`
- Spell ID: `443449`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Ancestors' spells are $s1% more powerful.
- Effect: Your Ancestors' spells are $s1% more powerful.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancient Fellowship
- Node ID: `94862`
- Entry ID: `123632`
- Definition ID: `128470`
- Spell ID: `443423`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Ancestors have a $s1% chance to call another Ancestor for $445624d when they depart.
- Effect: Ancestors have a $s1% chance to call another Ancestor for $445624d when they depart.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Reverb
- Node ID: `94869`
- Entry ID: `117466`
- Definition ID: `122478`
- Spell ID: `443418`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lava Burst gains an additional charge and deals $s2% increased damage.$?a137039[

Riptide gains an additional charge and heals for $s3% more.][]
- Effect: Lava Burst gains an additional charge and deals $s2% increased damage.$?a137039[

Riptide gains an additional charge and heals for $s3% more.][]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earth Shield
- Node ID: `103596`
- Entry ID: `127871`
- Definition ID: `132680`
- Spell ID: `974`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Protects the target with an earthen shield, increasing your healing on them by $s1% and healing them for ${$379s1*(1+$s1/100)} when they take damage. This heal can only occur once every $?a462454[${$proccooldown+($462454s2/1000)}.1][$proccooldown] sec. $?a1217622[Lasts $d][Maximum $u charges].

$?s383010[Earth Shield can only be placed on the Shaman and one other target at a time. The Shaman can have up to two Elemental Shields active on them.][Earth Shield can only be placed on one target at a time. Only one Elemental Shield can be active on the Shaman.]
- Effect: Protects the target with an earthen shield, increasing your healing on them by $s1% and healing them for ${$379s1*(1+$s1/100)} when they take damage. This heal can only occur once every $?a462454[${$proccooldown+($462454s2/1000)}.1][$proccooldown] sec. $?a1217622[Lasts $d][Maximum $u charges].

$?s383010[Earth Shield can only be placed on the Shaman and one other target at a time. The Shaman can have up to two Elemental Shields active on them.][Earth Shield can only be placed on one target at a time. Only one Elemental Shield can be active on the Shaman.]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103588` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Wolf Affinity
- Node ID: `103610`
- Entry ID: `127886`
- Definition ID: `132695`
- Spell ID: `382197`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Cleanse Spirit, Wind Shear, Purge, and totem casts no longer cancel Ghost Wolf.
- Effect: Cleanse Spirit, Wind Shear, Purge, and totem casts no longer cancel Ghost Wolf.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103588` (type `2`), node `103598` (type `2`), node `109389` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fire and Ice
- Node ID: `103605`
- Entry ID: `127880`
- Definition ID: `132689`
- Spell ID: `382886`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases all Fire and Frost damage you deal by $s1%.
- Effect: Increases all Fire and Frost damage you deal by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103598` (type `2`), node `109389` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spirit Wolf
- Node ID: `103581`
- Entry ID: `127854`
- Definition ID: `132663`
- Spell ID: `260878`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While transformed into a Ghost Wolf, you gain $260881s1% increased movement speed and $260881s2% damage reduction every $260882t1 sec, stacking up to $260881u times.
- Effect: While transformed into a Ghost Wolf, you gain $260881s1% increased movement speed and $260881s2% damage reduction every $260882t1 sec, stacking up to $260881u times.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103583` (type `2`), node `103598` (type `2`), node `109389` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thunderous Paws
- Node ID: `103581`
- Entry ID: `127853`
- Definition ID: `132662`
- Spell ID: `378075`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Ghost Wolf removes snares and increases your movement speed by an additional $s1% for the first $338036d. May only occur once every $proccooldown sec.
- Effect: Ghost Wolf removes snares and increases your movement speed by an additional $s1% for the first $338036d. May only occur once every $proccooldown sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103583` (type `2`), node `103598` (type `2`), node `109389` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Frost Shock
- Node ID: `109492`
- Entry ID: `135718`
- Definition ID: `140473`
- Spell ID: `196840`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Chills the target with frost, causing $s1 Frost damage and reducing the target's movement speed by $s2% for $d.$?a343725&a210714[

|cFFFFFFFFGenerates ${$343725s10+$343725s7} Maelstrom.|r]?a343725[

|cFFFFFFFFGenerates $343725s10 Maelstrom.|r][]
- Effect: Chills the target with frost, causing $s1 Frost damage and reducing the target's movement speed by $s2% for $d.$?a343725&a210714[

|cFFFFFFFFGenerates ${$343725s10+$343725s7} Maelstrom.|r]?a343725[

|cFFFFFFFFGenerates $343725s10 Maelstrom.|r][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103583` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Heed My Call
- Node ID: `94884`
- Entry ID: `117481`
- Definition ID: `122493`
- Spell ID: `443444`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ancestors last an additional ${$s1/1000} sec.
- Effect: Ancestors last an additional ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Routine Communication
- Node ID: `94884`
- Entry ID: `123630`
- Definition ID: `128468`
- Spell ID: `443445`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137040[Lightning Bolt, Lava Burst, Flame Shock, Voltaic Blaze, and Chain Lightning have a $s2][Riptide has a $s1]% chance to call an Ancestor to your side for $445624d.
- Effect: $?a137040[Lightning Bolt, Lava Burst, Flame Shock, Voltaic Blaze, and Chain Lightning have a $s2][Riptide has a $s1]% chance to call an Ancestor to your side for $445624d.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Influence
- Node ID: `109732`
- Entry ID: `135990`
- Definition ID: `140745`
- Spell ID: `1270446`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Intellect is increased by ${$s1}.1% for each Ancestor active.
- Effect: Your Intellect is increased by ${$s1}.1% for each Ancestor active.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94888` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Windfury Weapon
- Node ID: `80958`
- Entry ID: `101823`
- Definition ID: `106876`
- Spell ID: `33757`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Imbue your main-hand weapon with the element of Wind for $319773d. Each main-hand attack has a $319773h% chance to trigger $?s390288[three][two] extra attacks, dealing $25504sw1 Physical damage each.
- Effect: Imbue your main-hand weapon with the element of Wind for $319773d. Each main-hand attack has a $319773h% chance to trigger $?s390288[three][two] extra attacks, dealing $25504sw1 Physical damage each.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `80941` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthquake
- Node ID: `80985`
- Entry ID: `101855`
- Definition ID: `106814`
- Spell ID: `462620`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Causes the earth within $a1 yards of your target to tremble and break, dealing ${$s4*$77478s1} Nature damage over $d and has a $77478s2% chance to knock the enemy down. Multiple uses of Earthquake may overlap.

|cFFFFFFFFThis spell is cast at your target.|r
- Effect: Causes the earth within $a1 yards of your target to tremble and break, dealing ${$s4*$77478s1} Nature damage over $d and has a $77478s2% chance to knock the enemy down. Multiple uses of Earthquake may overlap.

|cFFFFFFFFThis spell is cast at your target.|r
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80984` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthquake
- Node ID: `80985`
- Entry ID: `127925`
- Definition ID: `132734`
- Spell ID: `61882`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Causes the earth within $a1 yards of the target location to tremble and break, dealing ${$s4*$77478s1} Nature damage over $d and has a $77478s2% chance to knock the enemy down. Multiple uses of Earthquake may overlap.

|cFFFFFFFFThis spell is cast at a selected location.|r
- Effect: Causes the earth within $a1 yards of the target location to tremble and break, dealing ${$s4*$77478s1} Nature damage over $d and has a $77478s2% chance to knock the enemy down. Multiple uses of Earthquake may overlap.

|cFFFFFFFFThis spell is cast at a selected location.|r
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80984` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Fury
- Node ID: `80983`
- Entry ID: `101853`
- Definition ID: `106810`
- Spell ID: `60188`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your damaging $?a343190[and healing ][]critical strikes deal ${$m1+200}% damage $?a343190[or healing ][]instead of the usual 200%.
- Effect: Your damaging $?a343190[and healing ][]critical strikes deal ${$m1+200}% damage $?a343190[or healing ][]instead of the usual 200%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80984` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Healing Rain
- Node ID: `81040`
- Entry ID: `101923`
- Definition ID: `106911`
- Spell ID: `73920`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Blanket the target area in healing rains, restoring ${$73921m1*6*2/$t2} health to up to $s4 allies over $d.

You can only have one Healing Rain active at a time.
- Effect: Blanket the target area in healing rains, restoring ${$73921m1*6*2/$t2} health to up to $s4 allies over $d.

You can only have one Healing Rain active at a time.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81027` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flametongue Weapon
- Node ID: `80942`
- Entry ID: `101805`
- Definition ID: `106864`
- Spell ID: `318038`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Imbue your $?s33757[off-hand ][]weapon with the element of Fire for $319778d$?c2[, causing each of your attacks to deal $10444s1 additional Fire damage]?c1[, increasing the damage of your Fire spells by ${$382028s1}.1%][].
- Effect: Imbue your $?s33757[off-hand ][]weapon with the element of Fire for $319778d$?c2[, causing each of your attacks to deal $10444s1 additional Fire damage]?c1[, increasing the damage of your Fire spells by ${$382028s1}.1%][].
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `80941` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echo of the Elements
- Node ID: `80981`
- Entry ID: `101850`
- Definition ID: `106837`
- Spell ID: `333919`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137039[Riptide and Lava Burst have][Lava Burst has] an additional charge.
- Effect: $?s137039[Riptide and Lava Burst have][Lava Burst has] an additional charge.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80984` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Healing Stream Totem
- Node ID: `81022`
- Entry ID: `101900`
- Definition ID: `106920`
- Spell ID: `392916`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelltooltip5394
- Effect: $@spelltooltip5394
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81027` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Rebound
- Node ID: `94890`
- Entry ID: `117487`
- Definition ID: `122499`
- Spell ID: `445025`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Lightning Bolt, Chain Lightning and Elemental Blast has a chance to unleash a Surging Bolt at your Surging Totem, increasing the totem's damage by $458269s1%, and then redirecting the bolt to your target for $458267s1 Nature damage. The damage bonus effect can stack.][Chain Heal now jumps to a nearby totem within $458357A3 yards once it reaches its last target, causing the totem to cast Chain Heal on an injured ally within $458357r yards for $458357s1. Jumps to $s1 nearby targets within $458357A3 yards.]
- Effect: $?a137041[Lightning Bolt, Chain Lightning and Elemental Blast has a chance to unleash a Surging Bolt at your Surging Totem, increasing the totem's damage by $458269s1%, and then redirecting the bolt to your target for $458267s1 Nature damage. The damage bonus effect can stack.][Chain Heal now jumps to a nearby totem within $458357A3 yards once it reaches its last target, causing the totem to cast Chain Heal on an injured ally within $458357r yards for $458357s1. Jumps to $s1 nearby targets within $458357A3 yards.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Amplification Core
- Node ID: `94874`
- Entry ID: `117471`
- Definition ID: `122483`
- Spell ID: `445029`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Surging Totem is active, your damage and healing done is increased by $456369s1%.
- Effect: While Surging Totem is active, your damage and healing done is increased by $456369s1%.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Oversurge
- Node ID: `94874`
- Entry ID: `125823`
- Definition ID: `130654`
- Spell ID: `445030`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Surging Totem $?a462110[heals for $s1% more][deals $s2% more damage] while Ascendance or Healing Tide Totem is active.
- Effect: Surging Totem $?a462110[heals for $s1% more][deals $s2% more damage] while Ascendance or Healing Tide Totem is active.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lively Totems
- Node ID: `94882`
- Entry ID: `117479`
- Definition ID: `122491`
- Spell ID: `445034`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Lava Lash has a chance to summon a Searing Totem to hurl Searing Bolts that deal $3606s1 Fire damage to a nearby enemy. Lasts $458101d.

Lava Lash and Voltaic Blaze cause your Searing Totems to shoot a Searing Volley at up to $s3 nearby enemies for $458147s1 Fire damage.][When you summon a Healing Tide Totem, Healing Stream Totem, or Spirit Link Totem you cast a free instant Chain Heal at $458221s2% effectiveness.]
- Effect: $?a137041[Lava Lash has a chance to summon a Searing Totem to hurl Searing Bolts that deal $3606s1 Fire damage to a nearby enemy. Lasts $458101d.

Lava Lash and Voltaic Blaze cause your Searing Totems to shoot a Searing Volley at up to $s3 nearby enemies for $458147s1 Fire damage.][When you summon a Healing Tide Totem, Healing Stream Totem, or Spirit Link Totem you cast a free instant Chain Heal at $458221s2% effectiveness.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Momentum
- Node ID: `109726`
- Entry ID: `135984`
- Definition ID: `140739`
- Spell ID: `1260644`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Lava Lash damage increased by $s2%.

Each stack of Maelstrom Weapon consumed increases the duration of an active Hot Hand by ${$s1/1000}.2 sec.][Reduces the cooldown of Healing Stream Totem by ${$s3/-1000} sec.]
- Effect: $?c2[Lava Lash damage increased by $s2%.

Each stack of Maelstrom Weapon consumed increases the duration of an active Hot Hand by ${$s1/1000}.2 sec.][Reduces the cooldown of Healing Stream Totem by ${$s3/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94877` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Offering from Beyond
- Node ID: `94887`
- Entry ID: `117484`
- Definition ID: `122496`
- Spell ID: `443451`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When an Ancestor is called, they reduce the cooldown of $?a137040[Stormkeeper by ${$s1/-1000} sec.][Riptide by ${$s2/-1000} sec.]
- Effect: When an Ancestor is called, they reduce the cooldown of $?a137040[Stormkeeper by ${$s1/-1000} sec.][Riptide by ${$s2/-1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94862` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primordial Capacity
- Node ID: `94860`
- Entry ID: `117457`
- Definition ID: `122469`
- Spell ID: `443448`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your maximum $?a137040[Maelstrom by $s1.][mana by $s2%.

Tidal Waves can now stack up to ${$s3+$s4} times.]
- Effect: Increases your maximum $?a137040[Maelstrom by $s1.][mana by $s2%.

Tidal Waves can now stack up to ${$s3+$s4} times.]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94884` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spiritwalker's Momentum
- Node ID: `94861`
- Entry ID: `117458`
- Definition ID: `122470`
- Spell ID: `443425`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Using spells with a cast time increases the duration of Spiritwalker's Grace and Spiritwalker's Aegis by ${$s1/1000} sec, up to a maximum of ${$s2/1000} sec.
- Effect: Using spells with a cast time increases the duration of Spiritwalker's Grace and Spiritwalker's Aegis by ${$s1/1000} sec, up to a maximum of ${$s2/1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94869` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Orbit
- Node ID: `103602`
- Entry ID: `127877`
- Definition ID: `132686`
- Spell ID: `383010`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the number of Elemental Shields you can have active on yourself by 1.

You can have Earth Shield on yourself and one ally at the same time.
- Effect: Increases the number of Elemental Shields you can have active on yourself by 1.

You can have Earth Shield on yourself and one ally at the same time.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103596` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spirit Walk
- Node ID: `103591`
- Entry ID: `127865`
- Definition ID: `132674`
- Spell ID: `58875`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Removes all movement impairing effects and increases your movement speed by $58875s1% for $58875d.
- Effect: Removes all movement impairing effects and increases your movement speed by $58875s1% for $58875d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103596` (type `2`), node `103610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Gust of Wind
- Node ID: `103591`
- Entry ID: `127864`
- Definition ID: `132673`
- Spell ID: `192063`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: A gust of wind hurls you forward.
- Effect: A gust of wind hurls you forward.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103596` (type `2`), node `103610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Astral Shift
- Node ID: `103616`
- Entry ID: `127893`
- Definition ID: `132702`
- Spell ID: `108271`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shift partially into the elemental planes, taking $s1% less damage for $d.
- Effect: Shift partially into the elemental planes, taking $s1% less damage for $d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103581` (type `2`), node `103605` (type `2`), node `103610` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nature's Guardian
- Node ID: `103613`
- Entry ID: `127890`
- Definition ID: `132699`
- Spell ID: `30884`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When your health is brought below $s1%, you instantly heal for ${$31616s1*(1+$s2/100)}% of your maximum health. Cannot occur more than once every $445698d.
- Effect: When your health is brought below $s1%, you instantly heal for ${$31616s1*(1+$s2/100)}% of your maximum health. Cannot occur more than once every $445698d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103581` (type `2`), node `109492` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Encasing Cold
- Node ID: `109493`
- Entry ID: `135719`
- Definition ID: `140474`
- Spell ID: `462762`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the cooldown of Frost Shock by ${$s1/1000} sec, but Frost Shock now freezes targets in place for $1258862d.
- Effect: Increases the cooldown of Frost Shock by ${$s1/1000} sec, but Frost Shock now freezes targets in place for $1258862d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109492` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arctic Snowstorm
- Node ID: `109493`
- Entry ID: `135717`
- Definition ID: `140472`
- Spell ID: `462764`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Enemies within $s1 yds of your Frost Shock are snared by $462765s1%.
- Effect: Enemies within $s1 yds of your Frost Shock are snared by $462765s1%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `109492` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Windspeaker
- Node ID: `109731`
- Entry ID: `135989`
- Definition ID: `140744`
- Spell ID: `1270447`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cast times of $?c1[Healing Surge, Chain Heal and][Healing Wave, Chain Heal, and] Lava Burst are reduced by $s1%.
- Effect: The cast times of $?c1[Healing Surge, Chain Heal and][Healing Wave, Chain Heal, and] Lava Burst are reduced by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109732` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Forceful Winds
- Node ID: `80969`
- Entry ID: `101834`
- Definition ID: `106888`
- Spell ID: `262647`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Windfury has a $s2% additional chance to trigger and its damage is increased by $s1%.
- Effect: Windfury has a $s2% additional chance to trigger and its damage is increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80958` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flash of Lightning
- Node ID: `80990`
- Entry ID: `101861`
- Definition ID: `106843`
- Spell ID: `381936`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the critical strike chance of Lightning Bolt$?a454009[, Tempest,][] and Chain Lightning by $s1%.
- Effect: Increases the critical strike chance of Lightning Bolt$?a454009[, Tempest,][] and Chain Lightning by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80985` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Soothing Rain
- Node ID: `103428`
- Entry ID: `127672`
- Definition ID: `132481`
- Spell ID: `1252874`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the healing done by $?a455630[Surging Totem by $s1%.][Healing Rain by $s1% and reduces its cast time by ${$s2/-1000}.1 sec.]
- Effect: Increases the healing done by $?a455630[Surging Totem by $s1%.][Healing Rain by $s1% and reduces its cast time by ${$s2/-1000}.1 sec.]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81040` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Crash Lightning
- Node ID: `80974`
- Entry ID: `101840`
- Definition ID: `106879`
- Spell ID: `187874`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Electrocutes all enemies in front of you, dealing $s1 Nature damage. 

Enhances your weapons for $187878d, causing Stormstrike and Lava Lash to discharge $195592s1 Nature damage split between up to $195592i enemies in front of you. $?s1252373[Multiple applications may overlap.][]
- Effect: Electrocutes all enemies in front of you, dealing $s1 Nature damage. 

Enhances your weapons for $187878d, causing Stormstrike and Lava Lash to discharge $195592s1 Nature damage split between up to $195592i enemies in front of you. $?s1252373[Multiple applications may overlap.][]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80942` (type `2`), node `80958` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tectonic Collapse
- Node ID: `81000`
- Entry ID: `101874`
- Definition ID: `106831`
- Spell ID: `1258899`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Earth Shock, Elemental Blast, and Earthquake deal $s1% increased damage.
- Effect: Earth Shock, Elemental Blast, and Earthquake deal $s1% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80983` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Aftershock
- Node ID: `81000`
- Entry ID: `101873`
- Definition ID: `106830`
- Spell ID: `273221`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Earth Shock, Elemental Blast, and Earthquake have a $s1% chance to refund all Maelstrom spent.
- Effect: Earth Shock, Elemental Blast, and Earthquake have a $s1% chance to refund all Maelstrom spent.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80983` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Acid Rain
- Node ID: `81039`
- Entry ID: `101922`
- Definition ID: `106910`
- Spell ID: `378443`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Deal ${$378597s1*$s1} Nature damage every $73920t3 sec to up to $378597s2 enemies inside of your Healing Rain.
- Effect: Deal ${$378597s1*$s1} Nature damage every $73920t3 sec to up to $378597s2 enemies inside of your Healing Rain.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81040` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ascendance
- Node ID: `81032`
- Entry ID: `101912`
- Definition ID: `106942`
- Spell ID: `114052`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Immediately heals for $294020s1 split between allies within $294020A1 yds and transforms into a Water Ascendant for $d.

While ascended, Chain Heal jumps to $s9 additional allies with $s17% healing reduced for all jumps, Healing Wave always critical heals and heals $s14 additional $Lally:allies; at $s15% effectiveness, and the mana cost of Chain Heal and Healing Wave is reduced by $s16%.
- Effect: Immediately heals for $294020s1 split between allies within $294020A1 yds and transforms into a Water Ascendant for $d.

While ascended, Chain Heal jumps to $s9 additional allies with $s17% healing reduced for all jumps, Healing Wave always critical heals and heals $s14 additional $Lally:allies; at $s15% effectiveness, and the mana cost of Chain Heal and Healing Wave is reduced by $s16%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81022` (type `2`), node `81040` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Healing Tide Totem
- Node ID: `81032`
- Entry ID: `135486`
- Definition ID: `140243`
- Spell ID: `108280`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Summons a totem at your feet for $d, which pulses every $t2 sec, healing all party or raid members within $114942A1 yards for $114942s1.

Healing reduced beyond $s1 targets.
- Effect: Summons a totem at your feet for $d, which pulses every $t2 sec, healing all party or raid members within $114942A1 yards for $114942s1.

Healing reduced beyond $s1 targets.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81022` (type `2`), node `81040` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Molten Assault
- Node ID: `80943`
- Entry ID: `101806`
- Definition ID: `106863`
- Spell ID: `334033`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lava Lash cooldown reduced by ${$m1/-1000}.1 sec, and if Lava Lash is used against a target affected by your Flame Shock, Flame Shock will be spread to up to $s2 nearby enemies.
- Effect: Lava Lash cooldown reduced by ${$m1/-1000}.1 sec, and if Lava Lash is used against a target affected by your Flame Shock, Flame Shock will be spread to up to $s2 nearby enemies.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80942` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Molten Wrath
- Node ID: `80999`
- Entry ID: `101872`
- Definition ID: `106832`
- Spell ID: `1258843`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lava Burst deals $s1% additional damage.
- Effect: Lava Burst deals $s1% additional damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80981` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Master of the Elements
- Node ID: `80999`
- Entry ID: `136714`
- Definition ID: `141486`
- Spell ID: `16166`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Casting Lava Burst increases the damage or healing of your next Nature$?a137039[][, Physical,] or Frost spell by $s2%.
- Effect: Casting Lava Burst increases the damage or healing of your next Nature$?a137039[][, Physical,] or Frost spell by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80981` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Water Totem Mastery
- Node ID: `81021`
- Entry ID: `101899`
- Definition ID: `106921`
- Spell ID: `382030`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Healing Stream Totem by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Healing Stream Totem by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81022` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Oversized Totems
- Node ID: `94859`
- Entry ID: `117456`
- Definition ID: `122468`
- Spell ID: `445026`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the size and radius of your totems by $458016s2%, and the health of your totems by $458016s1%.
- Effect: Increases the size and radius of your totems by $458016s2%, and the health of your totems by $458016s1%.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94890` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swift Recall
- Node ID: `94859`
- Entry ID: `125825`
- Definition ID: `130656`
- Spell ID: `445027`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Successfully removing a harmful effect with Tremor Totem or Poison Cleansing Totem, or controlling an enemy with Capacitor Totem or Earthgrab Totem reduces the cooldown of the totem used by $/1000;s1 sec.

Cannot occur more than once every $457676d per totem.
- Effect: Successfully removing a harmful effect with Tremor Totem or Poison Cleansing Totem, or controlling an enemy with Capacitor Totem or Earthgrab Totem reduces the cooldown of the totem used by $/1000;s1 sec.

Cannot occur more than once every $457676d per totem.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94890` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wind Barrier
- Node ID: `94891`
- Entry ID: `117488`
- Definition ID: `122500`
- Spell ID: `445031`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: If you have a totem active, your totem grants you a shield absorbing ${$mhp*$s1/100} damage for $457387d every $457390d.
- Effect: If you have a totem active, your totem grants you a shield absorbing ${$mhp*$s1/100} damage for $457387d every $457390d.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94874` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Splitstream
- Node ID: `94872`
- Entry ID: `117469`
- Definition ID: `122481`
- Spell ID: `445035`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[While Hot Hand is active Lava Lash shatters the earth, causing a Sundering at $s1% effectiveness.][Your Healing Stream Totems heals an additional ally at $s3% effectiveness.

Healing Tide Totem healing increased by $s2%.]
- Effect: $?a137041[While Hot Hand is active Lava Lash shatters the earth, causing a Sundering at $s1% effectiveness.][Your Healing Stream Totems heals an additional ally at $s3% effectiveness.

Healing Tide Totem healing increased by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94882` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Attunement
- Node ID: `109725`
- Entry ID: `135983`
- Definition ID: `140738`
- Spell ID: `1263288`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Mastery increased by $s1%.
- Effect: Mastery increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109726` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Healing Stream Totem
- Node ID: `103590`
- Entry ID: `127863`
- Definition ID: `132672`
- Spell ID: `392915`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelltooltip5394
- Effect: $@spelltooltip5394
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `node`; type `4`; currency `2801` spend gate `0` | source `node`; type `4`; currency `2801` spend gate `0`
- Incoming edges: node `103591` (type `2`), node `103602` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Winds of Al'Akir
- Node ID: `103614`
- Entry ID: `127891`
- Definition ID: `132700`
- Spell ID: `382215`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Increases your movement speed by $s1% and the movement speed bonus of Ghost Wolf by an additional $s2%.
- Effect: Increases your movement speed by $s1% and the movement speed bonus of Ghost Wolf by an additional $s2%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103591` (type `2`), node `103616` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `95921`, index `1`, operation `0`, curve `95920`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Planes Traveler
- Node ID: `103611`
- Entry ID: `127888`
- Definition ID: `132697`
- Spell ID: `381647`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Astral Shift by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Astral Shift by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103616` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Astral Bulwark
- Node ID: `103611`
- Entry ID: `127887`
- Definition ID: `132696`
- Spell ID: `377933`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Astral Shift reduces damage taken by an additional $s1%.
- Effect: Astral Shift reduces damage taken by an additional $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103616` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Brimming with Life
- Node ID: `103582`
- Entry ID: `127855`
- Definition ID: `132664`
- Spell ID: `381689`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Stamina increased by $s1%.

While you are at full health, Reincarnation cools down $s2% faster.
- Effect: Stamina increased by $s1%.

While you are at full health, Reincarnation cools down $s2% faster.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103613` (type `2`), node `103616` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `95919`, index `1`, operation `0`, curve `95918`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wind Shear
- Node ID: `103615`
- Entry ID: `127892`
- Definition ID: `132701`
- Spell ID: `57994`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Disrupts the target's concentration with a burst of wind, interrupting spellcasting and preventing any spell in that school from being cast for $d.
- Effect: Disrupts the target's concentration with a burst of wind, interrupting spellcasting and preventing any spell in that school from being cast for $d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: none attached to this node or entry
- Incoming edges: node `103613` (type `2`), node `109493` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Natural Harmony
- Node ID: `94858`
- Entry ID: `117455`
- Definition ID: `122467`
- Spell ID: `443442`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Nature's Guardian by ${$s1/-1000} sec and causes it to heal for an additional $s2% of your maximum health.
- Effect: Reduces the cooldown of Nature's Guardian by ${$s1/-1000} sec and causes it to heal for an additional $s2% of your maximum health.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94887` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthen Communion
- Node ID: `94858`
- Entry ID: `123631`
- Definition ID: `128469`
- Spell ID: `443441`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Earth Shield has an additional $s1 charges and heals you for $s3% more.
- Effect: Earth Shield has an additional $s1 charges and heals you for $s3% more.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94887` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Maelstrom Supremacy
- Node ID: `94883`
- Entry ID: `117480`
- Definition ID: `122492`
- Spell ID: `443447`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137040[Increases the damage of Earth Shock, Elemental Blast, and Earthquake by $s1%.

Increases the healing of Healing Surge and Chain Heal by $s2%.][Increases the healing done by Healing Wave, Downpour, and Chain Heal by $s2%.]
- Effect: $?a137040[Increases the damage of Earth Shock, Elemental Blast, and Earthquake by $s1%.

Increases the healing of Healing Surge and Chain Heal by $s2%.][Increases the healing done by Healing Wave, Downpour, and Chain Heal by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94860` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Final Calling
- Node ID: `94875`
- Entry ID: `117472`
- Definition ID: `122484`
- Spell ID: `443446`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When an Ancestor departs, they cast $?a137040[Elemental Blast at a nearby enemy.][Hydrobubble on a nearby injured ally.

$@spellicon444490 |cFFFFFFFF$@spellname444490|r
$@spelldesc444490]
- Effect: When an Ancestor departs, they cast $?a137040[Elemental Blast at a nearby enemy.][Hydrobubble on a nearby injured ally.

$@spellicon444490 |cFFFFFFFF$@spellname444490|r
$@spelldesc444490]
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94861` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mystic Knowledge
- Node ID: `109730`
- Entry ID: `135988`
- Definition ID: `140743`
- Spell ID: `1270450`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[For $1270453d after casting Nature's Swiftness or Ancestral Swiftness, the recharge rate of Riptide is increased by $1270453s1%.

][]Increases the chance for Lava Surge to occur by $s1%.
- Effect: $?c3[For $1270453d after casting Nature's Swiftness or Ancestral Swiftness, the recharge rate of Riptide is increased by $1270453s1%.

][]Increases the chance for Lava Surge to occur by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109731` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightning Capacitor
- Node ID: `80997`
- Entry ID: `101870`
- Definition ID: `106817`
- Spell ID: `462862`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Lightning Shield is active, your Nature damage dealt is increased by $s3%.
- Effect: While Lightning Shield is active, your Nature damage dealt is increased by $s3%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80990` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unruly Winds
- Node ID: `80968`
- Entry ID: `101833`
- Definition ID: `106887`
- Spell ID: `390288`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Windfury Weapon has a $s1% chance to trigger a third attack.
- Effect: Windfury Weapon has a $s1% chance to trigger a third attack.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80969` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overflowing Shores
- Node ID: `92677`
- Entry ID: `114813`
- Definition ID: `119820`
- Spell ID: `383222`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a455630[Surging Totem][Healing Rain] instantly restores $383223s1 health to $s3 allies within its area, and its radius is increased by $s1 $Lyard:yards;.
- Effect: $?a455630[Surging Totem][Healing Rain] instantly restores $383223s1 health to $s3 allies within its area, and its radius is increased by $s1 $Lyard:yards;.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `103428` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overflowing Maelstrom
- Node ID: `80939`
- Entry ID: `101802`
- Definition ID: `106871`
- Spell ID: `384143`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Maelstrom Weapon can now stack $s1 additional times.

Each Maelstrom Weapon stacks consumed grants Overflowing Maelstrom, reducing the cast time of your next Healing Surge or Chain Heal by $s3%, and increasing their healing by $s4% up to $s5 times. This effect can be accumulated up to $410681u times.
- Effect: Maelstrom Weapon can now stack $s1 additional times.

Each Maelstrom Weapon stacks consumed grants Overflowing Maelstrom, reducing the cast time of your next Healing Surge or Chain Heal by $s3%, and increasing their healing by $s4% up to $s5 times. This effect can be accumulated up to $410681u times.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80974` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormkeeper
- Node ID: `80988`
- Entry ID: `101859`
- Definition ID: `106819`
- Spell ID: `191634`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Charge yourself with lightning, causing your next $s5 Lightning $lBolt:Bolts; to be instant cast and deal $s2% more damage, or cause your next $s5 Chain $LLightning:Lightings; to be instant cast and trigger an Elemental Overload on every target.$?a1264863[

Additionally, increases Lightning Bolt and Chain Lightning damage by ${$1264863s2}.1%.][]$?a1264762[

|cFFFFFFFFGenerates $1264762s2 Maelstrom.|r][]
- Effect: Charge yourself with lightning, causing your next $s5 Lightning $lBolt:Bolts; to be instant cast and deal $s2% more damage, or cause your next $s5 Chain $LLightning:Lightings; to be instant cast and trigger an Elemental Overload on every target.$?a1264863[

Additionally, increases Lightning Bolt and Chain Lightning damage by ${$1264863s2}.1%.][]$?a1264762[

|cFFFFFFFFGenerates $1264762s2 Maelstrom.|r][]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `81000` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Vigor
- Node ID: `103429`
- Entry ID: `127673`
- Definition ID: `132482`
- Spell ID: `207401`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Targets you heal with Healing Wave, Chain Heal, or Riptide's initial heal gain $s2% increased health for $207400d.
- Effect: Targets you heal with Healing Wave, Chain Heal, or Riptide's initial heal gain $s2% increased health for $207400d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81032` (type `2`), node `81039` (type `2`), node `103428` (type `2`)
- Effect-point records: index `1`, operation `0`, curve `81482`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### First Ascendant
- Node ID: `81033`
- Entry ID: `101913`
- Definition ID: `106933`
- Spell ID: `462440`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cooldown of Ascendance$?a137039[ and Healing Tide Totem][] is reduced by ${$s1/-1000} sec.
- Effect: The cooldown of Ascendance$?a137039[ and Healing Tide Totem][] is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81032` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Preeminence
- Node ID: `81033`
- Entry ID: `135485`
- Definition ID: `140242`
- Spell ID: `462443`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your haste is increased by $s2% $?a137039 [while Ascendance or Healing Tide Totem is active and their durations are][during Ascendance and its duration is] increased by ${$s1/1000} sec.
- Effect: Your haste is increased by $s2% $?a137039 [while Ascendance or Healing Tide Totem is active and their durations are][during Ascendance and its duration is] increased by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81032` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ashen Catalyst
- Node ID: `80947`
- Entry ID: `101811`
- Definition ID: `106897`
- Spell ID: `390370`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: When Lava Lash strikes a target affected by your Flame Shock, its cooldown is reduced by ${$s1/1000}.1 sec.
- Effect: When Lava Lash strikes a target affected by your Flame Shock, its cooldown is reduced by ${$s1/1000}.1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80943` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Resurgence
- Node ID: `81024`
- Entry ID: `101902`
- Definition ID: `106916`
- Spell ID: `16196`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your direct heal criticals refund a percentage of your maximum mana: $<healingwave>% from Healing Wave, $<riptide>% from Riptide, and $<chainheal>% from Chain Heal.
- Effect: Your direct heal criticals refund a percentage of your maximum mana: $<healingwave>% from Healing Wave, $<riptide>% from Riptide, and $<chainheal>% from Chain Heal.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81021` (type `2`), node `81032` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flametongue Weapon
- Node ID: `81004`
- Entry ID: `101879`
- Definition ID: `106829`
- Spell ID: `318038`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Imbue your $?s33757[off-hand ][]weapon with the element of Fire for $319778d$?c2[, causing each of your attacks to deal $10444s1 additional Fire damage]?c1[, increasing the damage of your Fire spells by ${$382028s1}.1%][].
- Effect: Imbue your $?s33757[off-hand ][]weapon with the element of Fire for $319778d$?c2[, causing each of your attacks to deal $10444s1 additional Fire damage]?c1[, increasing the damage of your Fire spells by ${$382028s1}.1%][].
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `80999` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Living Stream
- Node ID: `81018`
- Entry ID: `101895`
- Definition ID: `106925`
- Spell ID: `382482`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing Stream Totem heals for $s1% more, decaying over its duration.
- Effect: Healing Stream Totem heals for $s1% more, decaying over its duration.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1`
- Incoming edges: node `81021` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Imbuement Mastery
- Node ID: `94871`
- Entry ID: `117468`
- Definition ID: `122480`
- Spell ID: `445028`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Increases the chance for Windfury Weapon to trigger by $s1% and increases its damage by $s2%.

When Flametongue Weapon triggers from Windfury Weapon attacks, it has a chance to gather a whirl of flame around the target, dealing $s5% of its damage to all nearby enemies.][Increases the duration of your Earthliving effect by ${$s3/1000} sec.]
- Effect: $?a137041[Increases the chance for Windfury Weapon to trigger by $s1% and increases its damage by $s2%.

When Flametongue Weapon triggers from Windfury Weapon attacks, it has a chance to gather a whirl of flame around the target, dealing $s5% of its damage to all nearby enemies.][Increases the duration of your Earthliving effect by ${$s3/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2800` spend gate `0` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `94859` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Pulse Capacitor
- Node ID: `94866`
- Entry ID: `117463`
- Definition ID: `122475`
- Spell ID: `445032`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Increases the damage of Surging Totem by $s1%.][Increases the healing done by Surging Totem by $s2%.]
- Effect: $?a137041[Increases the damage of Surging Totem by $s1%.][Increases the healing done by Surging Totem by $s2%.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94891` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Supportive Imbuements
- Node ID: `94866`
- Entry ID: `125824`
- Definition ID: `130655`
- Spell ID: `445033`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137041[Increases the critical strike chance of Flametongue Weapon by $s1%, and its critical strike damage by $s2%.][Learn a new weapon imbue, Tidecaller's Guard.

$@spellicon457481 $@spellname457481
$@spelldesc457481 ]
- Effect: $?a137041[Increases the critical strike chance of Flametongue Weapon by $s1%, and its critical strike damage by $s2%.][Learn a new weapon imbue, Tidecaller's Guard.

$@spellicon457481 $@spellname457481
$@spelldesc457481 ]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94891` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Coordination
- Node ID: `94881`
- Entry ID: `117478`
- Definition ID: `122490`
- Spell ID: `445036`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137041[Increases the critical strike chance of your Searing Totem's attacks by $s1%, and its critical strike damage by $s2%.][Chain Heals from Lively Totem and Totemic Rebound are $s3% more effective.]
- Effect: $?a137041[Increases the critical strike chance of your Searing Totem's attacks by $s1%, and its critical strike damage by $s2%.][Chain Heals from Lively Totem and Totemic Rebound are $s3% more effective.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94872` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthsurge
- Node ID: `94881`
- Entry ID: `125822`
- Definition ID: `130653`
- Spell ID: `455590`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?a137041[Casting Sundering within $s2 yards of your Surging Totem causes it to create a Tremor at $s1% effectiveness at the target area.][Allies affected by your Earthliving effect receive $s3% increased healing from you.]
- Effect: $?a137041[Casting Sundering within $s2 yards of your Surging Totem causes it to create a Tremor at $s1% effectiveness at the target area.][Allies affected by your Earthliving effect receive $s3% increased healing from you.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94872` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primal Catalyst
- Node ID: `109724`
- Entry ID: `135982`
- Definition ID: `140737`
- Spell ID: `1260874`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[After casting Surging Totem, your next Lava Lash casts again at $s1% effectiveness.][Healing Stream Totem and Healing Tide Totem healing has a $s2% chance to apply Earthliving to allies it heals.]
- Effect: $?c2[After casting Surging Totem, your next Lava Lash casts again at $s1% effectiveness.][Healing Stream Totem and Healing Tide Totem healing has a $s2% chance to apply Earthliving to allies it heals.]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109725` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Resistance
- Node ID: `103601`
- Entry ID: `127876`
- Definition ID: `132685`
- Spell ID: `462368`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing from Healing Stream Totem reduces Fire, Frost, and Nature damage taken by $462568s1% for $462568d.
- Effect: Healing from Healing Stream Totem reduces Fire, Frost, and Nature damage taken by $462568s1% for $462568d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103590` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthgrab Totem
- Node ID: `103622`
- Entry ID: `127902`
- Definition ID: `132711`
- Spell ID: `51485`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summons a totem at the target location for $d. The totem pulses every $116943t1 sec, rooting all enemies within $64695A1 yards for $64695d. Enemies previously rooted by the totem instead suffer $116947s1% movement speed reduction.
- Effect: Summons a totem at the target location for $d. The totem pulses every $116943t1 sec, rooting all enemies within $64695A1 yards for $64695d. Enemies previously rooted by the totem instead suffer $116947s1% movement speed reduction.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103590` (type `2`), node `103614` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Capacitor Totem
- Node ID: `103579`
- Entry ID: `127851`
- Definition ID: `132660`
- Spell ID: `192058`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summons a totem at the target location that gathers electrical energy from the surrounding air and explodes after $s2 sec, stunning all enemies within $118905A1 yards for $118905d.
- Effect: Summons a totem at the target location that gathers electrical energy from the surrounding air and explodes after $s2 sec, stunning all enemies within $118905A1 yards for $118905d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103611` (type `2`), node `103614` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spiritual Awakening
- Node ID: `110085`
- Entry ID: `136585`
- Definition ID: `141358`
- Spell ID: `1270375`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Mastery increased by $s1%.
- Effect: Mastery increased by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103582` (type `2`), node `103611` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Enhanced Imbues
- Node ID: `103606`
- Entry ID: `127881`
- Definition ID: `132690`
- Spell ID: `462796`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The effects of your weapon $?a137041[][and shield ]imbues are increased by $?c1[$s1]?c2[$s2]?c3[$s3][]%.
- Effect: The effects of your weapon $?a137041[][and shield ]imbues are increased by $?c1[$s1]?c2[$s2]?c3[$s3][]%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103582` (type `2`), node `103615` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Windveil
- Node ID: `103628`
- Entry ID: `127910`
- Definition ID: `132719`
- Spell ID: `355630`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Interrupting a spell with Wind Shear reduces all spell damage taken by $355634s1% for $355634d.
- Effect: Interrupting a spell with Wind Shear reduces all spell damage taken by $355634s1% for $355634d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103615` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Swiftness
- Node ID: `94894`
- Entry ID: `117491`
- Definition ID: `122503`
- Spell ID: `448861`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc443454
- Effect: $@spelldesc443454
- Point cost per purchased rank: `1` × Hero pool (Farseer) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94858` (type `2`), node `94875` (type `2`), node `94883` (type `2`), node `109730` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormblast
- Node ID: `80960`
- Entry ID: `101825`
- Definition ID: `106877`
- Spell ID: `319930`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stormstrike has an additional charge.

Stormsurge now also causes your next Stormstrike to deal $s1% additional damage as Nature damage, stacking up to $470466u times.
- Effect: Stormstrike has an additional charge.

Stormsurge now also causes your next Stormstrike to deal $s1% additional damage as Nature damage, stacking up to $470466u times.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80968` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Frenzy
- Node ID: `103635`
- Entry ID: `127917`
- Definition ID: `132726`
- Spell ID: `462695`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cast time of Lightning Bolt$?s454009[, Tempest,][] and Chain Lightning by $s1%.
- Effect: Reduces the cast time of Lightning Bolt$?s454009[, Tempest,][] and Chain Lightning by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80990` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overcharge
- Node ID: `80944`
- Entry ID: `101808`
- Definition ID: `106900`
- Spell ID: `1251026`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The critical strike damage of your Nature abilities are increased by $s2% of your critical strike chance.
- Effect: The critical strike damage of your Nature abilities are increased by $s2% of your critical strike chance.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80939` (type `2`), node `80968` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swelling Maelstrom
- Node ID: `81016`
- Entry ID: `101893`
- Definition ID: `106815`
- Spell ID: `381707`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your maximum Maelstrom by $s1.

Increases Earth Shock, Elemental Blast, and Earthquake damage by $s2%.
- Effect: Increases your maximum Maelstrom by $s1.

Increases Earth Shock, Elemental Blast, and Earthquake damage by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Current Control
- Node ID: `81038`
- Entry ID: `101920`
- Definition ID: `106908`
- Spell ID: `1253093`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the mana cost of Healing Wave by $s1% and the mana cost of Chain Heal by $s2%.
- Effect: Reduces the mana cost of Healing Wave by $s1% and the mana cost of Chain Heal by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `103428` (type `2`), node `103429` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Raging Maelstrom
- Node ID: `80938`
- Entry ID: `101801`
- Definition ID: `106880`
- Spell ID: `384149`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Lightning Bolt and Chain Lightning can consume up to $s1 Maelstrom Weapon stacks.
- Effect: Lightning Bolt and Chain Lightning can consume up to $s1 Maelstrom Weapon stacks.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80939` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primordial Fury
- Node ID: `103639`
- Entry ID: `127920`
- Definition ID: `132729`
- Spell ID: `378193`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Elemental Fury increases critical strike damage by an additional $s1%.
- Effect: Elemental Fury increases critical strike damage by an additional $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fury of the Storms
- Node ID: `80998`
- Entry ID: `101871`
- Definition ID: `106816`
- Spell ID: `191717`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Stormkeeper summons a $?a117013[Primal][Greater] Storm Elemental to hurl gusts of wind at your enemies for $157299d.
- Effect: Casting Stormkeeper summons a $?a117013[Primal][Greater] Storm Elemental to hurl gusts of wind at your enemies for $157299d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Herald of the Storms
- Node ID: `80998`
- Entry ID: `128223`
- Definition ID: `133030`
- Spell ID: `468571`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Reduces the cooldown of Stormkeeper by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Stormkeeper by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80988` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### White Water
- Node ID: `81047`
- Entry ID: `101932`
- Definition ID: `106929`
- Spell ID: `462587`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your critical heals have ${$s2+$s1}% effectiveness instead of the usual $s2%.
- Effect: Your critical heals have ${$s2+$s1}% effectiveness instead of the usual $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81024` (type `2`), node `81033` (type `2`), node `103429` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flurry
- Node ID: `103642`
- Entry ID: `101799`
- Definition ID: `106872`
- Spell ID: `382888`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your attack speed by $382889s1% for your next $382889n melee swings after dealing a critical strike with a spell or ability.
- Effect: Increases your attack speed by $382889s1% for your next $382889n melee swings after dealing a critical strike with a spell or ability.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80939` (type `2`), node `80947` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hot Hand
- Node ID: `80945`
- Entry ID: `101809`
- Definition ID: `106898`
- Spell ID: `201900`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Melee auto-attacks with Flametongue Weapon active have a $h% chance to reduce the cooldown of Lava Lash by ${100*(1-(100/(100+$m2)))}% and increase the damage of Lava Lash by $s3% for $215785d.

May not occur during an active Hot Hand.
- Effect: Melee auto-attacks with Flametongue Weapon active have a $h% chance to reduce the cooldown of Lava Lash by ${100*(1-(100/(100+$m2)))}% and increase the damage of Lava Lash by $s3% for $215785d.

May not occur during an active Hot Hand.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80947` (type `2`)
- Effect-point records: index `2`, operation `0`, curve `58604`, index `1`, operation `0`, curve `58603`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wavespeaker's Blessing
- Node ID: `103427`
- Entry ID: `127671`
- Definition ID: `132480`
- Spell ID: `381946`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Increases Riptide's duration by ${$s1/1000}.1 sec and its healing over time by $s2%.
- Effect: Increases Riptide's duration by ${$s1/1000}.1 sec and its healing over time by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81018` (type `2`), node `81024` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `78407`, index `1`, operation `0`, curve `81481`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flames of the Cauldron
- Node ID: `103630`
- Entry ID: `127912`
- Definition ID: `132721`
- Spell ID: `378266`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Flame Shock and Voltaic Blaze by ${$s2/-1000}.1 sec.

Flame Shock deals damage ${100*(1/(1+$m1/100)-1)}% faster.
- Effect: Reduces the cooldown of Flame Shock and Voltaic Blaze by ${$s2/-1000}.1 sec.

Flame Shock deals damage ${100*(1/(1+$m1/100)-1)}% faster.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `81004` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Quickstream
- Node ID: `81048`
- Entry ID: `101934`
- Definition ID: `106927`
- Spell ID: `1253099`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing Stream Totem heals ${100*(1/(1+$s1/100)-1)}% more often.
- Effect: Healing Stream Totem heals ${100*(1/(1+$s1/100)-1)}% more often.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81018` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Whirling Elements
- Node ID: `94879`
- Entry ID: `117476`
- Definition ID: `122488`
- Spell ID: `445024`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Elemental motes orbit around your Surging Totem. Your abilities consume the motes for enhanced effects. 

$?a137041[|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406

|cFFFFFFFFFire:|r $@spelldesc453405][|cFFFFFFFFWater:|r $@spelldesc453407

|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406]
- Effect: Elemental motes orbit around your Surging Totem. Your abilities consume the motes for enhanced effects. 

$?a137041[|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406

|cFFFFFFFFFire:|r $@spelldesc453405][|cFFFFFFFFWater:|r $@spelldesc453407

|cFFFFFFFFAir:|r $@spelldesc453409

|cFFFFFFFFEarth:|r $@spelldesc453406]
- Point cost per purchased rank: `1` × Hero pool (Totemic) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94866` (type `2`), node `94871` (type `2`), node `94881` (type `2`), node `109724` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Refreshing Waters
- Node ID: `103594`
- Entry ID: `127869`
- Definition ID: `132678`
- Spell ID: `378211`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Healing $?a137039[Wave][Surge] is $s1% more effective on yourself.
- Effect: Your Healing $?a137039[Wave][Surge] is $s1% more effective on yourself.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103601` (type `2`), node `103622` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Purify Spirit
- Node ID: `81073`
- Entry ID: `101964`
- Definition ID: `106962`
- Spell ID: `383016`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `0`
- Description: Purify Spirit additionally removes all Curse effects.
- Effect: Purify Spirit additionally removes all Curse effects.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1`
- Incoming edges: node `103579` (type `2`), node `103622` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Cleanse Spirit
- Node ID: `103608`
- Entry ID: `127884`
- Definition ID: `132693`
- Spell ID: `51886`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Removes all Curse effects from a friendly target.
- Effect: Removes all Curse effects from a friendly target.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8` | source `node`; type `1` | source `node`; type `1`
- Incoming edges: node `103579` (type `2`), node `103622` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Static Charge
- Node ID: `103618`
- Entry ID: `127896`
- Definition ID: `132705`
- Spell ID: `265046`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Reduces the cooldown of Capacitor Totem by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of Capacitor Totem by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103579` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `95922`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wind Rush Totem
- Node ID: `103627`
- Entry ID: `127909`
- Definition ID: `132718`
- Spell ID: `192077`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Summons a totem at the target location for $d, continually granting all allies who pass within $a1 yards $192082s1% increased movement speed for $192082d.
- Effect: Summons a totem at the target location for $d, continually granting all allies who pass within $a1 yards $192082s1% increased movement speed for $192082d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103579` (type `2`), node `110085` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earth Elemental
- Node ID: `103585`
- Entry ID: `127858`
- Definition ID: `132667`
- Spell ID: `198103`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Calls forth a $?a117013[Primal][Greater] Earth Elemental to protect you$?a1279819[, increasing your maximum health by $381755s1%][ and your allies, generating high threat and taunting enemies periodically] for $188616d.
- Effect: Calls forth a $?a117013[Primal][Greater] Earth Elemental to protect you$?a1279819[, increasing your maximum health by $381755s1%][ and your allies, generating high threat and taunting enemies periodically] for $188616d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103606` (type `2`), node `110085` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tempest
- Node ID: `94892`
- Entry ID: `117489`
- Definition ID: `122501`
- Spell ID: `454009`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Each Maelstrom spent has a ${$s1/100}.2% chance to upgrade][Each Maelstrom Weapon spent has a ${$s2/100}.2% chance to upgrade] your next Lightning Bolt to Tempest.

$@spelltooltip452201
- Effect: $?s137040[Each Maelstrom spent has a ${$s1/100}.2% chance to upgrade][Each Maelstrom Weapon spent has a ${$s2/100}.2% chance to upgrade] your next Lightning Bolt to Tempest.

$@spelltooltip452201
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Amped Up
- Node ID: `103638`
- Entry ID: `127919`
- Definition ID: `132728`
- Spell ID: `1269360`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your haste by $s1%.
- Effect: Increases your haste by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80997` (type `2`), node `103635` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm's Wrath
- Node ID: `80967`
- Entry ID: `101832`
- Definition ID: `107009`
- Spell ID: `392352`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increase the chance for Mastery: Enhanced Elements to trigger Windfury and Stormsurge by $s1%.
- Effect: Increase the chance for Mastery: Enhanced Elements to trigger Windfury and Stormsurge by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80944` (type `2`), node `80960` (type `2`), node `80968` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rip Current
- Node ID: `109301`
- Entry ID: `135487`
- Definition ID: `140244`
- Spell ID: `1254251`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Riptide by ${$s1/-1000}.1 sec.
- Effect: Reduces the cooldown of Riptide by ${$s1/-1000}.1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81038` (type `2`), node `92677` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Resonance
- Node ID: `103631`
- Entry ID: `127913`
- Definition ID: `132722`
- Spell ID: `1258895`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: All Elemental damage increased by $s1%.
- Effect: All Elemental damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `81016` (type `2`), node `103635` (type `2`), node `103639` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thunderstrike Ward
- Node ID: `103631`
- Entry ID: `135716`
- Definition ID: `140471`
- Spell ID: `462757`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Imbue your shield with the element of Lightning for $d, giving Lightning Bolt$?a454009[, Tempest,][] and Chain Lightning a chance to call down $s1 Thunderstrikes on your target for $462763s1 Nature damage.
- Effect: Imbue your shield with the element of Lightning for $d, giving Lightning Bolt$?a454009[, Tempest,][] and Chain Lightning a chance to call down $s1 Thunderstrikes on your target for $462763s1 Nature damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `81016` (type `2`), node `103635` (type `2`), node `103639` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Crashing Waves
- Node ID: `110084`
- Entry ID: `136583`
- Definition ID: `141356`
- Spell ID: `1253090`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing Wave's critical strike chance is increased by $s1%.
- Effect: Healing Wave's critical strike chance is increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81038` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Tempo
- Node ID: `80961`
- Entry ID: `101826`
- Definition ID: `106861`
- Spell ID: `1250364`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Elemental damage increased by $s1%. 

Each stack of Maelstrom Weapon consumed reduces the cooldown of Stormstrike by ${$s3/1000}.1 sec and Lava Lash by ${$s4/1000}.1 sec.
- Effect: Elemental damage increased by $s1%. 

Each stack of Maelstrom Weapon consumed reduces the cooldown of Stormstrike by ${$s3/1000}.1 sec and Lava Lash by ${$s4/1000}.1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80938` (type `2`), node `80944` (type `2`), node `103642` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unleash Life
- Node ID: `92675`
- Entry ID: `114811`
- Definition ID: `119818`
- Spell ID: `73685`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash elemental forces of Life, healing a friendly target for $s1.

Increases the healing of your next Riptide, Chain Heal, or Healing Wave by $s2% and reduces its cast time by $s3%.
- Effect: Unleash elemental forces of Life, healing a friendly target for $s1.

Increases the healing of your next Riptide, Chain Heal, or Healing Wave by $s2% and reduces its cast time by $s3%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `81038` (type `2`), node `81047` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Path of the Seer
- Node ID: `110066`
- Entry ID: `136561`
- Definition ID: `141334`
- Spell ID: `1269364`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases your Intellect by $s1%.
- Effect: Increases your Intellect by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `103639` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Torrent
- Node ID: `103432`
- Entry ID: `127678`
- Definition ID: `132487`
- Spell ID: `200072`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Riptide's initial heal is increased $s1% and has a $s2% increased critical strike chance.
- Effect: Riptide's initial heal is increased $s1% and has a $s2% increased critical strike chance.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81047` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Unity
- Node ID: `103633`
- Entry ID: `127915`
- Definition ID: `132724`
- Spell ID: `462866`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While a Fire Elemental is active, your Fire damage dealt is increased by $s1%.

While a Storm Elemental is active, your Nature damage dealt is increased by $s1%.
- Effect: While a Fire Elemental is active, your Fire damage dealt is increased by $s1%.

While a Storm Elemental is active, your Nature damage dealt is increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80998` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voltaic Blaze
- Node ID: `80954`
- Entry ID: `101819`
- Definition ID: `106869`
- Spell ID: `470057`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Instantly shocks the target and $s4 enemies within $A1 yds with blazing thunder, applying Flame Shock and dealing $1259101s1 Nature damage. Always critically strikes.$?a343725[

|cFFFFFFFFGenerates $343725s14 Maelstrom.|r][

Generates $s2 $Lstack:stacks; of Maelstrom Weapon.]
- Effect: Instantly shocks the target and $s4 enemies within $A1 yds with blazing thunder, applying Flame Shock and dealing $1259101s1 Nature damage. Always critically strikes.$?a343725[

|cFFFFFFFFGenerates $343725s14 Maelstrom.|r][

Generates $s2 $Lstack:stacks; of Maelstrom Weapon.]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80945` (type `2`), node `80947` (type `2`), node `103642` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Searing Flames
- Node ID: `81005`
- Entry ID: `101880`
- Definition ID: `106847`
- Spell ID: `381782`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Flame Shock damage has a chance to generate $s1 Maelstrom.
- Effect: Flame Shock damage has a chance to generate $s1 Maelstrom.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `80998` (type `2`), node `103630` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthliving Weapon
- Node ID: `81049`
- Entry ID: `101935`
- Definition ID: `106928`
- Spell ID: `382021`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Imbue your weapon with the element of Earth for $382022d. Your Riptide, Healing Wave, and Chain Heal healing has a $382022s2% chance to trigger Earthliving on the target, healing for $382024o1 over $382024d.
- Effect: Imbue your weapon with the element of Earth for $382022d. Your Riptide, Healing Wave, and Chain Heal healing has a $382022s2% chance to trigger Earthliving on the target, healing for $382024o1 over $382024d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `node`; type `4`; currency `2800` spend gate `0`
- Incoming edges: node `81047` (type `2`), node `103427` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthweaver
- Node ID: `81046`
- Entry ID: `101931`
- Definition ID: `106931`
- Spell ID: `1254210`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases Earth Shield healing by $s1%.
- Effect: Increases Earth Shield healing by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81048` (type `2`), node `103427` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unlimited Power
- Node ID: `94886`
- Entry ID: `117483`
- Definition ID: `122495`
- Spell ID: `454391`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Spending $?s137040[Maelstrom][Maelstrom Weapon stacks] grants you $454394s1% haste for $454394d.

Multiple applications may overlap.
- Effect: Spending $?s137040[Maelstrom][Maelstrom Weapon stacks] grants you $454394s1% haste for $454394d.

Multiple applications may overlap.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormcaller
- Node ID: `94893`
- Entry ID: `117490`
- Definition ID: `122502`
- Spell ID: `454021`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the critical strike chance of your Nature damage spells by $s1% and the critical strike damage of your Nature spells by $s2%.
- Effect: Increases the critical strike chance of your Nature damage spells by $s1% and the critical strike damage of your Nature spells by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightning Conduit
- Node ID: `94863`
- Entry ID: `117460`
- Definition ID: `122472`
- Spell ID: `467778`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: You have a chance to get struck by lightning, increasing your movement speed by $468226s2% for $468226d. The effectiveness is increased to $s3% in outdoor areas.

You call down a Thunderstorm when you Reincarnate.
- Effect: You have a chance to get struck by lightning, increasing your movement speed by $468226s2% for $468226d. The effectiveness is increased to $s3% in outdoor areas.

You call down a Thunderstorm when you Reincarnate.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Electroshock
- Node ID: `94863`
- Entry ID: `128226`
- Definition ID: `133033`
- Spell ID: `454022`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Tempest increases your movement speed by $454025s1% for $454025d.
- Effect: Tempest increases your movement speed by $454025s1% for $454025d.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Purge
- Node ID: `103624`
- Entry ID: `127905`
- Definition ID: `132714`
- Spell ID: `370`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Purges the enemy target, removing $m1 beneficial Magic $leffect:effects;.$?(s147762&s51530)
[ Successfully purging a target grants a stack of Maelstrom Weapon.][]
- Effect: Purges the enemy target, removing $m1 beneficial Magic $leffect:effects;.$?(s147762&s51530)
[ Successfully purging a target grants a stack of Maelstrom Weapon.][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `81073` (type `2`), node `103594` (type `2`), node `103608` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Greater Purge
- Node ID: `103624`
- Entry ID: `127904`
- Definition ID: `132713`
- Spell ID: `378773`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Purges the enemy target, removing $m1 beneficial Magic effects.
- Effect: Purges the enemy target, removing $m1 beneficial Magic effects.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `81073` (type `2`), node `103594` (type `2`), node `103608` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nature's Fury
- Node ID: `103617`
- Entry ID: `127894`
- Definition ID: `132703`
- Spell ID: `381655`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Increases the critical strike chance of your Nature spells and abilities by $s1%.
- Effect: Increases the critical strike chance of your Nature spells and abilities by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `81073` (type `2`), node `103608` (type `2`), node `103618` (type `2`), node `103627` (type `2`)
- Effect-point records: index `0`, operation `1`, curve `95495`, index `1`, operation `1`, curve `95494`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ascending Air
- Node ID: `103607`
- Entry ID: `127883`
- Definition ID: `132692`
- Spell ID: `462791`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Wind Rush Totem's cooldown is reduced by ${$s1/-1000} sec and its movement speed effect lasts an additional ${$s2/1000} sec.
- Effect: Wind Rush Totem's cooldown is reduced by ${$s1/-1000} sec and its movement speed effect lasts an additional ${$s2/1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103627` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Jet Stream
- Node ID: `103607`
- Entry ID: `127882`
- Definition ID: `132691`
- Spell ID: `462817`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Wind Rush Totem's movement speed bonus is increased by $s1% and now removes snares.
- Effect: Wind Rush Totem's movement speed bonus is increased by $s1% and now removes snares.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103627` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primordial Bond
- Node ID: `103612`
- Entry ID: `127889`
- Definition ID: `132698`
- Spell ID: `1279819`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Earth Elemental no longer taunts nearby enemies or generates threat and instead increases your maximum health by $381755s1% while active.
- Effect: Your Earth Elemental no longer taunts nearby enemies or generates threat and instead increases your maximum health by $381755s1% while active.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103585` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Hex
- Node ID: `103623`
- Entry ID: `127903`
- Definition ID: `132712`
- Spell ID: `51514`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Transforms the enemy into a frog for $d. While hexed, the victim is incapacitated, and cannot attack or cast spells. Damage may cancel the effect. Limit 1. Only works on Humanoids and Beasts.
- Effect: Transforms the enemy into a frog for $d. While hexed, the victim is incapacitated, and cannot attack or cast spells. Damage may cancel the effect. Limit 1. Only works on Humanoids and Beasts.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103585` (type `2`), node `103628` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormwell
- Node ID: `109729`
- Entry ID: `135987`
- Definition ID: `140742`
- Spell ID: `1264762`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Storm Elemental lasts ${$s1/1000} sec longer, and Stormkeeper generates $s2 Maelstrom.][Windfury Weapon damage increased by $s3%.

When Crash Lightning hits a single enemy, it activates Windfury Weapon.]
- Effect: $?c1[Storm Elemental lasts ${$s1/1000} sec longer, and Stormkeeper generates $s2 Maelstrom.][Windfury Weapon damage increased by $s3%.

When Crash Lightning hits a single enemy, it activates Windfury Weapon.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94892` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Power of the Maelstrom
- Node ID: `80996`
- Entry ID: `101869`
- Definition ID: `106823`
- Spell ID: `191861`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Chain Lightning and Lightning Bolt have a $s1% chance to cause your next Lava Burst deal $191877s1% extra damage, stacking up to $191877U times.
- Effect: Chain Lightning and Lightning Bolt have a $s1% chance to cause your next Lava Burst deal $191877s1% extra damage, stacking up to $191877U times.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `103638` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chaining Storms
- Node ID: `109192`
- Entry ID: `135254`
- Definition ID: `140022`
- Spell ID: `334308`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Chain Lightning now jumps to $s2 additional targets and deals $s1% increased damage.
- Effect: Chain Lightning now jumps to $s2 additional targets and deals $s1% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80960` (type `2`), node `80967` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Converging Storms
- Node ID: `80973`
- Entry ID: `101839`
- Definition ID: `106878`
- Spell ID: `384363`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each target hit by Crash Lightning increases the damage of your next Stormstrike by $198300s1%, up to a maximum of $198300u stacks.
- Effect: Each target hit by Crash Lightning increases the damage of your next Stormstrike by $198300s1%, up to a maximum of $198300u stacks.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80967` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthshatter
- Node ID: `80995`
- Entry ID: `101867`
- Definition ID: `106821`
- Spell ID: `468626`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases Earth Shock and Earthquake damage by $s1% and the stat bonuses granted by Elemental Blast by $s2%.
- Effect: Increases Earth Shock and Earthquake damage by $s1% and the stat bonuses granted by Elemental Blast by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `103631` (type `2`), node `103635` (type `2`), node `103638` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deluge
- Node ID: `81037`
- Entry ID: `101919`
- Definition ID: `106907`
- Spell ID: `200076`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing Wave and Chain Heal heal for an additional $s1% on targets affected by your Healing Rain or Riptide.
- Effect: Healing Wave and Chain Heal heal for an additional $s1% on targets affected by your Healing Rain or Riptide.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `92675` (type `2`), node `109301` (type `2`), node `110084` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Infusion
- Node ID: `103636`
- Entry ID: `127918`
- Definition ID: `132727`
- Spell ID: `1258889`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spellicon1258895 $@spellname1258895
All elemental damage is increased by an additional $s3%.

$@spellicon462757 $@spellname462757
Increases the chance for Thunderstrikes to occur by $s2% and increases Thunderstrike damage by $s1%.
- Effect: $@spellicon1258895 $@spellname1258895
All elemental damage is increased by an additional $s3%.

$@spellicon462757 $@spellname462757
Increases the chance for Thunderstrikes to occur by $s2% and increases Thunderstrike damage by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `103631` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormflurry
- Node ID: `103871`
- Entry ID: `128270`
- Definition ID: `133077`
- Spell ID: `344357`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stormstrike has a $s1% chance to strike the target an additional time for $s2% of normal damage. This effect can chain off of itself.
- Effect: Stormstrike has a $s1% chance to strike the target an additional time for $s2% of normal damage. This effect can chain off of itself.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80961` (type `2`), node `80967` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echo Chamber
- Node ID: `81015`
- Entry ID: `101892`
- Definition ID: `106824`
- Spell ID: `382032`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the damage dealt by your Elemental Overloads by $s1%.
- Effect: Increases the damage dealt by your Elemental Overloads by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `103631` (type `2`), node `103633` (type `2`), node `110066` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormbind
- Node ID: `109191`
- Entry ID: `135253`
- Definition ID: `140021`
- Spell ID: `1251069`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strikes of your Nature abilities reduce the target's movement speed by $1251059s1% for $1251059d.
- Effect: Critical strikes of your Nature abilities reduce the target's movement speed by $1251059s1% for $1251059d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthen Accord
- Node ID: `110083`
- Entry ID: `136582`
- Definition ID: `141355`
- Spell ID: `1271104`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash Life heals for $s1% more and its bonus healing effect is increased by $s2%.
- Effect: Unleash Life heals for $s1% more and its bonus healing effect is increased by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `92675` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Weapons
- Node ID: `80953`
- Entry ID: `101818`
- Definition ID: `106868`
- Spell ID: `384355`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each active weapon imbue increases all Fire, Frost, and Nature damage dealt by ${$s1/10}.1%.
- Effect: Each active weapon imbue increases all Fire, Frost, and Nature damage dealt by ${$s1/10}.1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80954` (type `2`), node `80961` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tidal Waves
- Node ID: `81044`
- Entry ID: `101928`
- Definition ID: `106941`
- Spell ID: `51564`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Riptide grants $s1 $Lstack:stacks; of Tidal Waves. Tidal Waves reduces the cast time of your next Healing Wave or Chain Heal by $53390s1%.

Can accumulate up to $53390U stacks.
- Effect: Casting Riptide grants $s1 $Lstack:stacks; of Tidal Waves. Tidal Waves reduces the cast time of your next Healing Wave or Chain Heal by $53390s1%.

Can accumulate up to $53390U stacks.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81049` (type `2`), node `92675` (type `2`), node `103432` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Everlasting Elements
- Node ID: `103634`
- Entry ID: `127916`
- Definition ID: `132725`
- Spell ID: `462867`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the duration of your Elementals by $s1%.
- Effect: Increases the duration of your Elementals by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `103633` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthen Rage
- Node ID: `81010`
- Entry ID: `101887`
- Definition ID: `106854`
- Spell ID: `170374`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your damaging spells incite the earth around you to come to your aid for $170377d, repeatedly dealing $170379s1 Nature damage to your most recently attacked target.
- Effect: Your damaging spells incite the earth around you to come to your aid for $170377d, repeatedly dealing $170379s1 Nature damage to your most recently attacked target.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `81005` (type `2`), node `103633` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Improved Earthliving Weapon
- Node ID: `81050`
- Entry ID: `101936`
- Definition ID: `106938`
- Spell ID: `382315`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Earthliving receives $s1% additional benefit from Mastery: Deep Healing.

Healing Wave always triggers Earthliving on its target.
- Effect: Earthliving receives $s1% additional benefit from Mastery: Deep Healing.

Healing Wave always triggers Earthliving on its target.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81049` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fire Nova
- Node ID: `109909`
- Entry ID: `136176`
- Definition ID: `140949`
- Spell ID: `1260666`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Voltaic Blaze generates $s1 additional Maelstrom Weapon and has a $s2% chance to cause a Fire Nova.

$@spellicon333974$@spellname333974
$@spelldesc333974
- Effect: Voltaic Blaze generates $s1 additional Maelstrom Weapon and has a $s2% chance to cause a Fire Nova.

$@spellicon333974$@spellname333974
$@spelldesc333974
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lashing Flames
- Node ID: `80948`
- Entry ID: `101812`
- Definition ID: `106896`
- Spell ID: `334046`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lava Lash and Sundering increases the damage of Flame Shock on its target by $334168s1% for $334168d.
- Effect: Lava Lash and Sundering increases the damage of Flame Shock on its target by $334168s1% for $334168d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `80945` (type `2`), node `80954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Reach
- Node ID: `81031`
- Entry ID: `101911`
- Definition ID: `106944`
- Spell ID: `382732`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Chain Heal bounces an additional time and its healing is increased by $s2%.
- Effect: Chain Heal bounces an additional time and its healing is increased by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81046` (type `2`), node `81049` (type `2`), node `103427` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flow of the Tides
- Node ID: `81031`
- Entry ID: `101910`
- Definition ID: `106943`
- Spell ID: `382039`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Chain Heal bounces an additional time and casting Chain Heal on a target affected by Riptide consumes Riptide, increasing the healing of your Chain Heal by $s1%.
- Effect: Chain Heal bounces an additional time and casting Chain Heal on a target affected by Riptide consumes Riptide, increasing the healing of your Chain Heal by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8`
- Incoming edges: node `81046` (type `2`), node `81049` (type `2`), node `103427` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lava Flows
- Node ID: `110186`
- Entry ID: `136713`
- Definition ID: `141485`
- Spell ID: `1273485`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lava Burst damage increased by $s1%.

Lava Burst and Lava Burst Overload generate $s2 additional Maelstrom.
- Effect: Lava Burst damage increased by $s1%.

Lava Burst and Lava Burst Overload generate $s2 additional Maelstrom.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `1`
- Incoming edges: node `81005` (type `2`), node `103630` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spiritwalker's Grace
- Node ID: `103584`
- Entry ID: `127857`
- Definition ID: `132666`
- Spell ID: `79206`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Calls upon the guidance of the spirits for $d, permitting movement while casting Shaman spells. Castable while casting.$?a192088[ Increases movement speed by $192088s2%.][]
- Effect: Calls upon the guidance of the spirits for $d, permitting movement while casting Shaman spells. Castable while casting.$?a192088[ Increases movement speed by $192088s2%.][]
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103594` (type `2`), node `103624` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Projection
- Node ID: `109386`
- Entry ID: `135590`
- Definition ID: `140346`
- Spell ID: `108287`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Relocates your active totems to the specified location.
- Effect: Relocates your active totems to the specified location.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103617` (type `2`), node `103624` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Warding
- Node ID: `103586`
- Entry ID: `127859`
- Definition ID: `132668`
- Spell ID: `381650`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces all magic damage taken by $s1%.
- Effect: Reduces all magic damage taken by $s1%.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103607` (type `2`), node `103617` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Focus
- Node ID: `103625`
- Entry ID: `127906`
- Definition ID: `132715`
- Spell ID: `382201`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the radius of your totem effects by $s3%.

Increases the duration of your Earthbind and Earthgrab Totems by ${$s1/1000} sec.

Increases the duration of your $?s157153[Cloudburst][Healing Stream], Tremor, Poison Cleansing, $?s137039[Ancestral Protection, Earthen Wall, ][]and Wind Rush Totems by ${$s2/1000}.1 sec.
- Effect: Increases the radius of your totem effects by $s3%.

Increases the duration of your Earthbind and Earthgrab Totems by ${$s1/1000} sec.

Increases the duration of your $?s157153[Cloudburst][Healing Stream], Tremor, Poison Cleansing, $?s137039[Ancestral Protection, Earthen Wall, ][]and Wind Rush Totems by ${$s2/1000}.1 sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103607` (type `2`), node `103612` (type `2`), node `103623` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Swell
- Node ID: `94873`
- Entry ID: `117470`
- Definition ID: `122482`
- Spell ID: `455088`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tempest grants ${$455089s1*$mas}% Mastery for $455089d.
- Effect: Tempest grants ${$455089s1*$mas}% Mastery for $455089d.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94886` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Supercharge
- Node ID: `94873`
- Entry ID: `128225`
- Definition ID: `133032`
- Spell ID: `455110`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?s137040[Lightning Bolt, Tempest, and Chain Lightning Elemental Overloads deal $s1% additional damage.][Lightning Bolt, Tempest, and Chain Lightning have a $s2% chance to refund $s3 Maelstrom Weapon stacks.]
- Effect: $?s137040[Lightning Bolt, Tempest, and Chain Lightning Elemental Overloads deal $s1% additional damage.][Lightning Bolt, Tempest, and Chain Lightning have a $s2% chance to refund $s3 Maelstrom Weapon stacks.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94886` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Arc Discharge
- Node ID: `94885`
- Entry ID: `117482`
- Definition ID: `122494`
- Spell ID: `455096`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Casting Tempest grants a charge of Stormkeeper.][Tempest causes your next Chain Lightning to be instant cast, deal $455097s2% increased damage, and cast an additional time.

Can accumulate up to $470532U charges.]
- Effect: $?s137040[Casting Tempest grants a charge of Stormkeeper.][Tempest causes your next Chain Lightning to be instant cast, deal $455097s2% increased damage, and cast an additional time.

Can accumulate up to $470532U charges.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94893` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Rolling Thunder
- Node ID: `94889`
- Entry ID: `117486`
- Definition ID: `122498`
- Spell ID: `454026`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Reduces the cooldown of Stormkeeper by ${$s1/-1000} sec.][Doom Winds summons a Nature Feral Spirit for ${$s2/1000} sec.

$@spellicon469314$@spellname469314
An Elemental Spirit infused with Nature magic, granting the summoner with $224125s1% increased Nature damage and $224125s3% Physical damage for ${$s2/1000} sec.]
- Effect: $?s137040[Reduces the cooldown of Stormkeeper by ${$s1/-1000} sec.][Doom Winds summons a Nature Feral Spirit for ${$s2/1000} sec.

$@spellicon469314$@spellname469314
An Elemental Spirit infused with Nature magic, granting the summoner with $224125s1% increased Nature damage and $224125s3% Physical damage for ${$s2/1000} sec.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94863` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Natural Gift
- Node ID: `109728`
- Entry ID: `135986`
- Definition ID: `140741`
- Spell ID: `1264691`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Nature damage is increased by $s1%
- Effect: Nature damage is increased by $s1%
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109729` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fusion of Elements
- Node ID: `80993`
- Entry ID: `101865`
- Definition ID: `106841`
- Spell ID: `462840`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming Power of the Maelstrom additionally fires an Elemental Blast at your target at $s1% effectiveness.
- Effect: Consuming Power of the Maelstrom additionally fires an Elemental Blast at your target at $s1% effectiveness.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80996` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ride the Lightning
- Node ID: `80962`
- Entry ID: `101827`
- Definition ID: `106860`
- Spell ID: `289874`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stormstrike and Lava Lash unleash a Chain Lightning at $s2% effectiveness that deals $s1% reduced damage with each jump.
- Effect: Stormstrike and Lava Lash unleash a Chain Lightning at $s2% effectiveness that deals $s1% reduced damage with each jump.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80973` (type `2`), node `103871` (type `2`), node `109192` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Downpour
- Node ID: `103436`
- Entry ID: `127682`
- Definition ID: `132491`
- Spell ID: `462486`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting $?a455630[Surging Totem][Healing Rain] grants a use of Downpour for $462488d.

$@spellicon207778 $@spellname207778
$@spelldesc207778
- Effect: Casting $?a455630[Surging Totem][Healing Rain] grants a use of Downpour for $462488d.

$@spellicon207778 $@spellname207778
$@spelldesc207778
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81037` (type `2`), node `109301` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Eye of the Storm
- Node ID: `81003`
- Entry ID: `101877`
- Definition ID: `106827`
- Spell ID: `381708`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Reduces the Maelstrom cost of Earth Shock and Earthquake by $s1.

Reduces the Maelstrom cost of Elemental Blast by $s3.
- Effect: Reduces the Maelstrom cost of Earth Shock and Earthquake by $s1.

Reduces the Maelstrom cost of Elemental Blast by $s3.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80995` (type `2`), node `81015` (type `2`), node `103636` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Doom Winds
- Node ID: `80959`
- Entry ID: `101824`
- Definition ID: `106859`
- Spell ID: `384352`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Unleash a devastating storm around yourself, dealing $469270s1 Stormstrike damage every $466772s5 sec to nearby enemies for $466772d.

Increases your chance to activate Windfury Weapon by $466772s1%, and the damage of Windfury Weapon by $466772s2%.
- Effect: Unleash a devastating storm around yourself, dealing $469270s1 Stormstrike damage every $466772s5 sec to nearby enemies for $466772d.

Increases your chance to activate Windfury Weapon by $466772s1%, and the damage of Windfury Weapon by $466772s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80953` (type `2`), node `103871` (type `2`), node `109191` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ascendance
- Node ID: `80989`
- Entry ID: `101860`
- Definition ID: `106820`
- Spell ID: `114050`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $@spelldesc1219480
- Effect: $@spelldesc1219480
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81015` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Echo of the Elements
- Node ID: `81055`
- Entry ID: `101942`
- Definition ID: `106939`
- Spell ID: `333919`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137039[Riptide and Lava Burst have][Lava Burst has] an additional charge.
- Effect: $?s137039[Riptide and Lava Burst have][Lava Burst has] an additional charge.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81037` (type `2`), node `81044` (type `2`), node `110083` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Inferno Arc
- Node ID: `81008`
- Entry ID: `101885`
- Definition ID: `106852`
- Spell ID: `1259047`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Lightning Bolt, $?a454009[Tempest, ][]Chain Lightning, Earth Shock, Elemental Blast, and Earthquake deal $s1% increased damage to targets affected by Flame Shock.
- Effect: Lightning Bolt, $?a454009[Tempest, ][]Chain Lightning, Earth Shock, Elemental Blast, and Earthquake deal $s1% increased damage to targets affected by Flame Shock.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81010` (type `2`), node `81015` (type `2`), node `103634` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Sundering
- Node ID: `80975`
- Entry ID: `101841`
- Definition ID: `106874`
- Spell ID: `197214`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Shatters a line of earth in front of you with your main hand weapon, causing $s1 Flamestrike damage to any enemy hit.
- Effect: Shatters a line of earth in front of you with your main hand weapon, causing $s1 Flamestrike damage to any enemy hit.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80948` (type `2`), node `80953` (type `2`), node `109909` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spirit Link Totem
- Node ID: `81041`
- Entry ID: `101924`
- Definition ID: `106915`
- Spell ID: `98008`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summons a totem at the target location for $d, which reduces damage taken by all party and raid members within $98007a1 yards by $98007s1%. Immediately and every $98017t1 sec, the health of all affected players is redistributed evenly.
- Effect: Summons a totem at the target location for $d, which reduces damage taken by all party and raid members within $98007a1 yards by $98007s1%. Immediately and every $98017t1 sec, the health of all affected players is redistributed evenly.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81031` (type `2`), node `81044` (type `2`), node `81050` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Flames of the Firelord
- Node ID: `103641`
- Entry ID: `127922`
- Definition ID: `132731`
- Spell ID: `381784`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Flame Shock damage increased by $s1%.
- Effect: Flame Shock damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81010` (type `2`), node `110186` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Earthen Harmony
- Node ID: `103430`
- Entry ID: `127674`
- Definition ID: `132483`
- Spell ID: `382020`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Earth Shield reduces damage taken by $s3% and its healing is increased by up to $s1% as its target's health decreases. Maximum benefit is reached below $s2% health.
- Effect: Earth Shield reduces damage taken by $s3% and its healing is increased by up to $s1% as its target's health decreases. Maximum benefit is reached below $s2% health.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81031` (type `2`), node `81046` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Graceful Spirit
- Node ID: `103626`
- Entry ID: `127908`
- Definition ID: `132717`
- Spell ID: `192088`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of Spiritwalker's Grace by ${$m1/-1000} sec and increases your movement speed by $s2% while it is active.
- Effect: Reduces the cooldown of Spiritwalker's Grace by ${$m1/-1000} sec and increases your movement speed by $s2% while it is active.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103584` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spiritwalker's Aegis
- Node ID: `103626`
- Entry ID: `127907`
- Definition ID: `132716`
- Spell ID: `378077`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When you cast Spiritwalker's Grace, you become immune to Silence and Interrupt effects for $378078d.
- Effect: When you cast Spiritwalker's Grace, you become immune to Silence and Interrupt effects for $378078d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103584` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mana Spring
- Node ID: `103587`
- Entry ID: `127860`
- Definition ID: `132669`
- Spell ID: `381930`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your $?!s137041[Lava Burst][]$?s137039[ and Riptide][]$?s137041[Stormstrike][] casts restore $?a137040[$381931s1]?a137041[$404550s1][$404551s1] mana to you and $s1 allies nearest to you within $395192a1 yards.

Allies can only benefit from one Shaman's Mana Spring effect at a time, prioritizing healers.
- Effect: Your $?!s137041[Lava Burst][]$?s137039[ and Riptide][]$?s137041[Stormstrike][] casts restore $?a137040[$381931s1]?a137041[$404550s1][$404551s1] mana to you and $s1 allies nearest to you within $395192a1 yards.

Allies can only benefit from one Shaman's Mana Spring effect at a time, prioritizing healers.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103586` (type `2`), node `109386` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tremor Totem
- Node ID: `103599`
- Entry ID: `127874`
- Definition ID: `132683`
- Spell ID: `8143`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Summons a totem at your feet that shakes the ground around it for $d, removing Fear, Charm and Sleep effects from party and raid members within $8146a1 yards.
- Effect: Summons a totem at your feet that shakes the ground around it for $d, removing Fear, Charm and Sleep effects from party and raid members within $8146a1 yards.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103586` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Poison Cleansing Totem
- Node ID: `103599`
- Entry ID: `136567`
- Definition ID: `141340`
- Spell ID: `383013`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Summons a totem at your feet that removes all Poison effects from a nearby party or raid member within $403922a yards every $383014t1 sec for $d.
- Effect: Summons a totem at your feet that removes all Poison effects from a nearby party or raid member within $403922a yards every $383014t1 sec for $d.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103586` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Therazane's Resilience
- Node ID: `103593`
- Entry ID: `127868`
- Definition ID: `132677`
- Spell ID: `1217622`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Earth Shield $?c3[and Water Shield no longer lose charges and are][no longer loses charges and is] ${100+$s1}% effective.
- Effect: Earth Shield $?c3[and Water Shield no longer lose charges and are][no longer loses charges and is] ${100+$s1}% effective.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103586` (type `2`), node `103625` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reactive Warding
- Node ID: `103593`
- Entry ID: `136584`
- Definition ID: `141357`
- Spell ID: `462454`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: When refreshing Earth Shield, your target is healed for $462477s1 for each stack of Earth Shield they are missing.$?c3[

When refreshing Water Shield, you are refunded $462479s1 mana for each stack of Water Shield missing.][]

Additionally, Earth Shield$?c3[ and Water Shield][] can consume charges ${$s2/-1000}.1 sec faster.
- Effect: When refreshing Earth Shield, your target is healed for $462477s1 for each stack of Earth Shield they are missing.$?c3[

When refreshing Water Shield, you are refunded $462479s1 mana for each stack of Water Shield missing.][]

Additionally, Earth Shield$?c3[ and Water Shield][] can consume charges ${$s2/-1000}.1 sec faster.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103586` (type `2`), node `103625` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voodoo Mastery
- Node ID: `103600`
- Entry ID: `127875`
- Definition ID: `132684`
- Spell ID: `204268`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your Hex target is slowed by $378080s1% during Hex and for $378080d after it ends.

Reduces the cooldown of Hex by ${($m1/1000)*-1} sec.
- Effect: Your Hex target is slowed by $378080s1% during Hex and for $378080d after it ends.

Reduces the cooldown of Hex by ${($m1/1000)*-1} sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103623` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voltaic Surge
- Node ID: `94870`
- Entry ID: `117467`
- Definition ID: `122479`
- Spell ID: `454919`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Earthquake][Crash Lightning] and Chain Lightning damage increased by $s1%.
- Effect: $?s137040[Earthquake][Crash Lightning] and Chain Lightning damage increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94873` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Conductive Energy
- Node ID: `94868`
- Entry ID: `117465`
- Definition ID: `122477`
- Spell ID: `455123`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s137040[Lightning Rod targets now also take $s2% of the damage that Tempest deals, and Tempest also applies Lightning Rod effect.][Gain the effects of the Lightning Rod talent:

$@spellicon210689 $@spellname210689
$@spelldesc210689]
- Effect: $?s137040[Lightning Rod targets now also take $s2% of the damage that Tempest deals, and Tempest also applies Lightning Rod effect.][Gain the effects of the Lightning Rod talent:

$@spellicon210689 $@spellname210689
$@spelldesc210689]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94885` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nature's Protection
- Node ID: `94880`
- Entry ID: `117477`
- Definition ID: `122489`
- Spell ID: `454027`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lightning Shield reduces the damage you take by $s1%.
- Effect: Lightning Shield reduces the damage you take by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94889` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Surging Currents
- Node ID: `94880`
- Entry ID: `125617`
- Definition ID: `130449`
- Spell ID: `454372`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Casting Tempest grants Surging Currents, increasing the effectiveness of your next Chain Heal or Healing Surge by $454376s1%, up to ${$454376s1*$454376u}%.
- Effect: Casting Tempest grants Surging Currents, increasing the effectiveness of your next Chain Heal or Healing Surge by $454376s1%, up to ${$454376s1*$454376u}%.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94889` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Descending Skies
- Node ID: `109727`
- Entry ID: `135985`
- Definition ID: `140740`
- Spell ID: `1264688`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Casting ][]Ascendance upgrades your next Lightning Bolt to Tempest.
- Effect: $?c1[Casting ][]Ascendance upgrades your next Lightning Bolt to Tempest.
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109728` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightning Strikes
- Node ID: `109193`
- Entry ID: `135255`
- Definition ID: `140023`
- Spell ID: `384450`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming $s2 stacks of Maelstrom Weapon increases the damage of your next Stormstrike or Lava Lash by $384451s1% and causes them to generate a stack of Maelstrom Weapon.
- Effect: Consuming $s2 stacks of Maelstrom Weapon increases the damage of your next Stormstrike or Lava Lash by $384451s1% and causes them to generate a stack of Maelstrom Weapon.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80962` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lightning Rod
- Node ID: `81012`
- Entry ID: `101889`
- Definition ID: `106838`
- Spell ID: `210689`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s454009[Tempest, ][]$?s137040[Earth Shock, Elemental Blast, and Earthquake][Lightning Bolt and Chain Lightning] make your target a Lightning Rod for $197209d.
 
Lightning Rods take $s2% of all damage you deal with $?s454009[Tempest, Lightning Bolt,][Lightning Bolt] and Chain Lightning.
- Effect: $?s454009[Tempest, ][]$?s137040[Earth Shock, Elemental Blast, and Earthquake][Lightning Bolt and Chain Lightning] make your target a Lightning Rod for $197209d.
 
Lightning Rods take $s2% of all damage you deal with $?s454009[Tempest, Lightning Bolt,][Lightning Bolt] and Chain Lightning.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80993` (type `2`), node `81003` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Water Expulsion
- Node ID: `103434`
- Entry ID: `127680`
- Definition ID: `132489`
- Spell ID: `1253014`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases Downpour healing by $s1%.
- Effect: Increases Downpour healing by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `103436` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Elemental Assault
- Node ID: `80951`
- Entry ID: `101815`
- Definition ID: `106893`
- Spell ID: `210853`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Stormstrike damage is increased by $s1%, and Stormstrike and Lava Lash have a $m3% chance to generate $m2 $Lstack:stacks; of Maelstrom Weapon.
- Effect: Stormstrike damage is increased by $s1%, and Stormstrike and Lava Lash have a $m3% chance to generate $m2 $Lstack:stacks; of Maelstrom Weapon.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80959` (type `2`), node `80962` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mountains Will Fall
- Node ID: `81002`
- Entry ID: `101876`
- Definition ID: `106826`
- Spell ID: `381726`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Earth Shock, Elemental Blast, and Earthquake can trigger your Mastery: Elemental Overload at $s1% effectiveness.

Overloaded Earthquakes do not knock enemies down.
- Effect: Earth Shock, Elemental Blast, and Earthquake can trigger your Mastery: Elemental Overload at $s1% effectiveness.

Overloaded Earthquakes do not knock enemies down.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80989` (type `2`), node `81003` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ancestral Awakening
- Node ID: `81043`
- Entry ID: `101927`
- Definition ID: `106914`
- Spell ID: `382309`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: When you heal with your Healing Wave or Riptide you have a $s2% chance to summon an Ancestral spirit to aid you, instantly healing an injured friendly party or raid target within 40 yards for $s1% of the amount healed. Critical strikes increase this chance to $s3%.
- Effect: When you heal with your Healing Wave or Riptide you have a $s2% chance to summon an Ancestral spirit to aid you, instantly healing an injured friendly party or raid target within 40 yards for $s1% of the amount healed. Critical strikes increase this chance to $s3%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81055` (type `2`), node `103436` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `78406`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Static Accumulation
- Node ID: `80950`
- Entry ID: `101814`
- Definition ID: `106881`
- Spell ID: `384411`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: During Doom Winds or Ascendance, you generate $s1 Maelstrom Weapon $lstack:stacks; every $384437t1 sec.
- Effect: During Doom Winds or Ascendance, you generate $s1 Maelstrom Weapon $lstack:stacks; every $384437t1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80959` (type `2`)
- Effect-point records: index `1`, operation `0`, curve `90581`, index `0`, operation `0`, curve `90582`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Call of Fire
- Node ID: `80992`
- Entry ID: `101864`
- Definition ID: `106846`
- Spell ID: `378255`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Ascendance summons a $?a117013[Primal][Greater] Fire Elemental to rain destruction on your enemies for $188592d. 

While the Fire Elemental is active, Flame Shock deals damage ${100*(1/(1+$188592s2/100)-1)}% faster, and newly applied Flame Shocks last $188592s3% longer.
- Effect: Ascendance summons a $?a117013[Primal][Greater] Fire Elemental to rain destruction on your enemies for $188592d. 

While the Fire Elemental is active, Flame Shock deals damage ${100*(1/(1+$188592s2/100)-1)}% faster, and newly applied Flame Shocks last $188592s3% longer.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80989` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Tidewaters
- Node ID: `103433`
- Entry ID: `127679`
- Definition ID: `132488`
- Spell ID: `462424`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: When you cast $?a455630[Surging Totem][Healing Rain], each ally with your Riptide on them is healed for $462425s1.
- Effect: When you cast $?a455630[Surging Totem][Healing Rain], each ally with your Riptide on them is healed for $462425s1.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81055` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Undercurrent
- Node ID: `81052`
- Entry ID: `101939`
- Definition ID: `106935`
- Spell ID: `382194`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: For each Riptide active on an ally, your heals are ${$s2/10}.1% more effective.
- Effect: For each Riptide active on an ally, your heals are ${$s2/10}.1% more effective.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81041` (type `2`), node `81055` (type `2`)
- Effect-point records: index `1`, operation `0`, curve `58612`, index `0`, operation `0`, curve `58611`, index `2`, operation `0`, curve `60403`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Feral Spirit
- Node ID: `109194`
- Entry ID: `128236`
- Definition ID: `133043`
- Spell ID: `469314`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Sundering summons $s1 Fire Feral $lSpirit:Spirits; and Doom Winds summons $s2 Nature Feral $lSpirit:Spirits; by your side for $469322d.

$@spellicon469314$@spellname469314
An Elemental Spirit $?s147783[Raptor][Wolf] infused with Fire or Nature magic, granting the summoner with $224125s1% increased Fire or Nature damage and $224125s3% Physical damage for $469322d.
- Effect: Casting Sundering summons $s1 Fire Feral $lSpirit:Spirits; and Doom Winds summons $s2 Nature Feral $lSpirit:Spirits; by your side for $469322d.

$@spellicon469314$@spellname469314
An Elemental Spirit $?s147783[Raptor][Wolf] infused with Fire or Nature magic, granting the summoner with $224125s1% increased Fire or Nature damage and $224125s3% Physical damage for $469322d.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80959` (type `2`), node `80975` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Voltaic Blaze
- Node ID: `81007`
- Entry ID: `101883`
- Definition ID: `106850`
- Spell ID: `470057`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Instantly shocks the target and $s4 enemies within $A1 yds with blazing thunder, applying Flame Shock and dealing $1259101s1 Nature damage. Always critically strikes.$?a343725[

|cFFFFFFFFGenerates $343725s14 Maelstrom.|r][

Generates $s2 $Lstack:stacks; of Maelstrom Weapon.]
- Effect: Instantly shocks the target and $s4 enemies within $A1 yds with blazing thunder, applying Flame Shock and dealing $1259101s1 Nature damage. Always critically strikes.$?a343725[

|cFFFFFFFFGenerates $343725s14 Maelstrom.|r][

Generates $s2 $Lstack:stacks; of Maelstrom Weapon.]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81008` (type `2`), node `103641` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Spouting Spirits
- Node ID: `103915`
- Entry ID: `128332`
- Definition ID: `133139`
- Spell ID: `462383`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Spirit Link Totem reduces damage taken by an additional $s1%, and it restores $462384s1 health to all nearby allies $m2 $Lsecond:seconds; after it is dropped. Healing reduced beyond $s3 targets.
- Effect: Spirit Link Totem reduces damage taken by an additional $s1%, and it restores $462384s1 health to all nearby allies $m2 $Lsecond:seconds; after it is dropped. Healing reduced beyond $s3 targets.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81041` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Surging Elements
- Node ID: `80964`
- Entry ID: `101829`
- Definition ID: `106884`
- Spell ID: `382042`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Casting Sundering grants you $s1% Haste for $382043d, and generates $s3 stacks of Maelstrom Weapon.
- Effect: Casting Sundering grants you $s1% Haste for $382043d, and generates $s3 stacks of Maelstrom Weapon.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80975` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Swelling Tides
- Node ID: `113376`
- Entry ID: `140663`
- Definition ID: `145345`
- Spell ID: `1312843`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Healing Stream Totem $?a1267016[and Stormstream Totem ][]extend$?a1267016[][s] the duration of your active Riptides by ${$m1/1000}.1 sec.
- Effect: Healing Stream Totem $?a1267016[and Stormstream Totem ][]extend$?a1267016[][s] the duration of your active Riptides by ${$m1/1000}.1 sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81041` (type `2`), node `103430` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nature's Swiftness
- Node ID: `103620`
- Entry ID: `127899`
- Definition ID: `132708`
- Spell ID: `378081`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Your next healing or damaging Nature spell $?a1246131[or Hex ][]is instant cast and costs no mana.
- Effect: Your next healing or damaging Nature spell $?a1246131[or Hex ][]is instant cast and costs no mana.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103587` (type `2`), node `103626` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Totemic Surge
- Node ID: `109388`
- Entry ID: `135592`
- Definition ID: `140348`
- Spell ID: `381867`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Reduces the cooldown of most totems by ${$s1/-1000} sec.
- Effect: Reduces the cooldown of most totems by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103587` (type `2`), node `103593` (type `2`), node `103599` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Instinctive Imbuements
- Node ID: `109387`
- Entry ID: `135591`
- Definition ID: `140347`
- Spell ID: `1270350`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c3[Water][Lightning] Shield increases your $?c2[Agility][Intellect] by $s1%.

Casting $?c3[Water][Lightning] Shield now applies your weapon imbuements. Earth Shield is also applied if you have the Elemental Orbit talent.
- Effect: $?c3[Water][Lightning] Shield increases your $?c2[Agility][Intellect] by $s1%.

Casting $?c3[Water][Lightning] Shield now applies your weapon imbuements. Earth Shield is also applied if you have the Elemental Orbit talent.
- Point cost per purchased rank: `1` × Specialization pool (Elemental, Enhancement, Restoration) (ID `2801`; group)
- Source gates: source `group`; type `0`; currency `2801` spend gate `23` | source `group`; type `0`; currency `2801` spend gate `8`
- Incoming edges: node `103593` (type `2`), node `103600` (type `2`), node `103625` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Awakening Storms
- Node ID: `94867`
- Entry ID: `117464`
- Definition ID: `122476`
- Spell ID: `455129`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137040[Each Maelstrom spent has an additional ${$s3/100}.2% chance to upgrade your next Lightning Bolt to Tempest.][Stormstrike has a small chance to upgrade your next Lightning Bolt to Tempest.]
- Effect: $?a137040[Each Maelstrom spent has an additional ${$s3/100}.2% chance to upgrade your next Lightning Bolt to Tempest.][Stormstrike has a small chance to upgrade your next Lightning Bolt to Tempest.]
- Point cost per purchased rank: `1` × Hero pool (Stormbringer) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94868` (type `2`), node `94870` (type `2`), node `94880` (type `2`), node `109727` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Charged Conduit
- Node ID: `80991`
- Entry ID: `101862`
- Definition ID: `106844`
- Spell ID: `468625`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Increases the duration of Lightning Rod by ${$s1/1000} sec and its damage bonus by $s2%.
- Effect: Increases the duration of Lightning Rod by ${$s1/1000} sec and its damage bonus by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81012` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thunder Capacitor
- Node ID: `109190`
- Entry ID: `135252`
- Definition ID: `140020`
- Spell ID: `1262635`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Lightning Bolt and Chain Lightning deal $s1% increased damage and have a $s2% chance to refund the Maelstrom Weapon spent.
- Effect: Lightning Bolt and Chain Lightning deal $s1% increased damage and have a $s2% chance to refund the Maelstrom Weapon spent.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `109193` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Double Dip
- Node ID: `104124`
- Entry ID: `128703`
- Definition ID: `133505`
- Spell ID: `1252882`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a455630[Surging Totem][Healing Rain] grants an additional use of Downpour.
- Effect: $?a455630[Surging Totem][Healing Rain] grants an additional use of Downpour.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `103434` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deeply Rooted Elements
- Node ID: `92219`
- Entry ID: `101816`
- Definition ID: `106894`
- Spell ID: `378270`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?a137039[Casting Riptide]?a137040[Each Maelstrom spent][Each stack of Maelstrom Weapon consumed] has a $?a137039[$s4]?a137040[${$s2/100}.2][${$s3/10}.1]% chance to activate Ascendance for ${$m1/1000}.1 sec.

$?a137039[$@spellicon114052 $@spellname114052
$@spelldesc114052]?a137040[$@spellicon114050 $@spellname114050
$@spelldesc114050][$@spellicon114051 $@spellname114051
Transform into an Air Ascendant for $114051d and unleash Doom Winds, reducing the cooldown and cost of Stormstrike by $114051s9%, and transforming your auto attack and Stormstrike into Wind attacks which bypass armor and have a $114089r yd range.]
- Effect: $?a137039[Casting Riptide]?a137040[Each Maelstrom spent][Each stack of Maelstrom Weapon consumed] has a $?a137039[$s4]?a137040[${$s2/100}.2][${$s3/10}.1]% chance to activate Ascendance for ${$m1/1000}.1 sec.

$?a137039[$@spellicon114052 $@spellname114052
$@spelldesc114052]?a137040[$@spellicon114050 $@spellname114050
$@spelldesc114050][$@spellicon114051 $@spellname114051
Transform into an Air Ascendant for $114051d and unleash Doom Winds, reducing the cooldown and cost of Stormstrike by $114051s9%, and transforming your auto attack and Stormstrike into Wind attacks which bypass armor and have a $114089r yd range.]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ascendance
- Node ID: `92219`
- Entry ID: `114291`
- Definition ID: `119296`
- Spell ID: `114051`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Transform into an Air Ascendant for $114051d and unleash Doom Winds, reducing the cooldown and cost of Stormstrike by $114051s9%, and transforming your auto attack and Stormstrike into Wind attacks which bypass armor and have a $114089r yd range.

Maelstrom Weapon spenders have a ${$1252197s1/10}.1% chance to unleash Doom Winds per Maelstrom Weapon spent while Ascendance is not active.
- Effect: Transform into an Air Ascendant for $114051d and unleash Doom Winds, reducing the cooldown and cost of Stormstrike by $114051s9%, and transforming your auto attack and Stormstrike into Wind attacks which bypass armor and have a $114089r yd range.

Maelstrom Weapon spenders have a ${$1252197s1/10}.1% chance to unleash Doom Winds per Maelstrom Weapon spent while Ascendance is not active.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### First Ascendant
- Node ID: `103640`
- Entry ID: `127921`
- Definition ID: `132730`
- Spell ID: `462440`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: The cooldown of Ascendance$?a137039[ and Healing Tide Totem][] is reduced by ${$s1/-1000} sec.
- Effect: The cooldown of Ascendance$?a137039[ and Healing Tide Totem][] is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80992` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Preeminence
- Node ID: `103640`
- Entry ID: `128224`
- Definition ID: `133031`
- Spell ID: `462443`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your haste is increased by $s2% $?a137039 [while Ascendance or Healing Tide Totem is active and their durations are][during Ascendance and its duration is] increased by ${$s1/1000} sec.
- Effect: Your haste is increased by $s2% $?a137039 [while Ascendance or Healing Tide Totem is active and their durations are][during Ascendance and its duration is] increased by ${$s1/1000} sec.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80992` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primal Tide Core
- Node ID: `80976`
- Entry ID: `101842`
- Definition ID: `106901`
- Spell ID: `382045`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Every $s1 casts of Riptide also applies Riptide to another friendly target near your Riptide target.
- Effect: Every $s1 casts of Riptide also applies Riptide to another friendly target near your Riptide target.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81043` (type `2`), node `81052` (type `2`), node `103433` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Thorim's Invocation
- Node ID: `80949`
- Entry ID: `101813`
- Definition ID: `106882`
- Spell ID: `384444`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Doom Winds and Deeply Rooted Elements last ${$s5/1000} sec longer, and the cooldown of Ascendance is reduced by ${$s4/-1000} sec.

During Doom Winds or Ascendance, Stormstrike and Crash Lightning consume up to $s1 Maelstrom Weapon to discharge a Lightning Bolt or Chain Lightning at $s2% effectiveness at your enemy, whichever you most recently used.
- Effect: Doom Winds and Deeply Rooted Elements last ${$s5/1000} sec longer, and the cooldown of Ascendance is reduced by ${$s4/-1000} sec.

During Doom Winds or Ascendance, Stormstrike and Crash Lightning consume up to $s1 Maelstrom Weapon to discharge a Lightning Bolt or Chain Lightning at $s2% effectiveness at your enemy, whichever you most recently used.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primal Elementalist
- Node ID: `80978`
- Entry ID: `101844`
- Definition ID: `106856`
- Spell ID: `117013`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Your Earth, Fire, and Storm Elementals are drawn from primal elementals $s1% more powerful than regular elementals, with additional abilities, and you gain direct control over your Primal Fire Elemental.
- Effect: Your Earth, Fire, and Storm Elementals are drawn from primal elementals $s1% more powerful than regular elementals, with additional abilities, and you gain direct control over your Primal Fire Elemental.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `80992` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Coalescing Water
- Node ID: `81042`
- Entry ID: `101925`
- Definition ID: `106912`
- Spell ID: `470076`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `400`
- Description: Healing Wave and Chain Heal increase the initial healing of your next Riptide by $470077s1%, stacking up to $470077u times.
- Effect: Healing Wave and Chain Heal increase the initial healing of your next Riptide by $470077s1%, stacking up to $470077u times.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `81052` (type `2`), node `103915` (type `2`), node `113376` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Crackling Fury
- Node ID: `103632`
- Entry ID: `127914`
- Definition ID: `132723`
- Spell ID: `1269215`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `100`
- Description: Voltaic Blaze's cooldown is reduced by ${$s1/-1000} sec and its instant damage is increased by $s2%.
- Effect: Voltaic Blaze's cooldown is reduced by ${$s1/-1000} sec and its instant damage is increased by $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81007` (type `2`)
- Effect-point records: index `0`, operation `0`, curve `95164`, index `1`, operation `0`, curve `95163`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primordial Storm
- Node ID: `80963`
- Entry ID: `101828`
- Definition ID: `106883`
- Spell ID: `1218047`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Sundering transforms into a single use Primordial Storm for $1218125d after it is cast.

$@spellicon1218047$@spellname1218047
Devastate nearby enemies with a Primordial Storm dealing $1218113s1 Flamestrike, $1218116s1 Froststrike, $1218118s1 Stormstrike damage, and unleashing a Lightning Bolt or a Chain Lightning at $s2% effectiveness. Deals reduced damage beyond $s3 targets.

|cFFFFFFFFConsumes Maelstrom Weapon for increased damage.|r
- Effect: Sundering transforms into a single use Primordial Storm for $1218125d after it is cast.

$@spellicon1218047$@spellname1218047
Devastate nearby enemies with a Primordial Storm dealing $1218113s1 Flamestrike, $1218116s1 Froststrike, $1218118s1 Stormstrike damage, and unleashing a Lightning Bolt or a Chain Lightning at $s2% effectiveness. Deals reduced damage beyond $s3 targets.

|cFFFFFFFFConsumes Maelstrom Weapon for increased damage.|r
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `80964` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Purging Flames
- Node ID: `103637`
- Entry ID: `101884`
- Definition ID: `106851`
- Spell ID: `1259471`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Voltaic Blaze unleashes volcanic rage, causing your next Lava Burst to also fire at $s3 additional targets with your Flame Shock at $1259491s1% effectiveness with reduced Maelstrom generation.

Lava Burst damage increased by $s1%.
- Effect: Voltaic Blaze unleashes volcanic rage, causing your next Lava Burst to also fire at $s3 additional targets with your Flame Shock at $1259491s1% effectiveness with reduced Maelstrom generation.

Lava Burst damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1`
- Incoming edges: node `81007` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deeply Rooted Elements
- Node ID: `81051`
- Entry ID: `101937`
- Definition ID: `106936`
- Spell ID: `378270`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: $?a137039[Casting Riptide]?a137040[Each Maelstrom spent][Each stack of Maelstrom Weapon consumed] has a $?a137039[$s4]?a137040[${$s2/100}.2][${$s3/10}.1]% chance to activate Ascendance for ${$m1/1000}.1 sec.

$?a137039[$@spellicon114052 $@spellname114052
$@spelldesc114052]?a137040[$@spellicon114050 $@spellname114050
$@spelldesc114050][$@spellicon114051 $@spellname114051
Transform into an Air Ascendant for $114051d and unleash Doom Winds, reducing the cooldown and cost of Stormstrike by $114051s9%, and transforming your auto attack and Stormstrike into Wind attacks which bypass armor and have a $114089r yd range.]
- Effect: $?a137039[Casting Riptide]?a137040[Each Maelstrom spent][Each stack of Maelstrom Weapon consumed] has a $?a137039[$s4]?a137040[${$s2/100}.2][${$s3/10}.1]% chance to activate Ascendance for ${$m1/1000}.1 sec.

$?a137039[$@spellicon114052 $@spellname114052
$@spelldesc114052]?a137040[$@spellicon114050 $@spellname114050
$@spelldesc114050][$@spellicon114051 $@spellname114051
Transform into an Air Ascendant for $114051d and unleash Doom Winds, reducing the cooldown and cost of Stormstrike by $114051s9%, and transforming your auto attack and Stormstrike into Wind attacks which bypass armor and have a $114089r yd range.]
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20`
- Incoming edges: node `103430` (type `2`), node `113376` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Unleashed
- Node ID: `110401`
- Entry ID: `136971`
- Definition ID: `141734`
- Spell ID: `1262713`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Each Maelstrom Weapon spent has a ${$s1/10}% chance to cause your next Crash Lightning to ignore its cooldown. The weapon enhancement effect of Crash Lightning may now overlap.
- Effect: Each Maelstrom Weapon spent has a ${$s1/10}% chance to cause your next Crash Lightning to ignore its cooldown. The weapon enhancement effect of Crash Lightning may now overlap.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Unleashed
- Node ID: `110401`
- Entry ID: `136970`
- Definition ID: `141733`
- Spell ID: `1262761`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `200`
- Description: Maelstrom Weapon spending abilities deal $s1% increased damage. 

Weapon Imbuements deal $s2% increased damage.
- Effect: Maelstrom Weapon spending abilities deal $s1% increased damage. 

Weapon Imbuements deal $s2% increased damage.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Effect-point records: index `0`, operation `0`, curve `98611`, index `1`, operation `0`, curve `98610`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Storm Unleashed
- Node ID: `110401`
- Entry ID: `136969`
- Definition ID: `141732`
- Spell ID: `1252373`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Crash Lightning electrocutes the area struck, dealing $s1% of its damage $s2 additional times over $1252433d, and its weapon enhancement effect now increases auto-attack speed by $s3%.
- Effect: Crash Lightning electrocutes the area struck, dealing $s1% of its damage $s2 additional times over $1252433d, and its weapon enhancement effect now increases auto-attack speed by $s3%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Feedback Loop
- Node ID: `110402`
- Entry ID: `136974`
- Definition ID: `141737`
- Spell ID: `1270061`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Damage of your spells and abilities increased by $s2%. Elemental Overload damage increased by $s1%.
- Effect: Damage of your spells and abilities increased by $s2%. Elemental Overload damage increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Feedback Loop
- Node ID: `110402`
- Entry ID: `136973`
- Definition ID: `141736`
- Spell ID: `1270062`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `400`
- Description: Spell critical strike chance increased by $s1%. Elemental Fury increases spell critical strike damage by an additional $s2%.
- Effect: Spell critical strike chance increased by $s1%. Elemental Fury increases spell critical strike damage by an additional $s2%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Effect-point records: index `1`, operation `1`, curve `98608`, index `0`, operation `1`, curve `98609`, index `2`, operation `1`, curve `106262`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Feedback Loop
- Node ID: `110402`
- Entry ID: `136972`
- Definition ID: `141735`
- Spell ID: `1270064`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `500`
- Description: Elemental Overloads have a $s1% chance to cause an additional Elemental Overload. This effect cannot chain.
- Effect: Elemental Overloads have a $s1% chance to cause an additional Elemental Overload. This effect cannot chain.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `group`; type `1` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormstream Totem
- Node ID: `110403`
- Entry ID: `136977`
- Definition ID: `141740`
- Spell ID: `1267016`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Riptide has a $s1% chance to upgrade your next Healing Stream Totem to Stormstream Totem which heals for $s2% more, heals $s3 additional $Lally:allies; at $s4% effectiveness, and heals $s5 injured allies for $1268684s1 healing when used.
- Effect: Riptide has a $s1% chance to upgrade your next Healing Stream Totem to Stormstream Totem which heals for $s2% more, heals $s3 additional $Lally:allies; at $s4% effectiveness, and heals $s5 injured allies for $1268684s1 healing when used.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormstream Totem
- Node ID: `110403`
- Entry ID: `136976`
- Definition ID: `141739`
- Spell ID: `1267093`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `2`; entry ordinal: `200`
- Description: Healing Stream and Stormstream Totem healing increased by $s1%.
- Effect: Healing Stream and Stormstream Totem healing increased by $s1%.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Effect-point records: index `0`, operation `0`, curve `98612`
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Stormstream Totem
- Node ID: `110403`
- Entry ID: `136975`
- Definition ID: `141738`
- Spell ID: `1267120`
- Tree ID: `786`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `300`
- Description: Casting $?s443454[Ancestral][Nature's] Swiftness grants a use of Stormstream Totem and Stormstream Totem no longer consumes a charge of Healing Stream Totem when used.
- Effect: Casting $?s443454[Ancestral][Nature's] Swiftness grants a use of Stormstream Totem and Stormstream Totem no longer consumes a charge of Healing Stream Totem when used.
- Point cost per purchased rank: `1` × Class pool (ID `2800`; group)
- Source gates: source `group`; type `1` | source `group`; type `0`; currency `2800` spend gate `8` | source `group`; type `0`; currency `2800` spend gate `20` | source `node`; type `5`; minimum level `90`; grants `4` rank(s) | source `node`; type `5`; minimum level `84`; grants `3` rank(s) | source `node`; type `5`; minimum level `81`; grants `1` rank(s) | source `node`; type `0`; minimum level `81`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
