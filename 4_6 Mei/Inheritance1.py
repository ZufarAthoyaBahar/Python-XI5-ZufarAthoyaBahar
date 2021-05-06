class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True

# Drier code
emp = Person("Joni") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Nawan") # An Obkect of Employee
print(emp.getName(), emp.isEmployee())