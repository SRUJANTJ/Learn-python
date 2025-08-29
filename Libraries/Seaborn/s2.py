# Categorical Plots

# Compare values across categories.

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # <-- Import matplotlib for plt.show()

# Sample dataset
df = sns.load_dataset('titanic')

# Count plot
sns.countplot(x='class', data=df, palette='Set2')
plt.show()

# Box plot
sns.boxplot(x='class', y='age', data=df, palette='Set3')
plt.show()

# Violin plot (like box plot but shows density)
sns.violinplot(x='class', y='age', data=df, hue='sex', split=True)
plt.show()


# Helps analyze relationships between categorical and numerical features.

# Detect outliers with boxplots or violins.


