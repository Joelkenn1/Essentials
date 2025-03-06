# This simple program opens a file and reads through it

fhand = open('mbox-short.txt')
for line in fhand:
    print(line)