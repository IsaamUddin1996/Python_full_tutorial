# # import numpy as np
# # x = np.float32(1.5)
# # print(x)
# # y = np.int_([1,2,4])
# # print(y)
# # v = np.array([3,4,43,2,1])
# # print(v)
#
# yearAge = int(input("What is your Age/Year of birth\n"))
# isAge = False
# isYear = False
#
# if len(str(yearAge)) == 4:
#     isYear = True
#
# else:
#     isAge = True
#
# if(yearAge<1900 and isYear):
#     print("You seem to be the oldest person alive")
#     exit()
#
# if(yearAge>2019):
#     print("You are not yet born")
#     exit()
#
# if isAge:
#     yearAge = 2019 - yearAge
#
# print(f"You will be 100 years old in {yearAge + 100}")
#
# interestedYear = int(input("Enter the year you want to know your age in\n"))
#
# print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")
#


def abc():
    return "abc"

def xyz():
    print("xyz")

n = abc()
j = xyz()

print(n)
print(j)