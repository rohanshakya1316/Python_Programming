# Write __str__() method to print the vector as follows: 7i + 8j + 10k


names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
print()

class Vector:
    def __init__(self, components):
        self.components = components  # a list of numbers

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        basis = ['i', 'j', 'k', 'm', 'n']
        terms = []
        for idx, val in enumerate(self.components):
            symbol = basis[idx] if idx < len(basis) else f"e{idx+1}"
            terms.append(f"{val}{symbol}")
        return " + ".join(terms)

    def __repr__(self):
        return self.__str__()
    
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

v3 = v1 + v2              # vector addition
dot_product = v1 * v2     # dot product

print("v1 + v2 =", v3)           # Vector([5, 7, 9])
print("v1 . v2 =", dot_product)  # 32 (1*4 + 2*5 + 3*6)

