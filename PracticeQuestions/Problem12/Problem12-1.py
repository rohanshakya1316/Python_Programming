# Write a python program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same. 

try:
    with open("./PracticeQuestions/Problem12/1.txt") as f1:
        content = f1.read()
        print(content)
except FileNotFoundError as fe:
    print("File not found.")
    print(fe)

try:
    with open("./PracticeQuestions/Problem12/2.txt") as f2:
        content = f2.read()
        print(content)
except FileNotFoundError as fe:
    print("File not found.")
    print(fe)

try:
    with open("./PracticeQuestions/Problem12/3.txt") as f3:
        content = f3.read()
        print(content)
except FileNotFoundError as fe:
    print("File not found.")
    print(fe)

print("This program is not crashed here.")