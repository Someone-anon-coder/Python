def my_decorator(func):
    def wrapper():
        print("Something is happening before function call")
        func()
        print("Something is happening after function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def add(a, b):
    print(f"Addition of {a} and {b} is {a + b}")

add(1, 2)


def decorator1(func):
    def wrapper():
        print("-"*10, ">>")
        func()
        print("-"*10, "<<")
    return wrapper

def decorator2(func):
    def wrapper():
        print("*"*5)
        func()
        print("*"*5)
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello, World!")

say_hello()


from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before Function Call")
        result = func(*args, **kwargs)
        print("After Function Call")
        return result
    return wrapper

def greet(name: str):
    print(f"Hello {name}")

print(greet.__name__)
print(greet.__doc__)


def logging(func):
    def my_wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return my_wrapper

@logging
def add(a, b):
    return a + b

add(1, 2)