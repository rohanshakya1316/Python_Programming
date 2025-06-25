# Simple python program to take input from the users. 

a = input("Enter first number: ")  # It takes input in string data type. 

b = int(input('Enter second number: ')) # now it takes input in int. 
c = int(input('Enter third number: ')) # now it takes input in int. 

print("First number is : ", a) 
print(f"Second number is : {b}")  # formatted string literals f""
print(f"Third number is : {b}") 
# print("Sum is : ", a + b); # if c = 1 and b = 3 it concats and prints 13 not 4

print("Sum is ", c + b); # now it sums and perform addition


print("========== 1. Basic input() ==========")
name = input("Enter your name: ")
print("Hello, ", name)

print("\n========== 2. All input() values are strings ==========")
x = input("Enter a number: ")
print(f"You entered: '{x}', type: {type(x)}")

print("\n========== 3. Type Casting input() ==========")
x = input("Enter an integer: ")
try:
    x = int(x)
    print("Integer:", x, "| Type:", type(x))
except ValueError:
    print("Invalid integer input!")

y = input("Enter a float: ")
try:
    y = float(y)
    print("Float:", y, "| Type:", type(y))
except ValueError:
    print("Invalid float input!")

print("\n========== 4. Boolean from input() ==========")
b = input("Enter True or False: ")
b = b.strip().lower() == "true"  # Convert to boolean (simple)
print("Boolean value:", b)

print("\n========== 5. Getting multiple values ==========")
a, b = input("Enter two values separated by space: ").split()
print("Value 1:", a)
print("Value 2:", b)

print("\n========== 6. Multiple values with type casting ==========")
x, y = input("Enter two numbers: ").split()
x = int(x)
y = float(y)
print("Integer:", x, "Float:", y)

print("\n========== 7. List from user input ==========")
numbers = input("Enter numbers separated by space: ").split()
int_list = [int(n) for n in numbers]
print("List of integers:", int_list)

print("\n========== 8. Prompt with default value (manual way) ==========")
name = input("Enter your name [default: Guest]: ")
if name == "":
    name = "Guest"
print("Welcome,", name)

print("\n========== 9. Custom separator input ==========")
data = input("Enter CSV values (comma-separated): ")
items = data.split(",")
print("Values:", items)

print("\n========== 10. Secure input for password (optional) ==========")
# Note: Uncomment the below lines to use it in terminal (won't work in some IDEs like online editors)
# import getpass
# password = getpass.getpass("Enter your password: ")
# print("Password received (not shown here)")

print("\n========== 11. Loop with input ==========")
while True:
    cmd = input("Type 'exit' to quit: ")
    if cmd.lower() == "exit":
        break
    print("You typed:", cmd)
