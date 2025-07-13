# Python Program to Demonstrate All Types of Operators

print("========== 1. Arithmetic Operators ==========")
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)   # Exponentiation (10^3)
print("a // b =", a // b)  # Floor Division

print("\n========== 2. Assignment Operators ==========")
x = 5
print("x =", x)
x += 3
print("x += 3:", x)
x -= 2
print("x -= 2:", x)
x *= 4
print("x *= 4:", x)
x /= 2
print("x /= 2:", x)
x %= 3
print("x %= 3:", x)
x //= 1
print("x //= 1:", x)
x **= 2
print("x **= 2:", x)

print("\n========== 3. Comparison Operators ==========")
a = 5
b = 10
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n========== 4. Logical Operators ==========")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n========== 5. Bitwise Operators ==========")
a = 5       # 0101
b = 3       # 0011
print("a & b:", a & b)     # 0001 -> 1
print("a | b:", a | b)     # 0111 -> 7
print("a ^ b:", a ^ b)     # 0110 -> 6
print("~a:", ~a)           # Inverts bits
print("a << 1:", a << 1)   # 1010 -> 10
print("a >> 1:", a >> 1)   # 0010 -> 2

print("\n========== 6. Identity Operators ==========")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)         # True, same object
print("x is z:", x is z)         # False, different object
print("x is not z:", x is not z)

a = 257
b = 257 
print(a is b)   # True
print(a is not b)   # False

print("\n========== 7. Membership Operators ==========")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits:", 'apple' in fruits)
print("'mango' not in fruits:", 'mango' not in fruits)

print("\n========== 8. Ternary Operator (Conditional Expression) ==========")
a = 10
b = 20
max_val = a if a > b else b
print("Max value using ternary operator:", max_val)
