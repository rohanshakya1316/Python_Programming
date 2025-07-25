from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_noise(self):   # abstract method
        pass 

class Dog(Animal):
    def make_noise(self):
        return "Woof! Woof!"
    
class Cat(Animal):
    def make_noise(self):
        return "Meow! Meow!"

# a = Animal()    # Error: Cannot instantiate abstract class

dog = Dog()
cat = Cat()

print(dog.make_noise())
print(cat.make_noise())

# what will happen if base class donot override 
class IncompleteAnimal(Animal):
    pass 

x = IncompleteAnimal()  # will raise TypeError 