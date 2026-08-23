# Preservation

Reviewed build: `12.1.0.69404`
Spec ID: `1468`
Role: `1`

Use this catalog after `overview.md`; point schedules are shared there and validation applies them per currency.

## Talents

### Mass Disintegrate
- Node ID: `94939`
- Entry ID: `117536`
- Definition ID: `122548`
- Spell ID: `436335`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empower spells cause your next Disintegrate to strike up to $s1 targets. When striking fewer than $s1 targets, Disintegrate damage is increased by $s2% for each missing target.
- Effect: Empower spells cause your next Disintegrate to strike up to $s1 targets. When striking fewer than $s1 targets, Disintegrate damage is increased by $s2% for each missing target.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `node`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Mass Eruption
- Node ID: `98931`
- Entry ID: `122279`
- Definition ID: `127179`
- Spell ID: `438587`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Empower spells cause your next Eruption to strike up to $s1 targets. When striking less than $s1 targets, Eruption damage is increased by $s2% for each missing target.
- Effect: Empower spells cause your next Eruption to strike up to $s1 targets. When striking less than $s1 targets, Eruption damage is increased by $s2% for each missing target.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `node`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Legacy of the Lifebinder
- Node ID: `94950`
- Entry ID: `117547`
- Definition ID: `122559`
- Spell ID: `1264269`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Fire Breath gains][Dream Breath and Fire Breath gain] an additional charge.
- Effect: $?c1[Fire Breath gains][Dream Breath and Fire Breath gain] an additional charge.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `2`; minimum level `71`; grants `1` rank(s) | source `group`; type `1`
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expunge
- Node ID: `93306`
- Entry ID: `115615`
- Definition ID: `120627`
- Spell ID: `365585`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Expunge toxins affecting an ally, removing all Poison effects.
- Effect: Expunge toxins affecting an ally, removing all Poison effects.
- Point cost per purchased rank: `1` × Specialization pool (Augmentation, Devastation, Preservation) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: none
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Trailblazer
- Node ID: `94937`
- Entry ID: `117534`
- Definition ID: `122546`
- Spell ID: `444849`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Hover and Deep Breath][Hover, Deep Breath, and Dream Flight] travel $s1% faster, and Hover travels $s1% further.
- Effect: $?c1[Hover and Deep Breath][Hover, Deep Breath, and Dream Flight] travel $s1% faster, and Hover travels $s1% further.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Shape of Flame
- Node ID: `94937`
- Entry ID: `123404`
- Definition ID: `128242`
- Spell ID: `445074`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Tail Swipe and Wing Buffet scorch enemies and blind them with ash, causing their next attack within $445134d to miss.
- Effect: Tail Swipe and Wing Buffet scorch enemies and blind them with ash, causing their next attack within $445134d to miss.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Ashes in Motion
- Node ID: `99857`
- Entry ID: `123416`
- Definition ID: `128254`
- Spell ID: `1264365`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fire Breath's cooldown is reduced by ${$s1/-1000} sec.
- Effect: Fire Breath's cooldown is reduced by ${$s1/-1000} sec.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Enkindle
- Node ID: `94956`
- Entry ID: `117553`
- Definition ID: `122565`
- Spell ID: `444016`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence abilities are enhanced with Flame, dealing $s1% of healing or damage done as Fire over 8 sec.
- Effect: Essence abilities are enhanced with Flame, dealing $s1% of healing or damage done as Fire over 8 sec.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Expanded Lungs
- Node ID: `94956`
- Entry ID: `128713`
- Definition ID: `133515`
- Spell ID: `444845`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Fire Breath's damage over time is increased by $s1%. Dream Breath's heal over time is increased by $s2%.
- Effect: Fire Breath's damage over time is increased by $s1%. Dream Breath's heal over time is increased by $s2%.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Essence Well
- Node ID: `109797`
- Entry ID: `136055`
- Definition ID: `140810`
- Spell ID: `1265993`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Fire Breath has][Dream Breath and Fire Breath have] a $s1% chance to generate Essence Burst.
- Effect: $?c1[Fire Breath has][Dream Breath and Fire Breath have] a $s1% chance to generate Essence Burst.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94950` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Verdant Embrace
- Node ID: `93341`
- Entry ID: `115655`
- Definition ID: `120667`
- Spell ID: `360995`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fly to an ally and heal them for $361195s1, or heal yourself for the same amount.
- Effect: Fly to an ally and heal them for $361195s1, or heal yourself for the same amount.
- Point cost per purchased rank: `1` × Specialization pool (Augmentation, Devastation, Preservation) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `93306` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Burning Adrenaline
- Node ID: `94946`
- Entry ID: `117543`
- Definition ID: `122555`
- Spell ID: `444020`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fire Breath $?c1[reaches its][and Dream Breath reach their] maximum empower level $s1% faster.
- Effect: Fire Breath $?c1[reaches its][and Dream Breath reach their] maximum empower level $s1% faster.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `99857` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fulminous Roar
- Node ID: `94923`
- Entry ID: `117520`
- Definition ID: `122532`
- Spell ID: `1218447`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Fire Breath deals its damage][Fire Breath and Dream Breath deal their damage and healing] $s1% more often.
- Effect: $?c1[Fire Breath deals its damage][Fire Breath and Dream Breath deal their damage and healing] $s1% more often.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94956` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Conduit of Flame
- Node ID: `94949`
- Entry ID: `117546`
- Definition ID: `122558`
- Spell ID: `444843`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Critical strike chance against targets above $s2% health increased by $s1%.
- Effect: Critical strike chance against targets above $s2% health increased by $s1%.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94937` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Twin Flame
- Node ID: `109798`
- Entry ID: `136056`
- Definition ID: `140811`
- Spell ID: `1265979`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Consuming Essence Burst fires a twin flame, $?c1[striking your target for $1265980s1 Fire damage][healing your target for $1265991s1].
- Effect: Consuming Essence Burst fires a twin flame, $?c1[striking your target for $1265980s1 Fire damage][healing your target for $1265991s1].
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109797` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Titanic Precision
- Node ID: `94920`
- Entry ID: `117517`
- Definition ID: `122529`
- Spell ID: `445625`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Living Flame $?c1[and Azure Strike have $s1 extra chance to trigger Essence Burst when they critically strike.][has $s1 extra chance to trigger Essence Burst when it critically strikes.]
- Effect: Living Flame $?c1[and Azure Strike have $s1 extra chance to trigger Essence Burst when they critically strike.][has $s1 extra chance to trigger Essence Burst when it critically strikes.]
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94949` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Deep Exhalation
- Node ID: `94945`
- Entry ID: `117542`
- Definition ID: `122554`
- Spell ID: `1264321`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Fire Breath's damage over time lasts $s1 sec longer.$?c2[

Dream Breath's heal over time lasts ${$s2/1000} sec longer.][]
- Effect: Fire Breath's damage over time lasts $s1 sec longer.$?c2[

Dream Breath's heal over time lasts ${$s2/1000} sec longer.][]
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94946` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Lifecinders
- Node ID: `94931`
- Entry ID: `117528`
- Definition ID: `122540`
- Spell ID: `444322`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Obsidian Scales also applies to your target or $s1 nearby injured $Lally:allies; at $s2% value.
- Effect: Obsidian Scales also applies to your target or $s1 nearby injured $Lally:allies; at $s2% value.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94923` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Draconic Instincts
- Node ID: `94931`
- Entry ID: `123405`
- Definition ID: `128243`
- Spell ID: `445958`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Your wounds have a small chance to cauterize, healing you for $s1% of damage taken. Occurs more often from attacks that deal high damage.
- Effect: Your wounds have a small chance to cauterize, healing you for $s1% of damage taken. Occurs more often from attacks that deal high damage.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94923` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Fire Torrent
- Node ID: `109796`
- Entry ID: `136054`
- Definition ID: `140809`
- Spell ID: `1265992`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Twin Flame bounces to up to $s1 additional targets.
- Effect: Twin Flame bounces to up to $s1 additional targets.
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109798` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Consume Flame
- Node ID: `94922`
- Entry ID: `117519`
- Definition ID: `122531`
- Spell ID: `444088`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Disintegrate consumes ${$s2/1000}.1 sec of Fire Breath from enemies it damages, detonating it for $s4% of the amount consumed.

Pyre consumes ${$s3/1000} sec of Fire Breath from enemies it damages, detonating it for $s7% of the amount consumed.][Verdant Embrace consumes ${$s5/1000} sec of Dream Breath from allies it heals, detonating it and healing them for $s6% of the amount consumed.

Emerald Blossom and Fluttering Seedlings consume ${$s1/1000} sec of Dream Breath from allies they heal, detonating it and healing them for $s6% of the amount consumed.]
- Effect: $?c1[Disintegrate consumes ${$s2/1000}.1 sec of Fire Breath from enemies it damages, detonating it for $s4% of the amount consumed.

Pyre consumes ${$s3/1000} sec of Fire Breath from enemies it damages, detonating it for $s7% of the amount consumed.][Verdant Embrace consumes ${$s5/1000} sec of Dream Breath from allies it heals, detonating it and healing them for $s6% of the amount consumed.

Emerald Blossom and Fluttering Seedlings consume ${$s1/1000} sec of Dream Breath from allies they heal, detonating it and healing them for $s6% of the amount consumed.]
- Point cost per purchased rank: `1` × Hero pool (Flameshaper) (ID `2987`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94920` (type `2`), node `94931` (type `2`), node `94945` (type `2`), node `109796` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
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
