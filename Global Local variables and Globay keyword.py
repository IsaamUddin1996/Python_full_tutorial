# Global and Local Variables

# l = 10 #Global Variable (Govt.)
# def func1(n):
#     l = 5 #Local Variable (Personel)
#     global l #ab aap global variable ko func main use karsakte hain
#     l = l + 5 #agr yahan pr local variable (l) nahi  hoga tou ye error dedega.q k ap global variable kesath chir char nahi karsakte
#     m = 8
#     print(n,"Sam")
#     print(l,m)
# func1("Hi")
#
# print(l)
x = 89 #global
def harry():
    #global x
    x = 20
    print("Harry")

    def rohan():
        print("Rohan")
        global x  # ye nested func wala global pechle func my sy nahi balke func ky bahar jakar dhondega variable
        x = 88
        print("After assigning global", x) # 88

    print("Before calling rohan()", x) # 20
    rohan()
    print("After calling rohan()", x) # 20

print(x) #89
harry()
print(x)  # ye global x ki wajah se bahar aik x = 88  bana lega
