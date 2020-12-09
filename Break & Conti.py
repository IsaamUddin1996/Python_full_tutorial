'''i=0
while(i<45):
    print(i+1 , end=" ")
    i = i + 1'''
'''i=0
while(True):
    print(i+1 , end=" ")
    if(i==44):
        break #Stop the loop
    i = i + 1'''

'''i=0
while(True):
    if i+1<5:
        i = i + 1
        continue
    print(i+1 , end=" ")
    if(i==44):
        break #Stop the loop
    i = i + 1'''


'''i = int ( input("Enter ur no"))
if(i<100):

   while(i<100):
       i = i + 1

       print(i)
       continue

   else:
        print("Break")'''

userInput = int (input("Enter a number on which you want to execute a loop: "))
while(userInput < 100):
    print(userInput)
    userInput = userInput +  1

