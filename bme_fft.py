import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq

fs = 500
t = np.linspace(0, 2, 2 * fs)

signal = (
    1.0 * np.sin(2 * np.pi * 1.2 * t)
    + 0.3 * np.sin(2 * np.pi * 40 * t)
    + 0.5 * np.sin(2 * np.pi * 50 * t)
)

N = len(t)
F = fft(signal)
freqs = fftfreq(N, d=1 / fs)

mask = freqs > 0
power = (2.0 / N) * np.abs(F[mask])
freqs_pos = freqs[mask]

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(freqs_pos, power, "b-", lw=1)
ax.set_xlim(0, 80)
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Amplitude")
ax.set_title("Power Spectrum - ECG with noise")

ax.annotate("Heart\n1.2 Hz", xy=(1.2, 1.0), fontsize=10, color="green")
ax.annotate("Muscle\n40 Hz", xy=(40, 0.3), fontsize=10, color="orange")
ax.annotate("Power line\n50 Hz", xy=(50, 0.5), fontsize=10, color="red")
ax.grid(True, alpha=0.3)

plt.show()