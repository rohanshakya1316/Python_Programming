# A Decorator is a function that modifies the behavior of the another function or method without changing its code. 

def decorator(func): 
    def wrapper(): 
        func()
        print("Before Function Call..")
        func()
        print("After Function Call..")
        func()
    return wrapper


@decorator  
def func_demo():
    print("This the args for the decorator. ")

# func_demo = decorator(func_demo) =====>  same as using @decorator
func_demo()

