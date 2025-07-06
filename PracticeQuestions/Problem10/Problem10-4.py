# Add a static method in problem 2, to greet the user with hello.

class Calculator: 
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"Square is {self.num * self.num}")
    
    def cube(self):
        print(f"Cube is {self.num * self.num * self.num}")
    
    def square_root(self):
        print(f"Square Root is {self.num ** 0.5}")

    @staticmethod
    def greet():
        print("Hello, please use the calculator!")

calc1 = Calculator(9)

calc1.greet()
calc1.square()
calc1.cube()
calc1.square_root()