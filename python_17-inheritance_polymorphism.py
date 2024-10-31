class Animal:
    def speak(self) -> str:
        return "Some animal sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

dog: Dog = Dog("Buddy")
cat: Cat = Cat("Whiskers")

print(f"Dog says {dog.speak()}")
print(f"Cat says {cat.speak()}")


class Vehicle:
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model
    
    def info(self) -> None:
        print(f"Starting {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make: str, model: str, num_doors: int) -> None:
        super().__init__(make, model)
        self.num_doors: int = num_doors
    
    def info(self) -> None:
        print(f"{super().info()} with number of doors: {self.num_doors}")

car: Car = Car("Toyota", "Camry", 4)
car.info()


class Bird:
    def fly(self) -> None:
        print("Bird is Flying")

class Airplane(Bird):
    def fly(self) -> None:
        print("Airplane is Flying")

def let_it_fly(entity: object) -> None:
    entity.fly()

bird: Bird = Bird()
airplane: Airplane = Airplane()

let_it_fly(bird)
let_it_fly(airplane)