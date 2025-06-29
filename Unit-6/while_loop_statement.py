# # Simple while loop
i = 1
while i < 6:
    print(i)
    i += 1      

# while loop with break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# while loop with continue statement
i = 1
while i < 6: 
    if i == 2:
        i += 1      # to avoid infinite loop
        continue
    print(i)
    i += 1

# while loop with else statement
i = 1
while i < 6: 
    print(i)
    i += 1
else: 
    print("i is no longer less than 6.")    # prints it when the condition is false.

# printing a string five times
i = 1
str = "Rohan Shakya"
while (i <= 5):
    print(str)
    i += 1

# we can print the content of a list using while loops

l = [True, 1, 'Rohan', 'S', 12.345, "Kamal", False]
i = 0

while(i < len(l)):
    print(l[i])
    i += 1

# we can print the content of a tuple using while loops

t = (True, 1, 'Rohan', 'S', 12.345, "Kamal", False)
i = 0

while(i < len(t)):
    print(t[i])
    i += 1

# we can iterate over strings as well
s = "Rohan Shakya"
i = 0
while i < len(s):
    print(s[i])
    i += 1