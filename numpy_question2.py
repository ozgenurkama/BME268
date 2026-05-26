import numpy as np
x = np.linspace(0, 2*np.pi, 100)

filtered = x[np.sin(x) > 0.5]

print(filtered)
print(len(filtered))