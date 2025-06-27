# Write a program to create a dictionary of Nepali words with values as their English 
# translation. Provide user with an option to look it up!

words = {
    'garo': 'difficult',
    'saro': 'strong',
    'bidyalaya': 'college', 
    'bida': 'holiday'
}

word = input("Enter the word to find the meaning in English: ");
print(f"The English meaning of {word} is {words[word]}.")