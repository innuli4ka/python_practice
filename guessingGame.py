import random

print("Welcome to the Guessing Game!")

while True:
    secret_number = random.randint(1, 20)
    tries_left = 5

    print("\nI'm thinking of a number between 1 and 20.")
    print("You have 5 tries to guess it!")

    while tries_left > 0:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("That's not a number! Try again.")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("Correct! You guessed it!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        tries_left -= 1
        print("Tries left:", tries_left)

    if tries_left == 0:
        print("Game over! The number was", secret_number)

    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
