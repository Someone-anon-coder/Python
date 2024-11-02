import math

print(f"Factorial of 5 is {math.factorial(5)}")
print(f"Square root of 25 is {math.sqrt(25)}")


from datetime import datetime

print(f"Current date and time is {datetime.now()}")
print(f"Formatted date and time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


import random

print(f"A random number between 1 and 10 is {random.randint(1, 10)}")
print(f"A random choice from a list ['a', 'b', 'c'] is {random.choice(['a', 'b', 'c'])}")


import os

python_files = [file for file in os.listdir() if file.endswith('.py')]
print(f"Python files in current directory:", *python_files, sep='\n')


# !pip install requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)


# !pip install pandas
import pandas

data = pandas.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(f"Data Frame:\n{data}")