import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_title("Фигура Лисажу: соотношение частот [0:1] → [1:1]")
line, = ax.plot([], [], lw=2, color='darkblue')

t = np.linspace(0, 2 * np.pi, 1000)
phase = 0
fx = 1


def init():
    line.set_data([], [])
    return line,


def update(frame):
    fy = frame / 100

    x = np.sin(fx * t + phase)
    y = np.sin(fy * t)

    line.set_data(x, y)
    ax.set_title(f"Фигура Лисажу: соотношение частот [{fy:.2f}:1]")
    return line,


ani = FuncAnimation(
    fig,
    update,
    frames=np.arange(0, 101),
    init_func=init,
    blit=True,
    interval=50,
    repeat=True
)

plt.show()
