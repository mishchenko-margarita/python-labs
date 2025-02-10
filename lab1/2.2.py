n = int(input("n: "))

for i in range(n, 0, -1):
    line = (n - i) * " "
    for j in range(i, 0, -1):
        line += str(j)
    for j in range(2, i + 1):
        line += str(j)
    print(line)
