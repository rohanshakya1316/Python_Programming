# Duck typing Polymorphism --> Python's dynamic typing allows any object to be used if it behaves correctly.
# don’t care about the type, only whether it has the methods we expect.
class Cat: 
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

# Creating instances of Cat and Dog
cat = Cat()
dog = Dog()

# Calling the function with different types of animals
animal_sound(cat)  # Output: Meow
animal_sound(dog)  # Output: Woof

# This demonstrates duck typing: both Cat and Dog have a speak method, so they can be used interchangeably.