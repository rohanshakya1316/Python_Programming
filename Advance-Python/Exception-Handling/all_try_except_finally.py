class CustomError(Exception):
    pass

def risky_divide(x, y):
    if y == 0:
        raise CustomError("Custom: Cannot divide by zero.")
    return x / y

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("Result:", risky_divide(a, b))

except CustomError as ce:
    print("Custom Error:", ce)

except ValueError:
    print("Please enter valid numbers.")

else: 
    print("Division has been successfully done.")

finally:
    print("This always runs.")