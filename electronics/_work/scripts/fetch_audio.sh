#!/bin/bash
# fetch_audio.sh -> download audio for E2–E4 (no YouTube subtitles) into audio/<C>-<NN>-<id>.m4a
cd "$(dirname "$0")/.."
grep -E '^E[234]\|' videos.txt | while IFS='|' read -r c n id dur title; do
  [ -f "audio/$c-$n-$id.m4a" ] && continue
  yt-dlp -q --no-warnings -x --audio-format m4a -f bestaudio -o "audio/$c-$n-$id.%(ext)s" \
    "https://www.youtube.com/watch?v=$id" 2>>audio/dl.err || echo "FAIL $c-$n"
done
echo DLDONE
