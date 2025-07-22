# Global Variable 

counter = 0 

def increment():
    global counter # Tells python to use the global 'counter' variable
    counter += 1
    print("Inside function:", counter)

print("Before function call:", counter)
increment()
print("After function call:", counter)

