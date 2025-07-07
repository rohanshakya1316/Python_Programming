# Hierarichal Inheritance

class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car()

bike = Bike()

car.move()
bike.move()