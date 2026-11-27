# Íslensk orðskipting — endurbygging og prófanir
# make build   byggir smidi/hyph_is_IS.dic og ber saman við utgafa/hyph_is_IS.dic
# make test    þjálfar samanburðarútgáfu án prófunarfjölskyldna og mælir hana
# make yfirfara  yfirfer tillogur.tsv
# make all     build + test
PY=python3 -I
B=smidi
UND=gogn/undantekningar/1-handgerd-mynstur.txt gogn/undantekningar/2-yfirfarin.txt gogn/undantekningar/3-gull.txt

all: build test

$(B):
	mkdir -p $(B)

# patgen vinnur með 8-bita stafi (latin-1)
$(B)/%.latin1: gogn/%.txt | $(B)
	iconv -f utf-8 -t latin1 $< > $@

$(B)/thjalfun-samanburdur.txt: gogn/arnastofnun.txt gogn/thjalfun.txt tools/ohad.py | $(B)
	$(PY) tools/ohad.py gogn/arnastofnun.txt gogn/thjalfun.txt $(B)
	cmp -s $(B)/lokaprof.txt gogn/prof/lokaprof.txt || (echo "VILLA: lokaprófunarsafn hefur breyst"; exit 1)
	cmp -s $(B)/throun.txt gogn/prof/throun.txt || (echo "VILLA: þróunarsafn hefur breyst"; exit 1)

$(B)/thjalfun-samanburdur.latin1: $(B)/thjalfun-samanburdur.txt
	iconv -f utf-8 -t latin1 $< > $@

$(B)/%.tex: $(B)/%.latin1
	cd $(B) && patgen $*.latin1 ../gogn/patgen/empty.pat $*.tex ../gogn/patgen/translate.tr < ../gogn/patgen/stillingar.txt > $*.log 2>&1
	! grep -q capacity $(B)/$*.log || (echo "VILLA: patgen fór yfir getu"; exit 1)

$(B)/undantekningar.txt: $(UND) | $(B)
	cat $(UND) > $@

$(B)/undantekningar-samanburdur.txt: $(B)/undantekningar.txt gogn/prof/lokaprof.txt gogn/prof/throun.txt
	$(PY) tools/sia.py $< $@ gogn/prof/lokaprof.txt gogn/prof/throun.txt

$(B)/hyph_is_IS.dic: $(B)/thjalfun.tex $(B)/undantekningar.txt
	$(PY) tools/pat2dic.py $< $(B)/hrátt.dic $(B)/undantekningar.txt
	$(PY) tools/subst.py $(B)/hrátt.dic $@ > /dev/null

$(B)/samanburdur.dic: $(B)/thjalfun-samanburdur.tex $(B)/undantekningar-samanburdur.txt
	$(PY) tools/pat2dic.py $< $(B)/samanburdur-hrátt.dic $(B)/undantekningar-samanburdur.txt
	$(PY) tools/subst.py $(B)/samanburdur-hrátt.dic $@ > /dev/null

build: $(B)/hyph_is_IS.dic
	@cmp -s $< utgafa/hyph_is_IS.dic && echo "build: eins og útgefin skrá (utgafa/hyph_is_IS.dic)" || echo "build: FRÁBRUGÐIN útgefinni skrá"

test: $(B)/samanburdur.dic
	@echo "== Samanburðarútgáfa, þjálfuð án prófunarfjölskyldna =="
	@$(PY) tools/prof.py $< gogn/prof/throun.txt gogn/prof/lokaprof.txt
	@echo "== Útgefin skrá á villum úr raunverulegum textum =="
	@$(PY) tools/prof.py $(B)/hyph_is_IS.dic gogn/prof/textavillur.txt

yfirfara: $(B)/hyph_is_IS.dic
	$(PY) tools/yfirfara.py tillogur.tsv $(B)/hyph_is_IS.dic gogn/arnastofnun.txt gogn/thjalfun.txt > $(B)/yfirferd.tsv
	@echo "Skýrsla: $(B)/yfirferd.tsv"

clean:
	rm -rf $(B)

.PHONY: all build test yfirfara clean
.SECONDARY:
