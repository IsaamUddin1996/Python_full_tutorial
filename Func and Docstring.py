'''a = 8
b = 9
c = sum((a , b))
print(c)'''


def function1(a, b):
    print("Hi you are in function 1", a - b)


(function1(7, 5))


def function2(a, b):
    """This is a function which will calculate avg of two no
    This func does not work with three no"""
    average = (a + b) / 2
    print(average)
    return average


v = function2(5, 7)
print(v)
print(function2.__doc__)
