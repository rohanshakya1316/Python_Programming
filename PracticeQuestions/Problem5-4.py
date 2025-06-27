# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 


dict_lang_name = {}         # empty dictionary

# name = input("Enter the name: ")
# lang = input("Enter the favorite language: ")
# dict_lang_name.update({name: lang})

# name = input("Enter the name: ")
# lang = input("Enter the favorite language: ")
# dict_lang_name.update({name: lang})

# name = input("Enter the name: ")
# lang = input("Enter the favorite language: ")
# dict_lang_name.update({name: lang})

# name = input("Enter the name: ")
# lang = input("Enter the favorite language: ")
# dict_lang_name.update({name: lang})

# print(dict_lang_name)



# Alternatives
for i in range(1, 5):
    name = input(f"Enter the name {i}: ")
    lang = input("Enter the favorite language: ")
    dict_lang_name.update({name: lang})

print(dict_lang_name)


# If the names of 2 friends are same (key); what will happen to the program.
# If the key is entered same then the last input value will be added in the respective key overwriting the previous value of same key. i.e., keys cannot be same in the dictionary.

# If languages of two friends are same (values); what will happen to the program in problem.
# If the values is entered same then these same inputted values will be paired with its respective keys. i.e., values can be same in the dictionary.