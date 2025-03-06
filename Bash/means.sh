#!/bin/bash


# A prompt for a number input
echo "Enter a number: "
read number 

# A count is for each number from 1 to the number input
count=1

# This variable stores the temporary value after all the numbers from 
# 1 to the number input are multiplied together
geoTemp=1

# This variable stores the temporary value after all the numbers from 
# 1 to the number input are added together
ariTemp=0


# While the count is less than the number input, multiply it
# by the current 'geoTemp' value then increment it by one.
while [[ count -le $number ]]
do
    ((geoTemp=geoTemp*$count))
    ((count=count+1))
done

# The count is reset for the arithmetic mean
count=1


# While the count is less than the number input, multiply it
# by the current 'num' value then increment it by one.
while [[ count -le $number ]]
do
    ((ariTemp=ariTemp+$count))
    ((count=count+1))
done



# The geometric mean is the square root of 1*2*3...*'number'
echo "The geometric mean between 1 and $number is:
$(awk -v g="$geoTemp" 'BEGIN {printf "%.2f", sqrt(g)}')"

# The arithmetic mean is 1+2+3...+'number'/'number'
echo "The arithmetic mean between 1 and $number is: 
$(awk -v x="$ariTemp" -v y="$number" 'BEGIN {printf "%.2f", x/y}')"

