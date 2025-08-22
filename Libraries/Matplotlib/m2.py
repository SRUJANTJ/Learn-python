# Common Plots for ML
# Line Plot – For trends (loss/accuracy curve)
# A line plot connects data points with lines.
# In ML, we often track how loss and accuracy change as training progresses (over epochs).
import matplotlib.pyplot as plt 

epochs = [1, 2, 3, 4, 5]
train_loss = [0.9, 0.7, 0.5,0.3,0.2]

plt.plot(epochs , train_loss, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Training Loss')
plt.title('Training Loss over Epochs')
plt.show()