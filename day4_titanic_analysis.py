# Day 4: Titanic Dataset Analysis
import pandas as pd
import numpy as np

print("=== LOAD TITANIC DATA ===")
# Load the data
df = pd.read_csv('train.csv')

print(f"Dataset loaded: {df.shape[0]} passengers, {df.shape[1]} features")
print("\nFirst few rows:")
print(df.head())

print("\n=== DATA OVERVIEW ===")
print("\nColumn names and types:")
print(df.info())

print("\nBasic statistics:")
print(df.describe())

print("\n=== MISSING DATA CHECK ===")
print("Missing values per column:")
print(df.isnull().sum())
print(f"\nAge has {df['Age'].isnull().sum()} missing values")
print(f"Cabin has {df['Cabin'].isnull().sum()} missing values")

print("\n=== KEY QUESTIONS ===")

# Q1: What was the overall survival rate?
survival_rate = df['Survived'].mean() * 100
print(f"\n1. Overall survival rate: {survival_rate:.1f}%")
print(f"   Survived: {df['Survived'].sum()} passengers")
print(f"   Died: {len(df) - df['Survived'].sum()} passengers")

# Q2: Did gender affect survival?
print("\n2. Survival by gender:")
gender_survival = df.groupby('Sex')['Survived'].agg(['count', 'sum', 'mean'])
gender_survival['survival_rate'] = gender_survival['mean'] * 100
print(gender_survival)

# Q3: Did class affect survival?
print("\n3. Survival by passenger class:")
class_survival = df.groupby('Pclass')['Survived'].agg(['count', 'sum', 'mean'])
class_survival['survival_rate'] = class_survival['mean'] * 100
print(class_survival)

# Q4: Age distribution
print("\n4. Age statistics:")
print(f"   Average age: {df['Age'].mean():.1f} years")
print(f"   Youngest: {df['Age'].min():.0f} years")
print(f"   Oldest: {df['Age'].max():.0f} years")

# Create age groups
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100], 
                         labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Senior'])
print("\nSurvival by age group:")
age_survival = df.groupby('AgeGroup')['Survived'].mean() * 100
print(age_survival)

# Q5: Fare analysis
print("\n5. Fare statistics:")
print(f"   Average fare: ${df['Fare'].mean():.2f}")
print(f"   Cheapest: ${df['Fare'].min():.2f}")
print(f"   Most expensive: ${df['Fare'].max():.2f}")

# Q6: Family size impact
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print("\n6. Survival by family size:")
family_survival = df.groupby('FamilySize')['Survived'].mean() * 100
print(family_survival)

# Q7: Embarked port
print("\n7. Survival by embarkation port:")
port_survival = df.groupby('Embarked')['Survived'].mean() * 100
print(port_survival)

print("\n=== ADVANCED INSIGHTS ===")

# Women and children first?
women = df[df['Sex'] == 'female']
children = df[df['Age'] < 18]
print(f"\nWomen survival rate: {women['Survived'].mean() * 100:.1f}%")
print(f"Children survival rate: {children['Survived'].mean() * 100:.1f}%")
print(f"Adult men survival rate: {df[(df['Sex'] == 'male') & (df['Age'] >= 18)]['Survived'].mean() * 100:.1f}%")

# Rich vs poor?
high_fare = df[df['Fare'] > df['Fare'].median()]
low_fare = df[df['Fare'] <= df['Fare'].median()]
print(f"\nHigh fare passengers survival: {high_fare['Survived'].mean() * 100:.1f}%")
print(f"Low fare passengers survival: {low_fare['Survived'].mean() * 100:.1f}%")

# Most common names
print("\n10 Most common first names:")
df['FirstName'] = df['Name'].str.split(',').str[1].str.split('.').str[1].str.strip().str.split().str[0]
print(df['FirstName'].value_counts().head(10))

print("\n=== SAVE CLEANED DATA ===")
# Create a cleaned version with new features
df_clean = df[['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age', 'Fare', 
               'FamilySize', 'AgeGroup']].copy()
df_clean.to_csv('titanic_cleaned.csv', index=False)
print("Cleaned data saved to 'titanic_cleaned.csv'")