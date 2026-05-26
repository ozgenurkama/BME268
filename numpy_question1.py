import numpy as np

I = np.eye(10)

A = np.random.rand(10,10)

result = I @ A

print(A)
print(result)
print(np.allclose(A, result))