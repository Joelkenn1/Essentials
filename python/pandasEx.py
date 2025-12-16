# Import pandas as pd
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


### Useful Methods ###

# single brackets = Series, double brackets = Dataframe
# cars.dropna() - drop cells with missing values
# cars.isna() - checks if each column contains a missing value
# cars.to_csv("cars.csv") - create excel file from dict
# dup = cars.duplicated(), cars[dup] - check which columns contain duplicates

# Use 'groupby' to group columns based on values and perform operations
# ex: df[['sex', 'height', 'age']].groupby('sex').mean()
# ex: df.groupby('col1')['col2'].transform(lamba x: x.mean())

# Use 'agg' to do operations on columns, ex: df[['col1', 'col2']].agg(["mean", "std"]) or df.agg("col1" : ["mean", "std"], "col2" : ["median"])

# Combining groupby and agg: df.groupby('sex').agg(mean_age = ("age", "mean"), median_height = ("height", "median"))



# Joining Data #
# x = set(df1[column1]).difference(df2[column2]) - returns only unique values in column1

# Cleaning Text
# df[column] = df[column].str.replace(x, y) # replacing invalid charcters in columns
# assert df[column].str.contains.any("x | y | z") == True - Check if x y or z is in the column, returns nothing if passes

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)


# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars.index = row_labels # Customize indexes of cars dataframe
us_index = row_labels.index('US') # Get the index of array element

print("Cars DataFrame: "  + "\n" + str(cars) + "\n")
print("Cars Values: " + "\n" + str(cars.values) + "\n")


print("Country & Drives_Right Columns: " + "\n" + str(cars[['country', 'drives_right']])  + "\n")
print("Cars DataFrame Sorted By Largest Cars_Per_Cap: " + "\n" + str(cars.sort_values("cars_per_cap", ascending=False)) + "\n") 


print("Cars_Per_Cap Of India:" + "\n" + str(cars.loc['IN', 'cars_per_cap'])  + "\n")
print("Country And Drives_Right Columns Of Russia And Morocco:" + "\n" + str(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])  + "\n")

# loc = location-based
print("US, Australia, & Russia Information Using loc: " + "\n" + str(cars.loc[['US', 'AUS', 'RU']])  + "\n")
# iloc = integer-based,
print("Japan & India Information Using iloc: " + "\n" + str(cars.iloc[[2, 3]])+ "\n" )

print("Iterate Over Rows Of Cars To Print Each Country's Cars_Per_Cap:")
for index, row in cars.iterrows():
    print(index + ": " + str(row['cars_per_cap']))


print("\nRows 2-5:")
print(cars[1:5])


print("\nFalse Drive_Right Countries:")
# Select rows where drives_right = false, then get only the country column
print(cars[cars['drives_right'] == False][['country']]  + "\n")

# Other agg functions: min, max, mode, median, std, var, sum, quantile
print("Average Cars_Per_Cap Value: " + str(cars['cars_per_cap'].mean()) + "\n")

# Grouping mechanisms
print("Pivot Tables Group Data: Grouped By Country, Seleceted Only Cars_Per_Cap")
group = cars.pivot_table(values ="cars_per_cap", index = "country")
print(str(group) + "\n")


# Cleaning Data
cars['drives_right'] = cars['drives_right'].astype('str') # convert drives_right column from bool to str type
print(cars.dtypes)

sns.barplot(data = cars, x="cars_per_cap", hue="drives_right")
plt.show()





