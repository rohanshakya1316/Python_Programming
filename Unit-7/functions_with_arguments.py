# Function with argument. 

def greet(name, greet):
    print("Hello,", name)
    print(greet)

greet("Rohan Shakya", "Good Morning!")
return_val = greet("Rohan Shakya", "Good Morning!")
print(return_val)       # None 

# Same function can be written with returning value
def greet(name): 
    greeting = f"Welcome, {name}!"
    return greeting 

gr = greet("Rohan")
print(gr)       # gr = 'Welcome, Rohan!'

# A function that returns average of three numbers
def avg(a, b, c):
    avg = (a + b + c) / 3
    return avg

average = avg(10, 15, 20)
print(f"The average is {average}.")
