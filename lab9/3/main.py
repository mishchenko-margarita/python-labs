import numpy as np


x = np.random.randn(10, 4)

min_values = np.min(x, axis=0)
max_values = np.max(x, axis=0)
mean_values = np.mean(x, axis=0)
std_dev_values = np.std(x, axis=0)

first_5_rows = x[:5]

print("Минимальные значения:", min_values)
print("Максимальные значения:", max_values)
print("Средние значения:", mean_values)
print("Стандартное отклонение:", std_dev_values)
print("\nПервые 5 строк массива:")
print(first_5_rows)
