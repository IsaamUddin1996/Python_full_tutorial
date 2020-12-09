class Employee:
    no_of_leaves = 8
        #This function is use to give argument to Employee
    def __init__(self,aname,asalary,arole): #it is called constructor
        self.name = aname
        self.salary = asalary
        self.role = arole
    # def printdetails(self):
    #     return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}"
harry = Employee("Harry",455,"Instructor")
# rohan =Employee()
# rohan.role = "Student"
# rohan.salary = 322
# rohan.name = "Rohan"
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
# print(rohan.printdetails())
# print(harry.printdetails())
print(harry.name)