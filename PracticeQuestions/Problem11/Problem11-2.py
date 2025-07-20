# Create a class 'Pets' from a class 'Animals' and further craete a class 'Dog' from 'Pets'. 
# Add a method 'bark' to class 'Dog'.

class Animals: 
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating food.")
    
class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)
    
class Dog(Pets):
    def __init__(self, name):
        super().__init__(name)
    
    def bark(self):
        print(f"{self.name} is barking.")

animal = Animals("Human")
animal.eat()
print(animal.name)

pet = Pets("Puppy")
print(pet.name)
pet.eat()

dogesh = Dog("Kale")
dogesh.bark()
dogesh.eat()