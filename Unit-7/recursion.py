# Recursion = a function which calls itself. 

# Recursive function to calculate factorial 

def factorial(n):
    if n < 0: 
        return "Invalid!"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter any number to find the factorial: "))

fact = factorial(num)

print(f"The factorial of {num} is {fact}.")