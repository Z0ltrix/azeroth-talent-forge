# Flameshaper

Reviewed build: `12.1.0.69404`
Hero subtree ID: `37`
Description: Flameshapers are closely attuned to Alexstrasza and specialize in protecting allies, rejuvenation, and renewal. They also have the unique ability to spread, intensify, and manipulate dragonflame.

## Hero talents

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
