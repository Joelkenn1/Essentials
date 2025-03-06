#!/bin/bash

read -a number -p "Enter the permissions of the user, group, and others in number format (Seperate values by spaces): "

#bash array
declare -a users
users=("The User" "The Group" "Others")

count=0

#while-loop
while [[ count -lt ${#number[*]} ]]
do
        
	if [[ ${number[$count]} == 7 ]]
    then	
	      echo "${users[$count]}: Can Read, Write, And Execute."
	      ((count=count+1))
   

    elif [[ ${number[$count]} == 6 ]] 
	then
          echo "${users[$count]}: Can Only Read And Write."
	      ((count=count+1))
	

	elif [[ ${number[$count]} == 5 ]]
    then
	      echo "${users[$count]}: Can Only Read And Execute."
	      ((count=count+1))
	

	elif [[ ${number[$count]} == 4 ]]
	then
	      echo "${users[$count]}: Can Only Read."
	      ((count=count+1))
	

	elif [[ ${number[$count]} == 3 ]]
	then	
	      echo "${users[$count]}: Can Only Write And Execute."
	      ((count=count+1))


	elif [[ ${number[$count]} == 2 ]]
	then 	
	       echo "${users[$count]}: Can Only Write."
	       ((count=count+1))
	 

 	elif [[ ${number[$count]} == 1 ]]
	then	   
          echo "${users[$count]}: Can Only Execute."
	      ((count=count+1))
	

    else
	      echo "${users[$count]}: Unknown."
	      ((count=count+1))
	fi
done

