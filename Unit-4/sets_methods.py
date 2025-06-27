# Various Sets methods 

print("========= Set Methods in Python =========")

# Initial Set 
student = {"Ram", "Shyam", "Hari", "Sita"}
print("Original Set:", student)
print("Length of set:", len(student))

# 1. add() = Adds a single item in the set 
student.add("Rohan")
print("add('Rohan'):", student)

# 2. update() or symbol (|=) = Adds multiple items
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print("update(set):", thisset)

thisset |= tropical
print("|= symbol update:", thisset)


# The object in update() can be set or any iterable object like tuple,list, dictionaries, etc.  
my_list = ["kiwi", "orange"]
my_tuple = ('Kamal', "Sonam")
thisset.update(my_list)
student.update(my_tuple)

print("update(list):", thisset)
print("update(tuple):", student)

# 3. remove() = removes an item (Error if not found) 
student.remove('Rohan')
print("remove('Rohan'):", student)

# student.remove('Shakya')    # Error: Shakya is not in set student

# 4. discard() = removes an item (No error if not found) 
student.discard('Ram')         # Ram present in set student
student.discard('Thakur')      # Thakur not in set student - No error
print("discard('Ram'):", student) 

# 5. pop() = returns and removes an arbitrary element i.e., random element due to unordered property of set
popped = thisset.pop()
print("pop() ->", popped)
print("thisset after pop():", thisset)

# 6. clear() = removes all elements 
thisset.clear() 
print("clear():", thisset)      # Output: set()

# 7. copy() = returns a shallow copy 
copy_student = student.copy()
print(copy_student)

# 8. del keyword = delete the set completely 
del student 
# print("del keyword:", student)        # Error - as student is not defined now deleted completely 



