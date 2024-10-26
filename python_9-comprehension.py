squares = [x*x for x in range(1, 11)]
print(f"Squares: {squares}")


even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even Numbers: {even_numbers}")

odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
print(f"Odd Numbers: {odd_numbers}")


fruits = ["apple", "banana", "cherry", "date"]

upper_fruits = [fruit.upper() for fruit in fruits]
print(f"Upper Fruits: {upper_fruits}")


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print(f"Flattened Matrix: {flattened}")


squares_dict = {x: x*x for x in range(1, 11)}
print(f"Squares Dictionary: {squares_dict}")


numbers_dict = {1:10, 2:15, 3:20, 4:25, 5:30}

even_numbers_dict = {k: v for k, v in numbers_dict.items() if v % 2 == 0}
print(f"Even Numbers Dictionary: {even_numbers_dict}")


fruits = ["apple", "banana", "cherry", "date"]
colors = ["red", "yellow", "red", "green"]

fruit_colors = {fruit: color for fruit, color in zip(fruits, colors)}
print(f"Fruit Colors Dictionary: {fruit_colors}")


multiplication_table = {i: {j: i * j for j in range(1, 6)} for i in range(1, 6)}
print(multiplication_table)