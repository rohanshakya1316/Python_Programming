# 1. map(function, iterable) --> Applies a function to each item of the iterable and returns a map object (which can be converted to a list, tuple, etc.). 	Transform all elements in a sequence

nums = [1, 2, 3, 4, 5, 6]
def cube(n):
    return n ** 3

squares = list(map(lambda x: x ** 2, nums))
print(squares)

cubes = list(map(cube, nums))
print(cubes)

# 2. filter(function, iterable) --> Filters items out of an iterable for which the function returns True. 	Select certain elements from a sequence
even = list(filter(lambda x : x % 2 == 0, nums))
print(even)

def odd(n):
    if n % 2 == 1: 
        return n

odds = list(filter(odd, nums))
print(odds)

# 3. reduce(function, iterable) --> Applies a function cumulatively to the items of an iterable. Import it from functools. Aggregate elements into a single value
from functools import reduce

addition = reduce(lambda x, y: x + y, nums)
print(addition)  

def multiply(x, y): return x * y
print(reduce(multiply, nums))


# Comparisions with List Comprehensions 

# map()
sq_num = [x ** 2 for x in nums]
print(sq_num)

# filter()
evens = [x for x in nums if x % 2 == 0]
print(evens)