# The ‘enumerate’ function adds counter to an iterable and returns it 

lists = ["Rohan", 1, 2, 3, "Shakya"]

index = 0 
for item in lists: 
    print(f"The item number at index {index} is {item}")
    index += 1

print()

# Using enumrate
print("-----------Enumerate-------------")

for index, item in enumerate(lists):
    print(f"The item number at index {index} is {item}")