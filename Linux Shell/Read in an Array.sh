#! /bin/bash


# Reads file from STDIN and prints in one line
file=( `cat < /dev/stdin `)

echo ${file[*]}

# file=( `cat "demo.txt" `)




# # Print line by line
# for t in "${file[@]}"
# do
#     echo $t
# done


