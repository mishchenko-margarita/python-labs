with open("input.txt") as file:
    numbers = (int(number) for number in file.read().split())
    print("numbers readed")

with open("output.txt", "w") as file:
    sort = "\n".join(str(number) for number in sorted(numbers))
    print("numbers sorted")
    file.write(sort)
    print("sort saved")

print("success")
