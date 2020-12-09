# class A():
#     classvar1 = "Iam a class variable in class A" #4th Check
#     def __init__(self):
#         self.var1 = "Iam inside class A's constructor"
#         # self.classvar1 = "2nd Check in instance variable of class whcih it belongs
# class B(A):       #1st check instance variable in its own class
#      classvar1 = "Iam in class B" #3rd check
#
# a = A()
# b = B()
#
# print(b.classvar1)

                      #-----For overriding-----------#
class A():
    classvar1 = "Iam a class variable in class A" #4th Check
    def __init__(self):
        self.var1 = "Iam inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
class B(A):
     classvar1 = "Iam in class B"
     def __init__(self):
         # super().__init__()  #It allow output to take special from constructor of class A if super allow here
         self.var1 = "Iam inside class B's constructor"
         self.classvar1 = "instance var in class B"
         super().__init__() #if Super allow here than constructor of A will apply for output
         print(super().classvar1)
a = A()
b = B()

print(b.special,b.classvar1,b.var1)