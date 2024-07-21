import os

def walk2():
    dir_path = "files"
    files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
]
    print(files_file)
    return files_file


if __name__ == "__main__":
    walk2()