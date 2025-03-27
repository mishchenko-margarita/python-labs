import sys
import os
import json


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("no file specified")

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("file doesn't exist")

    with open(filename) as json_file:
        json_data = json.load(json_file)
        for csv_filename, data in json_data.items():
            if os.path.exists(csv_filename):
                os.remove(csv_filename)
            with open(f"{csv_filename}.csv", "a") as csv_file:
                headers = json_data[csv_filename][0].keys()
                csv_file.write(";".join(headers) + "\n")
                for entry in data:
                    csv_file.write(";".join(str(i) for i in entry.values()) + "\n")
