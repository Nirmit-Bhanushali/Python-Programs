# 9. Program to make use of NumPy Library in Python File
#usage of numpy
import numpy as np

# 1. Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("1D Array:", arr1)
print("2D Array:\n", arr2)

# 2. Array operations
print("Addition:", arr1 + 5)          # add 5 to each element
print("Multiplication:", arr1 * 2)    # multiply each element by 2
print("Square root:", np.sqrt(arr1))

# 3. Array statistics
print("Sum:", np.sum(arr1))
print("Mean:", np.mean(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))

# 4. Reshaping arrays
reshaped = arr2.reshape(3, 2)
print("Reshaped Array:\n", reshaped)

# 5. Creating special arrays
zeros = np.zeros((2, 3))   # 2x3 matrix of zeros
ones = np.ones((3, 3))     # 3x3 matrix of ones

print("Zeros:\n", zeros)
print("Ones:\n", ones)