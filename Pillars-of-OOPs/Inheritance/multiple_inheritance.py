# Multiple Inheritance in Python
# Multiple Inheritance occurs when the child class inherits from more than one parent classes.


# Parent class
class Animal: 
    name = "Animal"

    def eat(self):
        print(f"{self.name} is eating. ")

# Parent class
class Dog: 
    breed = "German Shephard"

    def info(self):
        print(f"The dog is {self.breed}.")

# Child class or Derived class
class Programmer(Animal, Dog):
    company = "WWE"
    
    def intro_demo(self):
        print(f"I like {self.company}.")

# Object Instantiation
programmer1 = Programmer()

# Accessing methods and properties of Animal class
print(programmer1.name)
programmer1.eat()

# Accessing methods and properties of Dog class
print(programmer1.breed)
programmer1.info()

# Accessing methods and properties of child class
print(programmer1.company)
programmer1.intro_demo()