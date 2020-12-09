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

Sam = Employee("Isaam","Uddin")

#Property ki wajah se email ky baad () nahi lagenge
print(Sam.email)

Sam.fname = "Saif"
#Property ki wajah se email ky baad () nahi lagenge
print(Sam.email)
#Ye kaam krne ky liye Setter apply krte hain.
#Hum chah rhe hain ky jese hi Email chng ho touf.name aurl.name bhi chng hojaen
Sam.email = "This.that@codewithharry.com"
#After applying Setter
print(Sam.lname)

#To delete in OOPs we use deleter decorator [line 23]
del Sam.email
print(Sam.email)

Sam.email = "Isaam.Azzam@codewithharry.com"
print(Sam.email)