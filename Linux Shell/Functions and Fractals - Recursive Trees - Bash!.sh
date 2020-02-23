#! /bin/bash


declare -A m
StartLegLength=16
maxrows=63
maxcols=100
iter=$(cat)


function Y {
  typeset -i row=$1 col=$2 len=$3 iter=$4
  typeset -i r=$row x=$len cl=$col cr=$col l=$((len/2))

  # leg
  while (( x-- > 0 ))
  do m[$((r--)),$col]=1
  done

  # fork
  x=$len
  while (( x-- > 0 ))
  do m[$r,$((--cl))]=1
     m[$r,$((++cr))]=1
     ((r--))
  done

  # subs
  if (( --iter > 0 ))
  then Y $r $cl $l $iter
       Y $r $cr $l $iter
  fi
}

# initialize
for (( row=0; row<maxrows; row++ ))
do  for (( col=0; col<maxcols; col++))
    do  m[$row,$col]=_
    done
done

# recurse
Y $(( maxrows-1 )) $(( (maxcols-1)/2 )) $StartLegLength $iter

# show the result
for (( r=0; r<maxrows; r++ ))
do  for (( c=0; c<maxcols; c++))
    do  printf "%s" ${m[$r,$c]}
    done
    printf "\n"
done

