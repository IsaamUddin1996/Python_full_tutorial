  #Lambda Function
# def add(a,b):
#     return a + b
# minus = lambda x , y: x - y
# print(minus(9,6))
# def minus(a, b):
#     return a - b
# print(minus(9,4))

def a_first(array):
    return array[2]

b = [[10, 1,3],[9, 603,7],[82, 2,10]]
a = [[1, 14,5],[9, 6,23],[8, 23,56]]
a.sort(key=a_first)
b.sort(key=a_first)
print(a)
print(b)

def nameFunc():

    x = 10
    y = 89
    z = x * y
    return "saif"

name = nameFunc()
print(name)

a = [[2, 4],[5, 8], [10, 1]]
a.sort(key= lambda x:x[1])
print(a)