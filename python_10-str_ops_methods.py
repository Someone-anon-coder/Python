greeting = "Hello" + "World"
print(f"The greeting is: {greeting}")


laugh = "ha" * 3
print(f"I am laughing {laugh}")


word = "Something"
print(f"The length of the word is: {len(word)}")


word = "Python"
print(f"The first character of the word is: {word[0]}")
print(f"The last character of the word is: {word[-1]}")

print(f"The 'Py' is in the word: {'Py' in word}")
print(f"The 'py' is not in the word: {'py' not in word}")


print(f"He said: \"Hello\"")


text = "The Python Programming"
print(f"The upper of text is: {text.upper()}")
print(f"The lower of text is: {text.lower()}")
print(f"The title of text is: {text.title()}")
print(f"The capitalize of text is: {text.capitalize()}")
print(f"The swapcase of text is: {text.swapcase()}")


text = "Hello, World"
print(f"\"World\" is at location {text.find('World')}")
# print(f"\"Python\" is at location {text.index('Python')}") # Raises Error if substring not found
print(f"Replacing \"World\" with \"Python\": {text.replace('World', 'Python')}")


text = "    Python is great    "
print(f"The strip of text is: {text.strip()}")
print(f"The left strip of text is: {text.lstrip()}")
print(f"The right strip of text is: {text.rstrip()}")

print(f"The split of text is: {text.strip().split()}")
print(f"The join of text is: {' '.join(['Python', 'is', 'great'])}")


print(f"Is the text alphabetic: {'Python'.isalpha()}")
print(f"Is the text numeric: {'1234'.isnumeric()}")
print(f"Is the text alphanumeric: {'Python123'.isalnum()}")


text = "python is amazing"
print(f"Formatted text: {text.split()[0].upper() + ', ' + ' '.join(text.split()[1:]) + '!'}")