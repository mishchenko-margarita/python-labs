frequency = dict()

for line in input().split():
    if line not in frequency:
        frequency[line] = 0

    frequency[line] += 1

print(*frequency.values())
