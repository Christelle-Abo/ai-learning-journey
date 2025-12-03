# Day 4: Simple Prediction Model
import pandas as pd
import numpy as np

print("=== BUILD A SURVIVAL PREDICTION MODEL ===\n")

# Load data
df = pd.read_csv('train.csv')
print(f"Loaded {len(df)} passengers")

print("\n=== STEP 1: PREPARE THE DATA ===")

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# Convert categorical to numeric
df['Sex_Numeric'] = (df['Sex'] == 'female').astype(int)
df['Embarked_S'] = (df['Embarked'] == 'S').astype(int)
df['Embarked_C'] = (df['Embarked'] == 'C').astype(int)

# Create useful features
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

print("Features prepared!")
print("\nFeatures we'll use for prediction:")
features_to_use = ['Pclass', 'Sex_Numeric', 'Age', 'Fare', 'FamilySize', 'IsAlone', 'Embarked_S', 'Embarked_C']
print(features_to_use)

print("\n=== STEP 2: SIMPLE RULE-BASED MODEL ===")
print("Let's start with simple rules based on what we learned:\n")

# Rule 1: All women survive, all men die
def simple_model_1(row):
    return 1 if row['Sex'] == 'female' else 0

df['Prediction_1'] = df.apply(simple_model_1, axis=1)
accuracy_1 = (df['Prediction_1'] == df['Survived']).mean() * 100
print(f"Model 1 (Women survive, men die): {accuracy_1:.1f}% accurate")

# Rule 2: Women and children survive
def simple_model_2(row):
    if row['Sex'] == 'female':
        return 1
    elif row['Age'] < 18:
        return 1
    else:
        return 0

df['Prediction_2'] = df.apply(simple_model_2, axis=1)
accuracy_2 = (df['Prediction_2'] == df['Survived']).mean() * 100
print(f"Model 2 (Women + children survive): {accuracy_2:.1f}% accurate")

# Rule 3: Women + 1st class survive
def simple_model_3(row):
    if row['Sex'] == 'female':
        return 1
    elif row['Pclass'] == 1:
        return 1
    else:
        return 0

df['Prediction_3'] = df.apply(simple_model_3, axis=1)
accuracy_3 = (df['Prediction_3'] == df['Survived']).mean() * 100
print(f"Model 3 (Women + 1st class survive): {accuracy_3:.1f}% accurate")

# Rule 4: Advanced rules
def simple_model_4(row):
    score = 0
    
    # Female gives +2 points
    if row['Sex'] == 'female':
        score += 2
    
    # First class gives +1 point
    if row['Pclass'] == 1:
        score += 1
    
    # Child gives +1 point
    if row['Age'] < 18:
        score += 1
    
    # High fare gives +1 point
    if row['Fare'] > 50:
        score += 1
    
    # Predict survive if score >= 2
    return 1 if score >= 2 else 0

df['Prediction_4'] = df.apply(simple_model_4, axis=1)
accuracy_4 = (df['Prediction_4'] == df['Survived']).mean() * 100
print(f"Model 4 (Scoring system): {accuracy_4:.1f}% accurate")

print("\n=== MODEL COMPARISON ===")
results = pd.DataFrame({
    'Model': ['Women only', 'Women + Children', 'Women + 1st Class', 'Scoring System'],
    'Accuracy': [accuracy_1, accuracy_2, accuracy_3, accuracy_4]
})
print(results)
print(f"\nBest model: {results.loc[results['Accuracy'].idxmax(), 'Model']} with {results['Accuracy'].max():.1f}%")

print("\n=== DETAILED ANALYSIS ===")
print("\nConfusion Matrix for best simple model:")
best_pred = 'Prediction_1'  # Usually this is the best

# True Positives, False Positives, etc.
tp = ((df[best_pred] == 1) & (df['Survived'] == 1)).sum()
fp = ((df[best_pred] == 1) & (df['Survived'] == 0)).sum()
tn = ((df[best_pred] == 0) & (df['Survived'] == 0)).sum()
fn = ((df[best_pred] == 0) & (df['Survived'] == 1)).sum()

print(f"True Positives (Correctly predicted survivors): {tp}")
print(f"False Positives (Predicted survive but died): {fp}")
print(f"True Negatives (Correctly predicted deaths): {tn}")
print(f"False Negatives (Predicted die but survived): {fn}")

precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0

print(f"\nPrecision: {precision:.2f} (When we predict survive, we're right {precision*100:.1f}% of time)")
print(f"Recall: {recall:.2f} (We catch {recall*100:.1f}% of actual survivors)")

print("\n=== TEST YOUR OWN PREDICTIONS ===")
print("\nLet's predict some specific passengers:")

test_passengers = [
    {'Name': 'Rich Woman', 'Pclass': 1, 'Sex': 'female', 'Age': 30, 'Fare': 100},
    {'Name': 'Poor Man', 'Pclass': 3, 'Sex': 'male', 'Age': 25, 'Fare': 8},
    {'Name': 'Child', 'Pclass': 2, 'Sex': 'male', 'Age': 8, 'Fare': 20},
    {'Name': 'Rich Man', 'Pclass': 1, 'Sex': 'male', 'Age': 40, 'Fare': 150}
]

for passenger in test_passengers:
    prediction = simple_model_4(passenger)
    prob = "HIGH" if prediction == 1 else "LOW"
    print(f"\n{passenger['Name']}:")
    print(f"  Class: {passenger['Pclass']}, Sex: {passenger['Sex']}, Age: {passenger['Age']}, Fare: ${passenger['Fare']}")
    print(f"  Survival prediction: {prob} chance")

print("\n=== SAVE PREDICTIONS ===")
df[['PassengerId', 'Name', 'Survived', 'Prediction_1', 'Prediction_2', 'Prediction_3', 'Prediction_4']].to_csv('titanic_predictions.csv', index=False)
print("Predictions saved to 'titanic_predictions.csv'")

print("\n" + "="*50)
print("🎉 YOU JUST BUILT YOUR FIRST PREDICTION MODEL! 🎉")
print("="*50)
print("\nWhat you learned:")
print("1. How to prepare data for modeling")
print("2. How to create prediction rules based on patterns")
print("3. How to measure model accuracy")
print("4. How to compare different approaches")
print("\nNext step: In future days, you'll learn Machine Learning")
print("algorithms that find these patterns automatically!")