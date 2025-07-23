# Write a python program with a list comprenhension to print a list which contains the multiplication table of a user entered number. 

# Without list comprehension

mul_num = int(input("Enter a number to print multiplication table: "))
table = []

for iter in range(1, 10 + 1):
    table.append(f"{mul_num * iter}")

for _ in table: 
    print(f"{_}  ", end="")    
print()

# With List comprehension
table_comprehensed = [i * mul_num for i in range(1, 10 + 1)]

if __name__ == "__main__": 
    print(table_comprehensed)
