# Vectorized Operations


data = [1, 2, 3]
result = []
for x in data:
    result.append(x*2)


print(result)  # [2, 4, 6]


# With NumPy:
import numpy as np
arr = np.array([1, 2, 3])
result = arr * 2
print(result)  # [2 4 6]
