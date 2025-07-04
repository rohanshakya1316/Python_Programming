# Repeat program 4 for a list of such words to be censored. 

filename = 'PracticeQuestions/Problem9/donkey.txt'

words = ["Donkey", "donkeys", 'donkey', 'stubborn']

# Read the file content
with open(filename, 'r') as f:
    content = f.read()

# Replace the word 'donkey' with '#####'
for word in words:
    content = content.lower().replace(word, '#' * len(word))

# Write the updated content back to the same file
with open(filename, 'w') as f:
    f.write(content)