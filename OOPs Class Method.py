class Employee:
    no_of_leaves = 8
        #This function is use to give argument to Employee
    #-------It is called Constructor----------#
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
         return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}"

         # ------ Here we change no. of leaves through function we use Class method-----#

    @classmethod   #It makes a class not instance
    def change_leaves(cls,newleaves):
         cls.no_of_leaves = newleaves

harry = Employee("Harry",455,"Instructor")
rohan =Employee("Rohan",345,"Student")
# print(rohan.printdetails())
# print(harry.printdetails())

harry.change_leaves(34)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)