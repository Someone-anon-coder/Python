import os

print(f"Current working directory: {os.getcwd()}")


file_path = os.path.join("folder", "subfolder", "file.txt")
print(f"File path: {file_path}")


path = "Files/read_example.txt"

print(f"Basename of path: {os.path.basename(path)}")
print(f"Directory of path: {os.path.dirname(path)}")
print(f"If path exists: {os.path.exists(path)}")
print(f"Is path a directory: {os.path.isdir(path)}")
print(f"Is path a file: {os.path.isfile(path)}")
print(f"Absolute path of path: {os.path.abspath(path)}")


from pathlib import Path

path = Path("Files/read_example.txt")

print(f"Name of path: {path.name}")
print(f"Parent of path: {path.parent}")
print(f"If path exists: {path.exists()}")
print(f"Is path a directory: {path.is_file()}")
print(f"Is path a file: {path.is_dir()}")
print(f"Absolute path of path: {path.resolve()}")


try:
    with open("example.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")


try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred: {e}")


try:
    with open("example.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully:", content)


try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Program end.")