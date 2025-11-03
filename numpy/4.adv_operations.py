"""
If the arrays do not have the same rank, prepend the shape of the smaller array with 1s.
Two dimensions are compatible when they are equal, or one of them is 1.
If the arrays have compatible shapes, they are broadcasted to a common shape.
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1], [2], [3]])

# Broadcasting b to the shape of a
result = a + b
print('A+B: ',result)

#Practical Application ==> Broadcasting can simplify code and make operations more efficient.

# Element-wise addition with broadcasting
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([1, 0, 1])

result = matrix + vector
print('A M  + B V',result)

'''
Common Pitfalls 
Mismatch in shapes: Ensure arrays have compatible shapes before broadcasting.
Unintended broadcasting: Be careful with operations that might unintentionally
 broadcast arrays, leading to unexpected results.
'''
# Mismatch shapes
try:
    a = np.array([1, 2, 3])
    b = np.array([1, 2])
    result = a + b
except ValueError as e:
    print("ValueError:", e)

'''Memory Layout
C-order and F-order
NumPy arrays can be stored in memory in C-order (row-major) or F-order (column-major).
'''
array = np.array([[1, 2, 3], [4, 5, 6]], order='C')
print("C-order:\n", array)

array = np.array([[1, 2, 3], [4, 5, 6]], order='F')
print("F-order:\n", array)

#Reshaping an array can affect memory layout. Using reshape often creates a view
# instead of a copy, but it can create a copy if necessary.

array = np.arange(6).reshape(2, 3)
print("Original array:\n", array)

reshaped_array = array.reshape(3, 2)
print("Reshaped array:\n", reshaped_array)

# Views vs. Copies ==> A view is a new array object that looks at the same data,
# whereas a copy is a new array with its own data.

array = np.array([1, 2, 3, 4])

# View
view = array[1:3]
print('view : ',view)
view[0] = 99
print("Original array after view modification:", array)
print('view : ',view)

array = np.array([1, 2, 3, 4])
# Copy
copy = array[1:3].copy()
print('copied : ', copy)
copy[0] = 88
print("Original array after copy modification:", array)
print('copied : ', copy)

'''Performance Optimization ==> Vectorization for Performance
Vectorization allows for faster computations by applying operations on entire arrays 
rather than using loops.

Avoiding Loops with NumPy
Using NumPy functions instead of Python loops can significantly speed up computations.
'''

# Using loop
array = np.arange(1e6)
result = np.zeros_like(array)
print(array, '\n', result)
for i in range(len(array)):
    result[i] = np.sin(array[i])

# Using vectorization
result = np.sin(array)
print('Vec sin : ', result)


'''
Numba for JIT Compilation
Numba is a JIT compiler that translates Python functions to optimized machine code at runtime.
'''

from numpy import jit
import numpy as np


@jit(nopython=True)
def sum_array(arr):
    total = 0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total

array = np.arange(5)
print(sum_array(array))

# Applications in Machine Learning
# 1. Data Preprocessing with NumPy
# 2. Feature Engineering and Transformation


data = np.random.rand(100, 3)  # Random data

# Normalizing data
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
normalized_data = (data - mean) / std
print("Normalized data:\n", normalized_data)


data = np.random.rand(100, 2)

# Polynomial features
poly_features = np.hstack((data, data**2, data**3))
print("Polynomial features:\n", poly_features)

# Simple linear regression using NumPy
X = np.random.rand(100, 1)
y = 3*X.squeeze() + 2 + np.random.randn(100) * 0.1

# Adding intercept term
X_b = np.c_[np.ones((100, 1)), X]

# Normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
print("Theta best (parameters):", theta_best)


