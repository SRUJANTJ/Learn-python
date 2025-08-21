# It helps you create 2D graphs & plots (line plots, bar charts, histograms, scatter plots, etc.).

# In ML, it’s mainly used for visualizing datasets, distributions, model results, and training progress.
# 🔹 Why Use Matplotlib in ML?

# Understand your data before training (Exploratory Data Analysis – EDA).

# Example: See how features are distributed with histograms.

# Visualize relationships between variables.

# Example: Scatter plots to check correlation.

# Track model performance.

# Example: Plot training vs validation accuracy/loss.

# Communicate results clearly.

# Example: Bar plots for feature importance.

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
plt.plot(x, y, label="sin(x)", color="blue")


plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Line Plot")

# Show legend and graph
# Legends describe each line/point/bar when you have multiple plots.
plt.legend()
# Without plt.show(), the plot might not display (especially in some IDEs or scripts).
plt.show()