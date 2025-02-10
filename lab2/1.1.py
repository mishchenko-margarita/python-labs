encoded_line = input()
line = ""

i = 0
while i < len(encoded_line):
    if encoded_line[i].isalpha():
        line += encoded_line[i]
        i += 1
        continue

    count, j = encoded_line[i], i + 1
    while count.isdigit():
        count += encoded_line[j]
        j += 1

    count = count[:-1]
    if count:
        line += line[-1] * (int(count) - 1)
        i += len(count)
    else:
        i += 1

print(line)
