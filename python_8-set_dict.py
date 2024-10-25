my_set = {1, 2.5, 'a', "banana", True}

print(f"Set: {my_set}")
print(f"Length: {len(my_set)}")


my_set.add(100)
print(f"Added Set: {my_set}")

my_set.remove(1) # Raises error if element does not exists
print(f"Removed Set: {my_set}")

my_set.discard(2.5) # Does not raise error if element does not exists
print(f"Discarded Set: {my_set}")


my_set1 = {1, 2, 3, 4, 5}
my_set2 = {4, 5, 6, 7, 8}

union_set = my_set1.union(my_set2)
print(f"Union Set: {union_set}")

intersection_set = my_set1.intersection(my_set2)
print(f"Intersection Set: {intersection_set}")

difference_set = my_set1.difference(my_set2)
print(f"Difference Set: {difference_set}")

is_element_in_set = 3 in my_set1
print(f"Is Element in Set: {is_element_in_set}")


my_dict = {'name': 'Someone', 'age': 100}

print(f"Dictionary: {my_dict}")
print(f"Length: {len(my_dict)}")
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")


my_dict['name'] = 'Someone Else'
print(f"Modified Dictionary: {my_dict}")

my_dict['gender'] = 'male'
print(f"Added Dictionary: {my_dict}")

del my_dict['age']
print(f"Deleted Dictionary: {my_dict}")