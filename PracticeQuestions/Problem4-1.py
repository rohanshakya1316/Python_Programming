# Write a program to store seven fruits in a list entered by the user. 

fruits = input('Enter seven fruits with space between them: ')

list_of_fruits = fruits.split(" ")

print(list_of_fruits)

print(type(list_of_fruits))


# Alternatives 

# Create an empty list 
fruit = []

# User input 
print('Enter the names of seven fruits: ')

for i in range(1, 8):
    frt = input(f'Enter fruit {i}: ')
    fruit.append(frt) 

print("\nThe list of fruits you entered are: ")

print(fruit)