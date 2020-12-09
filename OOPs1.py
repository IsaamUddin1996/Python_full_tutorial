#class-template
#object-instance
class Student():
    pass #It does nothing but class need something
harry = Student()
larry = Student()
#instance variable
harry.name = "Harry"
harry.std = 1
harry.sec = "B"

larry.std = 2
larry.subjects = ["Physics", "Chemistry"]
print(harry.std,larry.subjects)