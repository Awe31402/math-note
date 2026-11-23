#!/bin/bash
# fetch_subs.sh -> download zh-TW (human) subtitles for every video in videos.txt into subs/<course>-<NN>-<id>.zh-TW.vtt, then make txt/
cd "$(dirname "$0")/.."
while IFS='|' read -r c n id dur title; do
  ls subs/$c-$n-*.vtt >/dev/null 2>&1 && continue
  yt-dlp -q --no-warnings --skip-download --write-subs --sub-langs zh-TW --sub-format vtt \
    -o "subs/$c-$n-$id" "https://www.youtube.com/watch?v=$id" || echo "FAIL $c-$n $id"
done < videos.txt
python3 scripts/vtt2txt.py
echo SUBSDONE
