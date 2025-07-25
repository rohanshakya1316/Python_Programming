# Runtime Polymorphism using Method Overriding
# Child class overrides the method from the parent class with its own implementation.

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting")

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")

def vehicle_start(vehicle):
    vehicle.start()

# Creating instances of Car and Bike
car = Car() 
bike = Bike()

# Calling the function with different types of vehicles
vehicle_start(car)  # Output: Car is starting   
vehicle_start(bike)  # Output: Bike is starting

# This demonstrates runtime polymorphism: the same function call behaves differently based on the object type.