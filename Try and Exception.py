# print("Enter num 1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
    # print("The sum of these two no is :",
    #       int(num1) + int(num2))
# except Exception as e:
    # print(e)

# print("This line is very important")

f1 = open("water.txt")

try:
    f = open("hehe.txt")
    print("it is try")
# except Exception as e:
#     print(e)
#     print("It is exception")
except EOFError as e:
    print("Print EOF error",e)
except IOError as e:
    print("Print Io Error",e)
else:
    print("This will only run if except does not run")
finally:
    print("Run this anyway")
    # f.close()
    f1.close()
