from create_list import create_list


numbers = create_list()
print(numbers)

min = 10**6
max = -min

i_min = i_max = 0
for i in range(len(numbers)):
    if numbers[i] < min:
        min = numbers[i]
        i_min = i
    if numbers[i] > max:
        max = numbers[i]
        i_max = i

print(f"min: {min}, max: {max}")

numbers[i_min], numbers[i_max] = numbers[i_max], numbers[i_min]

print(numbers)
