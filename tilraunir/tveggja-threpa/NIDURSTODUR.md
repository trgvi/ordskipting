# Tveggja þrepa orðskipting — tilraunir 27.11.2026

Mælt á gogn/prof/throun.txt (4.255 orð, óséðar fjölskyldur). Lokapróf ekki keyrt.

| Útgáfa | Heil orð | Rangir | Vantar | Einstafsbútar |
|---|---:|---:|---:|---:|
| Grunnur (eitt þrep) | 93,91% | 97 | 219 | 41 |
| Hamlandi mynstur úr krossprófun | 93,91–93,94% | 96–97 | 219 | 41 |
| Tvö þrep, samskeyti MIN 3, pE | 93,63% | 118 | 236 | 33 |
| + jaðarbann í þrepi 1 | 94,17% | 116 | 214 | 33 |
| MIN 4, pE | 94,15% | 106 | 217 | 32 |
| **MIN 4, hærri þröskuldar (vT)** | **94,15%** | **100** | **223** | **27** |
| MIN 5, vT | 94,01% | 100 | 218 | 35 |
| MIN 4, vT + þrep 2 þjálfað á orðhlutum | 92,78% | 146 | 263 | 44 |

InDesign 2027 les NEXTLEVEL og COMPOUND*HYPHENMIN (A/B-próf, skjámyndir 27.11).

Samskeyti eru leidd út með joints.py: skiptistaðir úr gulli þar sem allir hlutar (≥ MIN stafir) eru orð í orðasafninu, fæstir hlutar vinna.

## Valin útfærsla (jv2): samskeyti MIN 4, jafntefli leyst með tíðni orðhluta (joints2.py), patgen vT, jaðarbann

| Safn | Útgáfa | Heil orð | Rangir | Vantar | Einstafsbútar |
|---|---|---:|---:|---:|---:|
| Þróun | grunnur | 93,91% | 97 | 219 | 41 |
| Þróun | tvö þrep | 94,20% | 94 | 225 | 27 |
| **Lokapróf** | grunnur | 93,89% | 112 | 216 | 42 |
| **Lokapróf** | tvö þrep | **94,18%** | **109** | 221 | **28** |

Lokapróf, breytingar miðað við grunn: 20 réttir skiptistaðir tapast, 15 réttir bætast við; 18 nýir rangir, 21 rangir hverfa.
Lokaprófið var keyrt einu sinni, eftir að útfærslan var valin á þróunarsafni.

Eftir fyrir útgáfu: undantekningar (heil orð) þurfa að virka í tveggja þrepa skrá; prófa InDesign 2026.
