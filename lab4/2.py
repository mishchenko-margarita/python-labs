data = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}
print(list(data.keys())[list(data.values()).index(input())])

data = {"beep": "car"}
print(list(data.keys())[list(data.values()).index(input())])

data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(list(data.keys())[list(data.values()).index(int(input()))])
