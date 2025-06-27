# Dictionary Demo 

# syntax 

# my_dict = {
#     "key1": "value1",
#     "key2": "value2"
# }

# Empty dictionary 
empty_dictionary = {}
print(type(empty_dictionary))


dict_marks = {
    "Rohan": 90, 
    "Shyam": 29, 
    "Dean": 78,
    'Roman': 50, 
    0: "Kamal",
    "lists": [1, 3, 5, 7]
}

print(dict_marks)

print(type(dict_marks)) 

print(dict_marks["Rohan"])      # prints 90 
print(dict_marks["lists"])      # prints [1, 3, 5, 7]
print(dict_marks[0])            # prints Kamal

# Various ways to create dictionary 

# 1. Using curly braces
d1 = {"a": 1, "b": 2}
print("From curly braces:", d1)

# 2. Using dict() constructor
d2 = dict(name="John", age=25)
print("From dict() constructor:", d2)

# 3. From list of tuples
d3 = dict([("x", 10), ("y", 20)])
print("From tuples:", d3)

# 4. Using fromkeys()
d4 = dict.fromkeys(["a", "b", "c"], 0)
print("fromkeys():", d4)

student = {"name": "Logan", "age": 21, "is_enrolled": True}

print("Accessing using key:",student["name"])      # Logan 
print("Accessing using key:", student["is_enrolled"])   # True 
print("Accessing using get():",student.get("age"))       # 21 
print("Access non - existent key:", student.get("grade", 'N/A'))  # N/A (default) 

# print(student.get('address'))       # returns None
# print(student['address'])       # returns an error called KeyError 


# Dictionary is unordered, indexed, and mutable and cannot contain duplicate keys. 
student["age"] = 25         # Update the value of key 'age'
student['grade'] = "A"      # Add new key 

print(student.get('age')) 

print(student["grade"])


# Deleting values in dictionary 
# print(student)
# del student["is_enrolled"] 
# print(student)
# student.pop("name") 
# print(student)
# student.popitem()       # Removes the last inserted pair
# print(student)
# student.clear()         # Empties the dictionary 
# print(student)

# Iterating through Dictionary 

for key in student:
    print(f"{key}:", student[key])   # OR

for key, value in student.items(): 
    print(key, "->", value)






