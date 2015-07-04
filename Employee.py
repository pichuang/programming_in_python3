__author__ = 'root'


class Employee(object):

    COUNT = 0

    def __init__(self, name, salary):
        print("Class name: {class_name}".format(class_name=type(self).__name__))
        self.name = name
        self.salary = salary
        Employee.COUNT += 1

    def displayCount(self):
        print("Total employee {0}".format(Employee.COUNT))

    def displayEmployee(self):
        """
        Test ok
        """
        str = "Name: {0}, Salary: {1}".format(self.name, self.salary)
        return str

class SuperEmployee(Employee):

    def __init__(self, name, salary):
        print("Class name: {class_name}".format(class_name=type(self).__name__))
        self.name = name
        self.salary = salary
        SuperEmployee.COUNT += 1

    def displayCount(self):
        print("Total Super employee {0}".format(SuperEmployee.COUNT))

    def displayEmployee(self):
        """
        Test ok
        """
        str = "Super Name: {0}, Salary: {1}".format(self.name, self.salary)
        return str


emplyee_list = []
emp1 = Employee("pichuang", 5000)
emplyee_list.append(emp1)
emp2 = Employee("free", 6000)
emplyee_list.append(emp2)

print("\n")
for emp in emplyee_list:
    print("Display: {display}".format(display=emp.displayEmployee()))

print("emp Count: {count}{nex}".format(count=Employee.COUNT))

emplyee_list = []
emp1 = SuperEmployee(name="pichuang", salary=5000)
emplyee_list.append(emp1)
emp2 = SuperEmployee(name="free", salary=6000)
emplyee_list.append(emp2)
print("\n")

for emp in emplyee_list:
    print("Display: {display}{nextline}".format(display=emp.displayEmployee(), nextline="\n"))

print("emp Count: {count}".format(count=SuperEmployee.COUNT))
