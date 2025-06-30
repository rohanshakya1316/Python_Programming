# Arbitrary Keyword Arguments = **kwargs in Python

# If we do not know how many keyword arguments that will be passed into our function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Simple function with **kwargs = a dictionary of arguments.


def kwargs_func(**kwargs):
    print("The main keyword argument is", kwargs['name'])
    print("The keyword arguments are", kwargs)

kwargs_func(name = "Rohan", age = 22, address = "Kathmandu")
kwargs_func(num1 = 1, name = "Nepal")
