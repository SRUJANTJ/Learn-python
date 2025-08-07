import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # Element-wise → [4 10 18]
print(a / b)  # Element-wise → [0.25 0.4 0.5]
print(np.dot(a, b))  # Dot product → 32
