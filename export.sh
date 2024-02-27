#!/bin/bash
docker run -it -v $(pwd):/usr/app/out --rm nevermendel/leetcode-export --only-last-submission  --only-accepted


find . -name "*.html" -type f | while read filename; do
    newfilename=readme.md
    pandoc "$filename" -o "$newfilename"
    echo "Конвертировано: $filename -> $newfilename"
done


