class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} is managing team.")

e = Employee("Rohan")
m = Manager("Reigns")

e.work()  # Rohan is working.
m.work()  # Reigns is managing team.
