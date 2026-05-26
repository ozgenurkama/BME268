import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

r = 0.04
K = 100
V0 = 0.5

def logistic(t, V):
   return r*V*(1 - V/K)

t_span = (0, 300)
t_eval = np.linspace(0, 300, 1000)

sol = solve_ivp(logistic, t_span, [V0], t_eval=t_eval)

t = sol.t
V = sol.y[0]

v25 = np.argmin(np.abs(V - 25))
v50 = np.argmin(np.abs(V - 50))
v75 = np.argmin(np.abs(V - 75))

plt.figure(figsize=(8,5))
plt.plot(t, V)

plt.plot(t[v25], V[v25], 'ro', label='V=25')
plt.plot(t[v50], V[v50], 'go', label='V=50')
plt.plot(t[v75], V[v75], 'bo', label='V=75')

plt.xlabel("Days")
plt.ylabel("Volume")
plt.legend()
plt.grid()
plt.show()

print("V=25 at day:", t[v25])
print("V=50 at day:", t[v50])
print("V=75 at day:", t[v75])