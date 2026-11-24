#!/bin/bash
# usage: transcribe.sh [NUM...]  (no args = every ⬜ row in PROGRESS.md)
cd /home/awe/disk/math-note/multiple-view-geometry/_work
grep -E "^\| [0-9]{2} " ../PROGRESS.md | while IFS='|' read _ num title id rest; do
  num=$(echo $num); id=$(echo $id)
  if [ $# -gt 0 ] && [[ ! " $* " =~ " $num " ]]; then continue; fi
  [ -f "txt/$num.txt" ] && continue
  [ -f "audio/$num-$id.mp3" ] || yt-dlp -q -x --audio-format mp3 -o "audio/$num-$id.%(ext)s" "https://www.youtube.com/watch?v=$id" 2>&1 | grep -v Deprecated
  whisper "audio/$num-$id.mp3" --model medium.en --device cuda --output_format vtt --output_dir audio > /dev/null 2>&1
  python3 -I scripts/vtt2txt.py "audio/$num-$id.vtt" "txt/$num.txt"
  echo "done $num $(date +%H:%M)"
done
echo ALLDONE
