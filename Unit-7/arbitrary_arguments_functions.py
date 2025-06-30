# If we do not know how many arguments that will be passed into our function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Simple *args function = a tuple of arguments.
def func1(*name):
    print("The name is", name[1])

func1("Kamal", "Rohan", "Alice")       # name[1] = 'Rohan'
func1("Kamal", "Alice")                 # name[1] = 'Alice'

# Function to add any numbers provided as argument
def add_all(*n):
    return sum(n)       # sum() = tuple method that returns sum

print(add_all(1, 2, 3, 4, 5))   # 15
print(add_all(1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5))   # 60.0


