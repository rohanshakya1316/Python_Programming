#  Class in Python
# Class Attribute: An attribute that belongs to the class rather than a particular object. 

class Student: 
    name = "Rohan Shakya"       # Class Attribute
    degree = "BCA"              # Class Attribute
    age = 12                    # Class Attribute


s1 = Student()    # Object instantiation

# Object Attribute: An attribute that belongs to the Instance (object). 
s1.address = "Kathmandu"    # Object Attribute

# Accessing class attribute through object.
print(f"The name is {s1.name}, degree is {s1.degree}, address is {s1.address} and age is {s1.age}")

# Instance attributes take preference over class attributes during assignment and retrieval. 

s1.name = "Reigns"  # Object Attribute > Class Attribute
s1.degree = "WWE"   # Adding Object Attribute

print(f"The name is {s1.name}, degree is {s1.degree}, address is {s1.address} and age is {s1.age}")


# We cannot call the class method directly like this through object as we get an error as,
# s1.display_info()     # TypeError: Student.display_info() takes 0 positional arguments but 1 was given










