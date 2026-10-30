#DATA ANALYSIS USIMNG NUMPY AND PANDAS
#NUMPY ARRAY OPERATIONS
#1.Create a 1D NUMPY ARRAY
import numpy as np

# Create 1D array for Week 1
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("temperatures_w1:", temperatures_w1)

#2.inspection and properties
print("Shape:", temperatures_w1.shape)        # (7,)
print("Data Type:", temperatures_w1.dtype)    # float64
print("Total Elements:", temperatures_w1.size) # 7

#3.Array operations
# Convert Celsius to Fahrenheit
fahrenheit = (temperatures_w1 * 9/5) + 32
print("Temperatures in Fahrenheit:", fahrenheit)

# Maximum, minimum, and mean temperatures
max_temp = np.max(temperatures_w1)
min_temp = np.min(temperatures_w1)
mean_temp = np.mean(temperatures_w1)

print(f"Max Temp: {max_temp}°C")
print(f"Min Temp: {min_temp}°C")
print(f"Mean Temp: {mean_temp:.2f}°C")

#4.Array slicing & indexing
# First three days of the week (indices 0, 1, 2)
first_three_days = temperatures_w1[:3]
print("First 3 days:", first_three_days)

# Weekend (last two days - indices 5, 6)
weekend = temperatures_w1[-2:]
print("Weekend:", weekend)

# Middle three days (indices 2, 3, 4)
middle_three_days = temperatures_w1[2:5]
print("Middle 3 days:", middle_three_day)
#5.Create a 2D array
# Create 2D array for 2 weeks
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],  # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]   # Week 2
])
print("2D Temperatures Array:\n", temperatures)

#Inspect & slice 2D the array 
# Properties
print("2D Shape:", temperatures.shape)       # (2, 7)
print("2D Data Type:", temperatures.dtype)   # float64
print("Total Elements:", temperatures.size)  # 14

# Extract each week
week1 = temperatures[0]
week2 = temperatures[1]
print("Week 1:", week1)
print("Week 2:", week2)

# Extract weekends (last two days) for both weeks
weekends = temperatures[:, -2:]
print("Weekends for both weeks:\n", weekends)

#PANDAS SERIES
#1,CREATING PANDAS SERIES
import pandas as pd

marks_data = [95, 92, 89, 85, 80]
custom_indices = ['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5']

marks = pd.Series(marks_data, index=custom_indices)
print(marks)
#2.Indexing & slicing
# Integer index position to access mark of 1st rank student
first_rank_mark = marks.iloc[0]
print("1st Rank Mark:", first_rank_mark)

# .loc accessor to retrieve marks of top 3 ranks
top_3_loc = marks.loc['Rank1':'Rank3']
print("Top 3 Ranks (.loc):\n", top_3_loc)

# .iloc accessor to retrieve mark of 3rd rank student
third_rank_iloc = marks.iloc[2]
print("3rd Rank Mark (.iloc):", third_rank_iloc)

# Boolean mask to filter ranks where marks > 90
greater_than_90 = marks[marks > 90]
print("Marks > 90:\n", greater_than_90)
#3.Manipulating series
# Modify the mark of 1st rank to 100
marks['Rank1'] = 100

# Remove the entry corresponding to the last rank
marks = marks.drop('Rank5')

# Compute CGPA by dividing each mark by 10
cgpa = marks / 10

print("Updated Series:\n", marks)
print("\nCalculated CGPA:\n", cgpa)


#3.PANDAS DATAFRAME
#1.CREATING PAMNDAS DATAFRAME
data = {
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 
                        'Clothing', 'Electronics', 'Furniture', 'Clothing', 
                        'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
}

transactions = pd.DataFrame(data)
print(transactions)


#2.DATA Exploration
# Display only ProductCategory and Amount
print("\nProductCategory & Amount:\n", transactions[['ProductCategory', 'Amount']])

# Retrieve last 3 columns (ProductCategory, Region, Amount)
last_3_cols = transactions.iloc[:, -3:]
print("\nLast 3 columns:\n", last_3_cols)

# Filter rows where Region is 'North' and Amount > 200
filtered_df = transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)]
print("\nRegion='North' and Amount > 200:\n", filtered_df)

# Value counts for ProductCategory
print("\nProductCategory Value Counts:\n", transactions['ProductCategory'].value_counts())

# Unique values in Region
print("\nUnique Regions:", transactions['Region'].unique())

# Group by Region and find mean amount
mean_by_region = transactions.groupby('Region')['Amount'].mean()
print("\nMean Amount by Region:\n", mean_by_region)

#3.Manipulatinhg the Dataframe
# Modify Amount for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165

# Add 'Discount' column (10% of Amount)
transactions['Discount'] = transactions['Amount'] * 0.10

# Remove row with TransactionID 109
transactions = transactions[transactions['TransactionID'] != 109]

# Delete 'Discount' column
transactions = transactions.drop(columns=['Discount'])

print("\nFinal DataFrame:\n", transactions)
