# Day 3: Real Data Analysis
import pandas as pd
import numpy as np

print("=== LOAD DATA ===")
# Read CSV file
df = pd.read_csv('students_data.csv')
print("Data loaded successfully!")
print(f"Shape: {df.shape} (rows, columns)")
print("\nFirst few rows:")
print(df.head())

print("\n=== DATA OVERVIEW ===")
print(df.info())
print("\nBasic statistics:")
print(df.describe())

print("\n=== ANALYSIS QUESTIONS ===")

# Q1: What's the average score in each subject?
print("1. Average scores by subject:")
print(f"   Math: {df['Math'].mean():.2f}")
print(f"   Science: {df['Science'].mean():.2f}")
print(f"   English: {df['English'].mean():.2f}")

# Q2: Who's the top student overall?
df['Total'] = df['Math'] + df['Science'] + df['English']
df['Average'] = df['Total'] / 3
top_student = df.loc[df['Average'].idxmax()]
print(f"\n2. Top student: {top_student['Name']} with average {top_student['Average']:.2f}")

# Q3: How many students in each city?
print("\n3. Students per city:")
print(df['City'].value_counts())

# Q4: What's the average age?
print(f"\n4. Average age: {df['Age'].mean():.2f} years")

# Q5: Who scored above 90 in Math?
high_math = df[df['Math'] > 90]
print(f"\n5. Students with Math > 90:")
print(high_math[['Name', 'Math']])

# Q6: Average scores by city
print("\n6. Average scores by city:")
city_averages = df.groupby('City')['Average'].mean().sort_values(ascending=False)
print(city_averages)

# Q7: Find students with all scores above 85
all_high = df[(df['Math'] > 85) & (df['Science'] > 85) & (df['English'] > 85)]
print(f"\n7. High performers (all subjects > 85):")
print(all_high[['Name', 'Math', 'Science', 'English']])

print("\n=== SAVE RESULTS ===")
# Add grades column
df['Grade'] = df['Average'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else 'C'))
print("Added grade column:")
print(df[['Name', 'Average', 'Grade']])

# Save to new CSV
df.to_csv('students_analysis.csv', index=False)
print("\nResults saved to 'students_analysis.csv'")