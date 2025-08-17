# Removing Duplicates (if any)
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David', 'Alice'],
    'Age': [25, 30, 25, 40, 25],
    'Score': [85, 90, 85, 76, 85]
})

print("Before:")
print(df)

df.drop_duplicates(inplace=True)

print("\nAfter:")
print(df)


# subset → Check duplicates only in certain columns.

# Detecting Outliers


# Outliers mean the data points that are very different (far away) from the rest of the data.
# Example: If most students score 70–95, but one student has 10, that 10 is an outlier.

# Outliers can happen due to errors (wrong entry) or rare but true cases.

# Sample dataset
data = {'Scores': [50, 52, 53, 54, 55, 100]}  # 100 is suspicious
df = pd.DataFrame(data)
mean = df['Scores'].mean()
std = df['Scores'].std()
outliers = df[(df['Scores'] < mean - 2*std) | (df['Scores'] > mean + 2*std)]

print("Outliers:\n", outliers)


