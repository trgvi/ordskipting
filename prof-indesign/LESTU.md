# Prófunarskjal í InDesign

`profunarskjal.jsx` býr til InDesign-skjal með öllum prófunarorðunum og vistar það á skjáborðinu sem `Prófunarskjal orðskiptingar.indd`.

- Orð í sex mjóum römmum (16–43 mm), 12 orð á síðu, svo InDesign skipti þeim á sem flestum stöðum.
- Samfelldur texti í þremur, tveimur og einum dálki, jafnaður.
- Aftast: vænt skipting hvers orðs (Á = Árnastofnun, T = tillaga úr lotu) og hvernig útgefna skráin skiptir því. ≠ merkir ósamræmi.
- Á forsíðu stendur hvaða orðskiptiskrá er uppsett og útgáfa InDesign.

Keyrsla (InDesign opið):
```
osascript -e 'tell application id "com.adobe.InDesign" to do script (POSIX file "/SLÓÐ/profunarskjal.jsx") language javascript'
```
eða setja skriftuna í Scripts-panelinn og tvísmella.

Breyta orðum: bættu í `ord.txt` (kaflar byrja á `## `) og keyrðu `python3 prof-indesign/mynda.py`. Lotur í `lotur/` og 100 orða úrtak Árnastofnunar bætast við sjálfkrafa.
