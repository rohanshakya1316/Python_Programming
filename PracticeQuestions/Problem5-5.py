# Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

# No, we cannot include a list inside a set in Python and therefore, we cannot change its values inside the set, because lists are unhashable and mutable types.

# Here's why:

s = {8, 7, 12, "Harry", [1,2]}

# This will raise:
# TypeError: unhashable type: 'list'

# Explanation:

# Sets in Python require all their elements to be hashable (i.e., have a fixed hash value and be immutable).
# Lists are mutable, so their contents can change, which means their hash would change — violating the rules of set membership.


# What can you use instead?

# If we want to include something like a list in a set, use a tuple instead, because tuples are immutable (and thus hashable if they only contain hashable items):

s = {8, 7, 12, "Harry", (1, 2)}  # Valid

# But even then, we cannot modify the values inside the tuple, because tuples are immutable.