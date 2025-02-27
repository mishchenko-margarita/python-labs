from random import randint as ri


def create_list():
    mode = input("enter[e] | generate[g]: ")
    numbers = None

    if mode == "e":
        numbers = [int(i) for i in input("number: ").split()]
    elif mode == "g":
        n = int(input("n: "))
        numbers = [ri(10, 100) for _ in range(n)]
    else:
        print("invalid.")
        exit()

    return numbers