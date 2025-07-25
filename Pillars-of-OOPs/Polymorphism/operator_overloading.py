# Operator Overloading --> Customize how operators like +, -, *, etc. work with objects using special methods (also called magic methods or dunder methods).

class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Number({self.value})"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __truediv__(self, other):
        return Number(self.value / other.value)

    def __floordiv__(self, other):
        return Number(self.value // other.value)

    def __mod__(self, other):
        return Number(self.value % other.value)

    def __pow__(self, other):
        return Number(self.value ** other.value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __and__(self, other):
        return Number(self.value & other.value)

    def __or__(self, other):
        return Number(self.value | other.value)

    def __xor__(self, other):
        return Number(self.value ^ other.value)

    def __invert__(self):
        return Number(~self.value)

    def __lshift__(self, other):
        return Number(self.value << other.value)

    def __rshift__(self, other):
        return Number(self.value >> other.value)

    def __call__(self):
        return f"Called: {self.value}"

    def __len__(self):
        return len(str(self.value))  # Just for fun

    def __getitem__(self, index):
        return str(self.value)[index]

    def __setitem__(self, index, value):
        raise NotImplementedError("Immutability enforced.")

    def __delitem__(self, index):
        raise NotImplementedError("Can't delete items.")

# Usage
a = Number(10)
b = Number(3)

print(a)           # Number(10)
print(repr(a))     # Number(10)
print(a + b)       # Number(13)
print(a - b)       # Number(7)
print(a * b)       # Number(30)
print(a / b)       # Number(3.333...)
print(a // b)      # Number(3)
print(a % b)       # Number(1)
print(a ** b)      # Number(1000)

print(a == b)      # False
print(a > b)       # True
print(a < b)       # False

print(a & b)       # Number(2)
print(a | b)       # Number(11)
print(~a)          # Number(-11)
print(a << b)      # Number(80)
print(a >> b)      # Number(1)

print(a())         # Called: 10
print(len(a))      # 2
print(a[0])        # '1'