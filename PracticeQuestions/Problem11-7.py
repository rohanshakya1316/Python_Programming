# Override the __len__() method on vector of problem 5 to display the dimension of the vector. 

class Vector: 
    def __init__(self, lists):
        self.lists = lists
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")
        result = [a + b for a, b in zip(self.lists, other.lists)]
        return Vector(result)
    
    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")
        return sum(a * b for a, b in zip(self.lists, other.lists))
    
    def __str__(self):
        return f"Vector({', '.join(map(str, self.lists))})"
    
    def __len__(self):
        return len(self.lists)
    
vec1 = Vector([1, 2, 3, 4])
vec2 = Vector([4, 5, 6, 7])
vec3 = Vector([7, 8, 9, 10])

print(vec1 + vec2)
print(vec1 * vec2)

print(vec1 + vec3)
print(vec1 * vec3)

print(len(vec1))