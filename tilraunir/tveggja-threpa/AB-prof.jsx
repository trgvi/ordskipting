// A/B-próf á íslenskri orðskiptingu. Býr til skjal með sömu orðum í mjóum römmum af ólíkri breidd.
#target indesign
(function () {
    var W = ["innviðaáskrift","mótherjaárás","vírusvörn","vírusvarnarforrit","bætakóði",
             "hvalsaga","tölvuleikjaframleiðandi","strætisvagnabílstjóri","maðkaveiðimaður",
             "sjóbirtingur","veiðimaður"];
    var lang = app.languagesWithVendors.itemByName("Icelandic");
    if (!lang.isValid) { alert("Íslensk orðskipting fannst ekki."); return; }
    // Hvaða skrá er uppsett? B hefur NEXTLEVEL.
    var útg = "?";
    try {
        var f = File(app.filePath.fsName + "/Resources/Dictionaries/LILO/Linguistics/Providers/Plugins2/AdobeHunspellPlugin.bundle/Contents/SharedSupport/Dictionaries/is_IS/hyph_is_IS.dic");
        f.encoding = "UTF-8";
        if (f.open("r")) { var s = f.read(); f.close(); útg = s.indexOf("NEXTLEVEL") >= 0 ? "B (tveggja þrepa)" : (s.indexOf("a9k8ó2ð") >= 0 ? "A (núverandi)" : "1.8"); }
    } catch (e) {}
    var doc = app.documents.add();
    doc.viewPreferences.horizontalMeasurementUnits = MeasurementUnits.MILLIMETERS;
    doc.viewPreferences.verticalMeasurementUnits = MeasurementUnits.MILLIMETERS;
    doc.documentPreferences.pageWidth = 297; doc.documentPreferences.pageHeight = 210;
    try { var dl = doc.languages.itemByName("Icelandic"); if (dl.isValid) dl.hyphenationVendor = "Hunspell"; } catch (e) {}
    var ps = doc.paragraphStyles.add({ name: "AB-próf" });
    ps.properties = { appliedLanguage: lang, pointSize: 14, leading: 17, hyphenation: true,
        hyphenateWordsLongerThan: 5, hyphenateAfterFirst: 2, hyphenateBeforeLast: 3,
        hyphenateLadderLimit: 0, hyphenationZone: 0, hyphenateCapitalizedWords: true,
        justification: Justification.LEFT_ALIGN, composer: "$ID/HL Single", spaceAfter: 4 };
    var pg = doc.pages[0];
    var t = pg.textFrames.add({ geometricBounds: [8, 10, 18, 287], contents: "Uppsett skrá: " + útg });
    t.texts[0].pointSize = 12;
    var x = 10, widths = [16, 19, 22, 26, 31, 37, 45];
    for (var i = 0; i < widths.length; i++) {
        var fr = pg.textFrames.add({ geometricBounds: [22, x, 205, x + widths[i]] });
        fr.contents = W.join("\r");
        fr.parentStory.texts[0].applyParagraphStyle(ps, true);
        fr.strokeWeight = 0.25; fr.strokeColor = doc.swatches.itemByName("Black");
        var lab = pg.textFrames.add({ geometricBounds: [18, x, 22, x + widths[i]], contents: widths[i] + " mm" });
        lab.texts[0].pointSize = 7;
        x += widths[i] + 4;
    }
})();
