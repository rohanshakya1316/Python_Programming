# Type hints (annotations) in Python

# 1. Basic Type Assignment (Dynamic Typing)
name = "Rohan"      # str
age = 22            # int
height = 5.8        # float
is_student = True   # bool

# 2. Using type() to check the type
print(type(name))           # <class 'str'>
print(type(is_student))     # <class 'bool'>

# 3. Type Hints (Static Typing with Annotations)
age: int = 25 
height: float = 5.6

def greet(name: str) -> str: 
    return f"Hello, {name}"

print(greet("Rohan"))

# 4. Type Hints for Complex Data Structures 
from typing import List, Tuple, Dict, Union
# List of strings
names: List[str] = ["Rohan", "Shakya", "Reigns"]

# Tuple of an integer and an integer
pair: Tuple[int, int] = (10, 20)

# Dictionary with string keys and integer values
grade: Dict[str, int] = {"Math": 99, "Computer": 100}

# Union type for variables that can hold multiple types
value: Union[int, float] = 3.14

print(names)
print(pair)
print(grade)
print(value)

# 5. Custom Type Aliases 
from typing import List

Vector = List[float]

def scale_vector(v: Vector, factor: float) -> Vector:
    return [x * factor for x in v]

print(scale_vector([1.3, 2.4], 2.5))

# 6. Using type() to create a new type (Advanced)
Person = type("Person", (), {"name": "Unknown", "greet": lambda self: f"Hi, I'm {self.name}"})
p = Person()
print(p.greet())

# 7. New Types (for semantic clarity)
from typing import NewType
UserID = NewType("UserID", int)

def get_user(user_id: UserID) -> str: 
    return f"User with ID {user_id}"
uid = UserID(124)
print(get_user(uid))