#!/bin/bash

declare -A hashmap

for file in $1/*.*
do
  hashmap["${file%.*}"]=$((hashmap["${file%.*}"]+1))
  mv -i "$file" "${file%.*}_${hashmap["${file%.*}"]}"
done