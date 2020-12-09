'''d1 = ()
print(type(d1))
d2 = []
print(type(d2))
d3 = {}
print(type(d3)'''

'''d1 = {"Harry": "Burger", "Rohan": "Roti","Azzam":"khechri",
     "Saif":{"B":"Juice","L":"daal","D":"Biryani"} }
print(d1["Saif"]["D"])
#If some client are not satisfied so u can also add them in the dictionary
d1 ["Monis"] = "Mouse"
d1 [420] = "Cockroach"
print(d1)
#del d1[420]
#print(d1)
#d3 = d2.copy()
#print(d1.get("Harry"))
d1.update({"Nabiha":"Chicken"})
print(d1)
print(d1.keys())
print(d1.items())'''
                              #Task
#Creat ur dictionary and take input from user
d1 = {
    "Name" : "Isaam",
    "Class": "3rd Sem",
    "Birthday": "18-Nov-1996"
}
# key = input("Enter what u want  "  ) #Key use as a variable
# value = d1.get(key) #Value use as a variable
# d1.update({"Name":"Azzam"})
# print(value)
# print(d1[key])

# d1 = {
#     "Name" : "Isaam",
#     "Class": "3rd Sem",
#     "Birthday": "18-Nov-1996"
# }
# key = input("Enter what u want  "  ) #Key use as a variable
#  #Value use as a variable
# print(d1[key])

#          +--------Build Your own dictionary-----------+

a ={}

n = int(input("enter no. of elements"))
for i in range(n):
    k = input("Enter key:")
    v = input("Enter Value")
    a.update({k:v})
print(a)

# Dictionaries

names = {'Harry': 22,
         'Shubham': 41,
         'Jyoti': 19,
         'Ramdev': 82}

print(names['Ramdev'])
names['Ramdev'] = 55
print(names['Ramdev'])

print(names.keys())
print(names.values())

