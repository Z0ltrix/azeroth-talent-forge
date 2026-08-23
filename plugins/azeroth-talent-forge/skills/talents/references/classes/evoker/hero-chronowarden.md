# Chronowarden

Reviewed build: `12.1.0.69404`
Hero subtree ID: `38`
Description: Chronowardens can manipulate time, giving them glimpses of the future to speed their attacks or recalling echoes to revisit past actions. Specialization in bronze magic can cause instabilities due to the many future possibilities they constantly see.

## Hero talents

### Chrono Flame
- Node ID: `94954`
- Entry ID: `117551`
- Definition ID: `122563`
- Spell ID: `431442`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Living Flame is enhanced with Bronze magic, repeating $?c2[$s1%][$s3%] of the damage or healing you dealt to the target in the last $s2 sec as Arcane, up to $?s1260647[$<cap2>][$<cap>].
- Effect: Living Flame is enhanced with Bronze magic, repeating $?c2[$s1%][$s3%] of the damage or healing you dealt to the target in the last $s2 sec as Arcane, up to $?s1260647[$<cap2>][$<cap>].
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Warp
- Node ID: `94948`
- Entry ID: `117545`
- Definition ID: `122557`
- Spell ID: `429483`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Hover now causes you to briefly warp out of existence and appear at your destination. Hover's cooldown is also reduced by ${$s1/-1000} sec.

Hover continues to allow Evoker spells to be cast while moving.
- Effect: Hover now causes you to briefly warp out of existence and appear at your destination. Hover's cooldown is also reduced by ${$s1/-1000} sec.

