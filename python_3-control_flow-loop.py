fruits: list[str] = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


for i in range(5):
    print(i)


for i in range(10, 2, -2):
    print(i)


for i, j in zip(range(2, 10, 2), range(1, 9, 2)):
    print(f"Odd: {j}, Even: {i}")


n: int = 5
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print()


count: int = 0
while count < 5:
    print(count)
    count += 1


count: int = 10
while count > 0:
    print(count)
    count -= 1