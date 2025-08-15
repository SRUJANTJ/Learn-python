# Clean the Data
import pandas as pd 

# Handling Missing Values

df= pd.read_csv('students.csv')


# Fill missing Age with the mean
# .fillna(value) replaces all NaN (missing values) with the given value.
# Mean → The average

# Add up all the numbers.

# Divide by how many numbers there are.

# Example:
# Numbers: 2, 4, 6
# Sum = 2 + 4 + 6 = 12
# Mean = 12 ÷ 3 = 4


df['StudentID'] = df['StudentID'].fillna(df['StudentID'].mean())

# Fill missing Score with the median
# If HoursStudied had missing values, they’d be replaced with that median value.

# Median → The middle value

# Arrange the numbers in order.

# Pick the one in the middle.

# Example:
# Numbers: 2, 4, 6
# Middle number = 4 (so median is 4)

# If there’s an even number of values:
# Numbers: 2, 4, 6, 8
# Middle two numbers = 4 and 6
# Median = (4 + 6) ÷ 2 = 5
df['HoursStudied'] = df['HoursStudied'].fillna(df['HoursStudied'].median())

print(df)

# Key difference:

# Mean is affected by very big or very small numbers.

# Median is just the middle, so it ignores extremes.