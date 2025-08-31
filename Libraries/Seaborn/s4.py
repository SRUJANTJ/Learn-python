
# Heatmaps
# Great for correlation matrices or confusion matrices.

# A heatmap is a data visualization tool that uses colors to represent values in a matrix (like correlations, distances, or feature importance).
# Darker/lighter colors show stronger/weaker relationships.

# In ML, they are often used to understand relationships between features before modeling.
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('tips')  #, titanic
# Compute correlation matrix for numeric columns only
corr = df.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Titanic Dataset")
plt.show()

# 📌 Where are Heatmaps used in ML?

# Exploratory Data Analysis (EDA)

# When you load a dataset (like Titanic), you want to understand the relationships between features.

# A heatmap of the correlation matrix shows which features are strongly related (positively or negatively).

# Example:

# In Titanic dataset, fare and pclass may be strongly correlated.

# This helps detect multicollinearity (when features carry duplicate info).