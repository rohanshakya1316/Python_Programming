from math import pi
# @property: Turn method into read-only attribute 

class Circle: 
    def __init__(self, radius):
        self.radius = radius

    @property 
    def area(self):
        return pi * self.radius ** 2 
    
c = Circle(5)

circle_area = c.area    # area has no parenthesis ()

print(f"The area of circle is {round(circle_area, 2)}.")


# @property: with getter setter and deleter
class Person: 
    def __init__(self):
        self._name = ""

    @property # Implicitly defines the getter
    def name(self):
        print("Getters Called.")
        return self._name
        
    
    @name.setter
    def name(self, value):
        print("Setter Called.")
        if not value: 
            raise ValueError("Name cannot be empyt. ")
        self._name = value
    
    @name.getter # override the original one 
    def name(self):
        print("Getters Called through @name.getter.")
        return self._name
    
    @name.deleter
    def name(self):
        print("Deleter Called.")
        del self._name

p1 = Person()
p1.name = "Rohan Shakya"    # Calls Setters
print(p1.name)              # Calls Getters
del p1.name                 # Calls Deleters