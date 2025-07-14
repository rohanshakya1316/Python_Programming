class Student: 
    # Class attribute
    college_name = "Engineering College"

    # Default Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.college_name = Student.college_name

    @classmethod
    def change_college(cls, name_new):
        cls.college_name = name_new
    
    # Alternate Constructor
    @classmethod
    def from_string(cls, data_info):
        name, age = data_info.split(',')
        return cls(name, int(age))
    
    def display(self):
        print(f"""Name: {self.name}\nAge: {self.age}\nCollege: {Student.college_name}\n """)

# Calling Default Constructor
stu1 = Student("Rohan", 22)

# Calling Alternate Constructor
stu2 = Student.from_string("Reigns,20")

# Change the college name class attribute using classmethod 
Student.change_college("Management College")

# Displays the new class value 
stu1.display()
stu2.display()

# instance cannot override class attribute
stu1.college_name = "Computer Training College"
stu1.display()