n = int(input("n: "))
shift = -len(str(n)) + 1

for i in range(n, 0, -1):
    shift += len(str(i + 1)) - 1
    line = (n - i + shift) * " "

    for j in range(i, 0, -1):
        line += str(j)
    for j in range(2, i + 1):
        line += str(j)
    print(line)
