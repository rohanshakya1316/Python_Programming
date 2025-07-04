# Write a program to mine a log file and find out whether it contains ‘python’.

filename = 'PracticeQuestions/Problem9/log.txt'

with open(filename) as f: 
    text = f.read()

if "python" in text:
    print("Word: Python is present in the file. ")
else: 
    print("Word: Python is not present in the file. ")