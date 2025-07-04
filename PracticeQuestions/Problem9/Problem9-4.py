# A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.  

filename = 'PracticeQuestions/Problem9/donkey.txt'

# Read the file content
with open(filename, 'r') as f:
    content = f.read()

# Replace the word 'donkey' with '#####'
new_content = content.lower().replace('donkey', '######')

# Write the updated content back to the same file
with open(filename, 'w') as f:
    f.write(new_content)
