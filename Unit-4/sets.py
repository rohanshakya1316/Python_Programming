# Sets Demo 

# empty set (use set(), not {} which creates a dict)
empty_set = set()
print(type(empty_set))

num_set = {1, 4, 5, 2}
print(num_set)

# From list or string
from_list = set([1, 2, 2, 3])
from_string = set("hello")  # {'e', 'h', 'l', 'o'}
print(from_list)
print(from_string)

# Non - repetition of elements in set
s = {1, 2, 3, 6, 5, 4, 3.5, 6, 2.5, "Rohan"}
print(s)

# Iterating in set 
for item in s:
    print(item)

# membership test 
print("Rohan" in s)         # True
print("Rohan" not in s)     # False


# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union => {1, 2, 3, 4, 5}
print(a & b)  # Intersection => {3}
print(a - b)  # Difference => {1, 2}
print(a ^ b)  # Symmetric Difference => {1, 2, 4, 5}

# Set Comprehension 
cube = {x**3 for x in range(6)}
print(cube)     # {0, 1, 8, 27, 64, 125}


# Frozenset = (Immutable Set)
frozen_set = frozenset({1, 2, 3, 4, 5})     # set to set
frozen_set = frozenset([1, 2, 3, 4, 5])     # list to set
print(frozen_set)
# frozen_set.add(6)       # Error - Frozenset is immutable 


# set_on_set = {{1, 2, 3, 4}, {1,2, 4, 5}}      # Error - set cannot contain another set directly
# print(set_on_set)                             # sets are mutable and thus not hashable

# However, frozenset is an immutable version of set and is hashable. 
# This means we can create a set that contains frozenset objects. 

# Create some frozensets
frozenset1 = frozenset({1, 2, 3})
frozenset2 = frozenset({'a', 'b'})
frozenset3 = frozenset({True, False})

# Create a set containing these frozensets
set_of_frozensets = {frozenset1, frozenset2, frozenset3}

print(set_of_frozensets)        # Output: {frozenset({'a', 'b'}), frozenset({1, 2, 3}), frozenset({False, True})}
