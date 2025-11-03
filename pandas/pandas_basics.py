
import pandas as pd

'''
Basic Usage and Conventions
Pandas provides two main data structures: DataFrame and Series. 
A DataFrame is a 2-dimensional labeled data structure with columns of potentially 
different types. 
A Series is a 1-dimensional labeled array.
'''

#Creating a Series:
data = [1, 2, 3, 4, 5]
print(type(data))
series = pd.Series(data)
print(series)
print(type(series))

#Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)

'''
Basic DataFrame Operations:
Head and Tail: View the first or last few rows of the DataFrame.
'''

print('head \n ',df.head())  # First 5 rows by default
print('tail - 2  \n ',df.tail(2)) # Last 2 rows

print(df.info())
print('desc   \n',df.describe())

#Selecting Columns
print(df['Name'])
print(df[['Name', 'City']])

#Filtering Rows
print(df[df['Age'] > 30])

