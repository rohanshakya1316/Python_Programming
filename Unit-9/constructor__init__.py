# __init__() constructor in Python

# It takes ‘self’ argument and can also take further arguments. 

class Employee: 
    name = "Guest"
    lang = 'Python'

# Note: The __init__() function is called automatically every time the class is being used to create a new object.
    def __init__(self):     # Constructor
        print("This is the constructor being called. ")

    
emp1 = Employee()   # calls the construtor

print(emp1.name, emp1.lang)

emp2 = Employee()