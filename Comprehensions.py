ls = []
for i in range(100):
    if i%5==0:
        ls.append(i)
# print(ls)
  #------- Or in one line -------#
ls = [ i for i in range(100) if i%5==0]
# print(ls)

dict1 = {i: f"Item{i}" for i in range(1,101) if i%5==0}
print(dict1)
   # REverse the dictionary-----#
# dict1 = {i: f"Item{i}" for i in range(5)}
dict2 = {value:key for key,value in dict1.items()}
# print(dict1, "\n",dict2)

dresses = {dress for dress in ["dress1","dress2",
                               "dress1","dress2"
                               ] }
# print(dresses)

evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

# for item in evens:
#     print(item)