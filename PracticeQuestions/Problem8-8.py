# Write a python function to print multiplication table of a given number. 

# Using normal function
def multiple_table(n):
    print(f"Multiplcation Table of {n}:")
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")
    return

number = int(input("Enter the number to find the multiplication table: "))

multiple_table(number)

# Using recursive function

def recursive_multiply(n, iterator = 1):
    if iterator > 10:
        return
    else:
        print(f"{n} X {iterator} = {n * iterator}")
        recursive_multiply(n, iterator + 1)

print("\nUsing recursive function: ")
recursive_multiply(number)
