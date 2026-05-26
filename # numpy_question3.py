import numpy as np

A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,3))

elementwise = A * B

matrix_mult = np.dot(A,B)

A_inv = np.linalg.inv(A)

identity = A @ A_inv

print(A)
print(B)
print(elementwise)
print(matrix_mult)
print(A_inv)
print(identity)