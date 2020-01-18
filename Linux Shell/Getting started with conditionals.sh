#! /bin/bash

read var

if [[ $var == Y || $var == y ]]
then
	echo "YES"
else
	echo "NO"
fi



# Second solution

read var

[[ "$var" == [yY] ]] && echo "YES" || echo "NO"

