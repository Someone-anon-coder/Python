def add_numbers(num1: int, num2: int) -> int:
    """Add two numbers and return the result.
    
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        
    Returns:
        int: The sum of the two numbers.
    """

    print(f"Adding two numbers..., {num1} + {num2}")
    result =  num1 + num2
    print(f"Done Adding two numbers")

    return result

print("Addition:", add_numbers(1, 2))


def divide_numbers(num1: int, num2: int) -> float:
    """Divide two numbers and return the result.

    Args:
        num1 (int): The numerator.
        num2 (int): The denominator.

    Returns:
        float: The quotient of the two numbers.
    """

    return num1 / num2

# print("Division:", divide_numbers(4, 0))


import pdb

def add(num1: int, num2: int) -> int:
    result = num1 + num2
    return result

def main():
    x = 10
    y = 20

    pdb.set_trace()
    z = add(x, y)
    print(f"Result: {z}")

main()


import logging

logging.basicConfig(level=logging.DEBUG)

def add(num1: int, num2: int) -> int:
    logging.debug(f"Adding two numbers..., {num1} + {num2}")
    result = num1 + num2
    return result

def main():
    x = 10
    y = 20

    logging.info(f"Starting the addition of {x} and {y}")
    result = add(x, y)
    logging.info(f"Result: {result}")

main()