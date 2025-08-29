import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib for plt.show()

# Relationship Plots

# Show correlation between features.

df = sns.load_dataset('titanic')

# Scatter plot with regression line
sns.lmplot(x='fare', y='age', data=df, hue='Gender', markers=['o', 'x'])
plt.show()

# Pairplot (all features relationships)
sns.pairplot(df, hue='Gender', palette='coolwarm')
plt.show()

# lmplot() → linear regression trends
# pairplot() → pairwise scatter plots + distribution

# Useful in ML to see feature correlations or separability.
