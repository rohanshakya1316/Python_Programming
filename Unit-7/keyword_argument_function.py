# Keyword Arguments in Functions, also know as kwargs in Python

# We can also send arguments with the key = value syntax. 

#  This way the order of the arguments does not matter. 

# Simple function with kwargs = a key-value pair arguments
def my_function(arg1, arg2, arg3):
    print("The main argument is", arg3)

my_function(arg3 = "Rohan", arg1 = 1, arg2 = 1.5)