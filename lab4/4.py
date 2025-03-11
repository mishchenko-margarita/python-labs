frequency = {}
sequence = input()

for n in sequence.strip():
    if n in frequency:
        frequency[n] += 1
    else:
        frequency[n] = 1

sequence = {n: frequency[n] for n in list(sorted(frequency, key=frequency.get, reverse=True))[:3]}

print(sequence)
