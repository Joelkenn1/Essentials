tuple1 = ("Caleb", 3, 29, 4.5, True)

tuple2 = ("Josh", "Dreads", 0, 'e', False)

tuple3 = tuple2 + tuple1

'Makes two tuples into 1'
print(tuple3)

""""" This does the same thing
print(tuple1.__add__(tuple2))
"""

'Gets one element from a tuple and adds it to another'
tuple4 = tuple1 + tuple(tuple2[3])

print(tuple4)

'Results in an error'
'tuple1[1] = 7'

'To change a value you have to convert the tuple to a list, then back to a tuple'
tuple1 = list(tuple1)
tuple1[1] = 7
tuple1 = tuple(tuple1)

print(tuple1); 


list1 = [1, "falcon", "Debbie", 15, True, "Victory"]

list1[4] = False

print(list1)

list2 = [55, 45, 100, 1.8]

list3 = list2 + list1

'Deletes first element in list'
del list3[0]

print(list3)

'Prints all the elements in list2 minus 1'
list4 = [x * 2 for x in range(11) if x % 2 == 0]

print("list4")
print(list4)

list5 = ['a', 'b', 'c','d','e']

'adds a z to all the elements in list5'
list6 = [x + 'z' for x in list5]

print(list6)

'removes z from each element in list6'
list7 = [x.strip('z') for x in list6 if x.endswith('z')]

print(list7)

