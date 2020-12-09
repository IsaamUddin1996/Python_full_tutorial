# f = open("Harry.txt","r") # (,) ky baad ka matlab hota hai ky (mode).Ap kis mode my open krna chahte hain
# f = open("Harry.txt","rb") #(rb) means binary mode
#f = open("Harry.txt", "rt")  # (rt) means text mode which is default

#print(f.readlines())
       #To read line by line
#print(f.readline())
#print(f.readline())
#print(f.readline())

#content = f.read()
                      #Jb bhi f.read karte hain tou file pointer khali hojata hai phir agli baar kuch print nahi hoga
#for line in f:
#    print(line,end="")

         # It gives character by character reading
    # for line in content:
#    print(line)

#print(content)
# content = f.read(3)
# print(content)

#content = f.read(3)
# # print(content)
# f = open("Harry.txt")
# #print(f.tell())
# f.seek(11) #To change the position of file pointer
# print(f.tell()) #tell the position of file pointer
# print(f.readline())
#print(f.tell())
#f.seek(11)
# print(f.readline())
#print(f.tell())

                        #Wtih  block
with open("Harry.txt") as f:
    a = f.readlines()
    print(a)
f = open("Harry.txt","rt")
print(f.readline())

f.close()
