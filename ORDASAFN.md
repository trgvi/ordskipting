# ORDASAFN.md
## Íslensk orðskipting — sameiginleg þróunarverklýsing
Útgáfa 1.2

## 1. Markmið

Þróa áreiðanlega íslenska orðskiptingu fyrir Adobe InDesign sem ræður bæði við þekkt íslensk orð og áður óþekkt orð, samsetningar og beygingarmyndir.

Verkefnið snýst ekki eingöngu um að stækka orðasafnið heldur að bæta getu orðskiptivélarinnar til að alhæfa út frá réttum þjálfunargögnum.

Grundvallarreglur:

- Gæði fram yfir magn.
- Málfræði fram yfir ágiskanir.
- Rangur skiptistaður er alvarlegri villa en skiptistaður sem vantar.
- Ný gögn mega ekki skemma eldri réttar skiptingar.
- Allar breytingar skulu vera rekjanlegar.
- Framfarir skulu vera mælanlegar.

## 2. Verkefnið

- Vefur: https://ordskipting.vercel.app
- GitHub: https://github.com/trgvi/ordskipting
- Núverandi útgáfa: 1.8
- Orðskiptivél: Hunspell/libhyphen
- Mynstur: Liang/TeX
- Þjálfunartól: patgen
- Úttaksskrá: `hyph_is_IS.dic`
- Núverandi stærð úttaksskrár: um 1,9 MB

Nánari tæknileg lýsing er í `ORDSKIPTING.md`.

## 3. Heimildir og ritreglur

Aðalheimild um orðskiptingu er 33. kafli Ritreglna Íslenskrar málnefndar.

### Þjálfunargögn

- Icelandic Hyphenation Dictionary 2.0 frá Árnastofnun, 218.308 orð, CC BY 4.0.
- Orðskiptimynstur Baldurs Jónssonar og Magnúsar Gíslasonar frá 1985.

Virða skal leyfi og tilvísunarskyldu.

### Heimildir til sannprófunar

- Beygingarlýsing íslensks nútímamáls (BÍN).
- Risamálheildin.
- Íslensk stafsetningarorðabók.
- Íslenskt orðanet.
- Útgefnir íslenskir textar.

BÍN má nýta með viðeigandi tilvísun og samkvæmt leyfisskilmálum.

Íslenska stafsetningarorðabókin er ekki opið gagnasafn og skal ekki afrituð inn í verkefnið.

Hlutar Risamálheildarinnar hafa takmörkuð leyfi.

Sjálfgefið skal nýta þessar heimildir til að sannreyna einstök orð, beygingar og málnotkun en ekki afrita heilu orðalistana.

Ekki má skrá heimild sem hefur ekki verið skoðuð.

## 4. Orðskiptireglur

### Samsett orð

Greina skal málfræðilega uppbyggingu og stofnamót samsettra orða.

Dæmi um orðhluta:

- maðka + veiði + maður
- strætis + vagna + bíl + stjóri
- skráningar + skylda
- þæginda + rammi
- sjó + birtingur

Greina skal á milli:

- Stofna.
- Tengistafa.
- Eignarfallsliða.
- Forskeyta.
- Afleiðsluviðskeyta.
- Beygingarendinga.
- Innri samsetninga.

Stofnamót og allir leyfilegir skiptistaðir eru ekki endilega það sama.

### Ósamsett orð

Beita skal viðeigandi ákvæðum 33. kafla ritreglnanna.

Ekki rugla saman:

- Atkvæðaskiptingu.
- Framburði.
- Málfræðilegum orðhlutum.
- Leyfilegri orðskiptingu við línuskil.

### Tæknilegar takmarkanir

Núverandi stillingar:

```text
LEFTHYPHENMIN 2
RIGHTHYPHENMIN 3
```

Greina skal á milli málfræðilega leyfilegra skiptistaða og þeirra sem orðskiptivélin getur birt miðað við þessar stillingar.

Við samanburðarprófanir skulu sömu tæknilegu takmarkanir gilda um viðmiðunargögn og niðurstöður vélarinnar.

## 5. Núverandi mynsturskrár

Eftirfarandi skrár eru hluti af byggingarferlinu:

