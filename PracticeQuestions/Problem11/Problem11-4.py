# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them. 

class Complex: 
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return Complex(real_part, imaginary_part)
    
    def __str__(self):  # mandatory method to make print nicely
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)
print(c1.__add__(c2))

print(c1.__mul__(c2))