my_list = ['a', "b", 1, True, 5.8]

print(f"List: {my_list}")
print(f"Length: {len(my_list)}")
print(f"First element: {my_list[0]}")
print(f"Last element: {my_list[-1]}")


my_list[2] = 100
print(f"Modified list: {my_list}")

my_list.append("Banana")
print(f"Appended list: {my_list}")

my_list.extend([1, 2, 3])
print(f"Extended list: {my_list}")

my_list.insert(3, False)
print(f"Inserted list: {my_list}")

my_list.remove(5.8)
print(f"Removed list: {my_list}")


my_tuple = 'a', "b", 1, True, 5.8

print(f"Tuple: {my_tuple}")
print(f"Length: {len(my_tuple)}")
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")


# my_tuple[0] = 1  # This will raise an Error

first, second, *rest = my_tuple

print(f"First: {first}")
print(f"Second: {second}")
print(f"Rest: {rest}")


one_element_tuple = (2,) # Include a comma for a single element tuple
print(f"One element tuple: {one_element_tuple}")