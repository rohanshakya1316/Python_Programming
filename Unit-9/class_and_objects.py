# Object Oriented Programming in Python

#  Class in Python
class Student: 
    name = "Rohan Shakya"       # Class Attribute
    degree = "BCA"              # Class Attribute
    age = 22                    # Class Attribute


s1 = Student()    # Object instantiation

s1.address = "Kathmandu"    # Object or instance Attribute

# Accessing class attribute through object.
print(f"The name is {s1.name}, degree is {s1.degree}, address is {s1.address} and age is {s1.age}")

kamal = Student()

kamal.name = "Kamal Thakur" # Object attribute

print(kamal.name, kamal.age, kamal.degree)      # Output: Kamal Thakur 22 BCA
