# Create a class 'Employee' and add salary and increment properties to it. 
# Write a method 'salaryAfterIncrement' with a @property decorator with a setter which changes the value of the increment based on the salary. 

class Employee: 
    # salary = 2000
    # increment = 10

    def __init__(self,salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * self.increment / 100

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary - self.salary) / self.salary) * 100
    
emp = Employee(2000, 15)

print(f"Initial Increment: {emp.increment}")
print(f"Initial final salary: {emp.salaryAfterIncrement}")

# setting the final salary directly
emp.salaryAfterIncrement = 2700     # automatically adjusts increment

print(f"\nNew increment: {round(emp.increment,2)}%")
print(f"Final salary: {emp.salaryAfterIncrement}")