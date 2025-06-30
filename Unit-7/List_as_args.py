# pass statement 

# function definitions cannot be empty, but if we for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def my_pass_function():
    pass


# Passing a List as an Argument

# We can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if we send a List as an argument, it will still be a List when it reaches the function:

def func(lists):
    for x in lists:
        print(x)

student = ["Rohan", 1, True, 25.532, False, "T", 0, 'OTC']

func(student)   # Function Call


