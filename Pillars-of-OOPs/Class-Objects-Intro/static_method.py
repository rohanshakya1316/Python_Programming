# Sometimes we need a function that does not use the self-parameter. 
# We can define a static method like this:

class Student: 
    name = "Rohan Shakya"       # Class Attribute
    degree = "BCA"              # Class Attribute
    age = 22                    # Class Attribute

    def display_info(self):     # 'self' is conventional
        print(f"The name is {self.name}, degree {self.degree} & age {self.age}")

    @staticmethod       # decorator to mark welcome as static method. 
    def welcome():     # No need of the self parameter
        print(f"Welcome, learning Python!")

s1 = Student()    # Object instantiation

s1.welcome()    

# Student.welcome(s1)     # Error: no need of s1 as argument

Student.welcome()   # class method called.