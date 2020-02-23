#! /bin/bash

# Read the size of the array
read
# Read the input in the array
arr=($(cat))
# Convert array into string
arr=${arr[*]}
# Replace all spaces with bitwise-XOR
echo $((${arr// /^}))

