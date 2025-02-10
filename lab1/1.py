a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

min, max = 1_000_000, -1_000_000

if a < min:
    min = a
if b < min:
    min = b
if c < min:
    min = c

if a > max:
    max = a
if b > max:
    max = b
if c > max:
    max = c

print("Минимальное число: ", min)
print("Максимальное число: ", max)
