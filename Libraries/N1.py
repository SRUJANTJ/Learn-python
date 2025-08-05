import numpy as np
# Indexing & Slicing
# 1D
a = np.array([10, 20, 30, 40])
print(a[0])     # 10
print(a[-1])    # 40
print(a[1:3])   # [20 30]

# 2D
b = np.array([[1, 2], [3, 4], [5, 6]])
print("its",b[0, 1])  # Row 0, Col 1 → 2
print(b[:, 0])  # All rows, first column → [1 3 5]

print(b.shape)