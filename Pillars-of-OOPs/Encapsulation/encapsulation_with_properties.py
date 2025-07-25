# Encapsulation using @property decorator 

class Person: 
    def __init__(self, age):
        self.__age = age

    @property 
    def age(self):          # getter
        return self.__age
    
    @age.setter
    def age(self, value):   # setter
        if value >= 0: 
            self.__age = value
        else: 
            raise ValueError("Age cannot be negative.")

p = Person(25)

print(p.age)    # 25
p.age = 30      # setter called

try: 
    p.age = -12
except ValueError as ve:
    print(ve)