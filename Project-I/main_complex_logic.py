# Snake, Water and Gun Game 

# Game rules : The "Snake Water Gun" game, also known as "Rock Paper Scissors," is a simple hand game where two players simultaneously choose one of three options: Snake, Water, or Gun. 

# The winner is determined by these rules:
#  Snake beats Water,
#  Water beats Gun, and 
#  Gun beats Snake. 
#  If both players choose the same option, it's a draw. 


# Snake, Water and Gun game using if elif else ladder:

print("\nWelcome To The Snake, Water and Gun Game: \n")

p1_choice = input("Player 1, Enter your choice (Snake, Water, or Gun): ").lower().strip()
p2_choice = input("Player 2, Enter your choice (Snake, Water, or Gun): ").lower().strip()

print(f"Player 1 chose {p1_choice.capitalize()}.")
print(f"Player 2 chose {p2_choice.capitalize()}")

if p1_choice == p2_choice:
    print("So, It's a draw!")

elif p1_choice == "snake":
    if p2_choice == "water":
        print("Player 1 wins! Snake drinks Water.")

    elif p2_choice == "gun":
        print("Player 2 wins! Gun shoots Snake.")

    else:
        print("Invalid input from Player 2.")

elif p1_choice == "gun":
    if p2_choice == "snake":
        print("Player 1 wins! Gun shoots Snake.")

    elif p2_choice == "water":
        print("Player 2 wins! Water drowns Gun.")

    else:
        print("Invalid input from Player 2.")

elif p1_choice == "water":
    if p2_choice == "gun":
        print("Player 1 wins! Water drowns Gun.")

    elif p2_choice == "snake":
        print("Player 2 wins! Snake drinks Water.")

    else:
        print("Invalid input from Player 2.")

else:
    print("Invalid input from Player 1.")