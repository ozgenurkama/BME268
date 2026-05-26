import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.signal import find_peaks

t = np.array([0,3,6,9,12,18,24])
T = np.array([37.0,37.8,38.5,39.1,38.6,37.9,37.2])

linear_interp = interp1d(t, T, kind='linear')
cubic_interp = interp1d(t, T, kind='cubic')

tt = np.linspace(0,24,500)

linear_T = linear_interp(tt)
cubic_T = cubic_interp(tt)

peaks, _ = find_peaks(cubic_T)

plt.figure(figsize=(10,5))

plt.plot(tt, linear_T, label='Linear')
plt.plot(tt, cubic_T, label='Cubic')
plt.scatter(t, T)

for p in peaks:
    plt.axvline(tt[p], linestyle='--')

plt.axhline(38.5, linestyle='--')

plt.fill_between(tt, cubic_T, 38.5, where=(cubic_T > 38.5), alpha=0.3)

plt.legend()
plt.show()