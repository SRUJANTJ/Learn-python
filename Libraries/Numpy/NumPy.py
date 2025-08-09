# Why numpy
# Machine Learning deals with large datasets and mathematical computations (like matrix multiplication, dot products, etc.).

# Python’s built-in lists are slow because they:

# Store elements as generic Python objects (not optimized for numbers).

# Lack built-in vectorized math operations.

# NumPy solves this by:

# Storing data in contiguous memory blocks (fast access).

# Using C/Fortran-optimized backend for computation.

# Allowing vectorized operations (no slow Python loops).

# Creating Arrays
import numpy as np

arr1=np.array([1, 2, 3, 4, 5])  # Create a 1D array

arr2= np.array([[1, 2, 3], [4, 5, 6]])  # Create a 2D array

# Creating arrays with special functions
zeros = np.zeros((3, 3))  # 3x3 matrix of zeros
ones = np.ones((2, 4))    # 2x4 matrix of ones
rand = np.random.rand(3, 2) # Random numbers between 0 and 1

print(arr1)
print(arr2)
print(zeros)
print(ones)
print(rand)



# Array Attributes
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)   # (2, 3) → 2 rows, 3 columns
print(arr.ndim)    # 2 dimensions
print(arr.size)    # Total elements
print(arr.dtype)   # Data type (int64, float32, etc.)
print(arr.itemsize)
print(arr.data)


