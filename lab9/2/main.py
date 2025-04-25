import numpy as np


x = [int(i) for i in input().split()]
print(np.unique(x, return_counts=True))
