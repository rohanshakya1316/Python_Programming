# List Comprehension is an elegant way to create lists based on existing lists.

l = [1, 3, 4, 5, 6, 7, 8]

squareList = []

for item in l: 
    squareList.append(item ** 2)

print(squareList)

print()

print("-----------List Comprehensions-----------")
squaredList = [i ** 2 for i in l]
print(squaredList)