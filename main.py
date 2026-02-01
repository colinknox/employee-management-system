class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name} earns ${self.salary}"
    
    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_team_info(self):
        return f"{self.name} manages {self.team_size} employees"



emp = Employee("Alice", 50000)
print(emp.get_info())  # Alice earns $50000
emp.give_raise(5000)
print(emp.get_info())  # Alice earns $55000

mgr = Manager("Bob", 75000, 10)
print(mgr.get_info())       # Bob earns $75000 (inherited!)
print(mgr.get_team_info())  # Bob manages 10 employees
mgr.give_raise(10000)       # Inherited method!
print(mgr.get_info())       # Bob earns $85000