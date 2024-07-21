import os

def walk():
    for root, directries, files in os.walk("."):
        
        for _file in files:
            abs_path = os.path.join(root,_file)
            print(abs_path)

if __name__ == "__main__":
    walk()