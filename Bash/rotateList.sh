# !/bin/bash

# prompt the user for the list of numbers
read -a ints -p "Enter a list of numbers (Seperate numbers by spaces): "

# prompt the user for the number of rotations
read -p "Enter the number of times the list needs to be rotated: " rotateNum


# A temporary variable to store each value being rotated
temp=0

# A variable used to store the remaining number of rotations
x=$rotateNum

# A variable used to store the index of the first value
count=0

echo "This is your list after being rotated $rotateNum times:"

while [[ x -gt 0 ]]
do
    # store the first number in the list
    temp=${ints[$count]}

    #'unset' completely removes elements from lists
    # The first number in 'ints' is removed
    unset ints[$count]

    # re-add the first value of the list to the end of the list - (rotation)
    ints+=($temp)

    # decrement the number of rotations needed
    ((x=x-1))

    # After each 'unset', the starting index of the list increases by one
    ((count=count+1))

    # output the list after each rotation
    echo ${ints[*]}
done


    