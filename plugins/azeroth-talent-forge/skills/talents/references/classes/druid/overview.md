# Druid

Reviewed build: `12.1.0.69404`
Class ID: `11`

## How to use this reference

Read the matching feature contract first, then inspect a string to identify its specialization. Use Entry IDs from the spec or hero catalog for modification and generation.

## Specs and roles

- `102` Balance (2)
- `103` Feral (2)
- `104` Guardian (0)
- `105` Restoration (1)
- `1447` Initial (2)

## Point pools and level schedules

The bold label is the in-game planning pool inferred from its tree placement. The numeric value is Blizzard's `TraitCurrencyID`, retained because the local graph uses it to validate exact costs and level unlocks.

- **Class pool** (internal ID `2800`): `34` points by level 90; unlock schedule `level (points)`: `11 (+1), 13 (+1), 15 (+1), 17 (+1), 19 (+1), 21 (+1), 23 (+1), 25 (+1), 27 (+1), 29 (+1), 31 (+1), 33 (+1), 35 (+1), 37 (+1), 39 (+1), 41 (+1), 43 (+1), 45 (+1), 47 (+1), 49 (+1), 51 (+1), 53 (+1), 55 (+1), 57 (+1), 59 (+1), 61 (+1), 63 (+1), 65 (+1), 67 (+1), 69 (+1), 81 (+1), 84 (+1), 87 (+1), 90 (+1)`.
- **Specialization pool (Balance, Feral, Guardian, Restoration)** (internal ID `2801`): `34` points by level 90; unlock schedule `level (points)`: `10 (+1), 12 (+1), 14 (+1), 16 (+1), 18 (+1), 20 (+1), 22 (+1), 24 (+1), 26 (+1), 28 (+1), 30 (+1), 32 (+1), 34 (+1), 36 (+1), 38 (+1), 40 (+1), 42 (+1), 44 (+1), 46 (+1), 48 (+1), 50 (+1), 52 (+1), 54 (+1), 56 (+1), 58 (+1), 60 (+1), 62 (+1), 64 (+1), 66 (+1), 68 (+1), 70 (+1), 82 (+1), 85 (+1), 88 (+1)`.
- **Hero pool (Druid of the Claw)** (internal ID `2986`): `13` points by level 90; unlock schedule `level (points)`: `71 (+1), 72 (+1), 73 (+1), 74 (+1), 75 (+1), 76 (+1), 77 (+1), 78 (+1), 79 (+1), 80 (+1), 83 (+1), 86 (+1), 89 (+1)`.
- **Hero pool (Elune's Chosen)** (internal ID `2987`): `13` points by level 90; unlock schedule `level (points)`: `71 (+1), 72 (+1), 73 (+1), 74 (+1), 75 (+1), 76 (+1), 77 (+1), 78 (+1), 79 (+1), 80 (+1), 83 (+1), 86 (+1), 89 (+1)`.
- **Hero pool (Keeper of the Grove)** (internal ID `2988`): `13` points by level 90; unlock schedule `level (points)`: `71 (+1), 72 (+1), 73 (+1), 74 (+1), 75 (+1), 76 (+1), 77 (+1), 78 (+1), 79 (+1), 80 (+1), 83 (+1), 86 (+1), 89 (+1)`.
- **Hero pool (Wildstalker)** (internal ID `2989`): `13` points by level 90; unlock schedule `level (points)`: `71 (+1), 72 (+1), 73 (+1), 74 (+1), 75 (+1), 76 (+1), 77 (+1), 78 (+1), 79 (+1), 80 (+1), 83 (+1), 86 (+1), 89 (+1)`.

## Hero subtrees

- `21` **Druid of the Claw** — Druids of the Claw are masters of their mighty animal forms. When they transform into cats or bears, they become ferocious combatants and protectors of the wild.
- `22` **Wildstalker** — Wildstalkers live amongst the remote wilds, hunting to perpetuate the cycle of life and death and destroy those who would despoil nature and using their healing powers to restore life to barren spaces.
- `23` **Keeper of the Grove** — Keepers of the Grove take inspiration from Cenarius' mighty children to protect the balance of nature and safeguard the Dream. They channel the power of the Dream to strengthen their spells and summon empowered treants to protect their allies and crush their enemies.
- `24` **Elune's Chosen** — Elune's Chosen dedicate themselves to the Moon Goddess and are granted her connection to the moon and stars. Their abilities are infused with astral might and they can call down potent lunar magics.

## Goal vocabulary

single-target, cleave, aoe, survivability, utility, control, mobility, comfort, leveling.

## Limits

This reference describes source facts and trade-offs; it does not claim a best build.
