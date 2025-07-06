# Constructor Overloading in Python
#  Python does not support traditional constructor overloading (i.e., multiple __init__() methods).
#  Instead, we use default arguments, *args, or @classmethod to simulate overloading behavior.

# Method 1: Using Default Arguments

class Person: 
    def __init__(self, name = "Guest", age = None):
        self.name = name
        self.age = age

person1 = Person()              # Uses default values
person2 = Person("Reigns")      # Only name provided
person3 = Person("Rohan", 22)      # Both values provided

print(person1.name, person1.age)    # Guest None
print(person2.name, person2.age)    # Reigns None
print(person3.name, person3.age)    # Rohan 22
    

# Method 2: Using *args for variable arguments. (arbitrary)
class Point: 
    def __init__(self, *args):
        if len(args) == 0:
            self.name = "Guest"
            self.age = None
        elif len(args) == 1:
            if type(args[0]) is str: 
                self.name = args[0]
                self.age = None
            elif isinstance(args[0], int):
                self.age = args[0]
                self.name = None
            else: 
                self.name = self.age = None
        elif len(args) == 2: 
            if type(args[0]) is str and type(args[1]) is int: 
                self.name = args[0]
                self.age = args[1]
            elif isinstance(args[0], int) and isinstance(args[1], str):
                self.age = args[0]
                self.name = args[1]
            else: 
                self.name = self.age = None
        else: 
            raise ValueError("Too many arguments.")
        
p1 = Point()
p2 = Point("Rohan")
p3 = Point("Reigns", 22)

print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)


# p4 = Point("Reigns", 12, "Hello")
# print(p4.name, p4.age)


# Method 3: Using #classmethod as Alternate Constructors 

class Student: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def constructor(cls, data_str):     # Alternate Constructor
        name, age = data_str.split(",")
        return cls(name, int(age))
    
s1 = Student("Reigns", 22)
s2 = Student.constructor("Rohan, 20")

print(s1.name, s1.age)  # Reigns 22
print(s2.name, s2.age)  # Rohan 20