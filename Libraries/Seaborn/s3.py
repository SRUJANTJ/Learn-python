import seaborn as sns
import matplotlib.pyplot as plt  # Import matplotlib for plt.show()

# Relationship Plots

# Show correlation between features.

df = sns.load_dataset('titanic')

# Relationship Plots mean how the two  fare and age is related to each other 
# Scatter plot with regression line
sns.lmplot(x='fare', y='age', data=df, hue='sex', markers=['o', 'x'])
plt.show()

# Pairplot (all features relationships)
sns.pairplot(df, hue='sex', palette='coolwarm')
plt.show()

# lmplot() → linear regression trends
# lmplot() → Scatter plot + regression line.

# It helps check if there’s a linear (or other) relationship between two numerical features.

# Example: Does fare increase with age in Titanic data?

# With hue='sex', you can see if the relation is different across categories.



# pairplot() → pairwise scatter plots + distribution

# pairplot() → Creates scatterplots for all feature pairs and histograms for individual features.

# Helps visualize feature correlations across the dataset.

# Example: In Titanic, you can see how age, fare, pclass, etc. interact with each other, and whether categories like sex separate them.

# Useful in ML to see feature correlations or separability.
