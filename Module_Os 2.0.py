import os
# print(os.getcwd())
# os.mkdir('movies')
# os.makedirs('movies/ironman')
# print(os.path.exists('movies/ironman'))
# if os.path.exists('movies'):
#     print('It is already exists')
# else:
#     os.mkdir('movies')
# print(os.listdir(r"C:\Isaam Halqa"))
   #+++++= To know path of every folder+++++++#
# for item in os.listdir(r'C:\Isaam Halqa'):
#     path = os.path.join(r'C:\Isaam Halqa' ,item)
#     print(path)

#++ To get depth of a Path++++++=#
# fileiter = os.walk(r'C:\Isaam Halqa')
# for current_path,folder_names,filenames in fileiter:
#     print(f'current path: {current_path}')
#     print(f'folder names: {folder_names}')
#     print(f'file names: {folder_names}')
# os.chdir(r'C:\Isa/)
#+++++==it only delete an empty folder
# os.rmdir('new')


# +++++ To delete a folder having folder/files we use:
import shutil
# os.chdir('C:\Isaam Halqa')
# shutil.rmtree(path)

# Note : Be carefull because it deletes permanently which means it not gives the file to recycleBin


# How to copy a folder and paste into another folder:
# shutil.copytree('new','Bazm Forms/new(new ky sath kuch bhi lekhenge tou rename hojayega folder')
os.chdir('C:\Isaam Halqa')
# shutil.copy('file.txt','new/file321.txt')
# shutil.move('file.txt','new/file.txt')
shutil.move('new2','new/new3')