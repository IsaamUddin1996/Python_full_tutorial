m = int(input("Enter number to multiply"))
min = int(input("Enter your min range"))
max = int(input("Enter your max range"))
table_list = []
table_list2 = []

for i in range(min, max + 1):
    v = m * i
    c = m * i
    table_list2.append(c)
    if m == 6 or m == 5:
        if i == 5:
            v += 1
            table_list.append(v)
            print(table_list)
        else:
            table_list.append(v)
    else:
        table_list.append(v)
print(table_list)
print(table_list2)
if table_list == table_list2:
    print("Done")
else:
    print("There is a error")




for index in range(len(table_list2)):
    # print(index)
    if table_list[index]  != table_list2[index]:
        print(index)
