# def function1():
    # print("Subscribe Now")
# func2 = function1
# del function1
# func2()

def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return int
    if num == 2:
        return sum
# a = funcret(0)
# c = funcret(2)
# print(a)
# print(b)
# print(c)

def executor(func,abc):
    func("This")
    abc(3+5)
# executor(print,print)
             #--------------Decorators--------------#
def dec1(func1):
    def nowexec():
        print("Executed")
        func1()
        print("Now Executed")
    return nowexec
@dec1      #It can be wriiten as line 35
def who_is_harry():
    print("Harry is a good boy")

# who_is_harry = dec1(who_is_harry)
who_is_harry()

#One more example
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)
    return inner
div = smart_div(div)
div(2,4)