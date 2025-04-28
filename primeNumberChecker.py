def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

# Testing the function
print(is_prime(2))    # True
print(is_prime(4))    # False
print(is_prime(7))    # True
print(is_prime(15))   # False
print(is_prime(17))   # True

input_number = int(input("Enter a number to check if it's prime: "))
if is_prime(input_number):
    print(f"{input_number} is a prime number.") 
else:
    print(f"{input_number} is not a prime number.")
print("End of prime number checker.")