with open("Files/read_example.txt", 'r', encoding='utf8') as file:
    print(file.read())

file = open("Files/read_example.txt", 'r', encoding='utf8')
print(file.read())
file.close()


class MyContextManager:
    """Class to demonstrate the use of context managers"""
    
    def __enter__(self) -> None:
        """Enter the context"""
        
        print("Entering the context")
    
    def __exit__(self, exc_type: object, exc_val: object, exc_tb: object) -> None:
        """Exit the context"""
        
        print("Exiting the context")

with MyContextManager() as manager:
    print("Inside the context")


from contextlib import contextmanager

@contextmanager
def my_context():
    """Function to demonstrate the use of context managers"""
    
    print("Entering the context")
    yield
    print("Exiting the context")

with my_context():
    print("Inside the context")


class FileManager:
    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File opened")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print("File closed")

with FileManager("Files/read_example.txt", "r") as file:
    print(file.read())


import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        print(f"Elapsed time: {self.end_time - self.start_time} seconds")

with Timer():
    time.sleep(2)