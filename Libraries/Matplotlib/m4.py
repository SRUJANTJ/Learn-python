# Bar Chart – For feature importance

# it represent the how much model is predicting the acurate or not

import matplotlib.pyplot as plt
import numpy as np


features = ["A", "B", "C", "D"]
importance = [0.2, 0.4, 0.1, 0.3]


# Feature A = 0.2 → This feature contributes 20% weight (less useful for the model).

# Feature B = 0.4 → This feature contributes 40% weight (more useful, stronger predictor than A).

# Feature C = 0.1 → Very low importance.

# Feature D = 0.3 → Moderate importance.

plt.bar(features, importance, color="purple")
plt.title("Feature Importance")
plt.show()

# the bar height represents how important (or useful) the feature is for predictions, not directly “accuracy.”

# What is Predictive Power?

# In ML, predictive power = how much a feature helps the model make correct predictions.

# Some features strongly correlate with the target → high predictive power.

# Some features barely relate to the target → low predictive power.

# Say we’re predicting House Price 🏡

# Feature A (Bedrooms) = 0.2

# Feature B (Size in sq ft) = 0.4

# Feature C (Color of the front door) = 0.1

# Feature D (Location) = 0.3


# If we remove Feature B (0.4) → House Size

# Size is strongly correlated with price (bigger house → higher price).

# Without it, the model loses important information.

# Predictions become less accurate because the model can’t “see” one of the strongest indicators.

# If we remove Feature C (0.1) → Door Color

# Door color hardly affects house price.

# Removing it won’t hurt accuracy.

# The model still has other useful features (Bedrooms, Size, Location).


# Why does this happen?

# The model learns weights (importance) during training.

# Features with higher importance explain more of the variation in the target.

# Removing them → model loses signal → predictive power drops.

# Removing low-importance ones → barely any effect.