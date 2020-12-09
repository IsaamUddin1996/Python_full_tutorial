#45*3 = 555 , 56+9 = 77 , 56/6 = 4

print("Enter Your first no")
num1 = int(input())
print("Enter your second no")
num2 = int(input())
print("enter your operator")
operator = input()

if num1 == 45 and num2 == 3 and operator == "*":
    print("555")
elif num1 == 56 and num2 == 9 and operator == "+":
    print("77")
elif num1 == 56 and num2 == 6 and operator == "/":
    print("4")
elif operator=="*":
    num4= num1*num2
    print(num4)
elif operator=="+":
    num4= num1+num2
    print(num4)
elif operator=="/":
    num4 = num1/num2
    print(num4)
elif operator=="%":
    num4 = num1%num2
    print(num4)
else:
    print("Unexpected Error")