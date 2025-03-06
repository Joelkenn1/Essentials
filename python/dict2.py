# This program uses a dictionary to see the most common word in a file, and then prints the number of 
# times that word appears

counts = dict()
fh = open('words.txt')
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print('Word:', bigword, ' ','Count:',bigcount)