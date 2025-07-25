# A list contains the multiplication table of 7. Write a program to convert it to vertical string of same numbers. 

multiples = [7 * i for i in range(1, 10 + 1)]

print(multiples)

vertical_multiples = "\n".join(map(str,multiples))
print(vertical_multiples)