Hover continues to allow Evoker spells to be cast while moving.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Temporal Burst
- Node ID: `94955`
- Entry ID: `117552`
- Definition ID: `122564`
- Spell ID: `431695`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tip the Scales overloads you with temporal energy, increasing your haste, movement speed, and cooldown recovery rate by ${$431698u*$431698s1}%, decreasing over $431698d.
- Effect: Tip the Scales overloads you with temporal energy, increasing your haste, movement speed, and cooldown recovery rate by ${$431698u*$431698s1}%, decreasing over $431698d.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Reverberations
- Node ID: `94925`
- Entry ID: `117522`
- Definition ID: `122534`
- Spell ID: `431615`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Verdant Embrace heals for an additional $s1% over $409895d.][Upheaval deals $s2% additional damage over $431620d.]
- Effect: $?c2[Verdant Embrace heals for an additional $s1% over $409895d.][Upheaval deals $s2% additional damage over $431620d.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chronoboon
- Node ID: `109510`
- Entry ID: `135743`
- Definition ID: `140498`
- Spell ID: `1260484`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Tip the Scales' cooldown is reduced by ${$s1/-1000} sec.
- Effect: Tip the Scales' cooldown is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `94954` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Temporality
- Node ID: `94935`
- Entry ID: `117532`
- Definition ID: `122544`
- Spell ID: `431873`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Warp reduces damage taken by ${$s1/-1}%, starting high and reducing over $431872d.
- Effect: Warp reduces damage taken by ${$s1/-1}%, starting high and reducing over $431872d.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94948` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Motes of Acceleration
- Node ID: `94935`
- Entry ID: `117784`
- Definition ID: `122796`
- Spell ID: `432008`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Warp leaves a trail of Motes of Acceleration. Allies who come in contact with a mote gain 20% increased movement speed for 30 sec.
- Effect: Warp leaves a trail of Motes of Acceleration. Allies who come in contact with a mote gain 20% increased movement speed for 30 sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94948` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nozdormu Adept
- Node ID: `94947`
- Entry ID: `117544`
- Definition ID: `122556`
- Spell ID: `431715`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Temporal Anomaly mana cost reduced by $s1% and cooldown reduced by ${$s2/-1000} sec.][Prescience cooldown reduced by ${$s3/-1000} sec and it grants $s4% additional critical strike chance.]
- Effect: $?c2[Temporal Anomaly mana cost reduced by $s1% and cooldown reduced by ${$s2/-1000} sec.][Prescience cooldown reduced by ${$s3/-1000} sec and it grants $s4% additional critical strike chance.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94955` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Chronal Dynamo
- Node ID: `109509`
- Entry ID: `135742`
- Definition ID: `140497`
- Spell ID: `1291522`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Living Flame's cast time is reduced by ${$s1/-1000}.1 sec, and it deals $s2% increased damage or healing when it is a non-instant cast.
- Effect: Living Flame's cast time is reduced by ${$s1/-1000}.1 sec, and it deals $s2% increased damage or healing when it is a non-instant cast.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `109510` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Primacy
- Node ID: `94951`
- Entry ID: `117548`
- Definition ID: `122560`
- Spell ID: `431657`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For each $?c2[healing over time effect from Verdant Embrace][damage over time effect from Upheaval], gain $s1% haste, up to $s2%.
- Effect: For each $?c2[healing over time effect from Verdant Embrace][damage over time effect from Upheaval], gain $s1% haste, up to $s2%.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94925` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Double-time
- Node ID: `94932`
- Entry ID: `117529`
- Definition ID: `122541`
- Spell ID: `431874`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[When Dream Breath or Fire Breath critically strike, their duration is extended by $s1 sec, up to a maximum of ${$s1*6} sec.][Ebon Might and Prescience gain a chance equal to your critical strike chance to grant $s2% additional stats. For Ebon Might, this increase lasts $<dura> sec.]
- Effect: $?c2[When Dream Breath or Fire Breath critically strike, their duration is extended by $s1 sec, up to a maximum of ${$s1*6} sec.][Ebon Might and Prescience gain a chance equal to your critical strike chance to grant $s2% additional stats. For Ebon Might, this increase lasts $<dura> sec.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94935` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Time Convergence
- Node ID: `94932`
- Entry ID: `117786`
- Definition ID: `122798`
- Spell ID: `431984`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Non-defensive abilities with a $s1 second or longer cooldown grant $431991s1% Intellect for $431991d.

Essence spells extend the duration by $s2 sec.
- Effect: Non-defensive abilities with a $s1 second or longer cooldown grant $431991s1% Intellect for $431991d.

Essence spells extend the duration by $s2 sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94935` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Overclock
- Node ID: `109508`
- Entry ID: `135741`
- Definition ID: `140496`
- Spell ID: `1260647`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Chrono Flames' maximum damage or healing is increased by $s1%, up to $<cap> Arcane.
- Effect: Chrono Flames' maximum damage or healing is increased by $s1%, up to $<cap> Arcane.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1` | source `node`; type `4`; currency `2801` spend gate `1`
- Incoming edges: node `109509` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Golden Opportunity
- Node ID: `94942`
- Entry ID: `117539`
- Definition ID: `122551`
- Spell ID: `432004`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c2[Echo is $s1% more effective.][Prescience lasts $s2% longer.]
- Effect: $?c2[Echo is $s1% more effective.][Prescience lasts $s2% longer.]
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94951` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Instability Matrix
- Node ID: `94930`
- Entry ID: `126310`
- Definition ID: `131136`
- Spell ID: `431484`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Each time you cast an empower spell, unstable time magic reduces its cooldown by up to $s1 sec.
- Effect: Each time you cast an empower spell, unstable time magic reduces its cooldown by up to $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94947` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Afterimage
- Node ID: `94929`
- Entry ID: `117526`
- Definition ID: `122538`
- Spell ID: `431875`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empower spells send up to $s1 Chrono Flames to your targets.
- Effect: Empower spells send up to $s1 Chrono Flames to your targets.
- Point cost per purchased rank: `1` × Hero pool (Chronowarden) (ID `2986`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94930` (type `2`), node `94932` (type `2`), node `94942` (type `2`), node `109508` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
