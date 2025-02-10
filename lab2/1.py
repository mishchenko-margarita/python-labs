line = input()
encoded_line = ""

for char in line:
    if char not in encoded_line:
        count = line.count(char)
        encoded_line += f"{char}{count if count > 1 else ''}"

print(encoded_line)
