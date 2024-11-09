# !pip install matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [x**2 for x in x]

plt.plot(x, y)

plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()


categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values)

plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.show()


import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)

plt.title("Simple Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()


x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)

plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()


labels = ['Apples', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.axis('equal')
plt.title("Simple Pie Chart")

plt.show()