import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Создание тестовых отсутсвующих файлов")
    parser.add_argument(
        "--dirpath",
        type=str,
        required=True,
        help="Путь к директории"
    )

    args = parser.parse_args()
    with open(os.path.join(args.dirpath, "info", "missing_files")) as missings:
        missing_files = missings.read().split()

    for missing in missing_files:
        with open(os.path.join(args.dirpath, missing), "w") as new_file:
            new_file.close()
