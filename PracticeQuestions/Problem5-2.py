# Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

sets = set()    # Empty set initialization

for i in range(1,9):
    n = int(input(f"Enter numeber {i}: "))
    sets.add(n)

print("All the unique numbers are: ")
print(sets)

# Can we have a set with 18 (int) and '18' (str) as a value in it?
str_int_set = {18, '18'}
print(str_int_set)      # Output: {18, '18'}
# Yes, we can have a set with 18 (int) and '18' (str) as a value in it.