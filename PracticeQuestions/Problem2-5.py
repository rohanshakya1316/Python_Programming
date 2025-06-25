# Write a python program to find an average of two numebers entered by the user and square it. 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2
square = pow(average, 2)  # average ** 2

# a ^ 2  (incorrect)

print(f"The average of {num1} and {num2} is {average}. ")
print(f"The square of {average} is {square}. ")