| Skrá | Innihald | Fjöldi |
|---|---|---:|
| gogn/undantekningar/1-handgerd-mynstur.txt (áður extra_beta.txt) | Handgerð orðskiptimynstur | 78 |
| gogn/undantekningar/2-yfirfarin.txt (áður extra_review.txt) | Leiðrétt orð á mynstrasniði | 87 |
| gogn/undantekningar/3-gull.txt (áður extra_gold.txt) | Undantekningamynstur | 2.695 |

Allar þrjár skrárnar eru á Liang/libhyphen-mynstrasniði, ekki venjulegir orðalistar.

Dæmi um snið:

```text
.s8j8ó9b8i8r8t...
```

Skrárnar eru ekki almenn trauststig fyrir ný orð.

Ekki skal setja nýjar orðatillögur beint í þessar skrár.

ChatGPT skal ekki breyta mynsturskránum beint í hefðbundnu orðasöfnunarferli.

Claude sér um að yfirfara tillögur, umbreyta staðfestum gögnum í mynstur og prófa áhrif þeirra.

## 6. Nýjar orðatillögur

Nota skal sérstaka skrá:

`tillogur.tsv`

Skráin er ekki hluti af sjálfvirku byggingarferli orðskiptivélarinnar.

### Gagnasnið

- UTF-8.
- Unicode NFC.
- Tab-separated values (TSV).
- Ein orðmynd í hverri línu.
- Fimm dálkar í fastri röð.
- Engar Markdown-töflur.
- Engar skýringar utan gagnasniðsins þegar verið er að skila orðalotu.
- Engar tvíteknar færslur.

Dálkar:

```text
orð	skipting	orðhlutar	heimild	öryggi
```

### Skilgreining dálka

**orð**

Rétt stafsett íslensk orðmynd án innsettra skiptimerkja.

**skipting**

Orðið með bandstrikum á öllum þeim stöðum þar sem línuskipting er talin leyfileg samkvæmt ritreglum.

Ef skipting er óleyst skal reiturinn vera auður.

Þegar bandstrik eru fjarlægð úr tillögu fyrir orð sem inniheldur ekki bandstrik að uppruna skal niðurstaðan vera nákvæmlega sama orð og í fyrsta dálki.

Orð með upprunalegum bandstrikum skulu fara í sérstaka yfirferð þar til skilgreint hefur verið hvernig þau eru skráð.

**orðhlutar**

Málfræðilegir orðhlutar aðskildir með plúsmerki.

Ekki rugla þessum dálki saman við leyfilega skiptistaði.

**heimild**

Raunverulega skoðuð heimild, helst með nákvæmri tilvísun eða slóð.

Ef engin ytri heimild hefur verið skoðuð skal skrá `óstaðfest`.

**öryggi**

Eitt af eftirfarandi gildum:

- `hátt`
- `miðlungs`
- `lágt`

Öryggi er mat á tillögunni en ekki formleg staðfesting á réttmæti hennar.

### Sniðdæmi

```tsv
orð	skipting	orðhlutar	heimild	öryggi
maðkaveiðimaður		maðka+veiði+maður	óstaðfest	miðlungs
strætisvagnabílstjóri		strætis+vagna+bíl+stjóri	óstaðfest	miðlungs
skráningarskylda		skráningar+skylda	óstaðfest	miðlungs
```

Dæmin sýna gagnasniðið. Þau eru ekki staðfest þjálfunargögn.

## 7. Sjálfvirk yfirferð tillagna

Claude skal þróa vinnuferli sem:

1. Les `tillogur.tsv`.
2. Staðfestir gagnasniðið.
3. Samræmir Unicode.
4. Fjarlægir tvítekningar.
5. Ber orð saman við fyrirliggjandi þjálfunargögn.
6. Keyrir núverandi orðskiptivél á orðin.
7. Ber niðurstöðuna saman við tillöguna.
8. Flokkar niðurstöður.
9. Skilar skýrslu um ágreining og ný orð.

### Flokkun niðurstaðna

