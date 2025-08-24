# Histogram

# A histogram shows the distribution of a single variable (one feature/column).
# It divides the range of values into bins (intervals) and counts how many data points fall into each bin.

import matplotlib.pyplot as plt
import numpy as np



data = np.random.randn(1000)  # Normally distributed data
plt.hist(data, bins=30, color="green", alpha=0.7)
plt.title("Data Distribution")
plt.show()

# What does a Histogram show?

# Shape of data distribution

# Is the data normal (bell curve), skewed left/right, or has multiple peaks?

# Spread of values

# Are values tightly grouped or widely spread out?

# Frequency of values

# Which ranges occur most often?

# Detect anomalies/outliers

# If some bars are far away from others, those may be outliers.







# Why is it useful in Machine Learning?

# Feature Understanding:
# Before training, you want to know how a feature looks. For example:

# Age column → Are most people young or old?

# Salary column → Is it normally distributed or skewed?

# Feature Scaling:
# If one feature has a wide spread, it may need normalization/standardization.

# Handling Imbalanced Data:
# For classification, histograms can show if one class dominates.

# Detecting Outliers:
# Extremely high or low values stand out in histograms.