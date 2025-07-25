# Write a program to find the maximum of the numbers in a list using the reduce function. 

from functools import reduce

lists = [12, 23, 34, 45, 56, 67, 78, 89, 90]

def max_find(x, y): return max(x, y)

maximum = reduce(max_find, lists)
print(maximum)

max_using_lambda = reduce(lambda x, y : x if x > y else y, lists)
print(max_using_lambda)