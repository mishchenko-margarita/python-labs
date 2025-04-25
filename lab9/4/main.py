import numpy as np


x = np.array([int(i) for i in input().split()])

mask = x[:-1] == 0
selected = x[1:][mask]

result = selected.max() if selected.size > 0 else None

print(result)