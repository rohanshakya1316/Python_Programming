# Using raise keyword to manually write exceptions. 

age = int(input("Enter your age: "))

# Raising exceptions manually
if age < 0: 
    raise ValueError("Age cannot be negative.")

# Creating custom exceptions inheriting Exception class
class YoungAgeError(Exception): pass
if age < 18:
    raise YoungAgeError("Not Eligible for Voting.")

print("This line will not be executed.")