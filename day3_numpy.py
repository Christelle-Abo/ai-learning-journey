# Day 3: NumPy Fundamentals
import numpy as np

print("=== CREATING ARRAYS ===")
# Create arrays different ways
arr1 = np.array([1, 2, 3, 4, 5])
print("Array:", arr1)
print("Shape:", arr1.shape)  # Shape tells you dimensions
print("Data type:", arr1.dtype)

# 2D array (matrix)
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2d)
print("Shape:", arr2d.shape)  # (2, 3) means 2 rows, 3 columns

# Special arrays
zeros = np.zeros((3, 3))  # 3x3 array of zeros
ones = np.ones((2, 4))    # 2x4 array of ones
range_arr = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
print("\nZeros:\n", zeros)
print("Range:", range_arr)


print("\n=== ARRAY OPERATIONS ===")
# Math on entire arrays (FAST!)
arr = np.array([1, 2, 3, 4, 5])
print("Original:", arr)
print("Add 10:", arr + 10)      # Adds 10 to every element
print("Multiply by 2:", arr * 2)
print("Square:", arr ** 2)

# Array with array operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("\nArray 1:", arr1)
print("Array 2:", arr2)
print("Add arrays:", arr1 + arr2)      # [5, 7, 9]
print("Multiply arrays:", arr1 * arr2)  # [4, 10, 18]


print("\n=== USEFUL FUNCTIONS ===")
data = np.array([10, 20, 30, 40, 50])
print("Data:", data)
print("Sum:", np.sum(data))
print("Mean:", np.mean(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
print("Std Dev:", np.std(data))


print("\n=== INDEXING & SLICING ===")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])  # Elements 1, 2, 3 (not 4!)

# Boolean indexing (powerful!)
print("\nElements > 25:", arr[arr > 25])  # [30, 40, 50]


print("\n=== 2D ARRAY OPERATIONS ===")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("Matrix:\n", matrix)
print("Element at row 1, col 2:", matrix[1, 2])  # 6
print("First row:", matrix[0, :])     # All columns of row 0
print("Second column:", matrix[:, 1])  # All rows of column 1
print("Sum of each row:", np.sum(matrix, axis=1))
print("Sum of each column:", np.sum(matrix, axis=0))


print("\n=== PRACTICAL EXAMPLE ===")
# Calculate grade statistics
grades = np.array([85, 92, 78, 90, 88, 76, 95, 89])
print("Grades:", grades)
print(f"Average: {np.mean(grades):.2f}")
print(f"Highest: {np.max(grades)}")
print(f"Lowest: {np.min(grades)}")
print(f"Students above 85: {np.sum(grades > 85)}")
print(f"Passing (>= 75): {np.sum(grades >= 75)}")