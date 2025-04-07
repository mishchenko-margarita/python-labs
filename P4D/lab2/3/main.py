import json


with open("ex_3.json", "r", encoding="utf-8") as file:
    data = json.load(file)

new_invoice = {
    "id": 3,
    "total": 150.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 2,
            "price": 50.00
        },
        {
            "name": "item 5",
            "quantity": 1,
            "price": 50.00
        }
    ]
}

data["invoices"].append(new_invoice)

with open("updated_ex_3.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Файл updated_ex_3.json успешно сохранен.")
