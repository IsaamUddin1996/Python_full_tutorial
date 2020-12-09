# execute same program using while loop
# i = 1
# while (i < 5):
#     j = 0
#     while (j < 5 - i):
#         print(j, end="")
#         j = j - 1
#
#     print()
#     i = i + 1
userInput = int (input())

def trueFunction():
    for i in range(1, 5):
        for j in range(0, i):
            print("*", end="")
        print("")


def falseFunction():
    for i in range(1, 5):
        for j in range(0, 5 - i):
            print("*", end="")
        print("")