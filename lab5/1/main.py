with open("input.txt") as file:
    numbers = [int(number) for number in file.read().split()]
    print("numbers readed")

with open("output.txt", "w") as file:
    product = 1
    for number in numbers: product *= number
    print("numbers multiplied")
    file.write(str(product))
    print("product saved")

print("success")