- **SAMHLJÓÐA:** Vélin og tillagan gefa sömu niðurstöðu.
- **ÓSAMMÁLA:** Vélin og tillagan gefa ólíka niðurstöðu.
- **NÝTT:** Orðið er ekki í fyrirliggjandi þjálfunargögnum.
- **FYRIRLIGGJANDI:** Orðið er þegar í gagnasafninu.
- **ÓLEYST:** Engin fullunnin orðskipting liggur fyrir.
- **ÓGILT:** Villa í orðinu eða gagnasniðinu.

Flokkarnir geta skarast. Orð getur til dæmis verið bæði NÝTT og SAMHLJÓÐA.

SAMHLJÓÐA þýðir ekki að skipting sé málfræðilega staðfest.

Engin tillaga fer sjálfkrafa í mynsturskrárnar vegna þess eins að hún samræmist niðurstöðu vélarinnar.

## 8. Söfnun nýrra orða

Leita skal sérstaklega að:

- Nýyrðum.
- Samsettum orðum.
- Löngum orðum.
- Sjaldgæfum beygingarmyndum.
- Orðum með flókna stofngerð.
- Orðum sem núverandi vél skiptir rangt.
- Orðum úr raunverulegum íslenskum textum.
- Orðum sem reyna á veikleika orðskiptimynstranna.

### Málaflokkar

- Almenn íslenska.
- Stjórnsýsla og stjórnmál.
- Lögfræði.
- Fjármál og bankastarfsemi.
- Heilbrigðismál.
- Sjávarútvegur.
- Landbúnaður.
- Veiði og útivist.
- Byggingariðnaður.
- Verkfræði.
- Upplýsingatækni.
- Gervigreind.
- Orkumál.
- Umhverfismál.
- Hönnun og prentvinnsla.
- Menning og listir.
- Íslensk örnefni.

Forgangsraða skal orðum sem koma fyrir í raunverulegri málnotkun.

Ekki framleiða þúsundir óþarfa tilbúinna samsetninga eingöngu til að fjölga færslum.

## 9. Orðafjölskyldur og beygingarmyndir

Greina skal skyld orð og mismunandi beygingarmyndir.

Dæmi um orðafjölskyldu:

```text
sjóbirtingur
sjóbirting
sjóbirtingi
sjóbirtings
sjóbirtingurinn
sjóbirtinginn
sjóbirtingnum
sjóbirtingar
sjóbirtingum
sjóbirtinga
```

Ekki skal gera ráð fyrir að rétt skipting einnar beygingarmyndar yfirfærist sjálfkrafa á aðrar beygingarmyndir.

Nýta skal staðfestar beygingarheimildir.

Sérstaklega skal leita að mynstrum sem geta leyst heilar orðafjölskyldur í stað þess að bæta við undantekningu fyrir hverja einstaka beygingarmynd.

## 10. GitHub og endurbygging

**Staða (27.11.2026):** Byggingargögn, tól og prófunarsöfn eru komin í GitHub. `make build` endurbyggir útgáfu 1.8 og skráin er bæti fyrir bæti eins og útgefna skráin.

| Skipun | Hvað hún gerir |
|---|---|
| `make build` | Byggir `smidi/hyph_is_IS.dic` og ber saman við `utgafa/hyph_is_IS.dic` |
| `make test` | Þjálfar samanburðarútgáfu án prófunarfjölskyldna og mælir hana |
| `make yfirfara` | Yfirfer `tillogur.tsv` og skrifar `smidi/yfirferd.tsv` |
| `make all` | build + test (um 1,5 mín.) |

Krefst `patgen`, `iconv`, `python3` og `libhyphen`. `substrings.pl` er útfært í `tools/subst.py` (sama aðferð, hámarksregla).

GitHub-verkefnið skal innihalda, eftir því sem leyfi heimila:

- Upprunaleg þjálfunargögn eða rekjanlegt niðurhalsferli.
- Núverandi mynsturskrár.
- Python-skriftur.
- patgen-stillingar.
- Translate-skrá.
- substrings.pl.
- Prófunarskriftur.
- Föst prófunarsöfn.
- tillogur.tsv.
- Verkefnislýsingar.
- Leyfi og heimildatilvísanir.
- Leiðbeiningar um endurbyggingu.

