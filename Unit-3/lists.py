lists = ['Apple', "Ball", 10, 23.42, False, True, "Python Language", "I am learning it. "]

print(type(lists))

print(lists[5]) 

lists[6] = "Programming Language Python"  # Unlike strings, lists are mutable 

print(lists[6]) 

print(lists[2:7])   # [10, 23.42, False, True, 'Programming Language Python']

print(lists[1:8:3])     # ['Ball', False, 'I am learning it.']

# print(lists[100])   # Error: List IndexOutOfBound 

print()

# Various List Methods 

print("=========== Python List Methods ==========\n") 

# Initialization of List 
students = ["Ram", "Shyam", "Hari", "Ram", "Sita", "Geeta", "Ram"]
print("Original List:", students) 

# append() = adds item to end of the lsit 
students.append("Rohan") 
print(f"\nappend('Rohan'): {students}") 

# insert() = inserts at specific index 
students.insert(3, "Kamal") 
print(f"\ninsert(3, 'Kamal'): {students}") 

# sort() = sorts the list in-place 
students.sort()
print(f"\nsort(): {students}") 

# reverse() = reverses the list 
students.reverse() 
print("\nreverse():", students) 

# pop() = removes and returns element at index (default value: last index) 
pop = students.pop()
print("\npop() =>", pop) 

pop_at_index = students.pop(2) 
print("\npop(2): ", pop_at_index)
print("\nList after pop():", students) 

# remove() = removes first occurance 
students.remove("Ram")
print("\nremove('Ram'):", students)

# index() = finds the first index of a value 
index_of_sita = students.index("Sita")
print("\nindex('Sita'):", index_of_sita) 

# count() = counts the occurrences 
count_ram = students.count("Ram")
print("\ncount('Ram'):", count_ram) 

# extend(): Appends another list
students.extend(["Freddy", "Alice"])
print("\nextend(['Freddy', 'Alice']):", students) 

# copy(): Creates a shallow copy
students_copy = students.copy()
print("\ncopy():", students_copy)

# clear(): Empties the list
students.clear()
print("\nclear():", students)

# List constructor
new_list = list(("one", "two", "three"))
print("\nlist(('one', 'two', 'three')):", new_list)

print("\n========= End of List Method =========")

