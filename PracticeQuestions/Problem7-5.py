# Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter any number to find the factorial: "))

fact = 1

if num == 0:
    print(f"The factorial of {num} is 1.")

if num < 0:
    print(f"Negative number cannot have a factorial. Try agian!")

if num > 0: 
    # using for loop
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}.")

    # using while loop
    fact = 1
    temp = num
    while temp > 0: 
        fact *= temp
        temp -= 1
    print(f"The factorial of {num} is {fact}.")