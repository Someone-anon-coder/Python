with open("Files/read_example.txt", 'r', encoding='utf8') as file:
    print(file.read())


with open("Files/read_example.txt", 'r', encoding='utf8') as file:
    for line in file:
        print(line)
    

with open("Files/read_example.txt", 'r', encoding='utf8') as file:
    lines = file.readlines()
    print(lines[0])


with open("Files/write_example.txt", 'w', encoding='utf8') as file:
    file.write("Hello World!\n")
    file.write("This is a new line.\n")


with open("Files/append_example.txt", 'a', encoding='utf8') as file:
    file.write("This is a new line.\n")


import csv

with open("Files/read_example.csv", 'r', encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open("Files/write_example.csv", 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Gender"])
    writer.writerow(["Someone", 100, "male"])
    writer.writerow(["Someone Else", 84, "female"])


import json

with open("Files/read_example.json", 'r', encoding='utf8') as file:
    data = json.load(file)
    print(data)


with open("Files/write_example.json", 'w', encoding='utf8') as file:
    data = {"name": "Someone", "age": 100, "gender": "male"}
    json.dump(data, file, indent=4)