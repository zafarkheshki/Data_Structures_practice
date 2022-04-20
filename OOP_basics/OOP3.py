# Inheritance

# Inherit, extend and override
class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working .....")


class SoftwareEngineer(Employee):                   # Inheritance
    
    def __init__(self, name, age, level, salary):   # Extending
        super().__init__(name, age, salary)
        self.level = level
    
    def work(self):
            print(f"{self.name} is coding .....")   # Overriding

    def debug(self):
        print(f"{self.name} is debugging .....")

class Designer(Employee):
    
     def work(self):
            print(f"{self.name} is designing .....")  # Overriding

     def draw(self):
        print(f"{self.name} is drawing .....")


se = SoftwareEngineer("Zafar", 30, 7000, "Senior")
# print(se.name)
# print(se.age)
# se.work()
# se.debug()

d = Designer("Khan",26, 5000)
# print(d.name, d.age)
# d.work()
# d.draw()


# Polymorphism
employees = [SoftwareEngineer('Max', 27, 7000, 'Senior'),
            SoftwareEngineer('Jia', 23, 4500, 'Junior'),
            Designer('Anna', 28, 6000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)


# Recap
# inheritance: ChildClass(BaseClass)
# inherit, extend, override
# super().__init__()
# polymorphism