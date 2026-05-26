import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

doses = np.array([0.01,0.1,1,5,10,50,100])
response = np.array([1,5,12,40,62,90,95])

def hill(x, Emax, EC50, n):
    return Emax * (x**n) / (EC50**n + x**n)

popt, pcov = curve_fit(hill, doses, response, p0=[100,10,1])

Emax, EC50, n = popt
perr = np.sqrt(np.diag(pcov))

xfit = np.logspace(-2, 2, 500)
yfit = hill(xfit, *popt)

residuals = response - hill(doses, *popt)

fig, ax = plt.subplots(1,2, figsize=(12,5))

ax[0].semilogx(doses, response, 'o')
ax[0].semilogx(xfit, yfit)
ax[0].set_title("Data + Fit")

ax[1].semilogx(doses, residuals, 'o-')
ax[1].axhline(0, linestyle='--')
ax[1].set_title("Residuals")

plt.tight_layout()
plt.show()

print("EC50 =", EC50, "+/-", perr[1])