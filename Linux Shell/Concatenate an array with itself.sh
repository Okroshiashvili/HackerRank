#! /bin/bash



# Read file from STDIN
file=( `cat < /dev/stdin `)

# Concatenate three times
FILE=("${file[@]}" "${file[@]}" "${file[@]}")

# Print
echo ${FILE[@]}


