# Write a program to greet all the person name stored in a list 'l' and which starts with S. 
l = ["Rohan", 'Sohan', 'Sachin', 'Rahul']

greeting = "Welcome,"

for item in l:
    if item.lower().startswith("s"):
        print(f"{greeting} {item}.")

