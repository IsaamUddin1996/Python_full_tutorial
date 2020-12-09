abc = [9,8,7,6,5,4,3,2,1]
(abc.reverse())
print(abc[::-1])
print(abc)
b = abc[0]
abc[0] = abc[8]
abc[8] = b

b = abc[1]
abc[1] = abc[7]
abc[7] = b

b = abc[2]
abc[2] = abc[6]
abc[6] = b

b = abc[3]
abc[3] = abc[5]
abc[5] = b

#i = 0, 1, 2, 3
#n = 8 ,7 ,6 ,5
for i in range(int(len(abc)/(2))):
    n = int(len(abc)) - 1  #n = 8
    n -= i
    # print(n)
    b = abc[n]
    abc[n] = abc[i]
    abc[i] = b
print(abc)
