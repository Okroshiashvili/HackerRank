#! /bin/bash


awk '{average=($2+$3+$4)/3; print $0, ":", (average<50)?"FAIL":(average<80)?"B":"A"}'

