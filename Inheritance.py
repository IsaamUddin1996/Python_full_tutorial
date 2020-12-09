class Employee:
    no_of_leaves = 8
        #This function is use to give argument to Employee
    def __init__(self,aname,asalary,arole,ahi):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.he = ahi
    def printdetails(self):
         return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}"

    @classmethod   #It makes a class not instance
    def change_leaves(cls,newleaves):
         cls.no_of_leaves = newleaves
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good" + string)

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,ahi,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.he = ahi
        self.languages = languages
    def printprog(self):
        return f"Name is {self.name}. Salary is {self.salary}. and role is {self.role}.The languages are {self.languages}"


harry = Employee("Harry",455,"Instructor","Hey")
rohan =Employee("Rohan",345,"Student","Bye")
karan = Programmer("Karan",555,"Programmer","Hoho",["Python","Cpp"])
Sam = Programmer("Isaam",777,"Programmer","Hehe",["Java"])

print(karan.printprog())
print(Sam.printprog())