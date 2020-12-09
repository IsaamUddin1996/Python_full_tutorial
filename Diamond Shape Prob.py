class A():
    def met(self):
        print("This is a method from classs A")
class B(A):
    def met(self):
        print("This is a method from classs B")
class C(A):
    def met(self):
        print("This is a method from classs C")
class D(B,C):
    def met(self):
        print("This is a method from classs D")
a = A()
b = B()
c = C()
d = D()

d.met()