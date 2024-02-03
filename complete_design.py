import numpy as np
import matplotlib.pyplot as plt

k = 1;  # MN/m
m = 200;  # kg
x = 0;  # m

k = k * 10 ** 6

def force_time(x):
    F_peak = 1000 + 9 * x ** 2 - 183 * x
    td = 20 - 0.12 * x ** 2 + 4.2 * x
    return (F_peak * 1000, td / 1000)  # SI Units

f_peak, td = force_time(x)
w = np.sqrt(k / m)
T = 2 * np.pi / w

tstep = 0.01
trange = np.arange(0, 2 * T + tstep, tstep)
z = np.zeros(len(trange))
i = -1
for t in trange:
    i = i + 1
    if t <= td:
        z[i] = ((f_peak / k) * (1 - np.cos(w * t)) + (f_peak / (k * td)) * ((np.sin(w * t) / w) - t))
    else:
        z[i] = ((f_peak / (k * w * td)) * (np.sin(w * t) - np.sin(w * (t - td))) - (f_peak / k) * np.cos(w * t))

zmax = max(z)
print(f"Maximum displacement: {zmax * 1000} mm")

index = np.where(z == zmax)[0][0]
tmax = trange[index]

i = -1
fig, ax = plt.subplots()
ax.scatter(tmax * 1000, zmax * 1000, edgecolor='red', facecolor='None', zorder=3)
ax.plot([i * 1000 for i in trange], [i * 1000 for i in z], color='k', zorder=2)

ax.grid(visible=True, which='both')
ax.minorticks_on()
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Displacement (mm)')

plt.show()
