#!/bin/bash

# A prompt for a word
echo "Enter a word: "
read word

# An array for the letters in reverse order
reverse=()

# i stores the length of the original word
i=${#word}

# Add the letters in the word input to the original array
while [[ i -gt 0 ]]
do
     ((i=i-1))

     # reverse adds each letter in the word beginning from the
     # end of the word. {string: index: # of characters}
     reverse+=${word:$i:1}
done

if [[ ${reverse[*]} == $word ]]
then
    echo "$word is a palindrome."

else
    echo "$word is not a palindrome."
fi
