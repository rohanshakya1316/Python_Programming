# Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

class TwoDVector: 
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j ")

class ThreeDVector(TwoDVector): 
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k ")

two_d_vector = TwoDVector(1, 2)
two_d_vector.show()

three_d_vector = ThreeDVector(1, 2, 3)
three_d_vector.show()