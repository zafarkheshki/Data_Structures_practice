# Properties of getters and setters

class SoftwareEngineer():
    
    def __init__(self):
        self._salary = None
       
    # getter
    @property
    def salary(self):
        return self._salary

    # setter
    @salary.setter
    def salary(self, value):
        self._salary = value


se = SoftwareEngineer()

se.salary = 600000
print(se.salary)

# Recap
# encapsulation
# abstraction
# public, private
# _foo(), _x
# getter and setter
# getter -> @property
# setter -> @name.setter