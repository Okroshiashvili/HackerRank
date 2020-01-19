#! /bin/bash


# file=( `cat < /dev/stdin `)
# file=( `cat "demo.txt" `)



# Read file from STDIN
file=( `cat < /dev/stdin `)

# Print slice [3:7]
echo "${file[@]:3:5}"

