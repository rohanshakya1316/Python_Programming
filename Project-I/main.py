# Snake, Water and Gun Game 

# Game rules : The "Snake Water Gun" game, also known as "Rock Paper Scissors," is a simple hand game where two players simultaneously choose one of three options: Snake, Water, or Gun. 

# The winner is determined by these rules:
#  Snake beats Water,
#  Water beats Gun, and 
#  Gun beats Snake. 
#  If both players choose the same option, it's a draw. 

""" 
    -1 for Snake
    0 for Water
    1 for Gun
"""

import random

computer = random.choice([-1, 0, 1])

print("\nWelcome To The Snake, Water and Gun Game!\n")

user_choice = input("Enter your choice (Snake, Water and Gun): ")

userDict = {"snake": -1, "water": 0, "gun": 1}

resultDict = {-1 : "Snake", 0 : "Water", 1 : "Gun"}

user = userDict[user_choice.lower()]

print(f"Computer chose {resultDict[computer]}.")
print(f"You chose {resultDict[user]}.")

if  computer == user:
    print("So, it's a draw. ")

else:
    if computer == -1 and user == 0:
        print("You lose!")

    elif computer == 0 and user == 1:
        print("You lose!")

    elif computer == 1 and user == -1:
        print("You lose!")

    elif computer == 0 and user == -1:
        print("You Win!")

    elif computer == 1 and user == 0:
        print("You Win!")

    elif computer == -1 and user == 1:
        print("You Win!")
    
    else: 
        print("Something anonymous problem occured.")