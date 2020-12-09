#Creat a list and print only numbers which are greater than 6

list = ["Merry",2,4,7,1,8,9,"Harry"]
for r in list:
    if str(r).isnumeric() and r>6:
        print(r)
    #if type(r) is int:
     #   if r > 6:
      #     print(r)
