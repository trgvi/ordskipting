# Íslensk orðskipting fyrir InDesign

Samantekt fyrir aðstoð við áframhaldandi vinnu. Lýsir verkefninu, reglunum, gögnunum, hvernig orðskiptiskráin er byggð og hvernig uppsetningin virkar.

- **Síða:** https://ordskipting.vercel.app
- **Kóði:** github.com/trgvi/ordskipting (branch `main`, Vercel birtir sjálfkrafa við push)
- **Útgáfa:** 1.8, Mac (Apple Silicon og Intel), InDesign 2020–2027
- **Höfundur:** Tryggvi Hilmars

---

## 1. Hvað þetta er

Íslenskar orðskiptireglur fyrir Hunspell-orðskiptivélina í Adobe InDesign. InDesign hefur ekki íslenska orðskiptingu innbyggða, svo uppsetningin bætir henni við. Hún fylgir líka með skriftum sem stilla InDesign sjálfkrafa.

Uppsetningin er **eingöngu orðskipting** og engin stafsetningarleiðrétting. Hún var tekin út því íslenska orðasafnið kunni ekki samsett orð og gaf vitlausar tillögur.

---

## 2. Opinberar reglur

Heimild: **Ritreglur Íslenskrar málnefndar (2018), 33. kafli: Orðskipting.**

### 33.1 Samsett orð
Samsettum orðum er skipt á mótum orðhlutanna (stofnamótum):
- `strætis-vagn`, `veiði-maður`, `mánaðar-kort`

### 33.2 Ósamsett orð
- **33.2.1** Ef seinni hlutinn byrjar á sérhljóði má skipta á undan honum. Seinni hlutinn má ekki vera einn stafur. Fyrri hlutinn má vera einn stafur.
- Almenna reglan er að einn samhljóði fer yfir í næstu línu: `ta-la`, `bú-a`.
- Þegar tveir eða fleiri samhljóðar standa saman fer sá síðasti yfir línuna nema samstafan sé leyfilegt upphaf orðs: `hes-tur`, `kart-öflur`.
- Afleiðsluviðskeyti fylgja líka mótum: `-legur`, `-ing`, `-un`, `-andi` o.s.frv.

### Hagnýtt
- `LEFTHYPHENMIN 2` og `RIGHTHYPHENMIN 3`: minnst tveir stafir á undan skiptingu og þrír á eftir.
- Lágmarkslengd orðs sem má skipta er stillt í InDesign (Hyphenation Settings). Það þarf ekki að vera í reglunum sjálfum.

---

## 3. Gögn

| Heimild | Lýsing | Leyfi |
|---|---|---|
| **Árnastofnun: Icelandic Hyphenation Dictionary 2.0** | 218.308 orð með merktum skiptingum, github.com/krunars/hyphenation-is | CC BY 4.0, krefst tilvísunar |
| **Baldur Jónsson og Magnús Gíslason (1985)** | Upprunalegu íslensku orðskiptimynstrin, dreift með LibreOffice | GPL/LGPL/MPL |

Tilvísun í Árnastofnun þarf að vera á síðunni og í uppsetningunni. Hún er núna í fæti síðunnar.

---

## 4. Hvernig orðskiptiskráin er byggð

Skráin heitir `hyph_is_IS.dic` og er á libhyphen-sniði (Liang-mynstur, sama aðferð og TeX notar).

### Ferlið
1. **Grunnur:** mynstur Baldurs og Magnúsar (1985).
2. **Þjálfun með `patgen`** á orðalista Árnastofnunar:
   - translate-skrá fyrir íslenska stafi (á, ð, é, í, ó, ú, ý, þ, æ, ö)
   - færibreytuskrár með hærri þröskuldi (pC, pE, pG) svo mynstrin fari ekki yfir getu patgen (4080 úttök)
3. **Sameining mynstra:** þegar sama mynstur kemur fyrir í fleiri en einni heimild ræður hæsta talan (`max`). Hún má ekki skrifa yfir.
4. **Undantekningar** í `gogn/undantekningar/`: handgerð mynstur (78), yfirfarin orð (87) og gull (2.695), öll á mynstrasniði.
5. **`substrings.pl`** (útfært í `tools/subst.py`): keyrist á lokaskrána. Án þess skiptir libhyphen vitlaust, t.d. `veiði-nnar` í stað `veið-innar`.
6. **Yfirferð:** 434 orð þar sem heimildirnar voru ósammála voru yfirfarin eftir ritreglum 33. kafla.

### Gildrur sem komu upp
- **Óunnin mynstur:** gáfu ð-hliðraðar skiptingar. Lagað með `substrings.pl`.
- **Of almennar reglur:** t.d. `a8r9æf` braut `pokaræfill`. Þrengt í `a8r9æfing`.
- **Undantekningar sem rekast á:** t.d. `hrað-rar` var fjarlægt.
- **Samhljóðabrot:** einn eða tveir samhljóðar einir í línu. Prófað sérstaklega og eru 0 í 1.8.

