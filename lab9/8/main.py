import numpy as np


x = np.array([int(i) for i in input().split()])
print(*np.arange(len(x))[x != 0])
