def greet():
    print("Hello")

greet()


def greet(name: str, age: int):
    print(f"Hello, {name}! You are {age} years old.")

greet("Someone", 100)
greet(age=84, name="Someone Else")


def greet(name: str, age: int=100) -> str:
    print(f"Hello, {name}! You are {age} years old.")

greet("Someone")


def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print("Total:", add(1, 2, 3, 4, 5))


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Someone", age=100)