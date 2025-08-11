# Pandas is the go-to Python library for data manipulation, preprocessing, and analysis.
# In ML, 80% of your time is usually spent preparing data before training — Pandas is the toolkit for that.

# Series
# A Pandas Series is a 1D labeled array — think of it as a single column from an Excel sheet or one variable in your dataset.


# Why important for ML:

# Used for feature (input) or label (output) representation.

# Lets you apply transformations to one column at a time.




import pandas as pd

s = pd.Series([10, 20, 30, 40], name="Scores")
print(s)
print(s.mean())  # Useful for feature engineering


# DataFrames
# A DataFrame is a 2D table with rows and columns — essentially your whole dataset.

# Why important for ML:

# It’s how you store your dataset (features + target).

# Allows filtering, joining, reshaping — all crucial for preprocessing.


df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
})
print(df.head())  # First 5 rows

# Extra ML Concepts with DataFrames:

# Feature selection: df[['Age', 'Score']]

# Adding features: df['AgeSquared'] = df['Age']**2

# Handling missing values before feeding into ML.

