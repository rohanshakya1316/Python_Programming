# Write a program to make a copy of a text file “this. txt”

filename = 'PracticeQuestions/Problem9/this.txt'
file_copy_name = 'PracticeQuestions/Problem9/this_copy.txt'

with open(filename, 'r', encoding='utf-8-sig') as f: 
    content = f.read()

with open(file_copy_name, 'w') as fptr: 
    fptr.write(content)