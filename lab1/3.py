n = int(input("n: "))

triangle = []
row = [1]
for _ in range(n):
    triangle.append(row)
    row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

max_width = len(triangle[-1]) + len(str(max(triangle[-1])))

for i, row in enumerate(triangle):
    print(" " * (max_width - i - len(str(max(row)))), *row)
