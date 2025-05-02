import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


fig = plt.figure(figsize=(12, 10))
gs = fig.add_gridspec(4, 4)

ax1 = fig.add_subplot(gs[0, :2])
ax2 = fig.add_subplot(gs[0, 2:])
ax_sum = fig.add_subplot(gs[1, :])

ax_amp1 = fig.add_subplot(gs[2, 0])
ax_freq1 = fig.add_subplot(gs[2, 1])
ax_amp2 = fig.add_subplot(gs[3, 0])
ax_freq2 = fig.add_subplot(gs[3, 1])

initial_amp1 = 1.0
initial_freq1 = 1.0
initial_amp2 = 1.0
initial_freq2 = 1.0

x = np.linspace(0, 4*np.pi, 1000)
wave1 = initial_amp1 * np.sin(initial_freq1 * x)
wave2 = initial_amp2 * np.sin(initial_freq2 * x)
wave_sum = wave1 + wave2

line1, = ax1.plot(x, wave1, lw=2, color="blue")
line2, = ax2.plot(x, wave2, lw=2, color="green")
line_sum, = ax_sum.plot(x, wave_sum, lw=2, color="red")

for ax in [ax1, ax2, ax_sum]:
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-3, 3)
    ax.grid(True, linestyle="--", alpha=0.7)
    
ax1.set_title("Волна 1: $A_1 \cdot \sin(f_1 x)$")
ax2.set_title("Волна 2: $A_2 \cdot \sin(f_2 x)$")
ax_sum.set_title("Результирующая волна: $A_1 \cdot \sin(f_1 x) + A_2 \cdot \sin(f_2 x)$")

amp1_slider = Slider(
    ax=ax_amp1,
    label="Амплитуда 1",
    valmin=0,
    valmax=2,
    valinit=initial_amp1,
    valstep=0.1
)

freq1_slider = Slider(
    ax=ax_freq1,
    label="Частота 1",
    valmin=0,
    valmax=5,
    valinit=initial_freq1,
    valstep=0.1
)

amp2_slider = Slider(
    ax=ax_amp2,
    label="Амплитуда 2",
    valmin=0,
    valmax=2,
    valinit=initial_amp2,
    valstep=0.1
)

freq2_slider = Slider(
    ax=ax_freq2,
    label="Частота 2",
    valmin=0,
    valmax=5,
    valinit=initial_freq2,
    valstep=0.1
)


def update(val):
    a1 = amp1_slider.val
    f1 = freq1_slider.val
    a2 = amp2_slider.val
    f2 = freq2_slider.val

    new_wave1 = a1 * np.sin(f1 * x)
    new_wave2 = a2 * np.sin(f2 * x)
    new_sum = new_wave1 + new_wave2

    line1.set_ydata(new_wave1)
    line2.set_ydata(new_wave2)
    line_sum.set_ydata(new_sum)

    fig.canvas.draw_idle()


amp1_slider.on_changed(update)
freq1_slider.on_changed(update)
amp2_slider.on_changed(update)
freq2_slider.on_changed(update)

plt.tight_layout()
plt.show()
