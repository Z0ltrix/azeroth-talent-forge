# Devastation

Reviewed build: `12.1.0.69404`
Spec ID: `1467`
Role: `2`

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
### Might of the Black Dragonflight
- Node ID: `94952`
- Entry ID: `117549`
- Definition ID: `122561`
- Spell ID: `441705`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Black spells deal $s1% increased damage.
- Effect: Black spells deal $s1% increased damage.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Bombardments
- Node ID: `94936`
- Entry ID: `117533`
- Definition ID: `122545`
- Spell ID: `434300`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mass Disintegrate][Mass Eruption] marks your primary target for destruction for the next $434473d.

You and your allies have a chance to trigger a Bombardment when attacking marked targets, dealing $<dmg> Volcanic damage split amongst all nearby enemies.
- Effect: $?c1[Mass Disintegrate][Mass Eruption] marks your primary target for destruction for the next $434473d.

You and your allies have a chance to trigger a Bombardment when attacking marked targets, dealing $<dmg> Volcanic damage split amongst all nearby enemies.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Onslaught
- Node ID: `94944`
- Entry ID: `117541`
- Definition ID: `122553`
- Spell ID: `441245`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Entering combat grants a charge of Burnout, causing your next Living Flame to cast instantly.
- Effect: Entering combat grants a charge of Burnout, causing your next Living Flame to cast instantly.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Command Squadron
- Node ID: `109795`
- Entry ID: `136053`
- Definition ID: `140808`
- Spell ID: `1260745`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While flying during $?s403631[Breath of Eons][Deep Breath] you are assisted by a squadron of Dracthyr who assault enemies with Pyre, dealing $1236970s1 Fire damage to nearby enemies up to $s3 times.
- Effect: While flying during $?s403631[Breath of Eons][Deep Breath] you are assisted by a squadron of Dracthyr who assault enemies with Pyre, dealing $1236970s1 Fire damage to nearby enemies up to $s3 times.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94939` (type `2`), node `98931` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Landslide
- Node ID: `93305`
- Entry ID: `115614`
- Definition ID: `120626`
- Spell ID: `358385`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Conjure a path of shifting stone towards the target location, rooting enemies for $355689d. Damage may cancel the effect.
- Effect: Conjure a path of shifting stone towards the target location, rooting enemies for $355689d. Damage may cancel the effect.
- Point cost per purchased rank: `1` × Specialization pool (Augmentation, Devastation, Preservation) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s) | source `group`; type `2`; grants `1` rank(s)
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
### Melt Armor
- Node ID: `94921`
- Entry ID: `117518`
- Definition ID: `122530`
- Spell ID: `441176`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s403631[Breath of Eons][Deep Breath] causes enemies to take $s2% increased damage from Bombardments and Essence abilities for $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Effect: $?s403631[Breath of Eons][Deep Breath] causes enemies to take $s2% increased damage from Bombardments and Essence abilities for $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94952` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Wingleader
- Node ID: `94953`
- Entry ID: `117550`
- Definition ID: `122562`
- Spell ID: `441206`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mass Disintegrate][Mass Eruption] reduces the remaining cooldown of $?c1[Deep Breath][Breath of Eons] by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec for each target struck.
- Effect: $?c1[Mass Disintegrate][Mass Eruption] reduces the remaining cooldown of $?c1[Deep Breath][Breath of Eons] by $?c1[${$s1/1000}.1][${$s2/1000}.1] sec for each target struck.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94936` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Unrelenting Siege
- Node ID: `94934`
- Entry ID: `117531`
- Definition ID: `122543`
- Spell ID: `441246`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: For each second you are in combat, Azure Strike, Living Flame, and $?c1[Disintegrate][Eruption] deal $s1% increased damage, up to $s2%.
- Effect: For each second you are in combat, Azure Strike, Living Flame, and $?c1[Disintegrate][Eruption] deal $s1% increased damage, up to $s2%.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94944` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Concentrated Power
- Node ID: `109794`
- Entry ID: `136052`
- Definition ID: `140807`
- Spell ID: `1261448`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?c1[Mass Disintegrate][Mass Eruption] strikes $s1 additional $Ltarget:targets;.
- Effect: $?c1[Mass Disintegrate][Mass Eruption] strikes $s1 additional $Ltarget:targets;.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109795` (type `2`), node `109795` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Natural Convergence
- Node ID: `93312`
- Entry ID: `115621`
- Definition ID: `120633`
- Spell ID: `369913`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Disintegrate channels $s1% faster$?c3[ and Eruption's cast time is reduced by $s3%][].
- Effect: Disintegrate channels $s1% faster$?c3[ and Eruption's cast time is reduced by $s3%][].
- Point cost per purchased rank: `1` × Specialization pool (Augmentation, Devastation, Preservation) (ID `2801`; group)
- Source gates: source `group`; type `2`; grants `1` rank(s)
- Incoming edges: node `93305` (type `2`)
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
### Hardened Scales
- Node ID: `94933`
- Entry ID: `117530`
- Definition ID: `122542`
- Spell ID: `441180`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Obsidian Scales reduces damage taken by an additional ${$s1/-1}%.
- Effect: Obsidian Scales reduces damage taken by an additional ${$s1/-1}%.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94921` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Menacing Presence
- Node ID: `94933`
- Entry ID: `120125`
- Definition ID: `125025`
- Spell ID: `441181`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Knocking enemies up or backwards reduces their damage done to you by $s1% for $441201d.
- Effect: Knocking enemies up or backwards reduces their damage done to you by $s1% for $441201d.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94921` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Extended Battle
- Node ID: `94928`
- Entry ID: `117525`
- Definition ID: `122537`
- Spell ID: `441212`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence abilities extend Bombardments by $s1 sec.
- Effect: Essence abilities extend Bombardments by $s1 sec.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94953` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Diverted Power
- Node ID: `94928`
- Entry ID: `120124`
- Definition ID: `125024`
- Spell ID: `441219`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: Bombardments have a chance to generate Essence Burst.
- Effect: Bombardments have a chance to generate Essence Burst.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94953` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Nimble Flyer
- Node ID: `94943`
- Entry ID: `117540`
- Definition ID: `122552`
- Spell ID: `441253`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: While Hovering, damage taken from area of effect attacks is reduced by ${$s1/-1}%.
- Effect: While Hovering, damage taken from area of effect attacks is reduced by ${$s1/-1}%.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94934` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Slipstream
- Node ID: `94943`
- Entry ID: `120123`
- Definition ID: `125023`
- Spell ID: `441257`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `200`
- Description: $?s403631[Breath of Eons][Deep Breath] resets a charge of Hover.
- Effect: $?s403631[Breath of Eons][Deep Breath] resets a charge of Hover.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94934` (type `2`)
- Planning tags: `source-derived only`
- Source: `db2`; build: `12.1.0.69404`
### Refined Essence
- Node ID: `109793`
- Entry ID: `136051`
- Definition ID: `140806`
- Spell ID: `1261452`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: Essence abilities deal $s1% additional damage.
- Effect: Essence abilities deal $s1% additional damage.
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `109794` (type `2`), node `109794` (type `2`)
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
### Maneuverability
- Node ID: `94941`
- Entry ID: `117538`
- Definition ID: `122550`
- Spell ID: `433871`
- Tree ID: `872`; tree kind: `class`
- Maximum ranks: `1`; entry ordinal: `100`
- Description: $?s403631[Breath of Eons][Deep Breath] can now be steered in your desired direction.

In addition, $?s403631[Breath of Eons][Deep Breath] burns targets for $441172o1 Volcanic damage over $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Effect: $?s403631[Breath of Eons][Deep Breath] can now be steered in your desired direction.

In addition, $?s403631[Breath of Eons][Deep Breath] burns targets for $441172o1 Volcanic damage over $441172d.$?c1[

The duration of this effect is extended when Deep Breath is cast multiple times.][]
- Point cost per purchased rank: `1` × Hero pool (Scalecommander) (ID `2988`; group)
- Source gates: source `group`; type `1` | source `group`; type `1`
- Incoming edges: node `94928` (type `2`), node `94933` (type `2`), node `94943` (type `2`), node `109793` (type `2`), node `109793` (type `2`)
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
