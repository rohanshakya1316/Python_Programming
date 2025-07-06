# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer: 
    company = "Microsoft"
    def __init__(self, name, age, degree):
        self.name = name
        self.age = age
        self.degree = degree

coder1 = Programmer("Rohan Shakya", 22, "BCA")
coder2 = Programmer("Batman", 32, "BIM")

print(f"Programmer 1: name: {coder1.name}, age: {coder1.age}, degree: {coder1.degree}, company: {coder1.company}")
print(f"Programmer 2: name: {coder2.name}, age: {coder2.age}, degree: {coder2.degree}, company: {coder2.company}")