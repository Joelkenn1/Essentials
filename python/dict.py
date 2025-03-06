purse = dict()
purse['Money'] = 12
purse[6] = 3
purse['Tissues'] = 75

print(purse[6])

x = {'Jordans': 2, 'Nikes': 3, 'Adidas': 1}

print(x)

counts = dict()
names = ['leo', 'dan', 'leo', 'dan', 'carl']
for name in names:
        counts[name] = counts.get(name, 0) + 1
print(counts)