# Python Functions Demo 

# Simple function definition or function signature
def func1():
    print("Hello from func1.")

# Function call
func1()

# A function to greet the user. 
def greet(): 
    user = input("Enter your name: ")
    print(f"Welcome, {user}! Have a good day.")

greet()

# A function to add two numbers. 
def sum():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 + num2

    print(f"The sum of {num1} and {num2} is {sum}.")

sum()
