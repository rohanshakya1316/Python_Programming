# Write a python program to perform arithmetic operations between two numbers. 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
diff = num1 - num2
product = num1 * num2
expn = num1 ** num2

print(f"The sum of {num1} and {num2} is {sum}.")
print(f"The difference of {num1} and {num2} is {diff}.")
print(f"The product of {num1} and {num2} is {product}.")
print(f"The exponential of {num1} to the power of {num2} is {expn}.")

if num2 > 0:
    quotient = num1 / num2
    remainder = num1 % num2
    floor = num1 // num2

    print(f"The quotient of {num1} and {num2} is {quotient}.")
    print(f"The remainder of {num1} and {num2} is {remainder}.")
    print(f"The floor division of {num1} and {num2} is {floor}.")
else:
    print("Division, modulo, and floor division is not possible since divisor is zero. ")
