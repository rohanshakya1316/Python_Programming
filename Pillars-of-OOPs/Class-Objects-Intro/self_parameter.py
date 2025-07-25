# In Python, self is a conventional name for the first parameter of instance methods within a class. It is not a reserved keyword but a widely adopted convention that refers to the instance of the class on which the method is being called.

#  Class in Python
# Class Attribute: An attribute that belongs to the class rather than a particular object. 

class Student: 
    name = "Rohan Shakya"       # Class Attribute
    degree = "BCA"              # Class Attribute
    age = 22                    # Class Attribute

    def display_info(self):     # 'self' is conventional
        print(f"The name is {self.name}, degree {self.degree} & age {self.age}")

    def welcome(greet):     # We can set the parameter other than self too but this params is must.
        print(f"Welcome, learning Python!, {greet.name}")

s1 = Student()    # Object instantiation

# We cannot call the class method directly like this through object as we get an error as,
# s1.display_info()     # TypeError: Student.display_info() takes 0 positional arguments but 1 was given
# The above call is same as Student.display_info(s1)  --> s1 argument is pass in the method. 
#  To solve the above error we use 'self' parameter in display_info() method. 

# Now calling the class method. 

s1.display_info()   # Or, we can call this method as 
Student.display_info(s1)    # s1 argument for parameter 'self'

s1.welcome()       # Or, 
Student.welcome(s1)













