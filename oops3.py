# methods

# class Employee:
#     noofl = 8
#
#     Employee
#
#     def printdet(self):
#         return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"
#
#
# harry = Employee()
# rohan = Employee()
#
# harry.name = "Harry"
# harry.salary = 45500
# harry.role = "instructor"
# rohan.name = "Rohan"
# rohan.salary = 90000
# rohan.role = "CEO"
#
# print(rohan.printdet())

# constructor


class Employee:
    noofl = 8

    def __init__(self, aname, asalary, arole):          #constructor
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdet(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}"


harry = Employee("Harry", 45000, "instructor")
rohan = Employee("rohan", 90000, "ceo")

print(harry.printdet())