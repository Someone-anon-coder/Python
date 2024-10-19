# Variable Declaration
name: str = "Someone"
age: int = 100
height: float = 6.7
is_student: bool = False


# Operators - Arithmetic
x = 10
y = 5

print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Floor Division: {x // y}")
print(f"Modulus: {x % y}")
print(f"Exponentiation: {x ** y}")


# Operators - Comparison
x = 5
y = 3

print(f"Equal to: {x == y}")
print(f"Not equal to: {x != y}")
print(f"Greater than: {x > y}")
print(f"Less than: {x < y}")
print(f"Greater than or equal to: {x >= y}")
print(f"Less than or equal to: {x <= y}")


# Operators - Logical
a = True
b = False

print(f"Logical AND: {a and b}")
print(f"Logical OR: {a or b}")
print(f"Logical NOT: {not a}")


# Operators - Bitwise
x = 5
y = 3

print(f"Bitwise AND: {x & y}")
print(f"Bitwise OR: {x | y}")
print(f"Bitwise XOR: {x ^ y}")
print(f"Bitwise NOT: {~x}")
print(f"Left shift: {x << 2}")
print(f"Right shift: {x >> 1}")


# Input / Output
name: str = input("Enter your name: ")
print(f"Hello, {name}!")


# Comments - Single line
name: str = "Someone" # Declaring name as a string variable with value 'Someone'


# Comments - Multiline
"""
This is a multiline comment.
It can span multiple lines.
"""


# Documentation Strings
def add(num1: int, num2: int) -> int:
    """
    This function takes two integers as input and returns their sum.

    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    
    return num1 + num2