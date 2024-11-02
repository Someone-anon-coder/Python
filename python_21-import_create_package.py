import math

num = 4

print(f"Square root of {num} is: {math.sqrt(num)}")
print(f"Factorial of {num} is: {math.factorial(num)}")


from math import pi, sqrt

num = 16

print(f"Value of pi is: {pi}")
print(f"Square root of {num} is: {sqrt(num)}")


from Packages.calculator import add, sub

nums = [1, 2, 3, 4, 5]

print(f"Internal Addition of {nums} is: {add(*nums)}")
print(f"Internal Subtraction of {nums} is: {sub(*nums)}")


from Packages import greet

name = input("Enter your name: ")
greet(name)