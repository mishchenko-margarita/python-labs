import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        print("Валидация успешна!")
    except ValidationError as e:
        print("Ошибка валидации:")
        print(f"Сообщение: {e.message}")
        print(f"Путь: {e.json_path}")


with open("ex_1_schema.json", "r") as schema_file:
    schema = json.load(schema_file)


print("Проверка исходного файла:")
with open("ex_1.json", "r") as file:
    valid_data = json.load(file)
validate_json(valid_data, schema)


print("\nПроверка файла с ошибкой:")
with open("ex_1_error.json", "r") as file:
    invalid_data = json.load(file)
validate_json(invalid_data, schema)
