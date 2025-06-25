empty_tuple = ()

a = (1)         # type = int 
print(type(a))

a1 = (1,)         # type = tuple
print(type(a1)) 

t= (1, 2, "Ram", 'gita', 12.343, False, True, "Python loading") 

print(t)

print(t[4])     # Tuples are immuatable like strings. 

# t[4] = 23.23423     # Error

# print(t[4])

print("\n")

# Various tuple methods 

numbers = (1, 3, 5, 3, 7, 3, 9, 3) 

print("Original Tuple:", numbers) 

# count() = returns the number of times specific element appeared in the tuple
print(numbers.count(3))     # Outputs: 4

# index() = returns the first index of value 
print(numbers.index(3))     # Outputs: 1

# len() = returns the total numbers of element in the tuple 
print(len(numbers))         # Outputs: 8 

# Operations that can be performed in the tuple 

print() 

# Creating new tuples 

tuple1 = (1.5, 3.5, 6.5) 
tuple2 = ('A', "B", 'C') 

print("Tuple1:", tuple1)
print("Tuple2:", tuple2)
 
# Indexing = Accessing the tuple elements 
print("First element of the tuple1:", tuple1[0])
print("Last element of the tuple2:", tuple2[-1])    # Supports negative index 

# SLicing = Divides the tuples in sub parts 
print("tuple1[1:3]: ", tuple1[1:3])     # Outputs: (3.5, 6,5)
print("tuple2[:::-1]:", tuple2[::-1])  # Outputs: reverses the tuple 

# Iteration = Looping through tuple 
for item in tuple1: 
    print("Item:", item)

# Membership Test = returns boolean value ensuring the presence of element in tuple 
print("Is 1.5 in tuple1: ", 1.5 in tuple1)
print("Is E in tuple2: ", 'E' in tuple2)

# Concatenation = joins the tuples and return new tuple 
tuple3 = t + tuple1 + tuple2
print("Concatenated tuple:", tuple3)

# Repetition = repeats the elements of tuple returning new one 
print("Repetition of tuple1 * 3:", tuple1 * 3)  # Repeats elements of tuple1 three times in new one 

# Tuple Packing and Unpacking
packed = (100, 200, 300) 
a, b, c = packed
print("Unpacked:", a, b, c)     # Outputs: 100 200 300 

# Nesting = tuple inside another tuple 
nesting = (tuple1, tuple2)
print("Nested Tuple:", nesting)
print("Access nested elment:", nesting[0][2])       # Outputs: 6.5 

# Built in functions 
print("Max of tuple1:", max(tuple1))              # Output: 6.5
print("Min of tuple1:", min(tuple1))              # Output: 1.5
print("Sum of tuple1:", sum(tuple1))              # Output: 11.5

# Conversion between tuple and list 
temp_list = list(tuple1)        # Tuple to list 
temp_list.append(8.5)
tuple1_modified = tuple(temp_list)  # List to tuple
print("Modified tuple:", tuple1_modified)

# Use in Dictionaries (as keys) or Sets (if immuatable)
key = (1, 2)
my_dict = {key: "Rohan"}
print("Dictionary using tuple as key:", my_dict[key])


