class Employee:
    no_of_leaves = 8
    pass
harry = Employee()
rohan = Employee()
harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"
rohan.role = "Student"
rohan.salary = 322
rohan.name = "Rohan"

print(harry.name)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
Employee.no_of_leaves = 20
print(Employee.no_of_leaves)
print(rohan.no_of_leaves)

rohan.no_of_leaves = 14 #Instance variable
print(rohan.no_of_leaves)

print(rohan.__dict__)
print(harry.__dict__)
print(Employee.__dict__)