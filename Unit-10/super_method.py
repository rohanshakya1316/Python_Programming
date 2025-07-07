# super() method = access the methods of a super class in the derived class.

# Accessing Parent Members: 
class Parent: 
    def show(self):
        print("Parent class show() method.")

class Child(Parent):
    def show(self):
        super().show()  # calls Parent's show()
        print("Child class show() method.")

parent1 = Parent()
Parent.show(parent1)

child1 = Child()
child1.show()
