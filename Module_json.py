import json
data = '{"var1":"harry","var2":"56"}'
print(data)
parsed = json.loads(data)
print(parsed)
print(parsed['var1'])

#--json.load is use to open files--------#
#--json.loads use to read data----#

data2 = {"channel name":"code with harry",
         "cars":['BMW','ferrari','Audi a8'],
         "fridge":('roti',432),
         "boolean":False
         }
jscomp = json.dumps(data2)
print(jscomp)
#------json.dumps changes the python into JAVA --#
#u can see that in Python F is capital in False but in Java F is small

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
