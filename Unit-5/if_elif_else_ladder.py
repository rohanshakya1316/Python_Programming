# If elif else ladder

# elif in python means [else if]. An if statements can be chained together with a lot of 
# these elif statements followed by an else statement. 

# IMPORTANT NOTES: 
# 1. There can be any number of elif statements. 
# 2. Last else is executed only if all the conditions inside elifs fail.

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are above the age of consent.")
    print("You can vote.")

elif(age < 0):
    print("Age cannot be negative. Please try again entering valid age. ")

elif(age == 0):
    print("You are entering 0 which is not a valid age.")

else: 
    print("You are below the age of consent.")
    print("You cannot vote.")
