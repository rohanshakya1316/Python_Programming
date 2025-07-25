# Multi Level Inheritance 
# When a child class becomes a parent for another child class. 

class Employee: 
    def __init__(self, name, eid):
        self.name = name
        self.eid = eid

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.eid}")

    def work(self):
        print(f"{self.name} is working as a general employee. ")

class Programmer(Employee): 
    def __init__(self, name, eid, language):
        super().__init__(name, eid)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

    def work(self):
        print(f"{self.name} is woriking as a programmer.")

class Manager(Programmer):
    def __init__(self, name, eid, language, team_size):
        # super().__init__(name, eid, language)
        Programmer.__init__(self, name, eid, language)
        self.team_size = team_size

    def manage(self):
        print(f"{self.name} is managing a team of {self.team_size} developers. ")
    
    def work(self):
        print(f"{self.name} is working as a project manager. ")

mngr = Manager('Rohan Shakya', 100, 'Python', 7)

mngr.display_info()  # Inherited from Employee
mngr.code()          # Inherited from Programmer
mngr.manage()        # Defined in Manager
mngr.work()          # Overridden in Manager