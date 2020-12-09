 #--- Object Introspection means where the object came from,from which class,which type-----#

class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property  #Ye lagane ki wajah se Print ko as a function use krne ki zarorat nahi parti means(Print main () lagane ki zarorat nahi hai)
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set.Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("Setting Now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf = Employee("Skill","F")
print(skillf.email)
print(type("This is string"))
print(id("This is string"))
#dir gives us what methods are define in ex:Skillf
print(dir(skillf))
o = Employee("Hi","ewe")
import inspect
print(inspect.getmembers(skillf))

