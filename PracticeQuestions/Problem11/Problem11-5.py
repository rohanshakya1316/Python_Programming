# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them. 

class Vector: 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
vec1 = Vector(1, 2, 3)
vec2 = Vector(4, 5, 6)
vec3 = Vector(7, 8, 9)

print(vec1 + vec2)
print(vec1 * vec2)

print(vec1 + vec3)
print(vec1 * vec3)
