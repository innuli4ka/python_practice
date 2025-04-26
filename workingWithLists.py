# 1. Create a list with 10 numbers
numbers = [1, 2, 5, 7, 8, 3, 9, 4, 6, 10]

# 2. Add number 11 to the end
numbers.append(11)

# 3. Remove number 5 if it exists
if 5 in numbers:
    numbers.remove(5)

# 4. Insert number 3 at index 2
numbers.insert(2, 3)

# 5. Calculate and print the sum of all numbers
total = sum(numbers)
print("Sum of numbers:", total)

# 6. Find and print the smallest and largest numbers
smallest = min(numbers)
largest = max(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)
