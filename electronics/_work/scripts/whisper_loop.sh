#!/bin/bash
# whisper_loop.sh -> transcribe audio/*.m4a as they appear (in E2→E4 order) to subs/*.vtt, refresh txt/; exit when all 60 done
cd "$(dirname "$0")/.."
PROMPT="以下是大學電子學課程的上課內容，使用繁體中文。電壓、電流、電阻、電容、阻抗、運算放大器、負回授、P-N介面、二極體、空乏區、MOSFET、金屬氧化半導體、BJT、雙極性介面電晶體、射極、基極、集極、源極、汲極、閘極、跨導、小信號模型、偏壓、差動放大器、共模、頻率響應、波特圖、極點、零點、米勒效應、輸出級、AB類。"
while true; do
  did=0
  for f in $(ls audio 2>/dev/null | grep -E '^E[234]-[0-9]{2}-.{11}\.m4a$' | sort); do
    b=${f%.m4a}
    [ -f "subs/$b.vtt" ] && continue
    whisper "audio/$f" --model large-v3-turbo --language zh --output_format vtt \
      --output_dir subs --initial_prompt "$PROMPT" --condition_on_previous_text False \
      --verbose False >>subs/whisper.log 2>&1 && echo "DONE $b" || echo "FAIL $b"
    python3 scripts/vtt2txt.py
    did=1
  done
  n=$(ls subs | grep -cE '^E[234]-.*\.vtt$')
  [ "$n" -ge 60 ] && { echo ALLDONE; exit 0; }
  [ $did -eq 0 ] && sleep 60
done
