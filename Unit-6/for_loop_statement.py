# for loop iterating over list

l = ['Rohan', 1, True, 0, False, 12.3456, 's']

for item in l:
    print(item)

# for loop iterating over tuple

t = ('Rohan', 1, True, 0, False, 12.3456, 's')

for item in t:
    print(item)

# for loop iterating over string

s = 'Rohan Shakya'

for item in s:
    print(item)

# for loop iterating over dictionary

d = {
    'name': 'Rohan',
    'age': 22,
    'address': 'Kathmandu'
}

for key in d:
    print(f"{key}: {d[key]}")   # OR

for key, value in d.items():
    print(f"{key} -> {value}")

# for loop iterating over set

sets = {12, 23, 34, 45, 56}

for item in sets:
    print(item)

# for loop does not require an indexing variable to set beforehand. 


# for loop with break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# for loop with continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range() function - returns sequence of number starting with 0 by default, and increments by 1 (by default), and ends at a specified number. 
for x in range(6):  # 0, 1, 2, 3, 4, 5 -> values 0 to 5
    print(x)

# range(2, 5) = starts with 2 to 4 (not including 5)
for x in range(2, 5): # 2, 3, 4
    print(x)

# range(1, 30, 3) = third parameter is the step-size i.e., increment value
for x in range(0, 30, 3):   # prints multiple of 3
    print(x)

# for loop with else statement
for x in range(6):
    print(x)
else:
    print("End of loop.")

# However else statment is not executed if the loo is stopped by a break statement. 
for x in range(5):
    if x == 2: break
    print(x)
else: 
    print("It will not executed due to loop exiting through break statement.")

# Nested Loop: 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# pass statement = since for loop cannot be empty, incase we want this use pass statement to avoid error. 
for x in [0, 1, 3]:
    pass        # without pass the program will throw an error