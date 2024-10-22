#!/bin/bash

if ! command -v cwebp &> /dev/null; then
    echo "cwebp not found. Please install or run sudo apt install webp"
    exit 1
fi

inputdir=$1
outputdir=$2

for img in "$inputdir"/*.{png,jpg,jpeg};
do
    [ -e "$img" ] || continue

    filename=$(basename -- "$img")
    extension="${filename##*.}"
    filename_no_ext="${filename%.*}"

    cwebp "$img" -o "$outputdir/${filename_no_ext}.webp"
done

echo "Converted successfully!"