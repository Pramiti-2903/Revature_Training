
'''
Array Operations
Element-wise Operations :  NumPy supports element-wise operations,
which apply operations to each element in the array individually.

'''

import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Element-wise addition
print("Element-wise addition:", array1 + array2)

# Element-wise subtraction
print("Element-wise subtraction:", array1 - array2)

# Element-wise multiplication
print("Element-wise multiplication:", array1 * array2)

# Element-wise division
print("Element-wise division:", array1 / array2)

'''
Basic Arithmetic Operations
NumPy provides functions for basic arithmetic operations which also operate element-wise.

Aggregate Functions
NumPy provides aggregate functions that operate over the entire array 
or along a specific axis.

'''

# Adding a scalar to an array
print("Adding 10 to each element:", array1 + 10)

# Multiplying each element by a scalar
print("Multiplying each element by 2:", array1 * 2)

# Using numpy functions
print("Square of each element:", np.square(array1))
print("Square root of each element:", np.sqrt(array1))


array = np.array([[1, 2, 3], [4, 5, 6]])

# Sum of all elements
print("Sum of all elements:", np.sum(array))

# Mean of all elements
print("Mean of all elements:", np.mean(array))

# Minimum element
print("Minimum element:", np.min(array))

# Maximum element
print("Maximum element:", np.max(array))

# Sum along each column
print("Sum along each column:", np.sum(array, axis=0))

# Sum along each row
print("Sum along each row:", np.sum(array, axis=1))

'''
Advanced Array Operations
Broadcasting
Broadcasting allows NumPy to perform operations on arrays 
of different shapes. The smaller array is "broadcast" to the shape 
of the larger array.

Vectorized Operations
Vectorized operations in NumPy allow you to perform batch operations
 on data without writing explicit loops, leading to more concise 
 and faster code.

Array Sorting and Searching
NumPy provides efficient functions for sorting and searching arrays.

'''

array1 = np.array([1, 2, 3])
array2 = np.array([[1], [2], [3]])

# Broadcasting array1 to match the shape of array2
print("Broadcasting array1 to match array2:\n", array1 + array2)

# Broadcasting scalar to array
print("Adding scalar 10 to array:\n", array1 + 10)



array = np.arange(1, 6)

# Vectorized operation: Adding 10 to each element
vectorized_addition = array + 10
print("Vectorized addition:", vectorized_addition)

# Vectorized operation: Squaring each element
vectorized_square = np.square(array)
print("Vectorized squaring:", vectorized_square)


array = np.array([3, 1, 4, 1, 5, 9])

# Sorting an array
sorted_array = np.sort(array)
print("Sorted array:", sorted_array)

# Finding indices of sorted elements
sorted_indices = np.argsort(array)
print("Indices of sorted elements:", sorted_indices)

# Searching for elements
# Finding index of first occurrence of 1
index_of_one = np.where(array == 1)
print("Indices where element is 1:", index_of_one)

# Checking if any element is greater than 5
any_greater_than_five = np.any(array > 5)
print("Any element greater than 5:", any_greater_than_five)

# Checking if all elements are positive
all_positive = np.all(array > 0)
print("All elements are positive:", all_positive)

