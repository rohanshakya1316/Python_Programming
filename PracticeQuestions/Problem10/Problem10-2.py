#  Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator: 
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f"Square is {self.num * self.num}")
    
    def cube(self):
        print(f"Cube is {self.num * self.num * self.num}")
    
    def square_root(self):
        print(f"Square Root is {self.num ** 0.5}")

calc1 = Calculator(9)

calc1.square()
calc1.cube()
calc1.square_root()

    