class CustomException(Exception):
    pass

try:
    if int(input("Enter positive number: ")) < 0:
        raise CustomException("Only positive numbers are allowed.")
except CustomException as e:
    print(f"Error: {e}")


class ValidationError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

users = {
    "abc": "cat", 
    "pqr": "dog", 
    "xyz": "zebra"
}

try:
    username = input("Enter your username: ")
    if username not in users:
        raise ValidationError("Invalid username.", 400)
    
    favorite_animal = input("Enter your favorite animal: ")
    if favorite_animal != users[username]:
        raise ValidationError("Invalid favorite animal.", 401)

    print("Login successful.")
except ValidationError as e:
    print(f"Error: {e}, Code: {e.code}")


class ConfigError(Exception):
    def __init__(self, message, config_key):
        super().__init__(message)
        self.config_key = config_key

try:
    raise ConfigError("Invalid configuration value", "database_url")
except ConfigError as e:
    print(f"Error: {e}, Config Key: {e.config_key}")