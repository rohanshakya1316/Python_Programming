# 1. Public Members ==> Public members are accessible from anywhere in the program.

class Student: 
    def __init__(self, name):
        self.name = name    # Public variable

s = Student("Rohan")
print(s.name)  # Accessing public member

# 2. Protected Members ==> Protected members are accessible within the class and its subclasses. They are not meant to be accessed from outside the class hierarchy.
# A single underscore _ is used as a convention to indicate that a variable or method is intended for internal use only (but it's not enforced by Python).

class Student: 
    def __init__(self, name):
        self._name = name # Protected variable

s = Student("Kamal")
print(s._name)  # Accessing protected member (not recommended, but possible)

# 3. Private Members ==> Private members are accessible only within the class they are defined in. They cannot be accessed from outside the class.
# A double underscore __ is used to indicate that a variable or method is private.
# A double underscore __ triggers name mangling, which means the variable is renamed to _ClassName__variableName to prevent access from outside the class.

class Student: 
    def __init__(self, name):
        self.__name = name  # Private variable

    def get_name(self):
        return self.__name # Public method to access private data 

s = Student("Reigns")

# Accessing private variables but not recommended
print(s._Student__name)  # Accessing private member using name mangling (not recommended)

# print(s.__name)  # This will raise an AttributeError because __name is private

print(s.get_name())  # Accessing private member through a public method