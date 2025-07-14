# class method is the method bound to the class and the not the object of the class. 

# sometimes can be called as alternative construtors. 

class Student:
    degree = "BCA"

    @classmethod    # This decorator returns the class attribute. 
    def display(cls):
        print(f"The degree is {cls.degree}.")


stu1 = Student()

# stu1.degree = "BIT"     # Instance attribute 
# stu1.display()      # Displays the instance attribute i.e. BIT 

stu1.display()