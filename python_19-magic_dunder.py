class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

person = Person("Someone", 100)
print(f"Hi, i am {person.name} and i am {person.age} years old.")


class Book:
    def __init__(self, title: str, author: str, pages: int=0) -> None:
        self.title: str = title
        self.author: str = author
        self.pages: int = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"
    
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}')"
    
    def __len__(self) -> int:
        return self.pages

book = Book("Python Programming", "Someone", 100)

print(str(book))
print(repr(book))
print("Pages in book:", len(book))


class CustomList:
    def __init__(self):
        self.data = []
    
    def __getitem__(self, index: int) -> int:
        print("Getting the item...")
        return self.data[index]
    
    def __setitem__(self, index: int, value: object) -> None:
        print("Setting the item...")
        self.data[index] = value
    
    def __delitem__(self, index: int) -> None:
        print("Deleting the item...")
        del self.data[index]

mylist = CustomList()
mylist.data = [1, 2, 3]

print(mylist[1])

mylist[1] = 10
print(mylist[1])

del mylist[1]