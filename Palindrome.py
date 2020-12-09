a = input("Enter number you want to palindrome: ")
b = ""
flag = True
while (flag):
    for i in range(len(a)):
        n = int(len(a)) - 1
        n -= i
        b += a[n]
    if int(a) < 10:
        print("You have put less than 10 number")
        flag = False
    elif a == b:
        print("a is palindrome")
        flag = False
    else:
        b = ""
        a = int(a) + 1
        a = str(a)
        print(a)

# a = saif
# b = fias

# a = input("Enter number you want to palindrome: ")
# for i in range(int(len(a)/2)):
#     print(i)
#     print("Gap")
#     print(a)
#     if(a[i] == a[len(a) - 1 - i]):
#         print("Gap111")
#         print(a)
#         print("is palindrome")
#     else:
#         print("is not palindrome")
#         break
