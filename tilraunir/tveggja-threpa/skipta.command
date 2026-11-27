#!/bin/sh
# Setur A.dic, B.dic eða 1.8.dic inn sem íslenska orðskiptiskrá í öllum InDesign-útgáfum.
# Notkun í Terminal:  sudo sh skipta.command A   (eða B, eða 1.8 til að fara aftur í útgefna skrá)
set -u
v=${1:-}; here="$(cd "$(dirname "$0")" && pwd)"; src="$here/$v.dic"
[ -f "$src" ] || { echo "Notkun: sudo sh skipta.command A|B|1.8"; exit 1; }
[ "$(id -u)" = 0 ] || { echo "Keyrðu með sudo."; exit 1; }
pgrep -x 'Adobe InDesign' >/dev/null && { echo "Lokaðu InDesign fyrst."; exit 1; }
n=0
for app_root in "/Applications/Adobe InDesign "20*; do
  b="$app_root/Resources/Dictionaries/LILO/Linguistics/Providers/Plugins2/AdobeHunspellPlugin.bundle"
  d="$b/Contents/SharedSupport/Dictionaries/is_IS"
  [ -d "$d" ] || continue
  install -m 644 "$src" "$d/hyph_is_IS.dic" && codesign --force --sign - "$b" >/dev/null 2>&1 && codesign --verify --strict "$b" \
    && { echo "$app_root: $v sett inn"; n=$((n+1)); } || echo "$app_root: MISTÓKST"
done
[ $n -gt 0 ] || echo "Engin InDesign-útgáfa með íslenskri orðskiptingu fannst."
