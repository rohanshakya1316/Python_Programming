# Write a program to read the text from a given file "poems.txt" and find out whether it contains the word "twinkle".

with open("PracticeQuestions/Problem9/poems.txt") as f:
    text = f.read().lower()

    if "twinkle" in text:
        print("The word twinkle is present in the file.")
        twinkle_count = text.count("twinkle")
        print("Total times:",twinkle_count)
    else: 
        print("The word twinkle is not present in the file.")