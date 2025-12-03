# Day 4: Advanced Pandas Techniques
import pandas as pd
import numpy as np

print("=== LOAD DATA ===")
df = pd.read_csv('train.csv')
print(f"Loaded {len(df)} passengers")

print("\n=== TECHNIQUE 1: PIVOT TABLES ===")
# Pivot tables = Excel pivot tables in Python!
# Show survival rate by Class AND Gender
pivot = df.pivot_table(
    values='Survived',
    index='Pclass',
    columns='Sex',
    aggfunc='mean'
)
print("Survival rate by Class and Gender:")
print(pivot)
print("\nAs percentages:")
print(pivot * 100)

print("\n=== TECHNIQUE 2: CROSSTAB ===")
# Count how many in each category
crosstab = pd.crosstab(
    df['Pclass'],
    df['Survived'],
    margins=True  # Add totals
)
print("\nPassengers by Class and Survival:")
print(crosstab)

# With percentages
crosstab_pct = pd.crosstab(
    df['Pclass'],
    df['Survived'],
    normalize='index'  # Percentage of each class
) * 100
print("\nSurvival percentage by Class:")
print(crosstab_pct)

print("\n=== TECHNIQUE 3: MULTIPLE GROUPBY ===")
# Group by multiple columns
multi_group = df.groupby(['Pclass', 'Sex'])['Survived'].agg([
    ('count', 'count'),
    ('survived', 'sum'),
    ('survival_rate', 'mean')
])
multi_group['survival_rate'] = multi_group['survival_rate'] * 100
print("\nDetailed breakdown by Class and Gender:")
print(multi_group)

print("\n=== TECHNIQUE 4: BINNING ===")
# Convert continuous variables to categories
# We already did this with Age, let's do Fare too
df['FareCategory'] = pd.cut(
    df['Fare'],
    bins=[0, 10, 30, 100, 600],
    labels=['Budget', 'Standard', 'Premium', 'Luxury']
)
print("\nSurvival by fare category:")
fare_survival = df.groupby('FareCategory')['Survived'].mean() * 100
print(fare_survival)

print("\n=== TECHNIQUE 5: HANDLING MISSING DATA ===")
print("\nMissing data summary:")
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing_Count': missing,
    'Percentage': missing_pct
})
print(missing_df[missing_df['Missing_Count'] > 0])

# Fill missing Age with median
df['Age_Filled'] = df['Age'].fillna(df['Age'].median())
print(f"\nFilled {df['Age'].isnull().sum()} missing ages with median: {df['Age'].median():.1f}")

# Fill missing Embarked with mode (most common)
most_common_port = df['Embarked'].mode()[0]
df['Embarked_Filled'] = df['Embarked'].fillna(most_common_port)
print(f"Filled missing Embarked with most common: {most_common_port}")

print("\n=== TECHNIQUE 6: FEATURE ENGINEERING ===")
# Create new meaningful features

# 1. Title from name (Mr, Mrs, Miss, etc.)
df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
print("\nTitles found:")
print(df['Title'].value_counts())

# Simplify titles
title_mapping = {
    'Mr': 'Mr',
    'Miss': 'Miss',
    'Mrs': 'Mrs',
    'Master': 'Master',
    'Dr': 'Rare',
    'Rev': 'Rare',
    'Col': 'Rare',
    'Major': 'Rare',
    'Mlle': 'Miss',
    'Mme': 'Mrs',
    'Don': 'Rare',
    'Dona': 'Rare',
    'Lady': 'Rare',
    'Countess': 'Rare',
    'Jonkheer': 'Rare',
    'Sir': 'Rare',
    'Capt': 'Rare',
    'Ms': 'Miss'
}
df['Title_Simple'] = df['Title'].map(title_mapping)
print("\nSimplified titles:")
print(df['Title_Simple'].value_counts())

print("\nSurvival by title:")
title_survival = df.groupby('Title_Simple')['Survived'].mean() * 100
print(title_survival.sort_values(ascending=False))

# 2. Is alone?
df['IsAlone'] = ((df['SibSp'] + df['Parch']) == 0).astype(int)
print(f"\nPassengers traveling alone: {df['IsAlone'].sum()}")
print(f"Alone survival rate: {df[df['IsAlone'] == 1]['Survived'].mean() * 100:.1f}%")
print(f"With family survival rate: {df[df['IsAlone'] == 0]['Survived'].mean() * 100:.1f}%")

# 3. Deck from Cabin (first letter)
df['Deck'] = df['Cabin'].str[0]
print("\nSurvival by deck:")
deck_survival = df.groupby('Deck')['Survived'].mean() * 100
print(deck_survival.sort_values(ascending=False))

print("\n=== TECHNIQUE 7: CORRELATIONS ===")
# Which features correlate with survival?
# Need to convert to numbers first
df_numeric = df.copy()
df_numeric['Sex_Numeric'] = (df['Sex'] == 'female').astype(int)
df_numeric['Embarked_Numeric'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

correlations = df_numeric[['Survived', 'Pclass', 'Sex_Numeric', 'Age_Filled', 
                            'Fare', 'SibSp', 'Parch', 'IsAlone']].corr()['Survived'].sort_values(ascending=False)
print("\nCorrelation with Survival:")
print(correlations)
print("\nInterpretation:")
print("Positive correlation = increases survival chance")
print("Negative correlation = decreases survival chance")

print("\n=== SAVE ENRICHED DATA ===")
# Save data with all new features
df_enriched = df[['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age_Filled', 
                   'Fare', 'Embarked_Filled', 'Title_Simple', 'IsAlone', 
                   'FareCategory']].copy()
df_enriched.to_csv('titanic_enriched.csv', index=False)
print("Enriched data saved to 'titanic_enriched.csv'")
print(f"Original features: 12")
print(f"New features added: {len(df.columns) - 12}")