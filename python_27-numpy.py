# !pip install numpy
import numpy

arr = numpy.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr}")


matrix = numpy.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{matrix}")


zeros = numpy.zeros((3, 3))
print(f"Zeros Array:\n{zeros}")


ones = numpy.ones((2, 4))
print(f"Ones Array:\n{ones}")


arr = numpy.array([10, 20, 30, 40, 50])

print(f"First Element: {arr[0]}")
print(f"Last Element: {arr[-1]}")
print(f"Array Slice: {arr[1:4]}")


a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")


arr = numpy.array([1, 4, 9, 16, 25, 36])

print(f"Square Root: {numpy.sqrt(arr)}")
print(f"Exponential: {numpy.exp(arr)}")
print(f"Sum: {numpy.sum(arr)}")
print(f"Mean: {numpy.mean(arr)}")

print(f"Reshaped Array:\n{arr.reshape(2, 3)}")


print(f"Random Array:\n{numpy.random.rand(3, 3)}")
print(f"Random Integer Array:\n{numpy.random.randint(1, 10, size=(3, 3))}")


A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([[5, 6], [7, 8]])

print(f"Matrix Multiplication:\n{numpy.matmul(A, B)}")