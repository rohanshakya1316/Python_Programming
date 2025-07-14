# Using dunder methods, operators can be overloaded in Python 

class Number: 
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.n + other.n)
    
    def __sub__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.n - other.n)
    
    def __mul__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.n * other.n)
    
    def __truediv__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.n / other.n)
    
    def __floordiv__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return Number(self.n // other.n)
    
    def __str__(self):      # string representation for users. 
        return str(self.n)

    def __repr__(self):     # representation usually for developers
        return f"Number({self.n})"
    
num1 = Number(50)
num2 = Number(10)

print(num1 + num2)
print(num1.__add__(num2))

print(num1 - num2)
print(num1.__sub__(num2))

print(num1 * num2)
print(num1.__mul__(num2))

print(num1 / num2)
print(num1.__truediv__(num2))

print(num1 // num2)
print(num1.__floordiv__(num2))

print(num1)
print(repr(num1))