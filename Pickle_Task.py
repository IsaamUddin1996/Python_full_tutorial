# uci ml repository//Data Sets//Iris//download data Folder(Up left)//take iris.data and iris.names/
# take iris.data not iris.name/take link and save into text file//then split or parsed
# then make a list then pickle it and code the read(2:00)
# Read the pickle
#Use Pickle
#Use requests


import pickle
import requests
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
response = requests.get(url)
irisDataText = response.text
irisDataList = irisDataText.splitlines()

irisDataList.pop()
irisDataList.pop()
print(irisDataList)


# file = "irisDataList.pkl"
# fileobj = open(file,'wb') #w means to open file for writing and b means binary= wb= open file in binary
# pickle.dump(irisDataList,fileobj)
# fileobj.close()
#
#  #how to do depickling
#
# file = "irisDataList.pkl"
# fileobj = open(file,'rb')
# mycar = pickle.load(fileobj) #file ko return karne ky liye pickle.load use hoga
# print(mycar)
