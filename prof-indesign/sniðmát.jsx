// Prófunarskjal fyrir íslenska orðskiptingu í InDesign.
// Búið til með prof-indesign/mynda.py úr ord.txt, texti.txt og lotum. Ekki breyta gögnunum hér; breyttu ord.txt og keyrðu mynda.py.
#target indesign
(function () {
    var D = /*GÖGN*/null;
    var lang = app.languagesWithVendors.itemByName("Icelandic");
    if (!lang.isValid) { alert("Íslensk orðskipting fannst ekki í InDesign."); return; }

    // Hvaða orðskiptiskrá er uppsett?
    var utg = "óþekkt";
    try {
        var f = File(app.filePath.fsName + "/Resources/Dictionaries/LILO/Linguistics/Providers/Plugins2/AdobeHunspellPlugin.bundle/Contents/SharedSupport/Dictionaries/is_IS/hyph_is_IS.dic");
        f.encoding = "UTF-8";
        if (f.open("r")) { var s = f.read(3000000); f.close();
            utg = (s.indexOf("NEXTLEVEL") >= 0 ? "1.9 eða nýrri (tveggja þrepa)" : "1.8 eða eldri (eitt þrep)") + ", " + Math.round(f.length / 1024) + " KB"; }
    } catch (e) {}

    var oldUI = app.scriptPreferences.userInteractionLevel;
    app.scriptPreferences.userInteractionLevel = UserInteractionLevels.NEVER_INTERACT;
    var doc = app.documents.add();
    try {
        with (doc.viewPreferences) { horizontalMeasurementUnits = MeasurementUnits.MILLIMETERS; verticalMeasurementUnits = MeasurementUnits.MILLIMETERS; }
        with (doc.documentPreferences) { facingPages = false; pageWidth = 210; pageHeight = 297; }
        try { var dl = doc.languages.itemByName("Icelandic"); if (dl.isValid) { dl.hyphenationVendor = "Hunspell"; dl.doubleQuotes = "„“"; } } catch (e) {}
        try { doc.textDefaults.appliedLanguage = lang; } catch (e) {}

        function font(st, name) { try { st.appliedFont = name; } catch (e) {} }
        function style(name, p) { var st = doc.paragraphStyles.add({ name: name }); p.appliedLanguage = lang; st.properties = p; font(st, "Minion Pro\tRegular"); return st; }
        var S = {
            titill: style("Titill", { pointSize: 22, leading: 26, hyphenation: false, spaceAfter: 4 }),
            kafli: style("Kafli", { pointSize: 13, leading: 16, hyphenation: false }),
            smatt: style("Smátt", { pointSize: 8, leading: 10.5, hyphenation: false }),
            ord: style("Orðalisti", { pointSize: 11, leading: 13, hyphenation: true, hyphenateWordsLongerThan: 5,
                hyphenateAfterFirst: 2, hyphenateBeforeLast: 3, hyphenateLadderLimit: 0, hyphenationZone: 0,
                hyphenateCapitalizedWords: true, justification: Justification.LEFT_ALIGN, composer: "$ID/HL Single", spaceAfter: 2.5 }),
            meg: style("Meginmál", { pointSize: 9.5, leading: 12.5, hyphenation: true, hyphenateWordsLongerThan: 5,
                hyphenateAfterFirst: 2, hyphenateBeforeLast: 3, hyphenateLadderLimit: 3, hyphenateCapitalizedWords: true,
                justification: Justification.LEFT_JUSTIFIED, composer: "$ID/HL Composer", spaceAfter: 3 }),
            vaent: style("Vænt skipting", { pointSize: 8, leading: 10.5, hyphenation: false })
        };
        S.vaent.tabStops.add({ position: 58 }); S.vaent.tabStops.add({ position: 116 }); S.vaent.tabStops.add({ position: 172 });
        try { S.vaent.appliedFont = "Minion Pro\tRegular"; } catch (e) {}

        var first = true;
        function page() { if (first) { first = false; return doc.pages[0]; } return doc.pages.add(LocationOptions.AT_END); }
        function box(pg, x, y, w, h, txt, st) {
            var fr = pg.textFrames.add({ geometricBounds: [y, x, y + h, x + w] });
            fr.contents = txt; fr.parentStory.texts[0].applyParagraphStyle(st, true); return fr;
        }
        function flow(fr, x, y, w, h) { // bætir við síðum þar til textinn kemst fyrir
            var n = 0;
            while (fr.overflows && n < 200) { var p = doc.pages.add(LocationOptions.AT_END); var nf = p.textFrames.add({ geometricBounds: [y, x, y + h, x + w] });
                if (fr.textFramePreferences.textColumnCount > 1) { nf.textFramePreferences.textColumnCount = fr.textFramePreferences.textColumnCount; nf.textFramePreferences.textColumnGutter = fr.textFramePreferences.textColumnGutter; }
                fr.nextTextFrame = nf; fr = nf; n++; }
        }
        var d = new Date();
        var dags = d.getDate() + "." + (d.getMonth() + 1) + "." + d.getFullYear();
        var n = 0; for (var i = 0; i < D.kaflar.length; i++) n += D.kaflar[i][1].length;

        // Forsíða
        var p0 = page();
        box(p0, 15, 15, 180, 12, "Prófunarskjal: íslensk orðskipting", S.titill);
        box(p0, 15, 30, 180, 60,
            "Uppsett orðskipting: " + utg + "\rInDesign " + app.version + " · búið til " + dags + " · " + n + " orð í " + D.kaflar.length + " köflum\r\r" +
            "Orðin eru sett í sex mjóa ramma (16–43 mm) svo InDesign skipti þeim á sem flestum stöðum. Berðu skiptingarnar saman við listann „Vænt skipting“ aftast. " +
            "≠ merkir orð þar sem orðskiptiskráin og væntanleg skipting eru ósammála (Á = Árnastofnun, T = tillaga úr lotu).\r" +
            "Á eftir orðalistunum kemur samfelldur texti í þremur dálkum, tveimur dálkum og einum, jafnaður eins og í tímariti.\r\r" +
            "Til að endurgera skjalið með nýjum orðum: bættu í prof-indesign/ord.txt í GitHub og keyrðu mynda.py.", S.smatt);
        var y0 = 95;
        var toc = "Efni\r"; for (i = 0; i < D.kaflar.length; i++) toc += D.kaflar[i][0] + " (" + D.kaflar[i][1].length + ")\r";
        box(p0, 15, y0, 180, 180, toc + "Samfelldur texti\rVænt skipting", S.smatt);

        // Orðalistar
        var W = [16, 20, 24, 28, 34, 43], CH = 12;
        for (i = 0; i < D.kaflar.length; i++) {
            var ws = D.kaflar[i][1], parts = Math.ceil(ws.length / CH);
            for (var c = 0; c < parts; c++) {
                var pg = page(), chunk = ws.slice(c * CH, (c + 1) * CH).join("\r");
                box(pg, 15, 12, 180, 8, D.kaflar[i][0] + (parts > 1 ? "  (" + (c + 1) + "/" + parts + ")" : ""), S.kafli);
                var x = 15;
                for (var k = 0; k < W.length; k++) {
                    box(pg, x, 22, W[k], 4, W[k] + " mm", S.smatt);
                    var fr = box(pg, x, 27, W[k], 258, chunk, S.ord);
                    fr.strokeWeight = 0.25; try { fr.strokeColor = doc.swatches.itemByName("Black"); fr.strokeTint = 30; } catch (e) {}
                    x += W[k] + 3;
                }
            }
        }
        // Samfelldur texti
        var lay = [[3, "Þrír dálkar, jafnað"], [2, "Tveir dálkar, jafnað"], [1, "Einn dálkur, jafnað"]];
        for (i = 0; i < lay.length; i++) {
            var pt = page(); box(pt, 15, 12, 180, 8, "Samfelldur texti: " + lay[i][1], S.kafli);
            var wd = lay[i][0] == 1 ? 110 : 180;
            var tf = box(pt, 15, 24, wd, 258, D.texti.join("\r"), S.meg);
            tf.textFramePreferences.textColumnCount = lay[i][0]; tf.textFramePreferences.textColumnGutter = 5;
            flow(tf, 15, 24, wd, 258);
        }
        // Vænt skipting
        var t = "Orð\tVænt skipting (heimild)\tUppsett skrá við gerð skjals\t\r";
        for (i = 0; i < D.vaent.length; i++) {
            var r = D.vaent[i];
            if (r.length == 1) { t += "\r" + r[0] + "\r"; continue; }
            t += r[0] + "\t" + (r[1] ? r[1] + " (" + r[2] + ")" : "–") + "\t" + r[3] + "\t" + r[4] + "\r";
        }
        var pv = page(); box(pv, 15, 12, 180, 8, "Vænt skipting", S.kafli);
        var vf = box(pv, 15, 24, 180, 258, t, S.vaent);
        flow(vf, 15, 24, 180, 258);
        // Kaflaheiti feitletruð í listanum
        try {
            app.findGrepPreferences = NothingEnum.NOTHING; app.changeGrepPreferences = NothingEnum.NOTHING;
            app.findGrepPreferences.findWhat = "^[^\\t\\r]+$"; app.findGrepPreferences.appliedParagraphStyle = S.vaent;
            app.changeGrepPreferences.pointSize = 10;
            vf.parentStory.changeGrep();
            app.findGrepPreferences = NothingEnum.NOTHING; app.changeGrepPreferences = NothingEnum.NOTHING;
        } catch (e) {}

        var out = File(Folder.desktop + "/Prófunarskjal orðskiptingar.indd");
        doc.save(out);
        app.scriptPreferences.userInteractionLevel = oldUI;
        alert("Prófunarskjalið er tilbúið (" + doc.pages.length + " síður) og vistað á skjáborðinu:\r" + out.name + "\r\rUppsett orðskipting: " + utg);
    } catch (e) {
        app.scriptPreferences.userInteractionLevel = oldUI;
        alert("Villa við gerð prófunarskjals: " + e + " (lína " + e.line + ")");
    }
})();
