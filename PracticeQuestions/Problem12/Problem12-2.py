# Write a python program to print third, fifth and seventh element from a list using enumerate function. 

lists = ["first", 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

for iter, item in enumerate(lists, start = 1):
    if iter == 3 or iter == 5 or iter == 7: 
        print(f"Element {iter} is {item}")
else: 
    print("Completed enumerating...")

# Alternatives List comprehensions
[print(f"Element {i} is {x}") for i, x in enumerate(lists, start=1) if i in (3, 5, 7)] and print("Completed enumerating...")


# List comprenhensions 
[print(f"Element {iter} is {item}") if iter in (3, 5, 7) else print("Nothing") for iter, item in enumerate(lists, start = 1)]