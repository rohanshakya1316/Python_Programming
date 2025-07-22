# The else block is executed only if no exception is raised. 

try: 
    num = int(input("Enter a number: "))
except ValueError: 
    print("Invalid Input. Please enter a number.")
# Executes if the try block is successful.
else: 
    print(f"You entered: {num}.")


# Another example 
try: 
    print("Hello World!")
except: 
    print("Something went wrong!")
else:
    print("Nothing went wrong!")