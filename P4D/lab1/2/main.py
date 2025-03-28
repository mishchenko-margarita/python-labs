import argparse
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Получение информации об папке")
    parser.add_argument(
        "--files",
        nargs="*",
        help="Файлы для проверки"
    )
    parser.add_argument(
        "--dirpath",
        type=str,
        required=True,
        help="Путь к директории"
    )

    args = parser.parse_args()
    if args.files:
        avaiable_files = set(os.listdir(args.dirpath))
        entered_files = set(args.files)
        missing_files = entered_files - avaiable_files
        common_files = avaiable_files & entered_files

        if not os.path.exists(os.path.join(args.dirpath, "info")):
            os.mkdir(os.path.join(args.dirpath, "info"))

        with open(os.path.join(args.dirpath, "info", "common_files"), "w") as commons:
            commons.write("\n".join(common_files))

        with open(os.path.join(args.dirpath, "info", "missing_files"), "w") as missings:
            missings.write("\n".join(missing_files))

        print("Missings:", *missing_files, sep="\n")
        print("Commons:", *common_files, sep="\n")
    else:
        with os.popen(f"dir {args.dirpath}") as dir_output:
            print(dir_output.read().encode("cp1251").decode("cp866"))
