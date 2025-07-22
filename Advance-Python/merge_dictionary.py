# A python program to merge two dictionaries. 

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1 | dict2

print(merged_dict)

dict1 |= dict2  # Update the dict1 with dict2

print(dict1)
print(dict2)