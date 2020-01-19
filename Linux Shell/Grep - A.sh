#! /bin/bash


# First method
egrep -i "the |that |then |those" < /dev/stdin


# Second method
grep -i 'the\|that\|then\|those' demo.txt


# Third method
grep -i -E 'the|that|then|those' demo.txt

# Fourth method
grep -i -e the -e that -e then -e those demo.txt



