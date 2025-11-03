"""
Data Structures in Pandas
Series
A Series is a one-dimensional labeled array capable of holding data of
any type (integer, string, float, python objects, etc.).
The axis labels are collectively referred to as the index.

Creating Series from Lists, Dictionaries, and Arrays
"""

import pandas as pd

data_list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(data_list)
print(series_from_list)

data_dict = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)

import numpy as np

data_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(data_array)
print(series_from_array)

'''
Series Attributes and Methods
Attributes, Methods
'''

print(series_from_list.index)  # RangeIndex(start=0, stop=5, step=1)
print(series_from_list.values) # array([1, 2, 3, 4, 5])
print(series_from_list.dtype)  # dtype('int64')

print(series_from_list.head(3))  # First 3 elements
print(series_from_list.tail(2))  # Last 2 elements
print(series_from_list.mean())   # Mean value
print(series_from_list.sum())    # Sum of all values
print(series_from_list.describe()) # Statistical summary


#Indexing and Slicing Series

print(series_from_list[2])
print(series_from_dict['b'])

print(series_from_list[1:4])
print(series_from_list[:3])
print(series_from_list[3:])

#Operations on Series
print(series_from_list + 2)  # Adding 2 to each element
print(series_from_list * 2)  # Multiplying each element by 2

other_series = pd.Series([10, 20, 30, 40, 50])
print(series_from_list + other_series)

'''
DataFrames
A DataFrame is a 2-dimensional labeled data structure with columns of 
potentially different types. You can think of it as a table or a spreadsheet in Excel.

Creating DataFrames from Dictionaries, Lists, and NumPy Arrays

'''

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df_from_dict = pd.DataFrame(data_dict)
print(df_from_dict)

data_list_dicts = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df_from_list_dicts = pd.DataFrame(data_list_dicts)
print(df_from_list_dicts)

data_array = np.array([
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
])

df_from_array = pd.DataFrame(data_array, columns=['Name', 'Age', 'City'])
print(df_from_array)

'''
DataFrame Attributes and Methods
Attributes, Methods

'''

print(df_from_dict.index)   # RangeIndex(start=0, stop=3, step=1)
print(df_from_dict.columns) # Index(['Name', 'Age', 'City'], dtype='object')
print(df_from_dict.values)  # 2D array of the DataFrame values


print(df_from_dict.head(2))     # First 2 rows
print(df_from_dict.tail(1))     # Last row
print(df_from_dict.info())      # Information about the DataFrame
print(df_from_dict.describe())  # Statistical summary of numeric columns


#Indexing and Slicing DataFrames
print(df_from_dict['Name'])
print(df_from_dict[['Name', 'City']])

print(df_from_dict.iloc[0])  # By integer index
print(df_from_dict.loc[0])   # By label index (same as iloc in this case)

print(df_from_dict.iloc[0:2])  # First 2 rows
print(df_from_dict.loc[0:1])   # Rows with labels 0 and 1

#Single column selection:
print(df_from_dict['Age'])

#Multiple columns selection:
print(df_from_dict[['Name', 'City']])

#Row selection using labels (loc):
print(df_from_dict.loc[0])
print(df_from_dict.loc[0:2])

#Row selection using integer positions (iloc):
print(df_from_dict.iloc[0])
print(df_from_dict.iloc[0:2])


'''
Panel Data
Panel data, also known as longitudinal data or cross-sectional time series data, 
involves observations of multiple phenomena obtained over multiple time periods 
for the same firms or individuals. In pandas, Panel data used to be handled using 
the Panel class, but it has since been deprecated in favor of using multi-index DataFrames.

Panel Data Structure
Panel data structure allows for the storage and manipulation of three-dimensional data,
 typically with dimensions (items, major_axis, minor_axis):

Items: Axis 0, each item corresponds to a DataFrame (like different variables).
Major_axis: Axis 1, usually represents time.
Minor_axis: Axis 2, represents individual entities (like different firms or individuals).
Due to the deprecation of Panel, we now use multi-index DataFrames to handle panel data.

Creating and Manipulating Panels
Creating Panel-like Data with Multi-index DataFrames
'''

import pandas as pd
import numpy as np

# Create a multi-index DataFrame
arrays = [
    ['A', 'A', 'B', 'B'],
    [1, 2, 1, 2]
]

index = pd.MultiIndex.from_arrays(arrays, names=('person', 'time'))
data = pd.DataFrame(np.random.randn(4, 3), index=index, columns=['entity1',
                                                                 'entity2', 'entity3'])

print("Multi-index DataFrame:")
print(data)

#Manipulating Multi-index DataFrames
# Access data for variable 'A'
print("\nData for variable 'A':")
print(data.loc['A'])

# Access data for time period 1
print("\nData for time period 1:")
print(data.xs(1, level='time'))

# Adding a new row for a new time period
new_data = pd.DataFrame({
    'entity1': [0.5, 0.3],
    'entity2': [1.5, 1.3],
    'entity3': [2.5, 2.3]
}, index=pd.MultiIndex.from_product([['A', 'B'], [3]], names=['variable', 'time']))
print(new_data)

data = pd.concat([data, new_data])
print("\nData after adding new time period:")
print(data)

'''
Applications and Use Cases

Economics and Finance: Analyzing the financial performance of different firms over time.
Healthcare: Monitoring patient health metrics across different time periods.
Social Sciences: Studying the behavior of individuals across various time points.
Marketing: Observing the impact of marketing campaigns over time.

'''

