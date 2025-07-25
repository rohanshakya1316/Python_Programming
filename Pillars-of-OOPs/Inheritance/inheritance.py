# Inheritance in Python

class LivingBeings:     # Base Class or Parent Class
    name = "Animal"

    def eat(self):
        print(f"{self.name} is eating. ")
    
# class Human: 
#     name = "Human Beings"
#     def eat(self):
#         print(f"{self.name} is eating.")

class Human(LivingBeings):      # Derived or child class
    name = "Human Beings"

    def talk(self):
        print(f"{self.name} is talking.")

obj1 = LivingBeings()
obj2 = Human()

obj1.eat()

obj2.eat()

obj2.talk()

# We can overwrite or add new attributes and methods in ‘Human’ class. 
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")  # overrides A
a = A()
b = B()
a.greet()  # Output: Hello from A
b.greet()  # Output: Hello from B
