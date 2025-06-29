# Conditinal Statements 

# Proper Indentation is requried. 
# if(True == 1):
# print("Valid condition True == 1.")     # Error - No indentation meaning if block is empty. 

# If statement 

if(True == 1):
    print("Valid condition True == 1.")

if(False != 1 ):
    print("Valid Condition False == 0.")

# Short - hand for if statment 
if(True == 1): print("It is true i.e., 1")

# The pass statement = if statements cannot be empty, but if we for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if True:
    pass

# If else ladder

age = int(input("Enter your age: "))

if(age >= 18):
    print("You are above the age of consent.")
    print("You can vote.")

else: 
    print("You are below the age of consent.")
    print("You cannot vote.")

# Short - hand for if else statement 
print("Vote eligibility passed.") if age >= 18 else print("Vote eligibility failed.")
# This technique is known as Ternary Operators, or Conditional Expressions.

# We can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Nested if statement 
x = 31

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# Logical operators

# 1. and = true if both operands are true else false.
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# 2. or = true if at least one operand is true or else false. 
if b > a or c > b: 
    print("At least one of the conditions is true.")

# 3. not = reverse the result of the conditional statement
if not a == b:
    print("a is not equal to b.") 
