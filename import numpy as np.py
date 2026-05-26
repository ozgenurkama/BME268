import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

C = lambda t: 20*np.exp(-0.15*t)

auc_48, _ = quad(C, 0, 48)
auc_inf, _ = quad(C, 0, np.inf)

percentage = (auc_48 / auc_inf) * 100

t1 = np.linspace(0, 48, 500)
t2 = np.linspace(0, 100, 1000)

fig, ax = plt.subplots(1, 2, figsize=(12,5))

ax[0].plot(t1, C(t1))
ax[0].fill_between(t1, C(t1), alpha=0.3)
ax[0].set_title("AUC 0-48h")

ax[1].plot(t2, C(t2))
ax[1].fill_between(t2, C(t2), alpha=0.3)
ax[1].set_title("AUC 0-inf")

plt.tight_layout()
plt.show()

print("AUC (0-48h):", auc_48)
print("AUC (0-inf):", auc_inf)
print("Percentage in first 48h:", percentage)