Ein skipun skal geta endurbyggt orðskiptiskrána og keyrt prófanir.

Tillaga:

```bash
make build
make test
make all
```

Nákvæm útfærsla er á ábyrgð Claude.

Markmiðið er að hægt sé að endurbyggja verkefnið frá grunni án þess að reiða sig á tímabundið vinnusvæði eða minni úr einstöku spjalli.

## 11. Fast óháð prófunarsafn — forgangsverkefni

**Staða (27.11.2026):** Prófunarsöfnin eru til, `gogn/prof/throun.txt` og `gogn/prof/lokaprof.txt`.

- Uppruni: orðalisti Árnastofnunar 2.0.
- Aðferð: `tools/ohad.py` flokkar orð í fjölskyldur (nálgaður stofn, beygingarendingar teknar af) og velur 2% fjölskyldna í hvort safn með föstu SHA-1-tætigildi. Sama fjölskylda lendir alltaf í sama safni.
- Allar orðmyndir þessara fjölskyldna eru teknar úr þjálfun og undantekningum samanburðarútgáfunnar (10.692 færslur og 113 undantekningar).
- `make` stöðvast ef prófunarsöfnin breytast.
- Takmörkun: fjölskyldugreiningin er nálgun og ekki byggð á BÍN-uppflettimyndum. Skyld orð með ólíkar endingar geta lent sitt hvorum megin. Stefnt er að BÍN-flokkun síðar.

Skipta skal gögnum í þrjú aðskilin söfn:

### Þjálfunarsafn

Gögn sem notuð eru til að mynda mynstur og undantekningar.

### Þróunarprófunarsafn

Gögn sem notuð eru til að meta breytingar og fínstilla orðskiptivélina.

### Óháð lokaprófunarsafn

Fast gagnasafn sem er ekki notað til þjálfunar, gerðar undantekninga eða fínstillingar.

Halda skal heilum orðafjölskyldum utan þjálfunar eftir því sem hægt er.

Ekki nægir að fjarlægja eina beygingarmynd ef allar aðrar beygingarmyndir sama orðs eru í þjálfunargögnum.

Skrá skal:

- Uppruna prófunargagna.
- Aðferð við skiptingu gagnasafna.
- Fjölda orða og orðafjölskyldna.
- Útgáfu prófunarsafns.
- Viðmiðunarniðurstöður.
- Mögulega skörun við þjálfunargögn.

Viðmiðunarprófun á núverandi útgáfu 1.8 skal fara fram áður en frekari orðalotur eru teknar inn.

Þar sem útgáfa 1.8 hefur þegar verið þjálfuð á orðalista Árnastofnunar er ekki sjálfkrafa hægt að líta á undirhluta þess lista sem áður óséð gögn fyrir þá útgáfu.

Nota þarf ný, yfirfarin prófunargögn eða endurbyggja samanburðarútgáfu með föstu útilokunarsafni.

## 12. Gæðamælingar

Uppgefin viðmið útgáfu 1.8:

| Mæling | Niðurstaða |
|---|---:|
| Heil orð rétt utan þjálfunar í fyrri keyrslu | 94,2% |
| **Fast lokaprófunarsafn (4.453 orð, 3.308 fjölskyldur)** | **93,9%** |
| Sama mæling í útgáfu 1.7 | 92,5% |
| Samhljóðabrot í prófuðum textum | 0 |
| Samsvörun við grunnlista Árnastofnunar | 100% |
| Fjöldi orða í grunnlista | 218.308 |
| Stærð orðskiptiskrár | Um 1,9 MB |

100% samsvörun við grunnlista Árnastofnunar er samræmispróf á þjálfunargögnum, ekki sjálfstæð gæðamæling.

94,2% er niðurstaða úr fyrri keyrslu en ekki niðurstaða úr föstu óháðu lokaprófunarsafni.

### Viðmiðun 1.8 á föstum prófunarsöfnum (`make test`)

