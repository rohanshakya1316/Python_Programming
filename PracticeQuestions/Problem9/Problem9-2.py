# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hiscore 
# whenever the game() function breaks the Hi-score. 

def game(): 
    # Simulating game score (random numbers)
    import random
    current_score = random.randint(1, 100)  # game returns a score between 1 and 100
    return current_score

def update_hi_score(cur_score):
    file_name = "PracticeQuestions/Problem9/Hi-score.txt"
    with open (file_name) as f:
        hiscore_from_file = f.read().strip()
        hi_score = int(hiscore_from_file) if hiscore_from_file else 0

        print(f"Current Score: {cur_score}")
        print(f"Previous Hi-Score: {hi_score}")

        if cur_score >= hi_score:
            with open(file_name, 'w') as f:
                f.write(str(cur_score))
            print("New Hi-Score Updated!")
        else: 
            print("Cannot beat the Hi-Score.")

# Simulate the game
score = game()
update_hi_score(score)