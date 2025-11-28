# Day 3: Pandas Fundamentals
import pandas as pd
import numpy as np

print("=== CREATING DATAFRAMES ===")
# DataFrame = table with rows and columns

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'NYC'],
    'Salary': [70000, 80000, 75000, 85000]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
print("\nShape:", df.shape)  # (rows, columns)
print("Columns:", df.columns.tolist())

print("\n=== VIEWING DATA ===")
# See first/last rows
print("First 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))

# Get info about the data
print("\nData Info:")
print(df.info())

print("\n=== SELECTING DATA ===")
# Select one column (returns Series)
print("Names:\n", df['Name'])

# Select multiple columns (returns DataFrame)
print("\nNames and Ages:\n", df[['Name', 'Age']])

# Select rows by index
print("\nFirst row:\n", df.iloc[0])  # iloc = integer location
print("\nRows 1-2:\n", df.iloc[1:3])

# Select by condition (filtering!)
print("\nPeople over 28:\n", df[df['Age'] > 28])
print("\nPeople in NYC:\n", df[df['City'] == 'NYC'])

print("\n=== ADDING/MODIFYING COLUMNS ===")
# Add new column
df['Bonus'] = df['Salary'] * 0.1
print("With bonus:\n", df)

# Modify existing column
df['Age'] = df['Age'] + 1  # Everyone gets older!
print("\nAfter birthday:\n", df[['Name', 'Age']])

print("\n=== STATISTICS ===")
print("Salary statistics:")
print(df['Salary'].describe())  # Count, mean, std, min, max, etc.

print("\nAverage salary:", df['Salary'].mean())
print("Max salary:", df['Salary'].max())
print("Min age:", df['Age'].min())

# Group by and aggregate
print("\nAverage salary by city:")
print(df.groupby('City')['Salary'].mean())

print("\n=== SORTING ===")
print("Sorted by salary (descending):")
print(df.sort_values('Salary', ascending=False))

print("\n=== HANDLING MISSING DATA ===")
# Create data with missing values
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df_nan = pd.DataFrame(data_with_nan)
print("Data with NaN:\n", df_nan)

print("\nCheck for missing values:")
print(df_nan.isnull())

print("\nCount missing values per column:")
print(df_nan.isnull().sum())

# Fill missing values
print("\nFill NaN with 0:")
print(df_nan.fillna(0))

# Drop rows with any NaN
print("\nDrop rows with NaN:")
print(df_nan.dropna())

print("\n=== PRACTICAL EXAMPLE ===")
# Student grades dataset
students = pd.DataFrame({
    'Student': ['John', 'Emma', 'Michael', 'Sophia', 'William'],
    'Math': [85, 92, 78, 95, 88],
    'Science': [90, 88, 85, 92, 86],
    'English': [88, 95, 80, 90, 92]
})

print("Student grades:\n", students)

# Calculate total and average
students['Total'] = students['Math'] + students['Science'] + students['English']
students['Average'] = students['Total'] / 3

print("\nWith totals:\n", students)

# Find top student
top_student = students.loc[students['Average'].idxmax()]
print(f"\nTop student: {top_student['Student']} with average {top_student['Average']:.2f}")

# Students with average above 88
print("\nHigh performers (avg > 88):")
print(students[students['Average'] > 88][['Student', 'Average']])