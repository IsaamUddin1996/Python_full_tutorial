import pickle

#picking a python object
# cars = ["Audi","BMW","Ferrari","Toyota"]
# file = "mycar.pkl"
# fileobj = open(file,'wb') #w means to open file for writing and b means binary= wb= open file in binary
# pickle.dump(cars,fileobj)
# fileobj.close()

 #how to do depickling

file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj) #file ko return karne ky liye pickle.load use hoga
print(mycar)
print(type(mycar))

#what pickle.loads do?
