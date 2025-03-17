with open("input.txt", encoding="utf-8") as file:
    records = []
    for line in file:
        records.append(line.split())
    print("records readed")

    sort = [
        " ".join(record)
        for record in sorted(
            records,
            key=lambda record: int(record[2]),
            reverse=True
        )
    ]
    print("records_sorted")

with open("record_max.txt", "w", encoding="utf-8") as file:
    file.write(sort[0])
    print("record_max saved")

with open("record_min.txt", "w", encoding="utf-8") as file:
    file.write(sort[-1])
    print("record_min saved")

print("success")
