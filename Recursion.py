# Recursion Error
#
# def print2(str1):
#     print2(str1)
#     print("Hi" + str1)
# print2("Sam")

# def factorial_iterative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
# Dry run
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 6 * 4 = 24
# 24 * 5 = 120


#     return fac
#
#
# def factorial_recursive(n):
#     # n = 5
#     print(n)
#     if n == 1:
#             return 1
#     else:
#         return n * factorial_recursive(n-1)
# n = 5, 5 * factorial_recursive(4) * factorial_recursive(3) * factorial_recursive(2) * factorial_recursive(1)

# number = int(input("Enter the number:"))
# print("This is iterative factorial",factorial_iterative(number))
# print("This is recursive factorial",factorial_recursive(number))


                        # Fabonacci Sequence
def fab(n):
    a = 0
    b = 1
    if n == 1:
        return (a)
    else:
        print(a)
        print(b)
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
number = int(input("Enter ur fabonacci Number:"))
fab(number)
