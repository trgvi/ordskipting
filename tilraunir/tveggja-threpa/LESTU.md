# A/B-próf: tveggja þrepa orðskipting í InDesign

**A** = núverandi skrá (1.8 + kóði-mynstur). **B** = sama skrá með tveggja þrepa skiptingu:
fyrst samskeyti, svo skipting innan hvers orðhluta með minnst tvo stafi (`COMPOUNDLEFTHYPHENMIN 2`, `COMPOUNDRIGHTHYPHENMIN 2`).
Í B eru samskeytin aðeins skráð fyrir prófunarorðin 11. Þetta prófar hvort InDesign styður aðferðina, ekki gæðin.

`vaentanlegt.tsv` sýnir væntanlega skiptingu hvers orðs í A og B (staðfest með libhyphen).

## Skref
1. Lokaðu InDesign. Opnaðu Terminal í þessari möppu og keyrðu:
   `sudo sh skipta.command A`
2. Opnaðu InDesign › File › Scripts › Browse… eða dragðu `AB-prof.jsx` í Scripts-panelinn og keyrðu hana.
   Efst stendur hvaða skrá er uppsett. Taktu skjámynd.
3. Lokaðu InDesign. `sudo sh skipta.command B`. Opnaðu InDesign, keyrðu skriftuna aftur og taktu skjámynd.
4. Til baka í útgefna skrá: `sudo sh skipta.command 1.8`

## Hvað á að sjást
- Í A: línur eins og `innv-` / `iða-`, `mótherj-` / `a-`, `vír-` / `u-`, `bæt-` / `a-` í mjóu römmunum.
- Í B: þessar einstafsskiptingar hverfa (`inn-` / `viða-`, `mótherja-`, `vírus-`, `bæta-`).
- Hin sex orðin eiga að skiptast eins í A og B, þar á meðal `fram-leið-andi` inni í seinni lið.

Ef B lítur út eins og A í InDesign styður InDesign ekki tveggja þrepa skrár og leiðin fellur út.
Ef InDesign sýnir enga orðskiptingu með B hafnar það skránni: farðu aftur í 1.8.
