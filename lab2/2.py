line = input()
frequency = {}

for char in line.replace(" ", ""):
    if char not in frequency:
        frequency[char] = line.count(char)

for i in range(3):
    top_char = max(frequency, key=frequency.get)
    print(top_char, frequency[top_char])
    frequency.pop(top_char)