### Mælingar (útgáfa 1.8)
| Próf | Niðurstaða |
|---|---|
| Orð sem voru haldin utan þjálfunar | 94,2 % heil orð rétt (1.7: 92,5 %) |
| Allur listi Árnastofnunar | 100 % |
| Raunverulegir textar (bókarkaflar og tímarit) | 0 samhljóðabrot |

---

## 5. Uppsetningin (.pkg)

Venjulegur macOS-uppsetningarpakki án `.sh`, sem má dreifa til annarra.

- `Islensk-ordskipting-InDesign-1.8.pkg`: setur inn
- `Fjarlaegja-islenska-ordskiptingu.pkg`: fjarlægir og setur upprunalegu skrárnar aftur

### Hvað pakkinn gerir
1. Finnur allar InDesign-útgáfur 2020–2027 í `/Applications`.
2. Í hverri útgáfu:
   - setur `hyph_is_IS.dic` í `AdobeHunspellPlugin.bundle/Contents/Resources/Dictionaries/is_IS/`
   - bætir íslensku við `ALPlugInLanguages:HyphenationService` í `Info.plist`
   - geymir afrit af upprunalegum skrám í `Dictionaries/.IcelandicHunspell/orig`
   - undirritar bundle-ið aftur (ad-hoc `codesign`) svo macOS hleypi því inn
3. Setur upp tvær InDesign-skriftur:
   - **Startup-skrifta:** stillir InDesign einu sinni á Icelandic + Hunspell orðskiptingu. Merki (app label) kemur í veg fyrir að hún keyri aftur.
   - **„Íslenska í skjalið.jsx“** (Scripts-panel): setur íslensku á alla stíla og texta í opnu skjali og lagar gæsalappir í „íslenskar“ með GREP. Hægt að afturkalla í einu skrefi (`UndoModes.ENTIRE_SCRIPT`).

### Uppbygging pakkans
Pakkinn er handsmíðaður í Python, án Apple-tóla:
- xar-safn (TOC með sha1 og heap)
- Payload sem gzip cpio (odc)
- Distribution XML með installation-check (JS) sem stoppar ef InDesign er opið
- HTML-skjáir á íslensku (Resources)
- postinstall-skriftur

Tólin eru `mkpkg.py`, `xar.py` og `cpio.py`.

### Textar í uppsetningu
- **Heiti:** Íslensk orðskipting fyrir InDesign
- **Velkomin:** Íslensk orðskipting fyrir Hunspell í InDesign 2020–2027. Lokaðu InDesign áður en þú heldur áfram.
- **Leyfi:** tilvísun í Árnastofnun (CC BY 4.0) og Baldur Jónsson og Magnús Gíslason (1985)
- **Lok:** stutt leiðbeining (opna InDesign og keyra skriftuna í skjölum)

Textarnir eiga að vera stuttir, á eðlilegri íslensku og án fyrirtækjanafns.

---

## 6. Í InDesign eftir uppsetningu
1. Opna InDesign. Startup-skriftan stillir sjálfgefið tungumál og orðskiptivél.
2. Í eldri skjölum: **Window › Utilities › Scripts › „Íslenska í skjalið“**.
3. Handvirkt: Character/Paragraph Style › Advanced Character Formats › Language: **Icelandic**, og Preferences › Dictionary › Hyphenation: **Hunspell**.

---

## 7. Síðan (ordskipting.vercel.app)
- Ein `index.html` með IBM Plex Sans og Mono. Aðeins svart og hvítt, ljóst og dökkt þema (`data-utlit`).
- Niðurhalshnappur (fylltur) og „Fjarlægja“ (outline), báðir með niðurhalstákni.
- Ljósblár textarammi sem má draga til. Textinn skiptist lifandi með eigin línubrotum (canvas `measureText`) svo bandstrikin geti verið blá. Letrið er Bespoke Serif.
- Allur grár texti er 12 px.
- `vercel.json` lætur `.pkg` hlaðast niður sem skrá.

---

## 8. Endurbygging

Allt sem þarf er í repoinu. `make all` endurbyggir 1.8 og keyrir prófanir. Sjá `ORDASAFN.md` kafla 10–12.

```
gogn/arnastofnun.txt        orðalisti Árnastofnunar 2.0 (CC BY 4.0)
gogn/thjalfun.txt           þjálfunargögn (Árnastofnun + aukin gögn)
gogn/undantekningar/        undantekningar og handgerð mynstur
gogn/patgen/                translate-skrá og patgen-stillingar
gogn/prof/                  þróunar- og lokaprófunarsöfn, villur úr textum
tools/                      Python-tól
utgafa/hyph_is_IS.dic       útgefin skrá (1.8)
tillogur.tsv                nýjar orðatillögur (ChatGPT)
```

## 9. Opið / næstu skref
- **Eigið lén:** CNAME `ordskipting.tryggvihilmars.com` → `cname.vercel-dns.com` hjá 1984.is, og bæta léninu við í Vercel.
- Notarization hjá Apple (krefst Apple Developer-aðgangs) svo Gatekeeper-viðvörunin hverfi. Án þess þarf að hægri-smella › Open.
- Windows-útgáfa ef áhugi er fyrir því.
- Halda áfram að safna orðum sem skiptast vitlaust í `extra_review.txt` og endurbyggja.
