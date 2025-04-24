def is_exit_attempt(text):
    text = text.lower().strip()
    if len(text) < 3:
        return False
    return text[0] == "e" and text[-1] == "t" and "x" in text #added this in case if the user will have a typo like I did 

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if is_exit_attempt(user_input):
        print("Goodbye!")
        break

    if not user_input.strip().lstrip('-').isdigit():
        print("That's not a valid number. Try again.")
        continue

    number = int(user_input)

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
