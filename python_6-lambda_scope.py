def add(num1: int, num2: int) -> int:
    return num1 + num2

print(add(1, 2))

add = lambda num1, num2: num1 + num2
print(add(3, 4))

greeting = lambda name: print(f'Hello, {name}')
greeting('Bob')


def something() -> None:
    x = 10
    print(x)

something()
# print(x)


def something() -> None:
    global x
    x = 10
    
    print("From function", x)

something()
print("Not from function", x)