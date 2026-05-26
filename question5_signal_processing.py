import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

fs = 1000
t = np.linspace(0, 3, fs*3)

signal = (
    1*np.sin(2*np.pi*5*t) +
    0.4*np.sin(2*np.pi*60*t) +
    0.2*np.random.randn(len(t))
)

N = len(signal)

yf = fft(signal)
xf = fftfreq(N, 1/fs)

power = np.abs(yf[:N//2])

filtered_yf = yf.copy()

filtered_yf[np.abs(xf-60) < 1] = 0
filtered_yf[np.abs(xf+60) < 1] = 0

filtered_signal = np.real(np.fft.ifft(filtered_yf))

fig, ax = plt.subplots(3,1, figsize=(10,8))

ax[0].plot(t, signal)
ax[0].set_title("Original Signal")

ax[1].plot(xf[:N//2], power)
ax[1].set_xlim(0,100)
ax[1].set_title("Power Spectrum")

peak_indices = np.argsort(power)[-5:]

for i in peak_indices:
    ax[1].text(xf[i], power[i], f"{xf[i]:.1f} Hz")

ax[2].plot(t, filtered_signal)
ax[2].set_title("Filtered Signal")

fig.tight_layout()
plt.show()