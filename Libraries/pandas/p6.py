import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David', 'Alice'],
    'Age': [25, 30, 25, 40, 25],
    'Score': [85, 90, 85, 76, 85],
    'Gender': ['F', 'M', 'F', 'M', 'F'],
    'Hours_Study': [5, 6, 4, 3, 7]
})

# Encode Gender as numeric (M=1, F=0)
df['Gender'] = df['Gender'].map({'M': 1, 'F': 0})

# Create a "Performance_Level" feature
df['Performance_Level'] = pd.cut(df['Score'],
                                 bins=[0, 80, 90, 100],
                                 labels=['Low', 'Medium', 'High'])
# Feature Engineering is the process of creating, transforming, or selecting features (columns/variables) from raw data to make them more useful for ML models.
# 👉 In simple words:
# It’s like preparing better ingredients before cooking — the better your features, the better your model learns.

# Create a feature: Age × Hours_Study
df['Age_Study'] = df['Age'] * df['Hours_Study']

print("DataFrame with new features:")
print(df)