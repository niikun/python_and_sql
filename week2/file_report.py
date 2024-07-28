import os

def file_report():
    file_dict = {}
    for dir, _, files in os.walk("week2"):
        for file in files:
            file_path = os.path.join(dir,file)
            file_size = os.path.getsize(file_path)
            file_dict[file_path]= file_size
    file_dict = dict(sorted(file_dict.items(), key=lambda x :x[1],reverse=True))
    print(file_dict)

if __name__=="__main__":
    file_report()
