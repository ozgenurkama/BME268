import numpy as np

A = np.arange(1,37).reshape(6,6)

submatrix = A[1:4,1:4]

flat = A.flatten()

selected = flat[::3]

print(A)
print(submatrix)
print(flat)
print(selected)