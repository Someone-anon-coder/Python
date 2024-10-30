class Person:
    species: str = "Human"

    def greet(self, name: str):
        print(f"Hello, I am {name}")

person1: Person = Person()
person1.greet("Someone")

person2: Person = Person()
person2.greet("Someone Else")

print(f"Person1 is a {person1.species}")
print(f"Person2 is a {person2.species}")


class Car:
    def __init__(self, color: str, year: int):
        self.color: str = color
        self.year: int = year

    def drive(self):
        print(f"The {self.color} car is driving.")

car1: Car = Car("Red", 2022)
car1.drive()

car2: Car = Car("Blue", 2021)
car2.drive()

print(f"{car1.color} car was made in {car1.year}")
print(f"{car2.color} car was made in {car2.year}")


class FileHandling:
    def __init__(self, filename: str):
        self.filename: str = filename
        self.file: object = open(filename, 'w')
        
        print(f"File {filename} opened")
    
    def write(self, text: str):
        self.file.write(text)
        print(f"File {self.filename} written")
    
    def __del__(self):
        self.file.close()
        print(f"File {self.filename} closed")

file1: FileHandling = FileHandling("Files/class_file1.txt")
file1.write("Hello, World!")

file2: FileHandling = FileHandling("Files/class_file2.txt")
file2.write("Bye, World!")

del file1, file2