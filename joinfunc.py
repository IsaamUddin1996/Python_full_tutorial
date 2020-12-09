lst = ["John", "Cena", "Undertakor", "Randy", "Orton", "Saif", 'Uddin']
# for item in lst:
    # print(item, "and", end=" ")
    #This can also be written as
a = " and ".join(lst)
print(a,"Other WWE Wrestlers")
name = "Isaam"
lName = "wasif"

dict = { "Name": "Isaam",
         "Class" : "3rd",
         "Roll No." : "057"
}
b = " True ".join(dict.get("Name"))
print(b ,"Thanku")
print(dict.get("Name"))

name = "Isaam"
print("and".join(name))

doggie = "Zardari"
print("YES".join(doggie)) # ZYesaYes

