import matplotlib.pyplot as plt
import numpy as np


ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]

t = np.linspace(0, 2 * np.pi, 3000)
phase = np.pi / 2

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Фигуры Лисажу с разными соотношениями частот", fontsize=16)

for ax, (fy, fx) in zip(axs.flat, ratios):
    x = np.sin(fx * t + phase)
    y = np.sin(fy * t)

    ax.plot(x, y, color="darkblue", linewidth=1.5)
    ax.set_title(f"Соотношение {fy}:{fx}", pad=15)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.axis("equal")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
