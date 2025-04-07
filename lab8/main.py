import os
import sys
import csv
import random
from tabulate import tabulate


def main(filename):
    headers = None
    rows = None

    with open(filename, "r", encoding="utf-8", newline="") as file:
        spamreader = csv.reader(file, delimiter=",")
        headers = next(spamreader)
        rows = list(spamreader)

    command = None
    while True:
        command = input("> ").split()
        if command[0].lower() == "exit": break
        elif command[0].lower() == "show" and len(command) > 1:
            count = int(command[2]) if len(command) == 3 else 5
            if command[1] == "top":
                print(tabulate(rows[0:count], headers=headers))
            elif command[1] == "bottom":
                print(tabulate(rows[len(rows) - count:len(rows)], headers=headers))
            elif command[1] == "random":
                print(tabulate((random.choice(rows) for _ in range(count)), headers=headers))
        elif command[0] == "info":
            print(f"Size: {len(rows)}x{len(headers)}")
            counts = [0] * len(headers)
            for row in rows:
                for i in range(len(row)):
                    if row[i]:
                        counts[i] += 1
            print(tabulate(zip(headers, counts)))
        elif command[0] == "delnan":
            with open(filename, "w", encoding="utf-8", newline="") as file:
                spamwriter = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(headers)
                for row in rows:
                    if all(row):
                        spamwriter.writerow(row)
            with open(filename, "r", encoding="utf-8", newline="") as file:
                spamreader = csv.reader(file, delimiter=",")
                headers = next(spamreader)
                rows = list(spamreader)
        elif command[0] == "makeds":
            if not os.path.exists("workdata"):
                os.mkdir("workdata")
            if not os.path.exists("workdata/learning"):
                os.mkdir("workdata/learning")
            if not os.path.exists("workdata/testing"):
                os.mkdir("workdata/testing")

            part30 = [random.choice(rows) for _ in range(int(len(rows) * .3 + 1))]
            part70 = [row for row in rows if row not in part30]

            with open("workdata/learning/train.csv", "w", encoding="utf-8", newline="") as file:
                spamwriter = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(headers)
                for row in part70:
                    spamwriter.writerow(row)

            with open("workdata/testing/test.csv", "w", encoding="utf-8", newline="") as file:
                spamwriter = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(headers)
                for row in part30:
                    spamwriter.writerow(row)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            main(sys.argv[1])
        else:
            print("file doesn't exist")
    else:
        print("filename not passed")
