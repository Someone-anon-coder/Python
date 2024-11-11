def count_up_to(num: int):
    """Count up to the specified number and yeild each value
    
    Args:
        num (int): The number to count up to.
        
    Yields:
        int: The current value of the counter."""

    count = 1
    while count <= num:
        yield count
        count += 1

counter = count_up_to(5)

for num in counter:
    print(f"Number is {num}")


generator_expression = ((x, x * x) for x in range(1, 6))

for num, squared_num in generator_expression:
    print(f"Square of {num} is {squared_num}")


counter = count_up_to(3)

try:
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter)) # Counter reached the end
except StopIteration:
    print("End of iteration")


def fibonacci(num: int):
    """Generate the first n Fibonacci numbers.
    Args:
        num (int): The number of Fibonacci numbers to generate.
    Yields:
        int: The next Fibonacci number."""
    
    a, b = 0, 1
    while num > 0:
        yield a
        a, b = b, a + b
        num -= 1

fib = fibonacci(10)

for num in fib:
    print(num, end=" ")
print()


def echo():
    while True:
        recieved = (yield)
        print(f"I received {recieved}")

generator = echo()
next(generator)

generator.send("Hello")
generator.send("World")


def count_up_to_fixed(num: int):
    """Count up to the specified number and yeild each value
    
    Args:
        num (int): The number to count up to.
        
    Yields:
        int: The current value of the counter."""

    count = 1
    while count <= num:
        yield count
        count += 1
    
    return "Counting is Done"

counter = count_up_to_fixed(3)

print(f"Number is {next(counter)}")
print(f"Number is {next(counter)}")
print(f"Number is {next(counter)}")
print(f"Number is {next(counter)}") # Counter reached the end