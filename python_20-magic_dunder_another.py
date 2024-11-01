class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, other: object):
        print("Adding two vectors...")
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: object):
        print("Subtracting two vectors...")
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f"Vector 1: {v1}, Vector 2: {v2}")
print(v1 + v2)
print(v1 - v2)


class Multiplier:
    def __init__(self, factor: float):
        self.factor = factor
    
    def __call__(self, value: float):
        print("Object called, returning result...")
        return self.factor * value

mul = Multiplier(2)
print(mul(5))


class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        self.file.close()

with FileManager("Files/Magic_file.txt", "w") as file:
    file.write("Hello, World!")