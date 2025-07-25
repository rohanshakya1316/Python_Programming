# Single Inheritance in Python
# Single inheritance occurs when child class inherits only a single parent class. 

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self, address = None):
        print(f"The name is {self.fname} {self.lname} and address {address}.")

# Student inherits Person
class Student(Person): 
    def __init__(self, fname, lname, address):
        Person.__init__(self, fname, lname)
        self.address = address

    def display(self):
        return Person.display(self, self.address)

# Object for the Person class 
p1 = Person("Rohan", "Reigns")

p1.display()
# Person.display(p1)

# Object for the Student class
s1 = Student("Kamal", "Thakur", "KTM")

s1.display()
# Student.display(s1)
