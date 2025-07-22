# The finally block executes no matter what, even if error is raised or not.

try: 
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a number")
finally:
    print("Finally block is executed.") 


# finally block can be used with function as it is executed even if the function returns. 
def finally_demo():
    try: 
        res = 10 / 0
        return res
    except ZeroDivisionError: 
        return "Cannot Divide by Zero."
    finally: 
        print("finally block executed even if the function returns.")
msg = finally_demo()
print(msg)


# File handling exceptions
try: 
    f = open("demo.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
else: 
    print("File read successfully.")
finally: 
    print("Closing file...")
    if 'f' in locals(): f.close()