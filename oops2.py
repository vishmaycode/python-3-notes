class Employee:
    noofl = 8
    pass


harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 45500
harry.role = "instructor"
rohan.name = "Rohan"
rohan.salary = 90000
rohan.role = "CEO"

print(harry.name, harry.salary, harry.role)
print(rohan.name, rohan.salary, rohan.role)
print(harry.noofl, rohan.noofl, Employee.noofl)
print(rohan.__dict__)
# Employee.noofl = 9
rohan.noofl = 9
print(Employee.noofl)
print(rohan.__dict__)