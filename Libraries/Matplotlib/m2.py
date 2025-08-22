# Common Plots for ML
# Line Plot – For trends (loss/accuracy curve)
# A line plot connects data points with lines.
# In ML, we often track how loss and accuracy change as training progresses (over epochs).
import matplotlib.pyplot as plt 
import numpy as np
epochs = [1, 2, 3, 4, 5]
train_loss = [0.9, 0.7, 0.5,0.3,0.2]

plt.plot(epochs , train_loss, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Training Loss')
plt.title('Training Loss over Epochs')
plt.show()



# Scatter Plot – For feature relationships
x = np.random.rand(50)
y = x * 2 + np.random.rand(50)

plt.scatter(x, y, color="red")
plt.xlabel("Feature X")
plt.ylabel("Feature Y")
plt.title("Feature Relationship")
plt.show()