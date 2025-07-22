# The walrus operator (:=) in Python is a new assignment expression operator introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression.

# Syntax:   variable := expression

# This assigns the result of expression to variable and returns the value, all in a single step.

if (n := len([1, 2, 3, 4 , 5])) > 3: 
    print(f"List is too long ({n} elements, expected < 3)")


# Without walrus operator 
data = input("Enter something: ")
while data != "exit": 
    print(f"You said: {data}")
    data = input("Enter something: ")

# With walrus operator 
while (data := input("Enter something: ")) != 'exit':
    print(f"You said: {data}")