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

user_choice = input("Enter your choice: ")

userDict = {"snake": -1, "water": 0, "gun": 1}

resultDict = {-1 : "Snake", 0 : "Water", 1 : "Gun"}

user = userDict[user_choice]

print(f"Computer chose {resultDict[computer]}.")
print(f"You chose {resultDict[user]}.")

if  computer == user:
    print(f"Computer chose {resultDict[computer]}.")
    print(f"You chose {resultDict[user]}.")
    print("So, it's a draw. ")

else:
    # This logic is based on pattern being formed performing (computer - user)
    # This logic is not reliable and readable, I have written it just to show that we can also obtain same result through this. 
    if (computer - user) == 1 or (computer - user) == -2 : 
        print("You win!")

    else: 
        print("You lose!")

    '''
    
    Analysis :     
    if computer == -1 and user == 0:    # computer - user = -1
        print("You lose!")

    elif computer == 0 and user == 1:   # computer - user = -1
        print("You lose!")

    elif computer == 1 and user == -1:  # computer - user = 2
        print("You lose!")

    elif computer == 0 and user == -1:  # computer - user = 1
        print("You Win!")

    elif computer == 1 and user == 0:   # computer - user = 1
        print("You Win!")

    elif computer == -1 and user == 1:  # computer - user = -2
        print("You Win!")
        
    '''