| Safn | Orð | Heil orð rétt | Nákvæmni | Heimt | Rangir | Vantar | Samhljóðabrot |
|---|---:|---:|---:|---:|---:|---:|---:|
| Þróun | 4.255 | 93,9% | 98,46% | 96,59% | 97 | 219 | 26 |
| Lokapróf | 4.453 | 93,9% | 98,31% | 96,79% | 112 | 216 | 33 |

Mælt á samanburðarútgáfu sem er þjálfuð með sömu aðferð og 1.8 en án prófunarfjölskyldnanna. Samhljóðabrot hér eru brot sem vélin myndar í orðum úr gögnum Árnastofnunar, ekki í raunverulegum texta.

### Mælingar fyrir hverja útgáfu

- Hlutfall heilla orða rétt.
- Rangir skiptistaðir.
- Leyfilegir skiptistaðir sem vantar.
- Nákvæmni skiptistaða (precision).
- Heimt skiptistaða (recall).
- Samhljóðabrot.
- Afturför í áður réttum orðum.
- Árangur á óþekktum samsettum orðum.
- Árangur á óþekktum orðafjölskyldum.
- Fjöldi undantekninga.
- Fjöldi mynstra.
- Stærð orðskiptiskrár.

Leggja skal meiri áherslu á að forðast ranga skiptistaði en að finna alla mögulega skiptistaði.

Fast prófunarsafn skal ekki verða að óbeinum þjálfunargögnum með endurtekinni fínstillingu út frá niðurstöðum einstakra orða.

## 13. Tæknilegar takmarkanir

Orðskiptivélin hefur takmarkaða getu.

- patgen hefur takmarkaða vinnslugetu.
- Undantekningar stækka orðskiptiskrána.
- Of almenn mynstur geta skapað nýjar villur.
- Fleiri mynstur þýða ekki sjálfkrafa betri orðskiptingu.
- Núverandi orðskiptiskrá er um 1,9 MB.

Sérstaklega skal gæta að:

- Hámarksreglu við sameiningu mynstra.
- Réttum íslenskum stöfum.
- Unicode-samræmingu.
- Keyrslu substrings.pl.
- Árekstrum mynstra.
- Árekstrum undantekninga.
- Afturför.
- Óþarfa skráarstækkun.

Forgangsraða skal hnitmiðuðum, vel prófuðum mynstrum sem leysa fleiri en eina orðmynd.

Undantekningar eru nauðsynlegar þegar almenn mynstur duga ekki, en þær skulu ekki vera sjálfgefin lausn við öllum villum.

## 14. Samvinna ChatGPT og Claude

### ChatGPT

Ber ábyrgð á:

- Söfnun nýrra orða.
- Málfræðilegri greiningu.
- Tillögum að orðskiptingu.
- Greiningu orðhluta.
- Sannprófun beygingarmynda.
- Heimildavinnu.
- Óháðri yfirferð.
- Gerð raunhæfra prófunartexta.
- Skilum á föstu TSV-sniði.

ChatGPT skilar tillögum en breytir ekki byggingargögnum beint.

### Claude

Ber ábyrgð á:

- GitHub-verkefninu.
- Tæknilegri útfærslu.
- Gagnavinnslu.
- Sjálfvirkri yfirferð tillagna.
- Samanburði við orðskiptivél.
- Mynsturskrám.
- Þjálfun.
- Endurbyggingu.
- Prófunum.
- Gæðamælingum.
- Útgáfustýringu.

### Tryggvi

Ber ábyrgð á:

- Raunverulegri prófun í InDesign.
- Söfnun villna úr umbrotavinnu.
- Forgangsröðun verkefnisins.
- Útgáfu og dreifingu.
- Ákvörðunum um breytingar á verkefninu.

### Samskipti í gegnum GitHub

GitHub er sameiginlegt vinnusvæði. Ekki þarf að líma skrár á milli spjalla.

1. ChatGPT setur lotu í `lotur/NNN-heiti.tsv` á grein `lota-NNN` og opnar pull request á `main`. Það breytir engu öðru, hvorki `gogn/`, `tools/` né `Makefile`.
2. Tryggvi segir Claude: „lota NNN er komin“.
3. Claude sækir greinina, keyrir yfirferðina, skrifar `lotur/NNN-heiti-yfirferd.tsv` og setur niðurstöðuna sem athugasemd í pull requestið.
4. ChatGPT les athugasemdina og svarar þar, eða gerir nýja útgáfu af lotunni á sömu grein.
5. Þegar lotan er samþykkt sameinar Claude hana í `main` og gerir mynsturbreytingar í sérstakri grein með mælingum.

