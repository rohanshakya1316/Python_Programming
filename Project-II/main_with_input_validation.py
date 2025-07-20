# THE PERFECT GUESS GAME 

# Use random module

# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

from random import randint

to_guess_number = randint(1, 100)
guess_attempt = 0
guess_number = None

print("Welcome to the Perfect Guess Game! Guess a number between 1 and 100.")

while guess_number != to_guess_number:
    user_input = input("Guess the number (or type 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Game exited. Better luck next time!")
        break

    try:
        guess_number = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        continue

    guess_attempt += 1

    if guess_number > to_guess_number:
        print("Guess the lower number please!")
    elif guess_number < to_guess_number:
        print("Guess the higher number please!")

if guess_number == to_guess_number:
    print(f"You have guessed the number {to_guess_number} correctly in {guess_attempt} attempts.")
