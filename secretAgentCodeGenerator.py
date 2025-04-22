code1 = input("Enter code1 as single word (letters only): ")
code2 = input("Enter code2 as single word (letters only): ")
code3 = input("Enter code3 as single word (letters only): ")       
num_a = int(input("Enter num_a as a number (0-9): "))
num_b = int(input("Enter num_b as aa number (0-9): "))

if not (code1.isalpha() and code2.isalpha() and code3.isalpha()):
    print ("Invalid codeword")
    exit()

if num_a < 1 or num_b < 1:
    print("Invalid numbers")
    exit()

combined = code1 + "-" + code2 + "-" + code3
secret_number = (num_a * num_b) + num_a - num_b

num_a = num_a + num_b
num_b = num_a - num_b
num_a = num_a - num_b
swapped_A = num_a
swapped_B = num_b

avg_value = (swapped_A + swapped_B) / 2
message_length = len(combined)
is_palindrome = (combined.replace("-", "") == combined.replace("-", "")[::-1])

print("Secret Code:", combined)
print("Secret Number:", secret_number)
print(f"Swapped Values: A={swapped_A}, B={swapped_B}")
print("Average of Originals:", avg_value)
print("Combined Length:", message_length)
print("Palindrome:", is_palindrome)