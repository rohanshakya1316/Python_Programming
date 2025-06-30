# Write a program using functions to find greatest of three numbers. 

def gretest_num_calc(n1, n2, n3):
    if n1 > n2 and n1 > n3: 
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3 
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

greatest_num = gretest_num_calc(num1, num2, num3)

print(f"The greatest among {num1}, {num2} and {num3} is {greatest_num}.")