import random

print("Welcome to the Boxing Simulator!")

print("Moves:")
print("1: Jab")
print("2: Cross")
print("3: Hook")
print("4: Uppercut")

fight_type = input("Is this a championship fight? (yes/no): ")

if fight_type == "yes":
    total_rounds = 5
else:
    total_rounds = 3

your_score = 0
opponent_score = 0

def did_you_win(your_move, opponent_move):
    if your_move == opponent_move:
        return "draw"
    elif your_move == 1 and opponent_move == 3:
        return "you"
    elif your_move == 2 and opponent_move == 1:
        return "you"
    elif your_move == 3 and opponent_move == 4:
        return "you"
    elif your_move == 4 and opponent_move == 2:
        return "you"
    else:
        return "opponent"

for round_number in range(1, total_rounds + 1):
    print("\nRound", round_number)
    
    your_input = input("Choose your move (1-4): ")
    
    if not your_input.isdigit():
        print("That's not a number! You lose this round.")
        opponent_score += 1
        continue

    your_move = int(your_input)

    if your_move < 1 or your_move > 4:
        print("Invalid move. You lose this round.")
        opponent_score += 1
        continue

    opponent_move = random.randint(1, 4)

    print("You chose:", your_move)
    print("Opponent chose:", opponent_move)

    winner = did_you_win(your_move, opponent_move)

    if winner == "you":
        print("You win this round!")
        your_score += 1
    elif winner == "opponent":
        print("Opponent wins this round.")
        opponent_score += 1
    else:
        print("It's a draw.")

    print("Score: You", your_score, "-", opponent_score, "Opponent")

print("\n=== Fight Over ===")
if your_score > opponent_score:
    print("You won the fight!")
elif your_score < opponent_score:
    print("You lost the fight.")
else:
    print("It's a draw!")
