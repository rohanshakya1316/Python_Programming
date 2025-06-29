# Write a program to print multiplication table of a given number using for loop. 

num = int(input("Enter an integer to print the multiplication table: "))

print(f"Multiplication Table of {num}")

# using for loop
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

# using while loop
i = 1
while i <= 10:
    print(f"{num} X {i} = {num * i}")
    i += 1


# in reverse order multiplication table 
print("In reverse order: ")
for i in range(10, 0, -1): 
    print(f"{num} X {i} = {num * i}")
