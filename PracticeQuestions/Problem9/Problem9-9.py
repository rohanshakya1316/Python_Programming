# Write a program to find out whether a file is identical & matches the content of another file.

filename1 = 'PracticeQuestions/Problem9/this.txt'
# filename2 = 'PracticeQuestions/Problem9/this_copy.txt'
filename2 = 'PracticeQuestions/Problem9/poems.txt'

with open(filename1, encoding="utf-8") as f: 
    content1 = f.read()

with open(filename2) as f: 
    content2 = f.read()

if content1 == content2:
    print("The files are identical.")
else: 
    print("The files are not identical.")