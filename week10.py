# Create and manipulate NumPy arrays
import numpy as np

# Create a simple NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Perform basic operations on the array
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

# Implement a simple matrix multiplication using NumPy
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print("Matrix Multiplication Result:\n", result)

