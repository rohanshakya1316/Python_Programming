# Constructor Inheritance

# In Python, constructors (__init__ methods) are not automatically inherited. However, they can be explicitly called from a subclass using super() or directly calling the parent class.

# Basic Constructor Inheritance using super()

class Animal: 
    def __init__(self, name):
        print("Animal constructor called.")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        print("Dog constructor called. ")
        self.breed = breed

# Object Instantiation
d = Dog("Kalle", "Bull Dog")
print(f"Name: {d.name}, Breed: {d.breed}")


# Constructor Inheritance by Directly calling Parent class

class Animal: 
    def __init__(self, name):
        print("Animal constrctor called. ")
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)    # Not using super()
        print("Dog constructor called.")
        self.breed = breed
    
    def bark(self):
        print(f'{self.name} is barking')

# Object Instantiation
d = Dog("Siyu", "German Shephard")
print(f"Name: {d.name}, Breed: {d.breed}")

d.bark()