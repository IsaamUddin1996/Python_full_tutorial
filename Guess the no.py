# Guess the no
'''n = 18
m = int(input())
if(m == n):
     print("You win")
elif(m>n):
    print("decrease your no")
else :
     print("increase your no")'''

i = 0
n = 18
while (i < 9):
    m = int(input("Enter ur value"))

    if (m == n):
        print("You win")
        print("You guess the no in turns:", i + 1)
        break
    elif (m > n):
        print("Decrease ur value")
    else:
        print("increase your value")
    i = i + 1

if (i == 9):
    print("Game over")
else:
    print("your remaining turns", 9 - i)
