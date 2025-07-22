# A python program that shows the use of try...except. 

# Simple try...except blocks
# try:
#   print(x)  # x is not defined
# except:     # NameError
#   print("An exception occurred")

# Basic try...except
try: 
   num = int(input("Enter a number: "))
   result = 100 / num
except ZeroDivisionError:
   print("You cannot divide by zero.")
except ValueError: 
   print("Invalid Input. Please enter a number.")

# try...except with generic exceptions  (NOT RECOMMENDED)
try: 
    # Code which might throw exception 
    result = 10 / 0
    print(result)
except Exception as e: 
    print(e)