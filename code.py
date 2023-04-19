import os

def organize_files(path):
    file_types = {}
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            file_extension = os.path.splitext(file_name)[1]
            if file_extension not in file_types:
                file_types[file_extension] = []
            file_types[file_extension].append(file_name)

    for file_extension, file_names in file_types.items():
        directory = os.path.join(path, file_extension[1:].upper())
        if not os.path.exists(directory):
            os.mkdir(directory)
        for file_name in file_names:
            src = os.path.join(path, file_name)
            dst = os.path.join(directory, file_name)
            os.rename(src, dst)

def list_files(path):
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            file_size = os.path.getsize(os.path.join(path, file_name))
            print(f"{file_name:<30}{file_size:>10} bytes")

if __name__ == "__main__":
    path = input("Enter the path to the directory to organize: ")
    organize_files(path)
    list_files(path)
