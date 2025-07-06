# pass statement in class 
class Example: 
    pass




class Person:
    def __init__(self, name, age = None):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}, age is {self.age}")

# Modify properties on objects like this:
p1 = Person("John", 36)

p1.age = 40

p1.myfunc()

# Delete properties on objects by using the 'del' keyword:
# del p1.age

# Delete objects by using the del keyword:
del p1

p1.myfunc()