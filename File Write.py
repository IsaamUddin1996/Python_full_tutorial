#f = open("Harry2.txt","w")#default mode hota hai read isliye
#f.write("Harry is a good person")
            #How to use append mode
#f = open("Harry2.txt","a")


     #No. of characters pata karne ky liye
#a = f.write("Harry is a good person")
#print(a)
       #How to handle read and write
f = open("Harry2.txt","r+")
print(f.read())
f.write("Thank u ")

f.close()