from create_list import create_list


numbers1 = create_list()
numbers2 = create_list()

print(numbers1, numbers2, sep="\n")
print(len([
    number for number in numbers2 if number in numbers1
]))