# Type Casting in Python 

a = 10 
b = float(a)
typeName = type(a) # <class 'int'
typeName = type(b) # <class 'float'
print(typeName)

print("========== 1. Implicit Type Casting ==========")
# Python automatically converts int to float
a = 10
b = 3.5
result = a + b
print(f"{a} (int) + {b} (float) = {result} (type: {type(result)})")

print("\n========== 2. Explicit Type Casting ==========")
# Using built-in functions to convert types manually

# int() - Converts to integer
x = "100"
print(f"String '{x}' to int:", int(x))

# float() - Converts to float
x = "12.34"
print(f"String '{x}' to float:", float(x))

# str() - Converts to string
x = 50
print(f"Integer {x} to string:", str(x))

# bool() - Converts to boolean
print(f"int 0 to bool:", bool(0))          # False
print(f"int 1 to bool:", bool(1))          # True
print(f"Empty string to bool:", bool(""))  # False
print(f"Non-empty string to bool:", bool("Python"))  # True

# list(), tuple(), set()
print("\n========== 3. Sequence Type Casting ==========")
s = "hello"
print(f"String to list: {list(s)}")   # ['h', 'e', 'l', 'l', 'o']
print(f"String to tuple: {tuple(s)}") # ('h', 'e', 'l', 'l', 'o')
print(f"List to set: {set(['a', 'b', 'a'])}")  # {'a', 'b'}

# dict() - From list of pairs
print(f"List of tuples to dict:", dict([('a', 1), ('b', 2)]))

print("\n========== 4. Complex Number Type Casting ==========")
real = 3
imaginary = 4
z = complex(real, imaginary)
print(f"complex({real}, {imaginary}) = {z}")

print("\n========== 5. Bytes and Bytearray ==========")
# str to bytes (encoded)
s = "hello"
b = bytes(s, 'utf-8')
print(f"String to bytes: {b}")

# bytes to bytearray
ba = bytearray(b)
print("Bytes to bytearray:", ba)

print("\n========== 6. Type Checking ==========")
print("Type of 10:", type(10))
print("Type of 10.5:", type(10.5))
print("Type of 'hello':", type("hello"))
print("Type of True:", type(True))
print("Type of [1, 2]:", type([1, 2]))
