# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 


class DemoAttribute:
    # class attribute
    a = 10

    def __init__(self):
        print(f"From class: {self.a}")

obj = DemoAttribute()   # Object Instantiation

print(obj.a)    # Prints the class attribute as instance attribute is not set

obj.a = 0   # Instance attribute is set

print(obj.a)    # Prints the instance attribute as it is being set.

print(DemoAttribute.a)  # Prints the class attribute

# So, the answer is NO. The class attribute is not change. 
