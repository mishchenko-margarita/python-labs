import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


w0 = np.linspace(-5, 5, 100)
w1 = np.linspace(-5, 5, 100)
W0, W1 = np.meshgrid(w0, w1)

MSE = W0**2 + W1**2 + 1e-8

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121, projection="3d")
surf1 = ax1.plot_surface(W0, W1, MSE, cmap="viridis", edgecolor="none")
ax1.set_title("MSE в линейном масштабе")
ax1.set_xlabel("Параметр w0")
ax1.set_ylabel("Параметр w1")
ax1.set_zlabel("MSE")

ax2 = fig.add_subplot(122, projection="3d")
surf2 = ax2.plot_surface(W0, W1, MSE, cmap="plasma", edgecolor="none")
ax2.set_zscale("log")
ax2.set_title("MSE с логарифмической осью Z")
ax2.set_xlabel("Параметр w0")
ax2.set_ylabel("Параметр w1")
ax2.set_zlabel("log(MSE)")

plt.tight_layout()
plt.show()
