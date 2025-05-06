import random as rd

# Mapping
choices = {-1: "water", 0: "gun", 1: "snake"}
you_dict = {"s": 1, "w": -1, "g": 0}

# Computer's turn
computer = rd.choice([-1, 0, 1])

# Your turn
you_str = input(
    "Enter your choice (s for snake, w for water, g for gun): ").lower()

# Input validation
if you_str not in you_dict:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
else:
    you = you_dict[you_str]

    print(f"You chose {choices[you]} and computer chose {choices[computer]}")

    if computer == you:
        print("It's a Tie!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You Win!")
    else:
        print("You Lose!")
