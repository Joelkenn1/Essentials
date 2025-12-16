import numpy as np

arr1 = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

np_arr1 = np.array(arr1)

first_row = np_arr1[0,:]
first_row_mean = np.mean(first_row)
first_row_bool = np.logical_and(first_row > 1, first_row < 4)

third_column = np_arr1[:,2]
third_column_median = np.median(third_column)

fifth_row = np_arr1[4,:]
fifth_row_standard_deviation = np.std(fifth_row)
first_third_correlation = np.corrcoef(first_row, fifth_row)


print("2D Numpy Array: " + str(np_arr1) + "\n")
print("First Row: " + str(first_row) + ", The Mean Is " + str(first_row_mean))
print("First Row Boolean Logic: x > 1 and x < 4 = " + str(first_row[first_row_bool]) + "\n")
print("Third Column: " + str(third_column) + ", The Median Is " + str(third_column_median) + "\n")
print("Fifth Row: " + str(fifth_row) + ", The Standard Deviation Is " + str(fifth_row_standard_deviation) + "\n")
print("The Correlation Between The First And Fifth Rows is " + str(first_third_correlation))

print("Each Indiviual Element:")
for i in np.nditer(np_arr1):
    print(str(i))
    

# Numpy is used to do arithmetic on array elements
arr2 = np.array([5, 10, 15])
times_two = arr2 * 2
print("\n" + str(times_two))

arr3 = np.array([1, 4, 3])
subtract = arr2 - arr3
print("\n" + "Array 1: " + str(arr2) + ", Array 2: " + str(arr3) + ", Subtract:")
print(str(subtract))

# You can also find specific elements
print("Array: " + str(arr2) + ", elements greater than 10:")
print(str(arr2[arr2 > 10]))


# Random Numbers
print("\nThree Random Numbers: ")
print(np.random.rand(3))

print("\nNew Random Numbers: ")

np.random.seed(1) # You can store random numbers using 'seed'
print("\n" + "First Random Num: " + str(np.random.rand(1)))

np.random.seed(2)
print("\n" + "Second Random Num: " + str(np.random.rand(1)))

np.random.seed(1)
print("\n" + "First Random Num Again: " + str(np.random.rand(1)))

print("\n" + "Will It be Zero or One: " + str(np.random.randint(0, 2)))








      