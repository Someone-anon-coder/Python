"""
if True # Syntax Error - ':' was expected
    print("Hello")

print(10 / 0) # ZeroDivision Exception - Tried dividing by zero
"""

try:
    value = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")


try:
    value = int("abc")
except ValueError:
    print("Invalid value.")
except TypeError:
    print("Invalid type.")


try:
    value = int("abc")
except (ValueError, TypeError):
    print("Invalid value or type.")


try:
    print(10 / 0)
except Exception as e:
    print(f"An error occurred: {e}")


try:
    print("Program Start")
    print(10 / 0)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Program End")