#!/bin/bash
# mark.sh E1 01 file.md "中文標題" 待確認數 -> update PROGRESS.md and README.md
cd "$(dirname "$0")/../.."
c=$1; n=$2; f=$3; t=$4; q=$5
sed -i "s#^| $c | $n | \([^|]*\) | \([^|]*\) | [^|]* | [^|]* | [^|]* |\$#| $c | $n | \1 | \2 | [$f]($c/$f) | ✅ | $q |#" PROGRESS.md
sed -i "s#^| $c | $n | [^|]* |\$#| $c | $n | [$t]($c/$f) |#" README.md
grep "^| $c | $n " PROGRESS.md README.md | cut -c1-150
