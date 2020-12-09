            #--------Mapping Operators to Function---------#

class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return f"The name is {self.name}.The salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.name + other.name



    def __truediv__(self, other):
        return self.salary / self.salary

    def __repr__(self):
        return  f"Employee ('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"The name is {self.name}.The salary is {self.salary} and role is {self.role}"

    def __mod__(self, other):
        return self.salary % other.salary

    def __mul__(self, other):
        return self.salary * other.salary
emp1 = Employee("Harry",4,"Programmer")
emp2 = Employee("Rohan",4,"Student")
print(emp1+emp2)
print(emp1/emp2)
print(emp1 % emp2)
print(emp1 * emp2)
emp3 = Employee("larry",54,"Cricketer")
print(emp3)
print(repr(emp3))