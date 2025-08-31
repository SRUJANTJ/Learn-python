# What is Seaborn?

# Seaborn is a Python data visualization library built on top of Matplotlib. It provides:

# High-level interface for creating visually appealing statistical graphics.

# Built-in themes and color palettes for more attractive plots.

# Functions for visualizing relationships, distributions, and categorical data in a simpler way than Matplotlib.




# Why Use Seaborn in ML?

# In Machine Learning, data visualization helps with:

# Exploratory Data Analysis (EDA) – understanding the dataset before training models.

# Pattern Detection – spotting trends, correlations, or anomalies.

# Feature Analysis – comparing distributions of features.

# Model Evaluation – visualizing results like confusion matrices or feature importance.




# Advantages over Matplotlib:

# Cleaner default styles.

# Built-in statistical plotting.

# Easier handling of Pandas DataFrames.




#  (A) Distribution Plots
# Show how data is distributed.

import seaborn as sns
import matplotlib.pyplot as plt

# Example data
import numpy as np
data = np.random.normal(loc=0, scale=1, size=1000)

# Histogram + KDE
sns.histplot(data, kde=True, bins=30, color='skyblue')
plt.show()

# histplot() → histogram with optional KDE (Kernel Density Estimation)

# kdeplot() → smooth curve showing distribution

# Useful for checking normality or skewness of features.