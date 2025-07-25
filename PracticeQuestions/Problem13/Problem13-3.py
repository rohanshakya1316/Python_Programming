# Write a program to filter a list of numbers which is divisible by 5. 

import random

lists = []

for i in range(10):
    lists.append(random.randint(1, 100))

print(lists)

def divisible_five(n):
    if n % 5 == 0: 
        return True
    return False

filtered_list = list(filter(divisible_five, lists))

print(filtered_list)

fileter_using_lambda = list(filter(lambda x: True if x % 5 == 0 else False, lists))
print(fileter_using_lambda)