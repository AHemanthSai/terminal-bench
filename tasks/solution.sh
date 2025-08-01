#!/bin/bash
# Removes blank and duplicate lines from .log files in logs/ and saves them in cleaned/

mkdir -p cleaned

for file in logs/*.log; do
    filename=$(basename "$file")
    grep -v '^$' "$file" | awk '!seen[$0]++' > "cleaned/$filename"
done

