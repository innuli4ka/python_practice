# 1. Create a set with 5 unique numbers
numbers_set = {2, 4, 6, 8, 10}

# 2. Create a tuple with the squares of the numbers
squares_tuple = (4, 16, 36, 64, 100)

# 3.1 Convert the set to a list and sort descending
numbers_list = list(numbers_set)
numbers_list.sort(reverse=True)
print("Sorted list (descending):", numbers_list)

# 3.2 Find intersection between the set and the tuple
intersection = numbers_set.intersection(squares_tuple)

# 3.3 Print the length of the tuple and the set
print("Length of tuple:", len(squares_tuple))
print("Length of set:", len(numbers_set))

# 3.4 Try to add a new value to the tuple
# squares_tuple.append(121)  # This will cause an error because tuples cannot be changed

print("You cannot add to a tuple. Tuples are immutable.")

# 3.5 Print the intersection result
print("Intersection between set and tuple:", intersection)
