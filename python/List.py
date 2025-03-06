# This program prompts to input 3 numbers and calculates the average of those numbers using a list

print('Input 3 numbers, then input "done" when finished')

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    values = float(inp)
    numlist.append(values)

average = sum(numlist) / len(numlist)
print('Average:', average)