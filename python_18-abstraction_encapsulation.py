class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner: str = owner
        self._account_type: str = "Checking"
        self.__balance: float = balance
    
    def deposit(self, amount: float) -> None:
        self.__balance += amount
    
    def withdraw(self, amount: float) -> None:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self) -> float:
        return self.__balance

account = BankAccount("Someone")

account.deposit(1000)
account.withdraw(500)

print(f"Account Balance: {account.get_balance()}")
print(f"Account Type: {account._account_type}")
# print(f"Account Balance: {account.__balance}") # AttributeError: 'BankAccount' object has no attribute '__balance'


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 10)

print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")