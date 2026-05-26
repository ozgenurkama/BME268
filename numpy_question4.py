import numpy as np

arr = np.random.randint(0,101,20)

mean = np.mean(arr)
median = np.median(arr)
std = np.std(arr)

indices = np.where(arr > 50)

arr[arr < 25] = 0

print(arr)
print(mean)
print(median)
print(std)
print(indices)