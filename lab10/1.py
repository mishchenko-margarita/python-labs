import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_legendre


plt.style.use("seaborn-v0_8")
plt.figure(figsize=(12, 8), dpi=100)

x = np.linspace(-1, 1, 500)

for n in range(1, 8):
    y = eval_legendre(n, x)
    plt.plot(x, y, lw=2, label=f"n = {n}")

    x_annot = 0.98
    y_annot = eval_legendre(n, x_annot)

    plt.annotate(
        f"n = {n}",
        xy=(x_annot, y_annot),
        xytext=(10, 0),
        textcoords="offset points",
        ha="left",
        va="center",
        fontsize=10,
        arrowprops=dict(arrowstyle="-|>", color="black", lw=0.8)
    )

plt.title("Полиномы Лежандра", fontsize=16, pad=20)
plt.xlabel("x", fontsize=12)
plt.ylabel("P_n(x)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.xlim(-1, 1)
plt.ylim(-1.5, 1.5)
plt.tight_layout()
plt.show()
