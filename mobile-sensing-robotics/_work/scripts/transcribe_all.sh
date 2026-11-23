#!/bin/bash
# Download audio + Whisper medium.en for every long video listed in PROGRESS.md (status ⬜)
cd /home/awe/disk/math-note/mobile-sensing-robotics/_work
grep -E "^\| [12]-[0-9]+ " ../PROGRESS.md | grep "⬜" | while IFS='|' read _ num title id rest; do
  num=$(echo $num); id=$(echo $id)
  [ -f "txt/$num.txt" ] && continue
  if [ ! -f "audio/$num-$id.mp3" ]; then
    yt-dlp -q -x --audio-format mp3 -o "audio/$num-$id.%(ext)s" "https://www.youtube.com/watch?v=$id" 2>&1 | grep -v Deprecated
  fi
  whisper "audio/$num-$id.mp3" --model medium.en --device cuda --output_format vtt --output_dir audio > /dev/null 2>&1
  python3 -I scripts/vtt2txt.py "audio/$num-$id.vtt" "txt/$num.txt"
  echo "done $num $(date +%H:%M)"
done
echo ALLDONE
