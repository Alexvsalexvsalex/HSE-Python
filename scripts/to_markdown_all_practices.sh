#!/bin/bash

SOURCES="./src/hse_python"

PRACTICE_DIRS=$(find -E $SOURCES -type d -regex ".*/practice\_[0-9]+")

echo "These practice directories were found:"
echo "$PRACTICE_DIRS"

for dir in $PRACTICE_DIRS; do
  echo "Running markdown transform for package $dir"
  python3 $SOURCES/practice_3/markdown.py "$dir"
done
