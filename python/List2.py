# This program opens a file and reads it line by line. For each line it splits the words into a list
# of words using the split method. If the word is already in the list, the program skips over it. It
# then prints the list in abc order.

list1 = list()
fh = open('romeo.txt')
for line in fh:
    words = line.split()
    for word in words:
        if word in list1:
            continue
        else:
            list1.append(word)
list1.sort()
print(list1)