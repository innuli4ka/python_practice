def reverse_string(text):
    return text[::-1]

user_text = input("Enter a string to reverse: " )
reversed_text = reverse_string(user_text)
print("Reversed string: " + reversed_text)