# A function with default parameter. 

def greet(name = "Guest"):      # Default parameter
    print("Welcome,", name)


greet()     # Outputs: 'Welcome, Guest' as it uses default value of name.
greet('Rohan Reigns')   # Outputs: "Welcome, Rohan Reigns" as the value of name is passed here.