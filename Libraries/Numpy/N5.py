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
#  ML Use Case:

# PCA (Principal Component Analysis).
# Solving systems of equations in regression.



# Random Number Generation

rand_nums = np.random.rand(3, 3)
normal_dist = np.random.randn(1000)
print("Random Numbers:\n", rand_nums)
print("Normal Distribution Sample:\n", normal_dist[:10])  # Display first 10

#  ML Use Case:
# Initializing neural network weights.
# Splitting datasets randomly.



# Data Normalization

X = np.array([[1, 2], [3, 4], [5, 6]])
X_norm = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
print("Normalized Data:\n", X_norm)
#  ML Use Case:
# Ensuring features have similar scales for faster convergence.