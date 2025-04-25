import numpy as np


with open("matrix") as file:
    matrix_raw = file.read().split()

matrix = np.matrix([
    [int(i) for i in row.split(",")]
    for row in matrix_raw
])

print(f"""
matrix:
{matrix}
sum: {np.sum(matrix)}
max: {np.max(matrix)}
min: {np.min(matrix)}
""", end="")
