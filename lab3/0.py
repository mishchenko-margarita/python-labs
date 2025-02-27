from create_list import create_list


numbers = create_list()
print(numbers)

result = []
previous = numbers[0]
for number in numbers[1:]:
    if number > previous:
        result.append(number)
    previous = number

print(result)
