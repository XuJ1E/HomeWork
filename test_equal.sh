#!/bin/bash
a=10; b=20
if [ $a -eq $b ]
then
  echo "$a -eq $b : a not equal to b"

elif [ $a -ne $b ]
then
  echo "$a -ne $b : a not equal to b"
elif [ $a -gt $b ]
then
  echo "$a -gt $b : a greater than b"
elif [ $a -lt $b ]
then
  echo "$a -lt $b : a less than b"
elif [ $a -ge $b ]
then
  echo "$a -ge $b : a greater than or equal to b"
elif [ $a -le $b ]
then
  echo "$a -le $b : a less than or equal to b"
else
  echo "Invalid operator"
fi
a=10
b=20

if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi


a=10
b=20
c=`expr ${a} + ${b}`
echo "The sum of $a and $b is $c"