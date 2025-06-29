# Write a program which finds out whether a given name is present in a list or not.

name_list = ['Rohan', 'Kamal', 'Roman', 'Dean', "Seth"]

name = input("Enter your name: ")

if name in name_list:
    print("Entered name is present in the list:", name)

else:
    print("Entered name is not present in the list:", name)

    