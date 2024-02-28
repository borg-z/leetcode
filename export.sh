#!/bin/bash
docker run -it -v $(pwd):/usr/app/out --rm nevermendel/leetcode-export --only-last-submission  --only-accepted


find . -name "*.html" -type f | while read filename; do
    dir=$(dirname "$filename")
    newfilename="$dir/readme.md"
    pandoc "$filename" -o "$newfilename"
    rm -rf $filename
done
