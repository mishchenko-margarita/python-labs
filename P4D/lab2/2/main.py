import json


with open("ex_2.json", "r", encoding="utf-8") as file:
    raw_content = file.read()

json_content = f"[{raw_content}]"

try:
    data = json.loads(json_content)
except json.JSONDecodeError as e:
    print(f"Ошибка при парсинге JSON: {e}")
    exit()


users_dict = {}
for user in data:
    name = user.get("name")
    phone = user.get("phoneNumber")
    if name and phone:
        users_dict[name] = phone
    else:
        print(f"Пропущен объект с отсутствующими данными: {user}")


print("\nСловарь пользователей:")
for name, phone in users_dict.items():
    print(f"{name}: {phone}")


with open("formatted_ex_2.json", "w", encoding="utf-8") as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

print("\nФайл formatted_ex_2.json успешно сохранен.")