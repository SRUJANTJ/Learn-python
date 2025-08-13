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






# Data Cleaning
# Before feeding data into an ML model, cleaning is critical to avoid garbage in → garbage out.


# Common Data Cleaning Steps


# | Task                  | Pandas Function                | Why for ML?                                   |
# | --------------------- | ------------------------------ | --------------------------------------------- |
# | Remove missing values | `dropna()`                     | Some models can’t handle NaN values           |
# | Fill missing values   | `fillna(value)`                | Keep data size same for better generalization |
# | Change data type      | `astype()`                     | ML algorithms require numeric data            |
# | Remove duplicates     | `drop_duplicates()`            | Avoid data leakage and bias                   |
# | Rename columns        | `rename(columns={...})`        | Keep features consistent                      |
# | Detect outliers       | `.describe()` / `quantile()`   | Outliers can skew models                      |
# | String cleanup        | `.str.lower()`, `.str.strip()` | Needed for NLP & categorical encoding         |






# Extra Pandas Concepts for ML

# Feature Engineering with Pandas
# Normalization / Scaling:

df['Age_norm'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()


# Binning Continuous Variables:


df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 30, 50], labels=['Teen', 'Young', 'Adult'])

# Encoding Categorical Variables:

df = pd.get_dummies(df, columns=['AgeGroup'], drop_first=True)


# Data Aggregation
# Grouping and summarizing before ML:
df.groupby('Age')['Score'].mean()



# Joining / Merging

# Often ML datasets come from multiple sources:

df1 = pd.DataFrame({
    'id': [1, 2, 3],
    'feature1': [10, 20, 30]
})

df2 = pd.DataFrame({
    'id': [1, 2, 4],
    'feature2': [100, 200, 400]
})

merged_df = pd.merge(df1, df2, on='id', how='inner')
print(merged_df)



# Time Series Features


# If working with temporal data:

# Example: Creating a Date column and extracting Month feature
df['Date'] = pd.to_datetime(['2024-01-15', '2024-02-20', '2024-03-10'])
df['Month'] = df['Date'].dt.month
print(df[['Date', 'Month']])


