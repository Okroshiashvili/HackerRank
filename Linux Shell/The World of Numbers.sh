#! /bin/bash


read x

read y

echo "$(($x + $y))"

echo "$(($x - $y))"

echo "$(($x * $y))"

echo "$(($x / $y))"



# second solution with loop

read x
read y

for i in {+,-,"*",/}
do
    var=$(((x)$i(y)))
    echo $var
done




