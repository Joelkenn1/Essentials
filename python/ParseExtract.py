# You can parse and extract certain amounts of strings using the 'find' operator. This program uses 
# the find operator to get the orginization of a email message: uct.ac.za

data = 'From calebkenney@uct.ac.za Sat Jan 5 09:14:16 2020'
atpos = data.find('@')

# The atpos in (' ', atpos) tells the program where to start to look for a space
endpos = data.find(' ', atpos)

# The '+1' is included so you wont see the @ sign
host = data[atpos+1 : endpos]
print(host)

