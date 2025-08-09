from numpy.linalg import inv, eig
import numpy as np

A = np.array([[1, 2], [3, 4]])

det = np.linalg.det(A)   # Determinant
inv_A = inv(A)           # Inverse
e_vals, e_vecs = eig(A)  # Eigenvalues/vectors

print("Determinant:", det)
print("Inverse:\n", inv_A)
print("Eigenvalues:", e_vals)
print("Eigenvectors:\n", e_vecs)