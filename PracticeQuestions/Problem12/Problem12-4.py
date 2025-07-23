# Write a python program to display a / b where a and b are integers. If b = 0, display infinite by handling the 'ZeroDivisionError'. 

a = int(input("Enter a: "))
b = int(input("Enter b: "))

try: 
    res = a / b 
    print(res)

except ZeroDivisionError as zde: 
    print("Divide by zero is infinite.")
    print(zde)
