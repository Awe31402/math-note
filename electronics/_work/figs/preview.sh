#!/bin/bash
# preview.sh <prefix> -> render figures/<prefix>-*.svg to PNG and join into _work/png/<prefix>-all.png
cd "$(dirname "$0")/../.."
fs=()
for f in figures/$1-*.svg; do p=_work/png/$(basename ${f%.svg}).png; inkscape "$f" -o "$p" -w 420 2>/dev/null; fs+=("$p"); done
convert "${fs[@]}" -background white -alpha remove -splice 30x0 +append _work/png/$1-all.png
echo _work/png/$1-all.png
