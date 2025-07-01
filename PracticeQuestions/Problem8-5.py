'''
Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3

'''

def print_pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)
        # print()


n_lines = int(input("Enter lines to print the pattern: "))

print("Using normal function:")
print_pattern(n_lines)

print()

# Recursive function to print the pattern
def pattern(n):
    if(n == 0):
        return
    print("* " * n)
    pattern(n - 1)

print("Using recursive function:")
pattern(n_lines)

