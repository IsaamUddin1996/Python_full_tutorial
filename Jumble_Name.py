tempList = []
JumbleNameList = []

friends = int(input("Enter Number of friends"))

for i in range(friends):
    name = input(f"Enter Name of friend: ")
    splitNameList  = name.split(" ")
    print(splitNameList)
    for splittedName in splitNameList:
        tempList.append(splittedName)
        print(splittedName)

for index in range(int(len(tempList)/2)):
    JumbleNameList.append(tempList[index] + " " + tempList[len(tempList) - index - 1])
print(JumbleNameList)