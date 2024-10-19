number: int = 45

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


number: int = -5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


age: int = 18
gender: str = "male"

if age >= 18:
    if gender == "male":
        print("You are an adult male.")
    elif gender == "female":
        print("You are an adult female.")
else:
    print("You are not an adult.")