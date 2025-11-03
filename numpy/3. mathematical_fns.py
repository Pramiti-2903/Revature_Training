"""
Basic Mathematical Functions
Trigonometric Functions
NumPy provides various trigonometric functions such as sine, cosine,
tangent, etc.
"""

import numpy as np

angles = np.array([0, np.pi/2, np.pi])
print(angles)
print("Sine of angles:", np.sin(angles))
print("Cosine of angles:", np.cos(angles))
print("Tangent of angles:", np.tan(angles))

# Inverse trigonometric functions
print("Arcsine of 1:", np.arcsin(1))
print("Arccosine of 0:", np.arccos(0))
print("Arctangent of 1:", np.arctan(1))

'''
Exponential and Logarithmic Functions
Rounding and Modulus Functions
'''

values = np.array([1, 2, 3])


print("Exponential of values:", np.exp(values))
print("Natural log of values:", np.log(values))
print("Base-10 log of values:", np.log10(values))

values = np.array([1.7, 2.3, 3.9])

print("Floor of values:", np.floor(values))
print("Ceil of values:", np.ceil(values))
print("Rounded values:", np.round(values))

print("Modulus of 5 and 2:", np.mod(7, -3))
print("Remainder of 5 divided by 2:", np.remainder(7, -3))
print(7%-3)

'''
Linear Algebra Functions
Dot Product and Matrix Multiplication
Determinants and Inverses
Eigenvalues and Eigenvectors

'''

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Dot product of A and B:", np.dot(A, B))
print("Matrix multiplication of A and B:", np.matmul(A, B))

print("Determinant of A:", np.linalg.det(A))
print("Inverse of A:\n", np.linalg.inv(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)

'''
Statistical Functions
Mean, Median, and Mode
Variance and Standard Deviation

'''

from  scipy import stats

data = np.array([1,2,2,3,3,3,3,4])

print("Mean of data:", np.mean(data))
print("Median of data:", np.median(data))
mode_result = stats.mode(data)
print('Res : ',mode_result, 'Type : ', type(mode_result))
mode = mode_result[0] if mode_result.mode.size > 0 else None
print("Mode of data:", mode)


print("Variance of data:", np.var(data))
print("Standard deviation of data:", np.std(data))

'''
Correlation and Covariance
'''

data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([5, 4, 3, 2, 1])

print("Correlation coefficient between data1 and data2:\n", np.corrcoef(data1, data2))
print("Covariance matrix of data1 and data2:\n", np.cov(data1, data2))

'''
Random Number Generation
Generating Random Numbers
Setting Random Seeds
Random Sampling from Distributions

'''

print("Random numbers from uniform distribution:", np.random.rand(5))
print("Random numbers from normal distribution:", np.random.randn(5))
print("Random integers between 1 and 10:", np.random.randint(1, 10, size=5))

np.random.seed(42)
print("Random numbers with seed 42:", np.random.rand(10))

np.random.seed(42)
print("Reproducible random numbers with seed 42:", np.random.rand(5))

# Normal distribution
samples = np.random.normal(loc=0, scale=1, size=10)
print("Samples from normal distribution:", samples)

# Uniform distribution
samples = np.random.uniform(low=0, high=1, size=10)
print("Samples from uniform distribution:", samples)