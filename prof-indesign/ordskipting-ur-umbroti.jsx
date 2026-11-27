#target indesign

// Les samsettar línur í megintexta og skráir skipt orð.
// Engar breytingar eru gerðar á skjalinu.
(function () {
    function isLetter(character) {
        return typeof character === "string" && character.length > 0 &&
            character.toLowerCase() !== character.toUpperCase();
    }

    function isWordCharacter(character) {
        return isLetter(character) ||
            (typeof character === "string" && /^[\u0300-\u036f]$/.test(character));
    }

    function isTypedHyphen(character) {
        return typeof character === "string" && /^[-\u00ad\u2010\u2011]$/.test(character);
    }

    function splitWord(characters, offset) {
        if (offset <= 0 || offset >= characters.length) return null;

        var before = characters.item(offset - 1).contents;
        var after = characters.item(offset).contents;
        if (!isWordCharacter(before) || !isLetter(after)) return null;

        var left = [];
        var right = [];
        var i;
        for (i = offset - 1; i >= 0; i--) {
            var previous = characters.item(i).contents;
            if (!isWordCharacter(previous)) break;
            left.unshift(previous);
        }
        if (i >= 0 && isTypedHyphen(characters.item(i).contents)) return null;

        for (i = offset; i < characters.length; i++) {
            var next = characters.item(i).contents;
            if (!isWordCharacter(next)) break;
            right.push(next);
        }
        if (i < characters.length && isTypedHyphen(characters.item(i).contents)) return null;

        var first = left.join("");
        var last = right.join("");
        return [first + last, first + "-" + last];
    }

    function linePage(line) {
        var frames = line.parentTextFrames;
        if (!frames.length) return null;
        var page = frames[0].parentPage;
        return page && page.isValid ? page : null;
    }

    function cleanField(value) {
        return String(value).replace(/[\t\r\n]/g, " ");
    }

    function collect(document) {
        var rows = [];
        var stories = document.stories.everyItem().getElements();
        for (var s = 0; s < stories.length; s++) {
            var story = stories[s];
            var lines = story.lines.everyItem().getElements();
            var characters = story.characters;
            for (var i = 0; i + 1 < lines.length; i++) {
                var line = lines[i];
                var following = lines[i + 1];
                var offset = following.insertionPoints.firstItem().index;
                if (line.insertionPoints.lastItem().index !== offset) continue;
                var word = splitWord(characters, offset);
                if (!word) continue;

                var page = linePage(line);
                if (!page || !linePage(following)) continue;
                rows.push({
                    page: page.name,
                    pageOrder: page.documentOffset,
                    storyOrder: s,
                    textOrder: offset,
                    word: word[0],
                    split: word[1]
                });
            }
        }
        rows.sort(function (a, b) {
            return a.pageOrder - b.pageOrder || a.storyOrder - b.storyOrder ||
                a.textOrder - b.textOrder;
        });
        return rows;
    }

    if (!app.documents.length) {
        alert("Opnaðu InDesign-skjal áður en skriftan er keyrð.");
        return;
    }

    try {
        var doc = app.activeDocument;
        var rows = collect(doc);
        var file = File.saveDialog("Vista orðskiptingar sem TSV");
        if (!file) return;
        if (!/\.tsv$/i.test(file.name)) file = new File(file.fsName + ".tsv");
        if (file.exists && !confirm("Skráin er þegar til. Á að skrifa yfir hana?")) return;
        file.encoding = "UTF-8";
        file.lineFeed = "Unix";
        if (!file.open("w")) throw new Error(file.error || "Ekki tókst að opna TSV-skrána.");
        try {
            if (!file.writeln("blaðsíða\torð\tskipting")) throw new Error(file.error);
            for (var r = 0; r < rows.length; r++) {
                var row = rows[r];
                if (!file.writeln([cleanField(row.page), row.word, row.split].join("\t"))) {
                    throw new Error(file.error);
                }
            }
        } finally {
            file.close();
        }
        alert("Vistaðar orðskiptingar: " + rows.length + "\n" + file.fsName);
    } catch (error) {
        alert("Ekki tókst að flytja út orðskiptingar.\n" + error.message);
    }
})();