### Óháð yfirferð

ChatGPT og Claude skulu eftir því sem hægt er greina orð óháð hvort öðru áður en niðurstöður eru bornar saman.

Samkomulag tveggja líkana er ekki sönnun um málfræðilegt réttmæti.

Ágreiningur skal leiða til frekari yfirferðar samkvæmt ritreglum og heimildum.

## 15. Vinna í lotum

Vinna skal í afmörkuðum orðalotum.

Hver lota skal:

1. Hafa skilgreindan uppruna eða málaflokk.
2. Vera á föstu TSV-sniði.
3. Vera yfirfarin með tilliti til orðmynda.
4. Vera laus við tvítekningar innan lotunnar.
5. Vera borin saman við fyrirliggjandi gögn.
6. Vera prófuð gegn núverandi vél.
7. Vera metin áður en hún fer í þjálfun.

Byrja skal með litlar lotur, til dæmis 100 orð, þar til vinnuferlið hefur verið sannreynt.

Stækka má loturnar í 500–1.000 orð þegar gæði og gagnavinnsla hafa verið staðfest.

Ekki skal bæta allri lotunni sjálfkrafa við þjálfunargögnin.

## 16. Raunverulegar prófanir

Prófa skal reglulega í InDesign með:

- Tímaritum.
- Bókum.
- Dagblöðum.
- Ársskýrslum.
- Stjórnsýsluskjölum.
- Fræðitextum.
- Mismunandi dálkabreiddum.
- Mismunandi leturstærðum.
- Jöfnuðum texta.

Villur úr raunverulegri umbrotavinnu hafa sérstakt vægi.

Halda skal utan um orðið, skiptingu vélarinnar og staðfesta leiðréttingu.

## 17. Forgangsröðun

### Áfangi 1 — Undirbúningur

- Setja byggingargögn og tól í GitHub.
- Tryggja rekjanleg leyfi.
- Útbúa endurbyggingarskipun.
- Útbúa fast prófunarsafn.
- Mæla viðmiðunarárangur.

### Áfangi 2 — Vinnuferli

- Skilgreina tillogur.tsv.
- Útbúa sjálfvirkan samanburð.
- Prófa 100 orða lotu.
- Yfirfara niðurstöður beggja líkana.
- Staðfesta gagnasnið og gæðakröfur.

### Áfangi 3 — Orðasöfnun

- Vinna kerfisbundið eftir málaflokkum.
- Safna nýjum og erfiðum orðum.
- Greina orðafjölskyldur.
- Finna veikleika núverandi mynstra.

### Áfangi 4 — Þjálfun og útgáfa

- Bæta við staðfestum þjálfunargögnum.
- Þróa almenn mynstur.
- Lágmarka óþarfa undantekningar.
- Keyra samanburðarprófanir.
- Prófa í InDesign.
- Gefa út þegar mælanlegar framfarir liggja fyrir.

## 18. Langtímamarkmið

- Ná að minnsta kosti 99% réttum heilum orðum í skilgreindu óháðu prófunarsafni.
- Halda röngum skiptistöðum í lágmarki.
- Viðhalda núlli samhljóðabrota í prófuðum textum.
- Bæta getu til að skipta óþekktum samsettum orðum.
- Draga úr þörf fyrir einstakar undantekningar.
- Halda stærð og flækjustigi orðskiptiskrár í skefjum.
- Tryggja sjálfstæða, endurtakanlega þróun.

99% er þróunarmarkmið en ekki staðfestur núverandi árangur.

---

Við erum ekki að reyna að skrá öll hugsanleg íslensk orð.

Við erum að byggja upp orðskiptivél sem getur skipt íslenskum orðum sem hún hefur aldrei séð áður.

**Gæði fram yfir magn. Málfræði fram yfir ágiskanir. Mælanlegar framfarir fram yfir fjölda orða.**
