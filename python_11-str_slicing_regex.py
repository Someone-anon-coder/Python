text = "Hello, World!"
print(text[:5])
print(text[7:])
print(text[-6: -1])
print(text[::2])
print(text[::-1])

import re

text = "Hello, World!"
print(re.match("Hello", text))
print(re.search("World", text))
print(re.findall("l", text))


text = "Hello, World!"
print(re.sub("World", "Python", text))
print(re.split(",", text))


text = "My number is 12345 and zip is 54321"
print(re.findall("\d+", text))


email = "abc@gmail.com"
print(f"Email is valid:", bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)))


text = "The quick brown fox jumps over the lazy dog"
words = re.findall(r"\b\w+\b", text)
print(words)