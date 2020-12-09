# Creat a function which takkes input
# takes path from input
# After taking path print files of that Path
# takes file name from input
# takes the format (jpg)
# Capitiliaze all the files in C Folder not the folders
# Gives no. to jpg files
# Capitiliaze all the words which after full stop of the folder of the Path Folder

import os
print(dir(os))
def soldier(path,file,format):
    n = input("Write your Path")
    print(os.getcwd())
    os.chdir(n)
    print(os.getcwd())
    print(os.listdir(n))
soldier()