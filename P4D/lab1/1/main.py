import sys
import os
import shutil


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    small_files = []

    for file_name in os.listdir(root):
        file_size = os.path.getsize(os.path.join(root, file_name)) / 1024
        if file_size < 2:
            if not os.path.exists(os.path.join(root, "small")):
                os.mkdir(os.path.join(root, "small"))
            shutil.copy(
                os.path.join(os.path.join(root, file_name)),
                os.path.join(os.path.join(root, "small", file_name)),
            )
            small_files.append(file_name)
    
    if len(small_files) > 0:
        print(*small_files, sep="\n")
    else:
        print("there are no small files in the directory")
