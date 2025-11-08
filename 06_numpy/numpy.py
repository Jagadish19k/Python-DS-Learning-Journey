# Python Practice File - numpy

import numpy as np

# ----------------------------------------------------
# 1. Array Creation
# ----------------------------------------------------

# Create a 1D array from a Python list
list_1d = [1, 2, 3, 4, 5]
array_1d = np.array(list_1d)
print("1D Array:\n", array_1d)

# Create a 2D array (Matrix) from a list of lists
list_2d = [[10, 20, 30], [40, 50, 60]]
array_2d = np.array(list_2d)
print("\n2D Array:\n", array_2d)

# Common creation functions
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns of zeros
ones_array = np.ones((1, 4))    # 1 row, 4 columns of ones
range_array = np.arange(0, 10, 2) # Array from 0 up to 10 (exclusive), step 2
linear_array = np.linspace(0, 1, 5) # 5 evenly spaced numbers between 0 and 1 (inclusive)

print("\nZeros Array:\n", zeros_array)
print("Ones Array:\n", ones_array)
print("Range Array (0, 2, 4, 6, 8):\n", range_array)
print("Linear Spacing Array:\n", linear_array)

print("-" * 30)

# ----------------------------------------------------
# 2. Array Attributes (Shape, Dims, Dtype)
# ----------------------------------------------------
print("--- Array Attributes ---")
print(f"Shape of 2D Array: {array_2d.shape} (rows, columns)")
print(f"Dimensions of 2D Array: {array_2d.ndim} (2 dimensions)")
print(f"Total elements in 2D Array: {array_2d.size}")
print(f"Data type: {array_2d.dtype}") # Typically int32 or int64

print("-" * 30)

# ----------------------------------------------------
# 3. Indexing and Slicing
# ----------------------------------------------------
print("--- Indexing and Slicing ---")
# Get the first element of the 1D array
print(f"First element (1D): {array_1d[0]}")

# Get element at row 1, column 2 (index 1, index 2) from 2D array
print(f"Element at [1, 2] (value 60): {array_2d[1, 2]}")

# Slice: get the second row (index 1)
print(f"Second row: {array_2d[1, :]}")

# Slice: get the last two columns for all rows
print(f"Last two columns:\n {array_2d[:, 1:]}")

print("-" * 30)

# ----------------------------------------------------
# 4. Array Mathematics (Vectorized Operations)
# ----------------------------------------------------
print("--- Vectorized Operations ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
print(f"a + b: {a + b}") 

# Element-wise multiplication
print(f"a * b: {a * b}")

# Scalar operation (applied to every element)
print(f"a * 2: {a * 2}")

# Matrix multiplication (Dot product)
# This is NOT element-wise multiplication
print(f"Dot product of a and b: {a.dot(b)}")

print("-" * 30)

# ----------------------------------------------------
# 5. Aggregation and Reshaping
# ----------------------------------------------------
data = np.arange(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("--- Aggregation ---")
print(f"Data for aggregation: {data}")
print(f"Sum: {data.sum()}")
print(f"Minimum: {data.min()}")
print(f"Mean (Average): {data.mean():.2f}") # Format to 2 decimal places

# Reshaping (must have the same number of elements: 9 = 3*3)
print("\n--- Reshaping ---")
matrix_3x3 = data.reshape(3, 3)
print("Reshaped 3x3 Matrix:\n", matrix_3x3)

# Aggregation along axes (axis=0 is columns, axis=1 is rows)
print(f"Sum of columns (axis=0): {matrix_3x3.sum(axis=0)}")
print(f"Sum of rows (axis=1): {matrix_3x3.sum(axis=1)}")