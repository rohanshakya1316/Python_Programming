# Various dictionary methods

student = {
    "name": "Logan", 
    "age": 21, 
    'address': 'Kathmandu', 
    "is_enrolled": True, 
    "grade": "A"
}

# Original Dictionary 
print("Original Dictionary: \n", student)

# 1. keys() = returns a list containing dictionary's keys
print("Keys():", student.keys())

# 2. values() = returns a list containing dictionary's values
print("Values():", student.values())

# 3. items() = returns a list of (key, values) tuples 
print("items():", student.items())

# 4. get(key, default) = returns the value of the existed specified key, else default 
print("get():", student.get("name"))
print("Default get():", student.get("address", "Kirtipur"))

# 5. update({key: value}) = updates the dictionary with supplied key - value pairs, if not present it appends it in dictionary 
student.update({"name": "Rohan"})
print("Name update():", student.get("name"))
student.update({"degree": "BCA"})    # appends it in the dictionary 
print("New key-value pair:", student)

# 6. setdefault(key, value) = if key does not exists, sets it 
print("After setdefault():", student.setdefault("marks", 99))

# 7. copy() = copies one dictionary and returns new dictionary 
student_copy = student.copy()
print("Copied Dict:", student_copy)

# 8. pop() 
popped = student.pop("address")
print("pop('address') ->", popped)
print("After popped:",student)

# 9. popitem()  
last = student.popitem()
print("popitem() ->", last)
print("After popitem():", student)

# 10. del 
del student['is_enrolled'] 
print("After del:", student)

# 11. clear()
student.clear()
print("After clear():", student)

print("\n========= Nested Dictionary =========")
students = {
    "101": {"name": "Rohan", "age": 20},
    "102": {"name": "Sita", "age": 22}
}
print("students['101']['name']:", students["101"]["name"])
print("students['102']['age']:", students["102"]["age"])

print("\n========= JSON Conversion =========")
import json
data = {"name": "Rohan", "age": 25}
json_str = json.dumps(data)
print("JSON string:", json_str)
data_loaded = json.loads(json_str)
print("Loaded from JSON:", data_loaded)