import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a - b)  # [-3 -3 -3]
print(a * b)  # Element-wise → [4 10 18]
print(a / b)  # Element-wise → [0.25 0.4 0.5]
print(np.dot(a, b))  # Dot product → 32


#  Broadcasting (Superpower of NumPy)
# Broadcasting = NumPy automatically expands dimensions for operations.


a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)

# b was stretched across rows automatically.



# Reshaping & Flattening

arr = np.arange(1, 7)  # [1 2 3 4 5 6]
print(arr.reshape(2, 3))
print(arr.flatten())   # [1 2 3 4 5 6]
