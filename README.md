# NumPy-and-pandas-using-for-data-analysis
NumPy and pandas using for data analysis
 1. NumPy Array Operations
​This section focuses on numerical computations and handling temperature data using NumPy.  
​1D Array Creation: Initializes a 1D NumPy array (temperatures_w1) containing daily average temperatures for Week 1.  
​Inspection & Properties: Uses .shape to check dimensions, .dtype to check the data type (e.g., float64), and .size to find the total number of elements.  
​Mathematical Operations: Performs vectorized arithmetic to convert Celsius to Fahrenheit using the formula (Celsius * 9/5) + 32, and computes summary statistics like maximum, minimum, and mean temperatures (np.max, np.min, np.mean).  
​Slicing & Indexing: Extracts specific subsets of data, such as the first three days, the weekend (last two days), and the middle three

 2. Pandas Series
This section demonstrates working with single-column labeled data structures using Pandas.  
Series Creation: Creates a Pandas Series named marks with predefined values and custom index labels (Rank1 to Rank5).  
Indexing & Slicing:
Accesses elements using positional indexing (.iloc[0] for the 1st rank).  
Uses label-based indexing (.loc['Rank1':'Rank3']) to retrieve a range of top ranks.  
Applies a boolean mask (marks > 90) to filter rows meeting a specific condition.  
Data Manipulation: Modifies values via index labels (marks['Rank1'] = 100), drops specific entries using .drop(), and performs vectorized division (marks / 10) to calculate CGPA.

 3. Pandas DataFrame
This section covers structured, tabular data analysis using Pandas DataFrames.  
DataFrame Creation: Constructs a DataFrame named transactions containing columns for TransactionID, ProductCategory, Region, and Amount.  
Data Exploration:
Uses .head(), .tail(), .info(), and .shape to inspect dataset structure and data types.  
Selects specific columns and slices the last 3 columns using .iloc.  
Filters rows using multiple conditions (Region == 'North' and Amount > 200).  
Utilizes aggregation tools like .value_counts(), .unique(), and .groupby('Region')['Amount'].mean() to analyze categorical and numerical data distributions.  
DataFrame Manipulation: Updates specific cells using .loc, creates new calculated columns (e.g., adding a Discount…
