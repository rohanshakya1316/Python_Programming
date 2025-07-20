# THE PERFECT GUESS GAME 

# Use random module

# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

import random

to_guess_number = random.randint(1, 100)
guess_number = None
guess_attempt = 1

print("Welcome to the Perfect Guess Game! Guess a number between 1 and 100.")

while(guess_number != to_guess_number):
    guess_number = int(input("Guess the number: "))

    if (guess_number > to_guess_number):
        print("Guess the lower number please! ")
        guess_attempt += 1
    
    elif guess_number < to_guess_number:
        print("Guess the higher number please! ")
        guess_attempt += 1

    else: 
        break

print(f"You have guessed the number {to_guess_number} correctly in {guess_attempt} attemps.")