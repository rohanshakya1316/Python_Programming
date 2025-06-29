'''
Write a program to print the following star pattern. 
    * 
  * * * 
* * * * * 
for n = 3
'''

n = int(input('Enter n: '))

for i in range(1, n + 1):
    print("  " * (n - i), end="")   # end prevent adding new line property of print()
    print("* " * (2 * i - 1), end="")
    print()