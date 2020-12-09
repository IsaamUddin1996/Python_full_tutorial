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

         # ------ Here we change no. of leaves through function we use Class method-----#

    @classmethod   #It makes a class not instance
    def change_leaves(cls,newleaves):
         cls.no_of_leaves = newleaves
        #------------CLass Alternative Method-----------#
        #-------- To made an object through String-------#
    @classmethod
    def from_dash(cls,string):
        # params = string.split("-") #Split makes a string into list
        # print(params)
        # return cls(params[0],params[1],params[2],params[3])
                 #For one liner------
        return cls(*string.split("-"))
harry = Employee("Harry",455,"Instructor","Hey")
rohan =Employee("Rohan",345,"Student","Bye")
karan = Employee.from_dash("Karan-459-Worker-hi")

print(karan.no_of_leaves)