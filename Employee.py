class Employee:

    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 500

class Manager(Employee):

    def __init__(self, name, bonus):
        super().__init__(name)
        self.bonus = bonus

    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + self.bonus

class Developer(Employee):

    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

manager = Manager(name="Alice", bonus=300)
developer = Developer(name="Bob", hourly_wage=25, hours_worked=40)

print(f"Manager {manager.name}'s final salary: ${manager.calculate_salary()}")
print(f"Developer {developer.name}'s final salary: ${developer.calculate_salary()}")