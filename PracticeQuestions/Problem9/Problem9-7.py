# Write a program to find out the line number where python is present from problem 6.

filename = 'PracticeQuestions/Problem9/log.txt'

with open(filename) as f: 
    lines = f.readlines()


line_no = 1
for line in lines: 
    if "python" in line:
        print(f"Word: Python is present in the file. Line Number: {line_no} ")
        break
    line_no += 1
else: 
    print("Word: Python is not present in the file. ")