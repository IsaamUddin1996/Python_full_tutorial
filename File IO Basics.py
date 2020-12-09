#File Io Basics
"""
"r" - Open file for reading - default
"w" - Open a file for writing
"x" - Creat file if not exists
"a" - add more content to a file (append )
"t" - text mode (Note Pad) - default
"b" - Binary mode (MP3 , Images)
"+" - read and write
"""
# File IO

file1 = open("Sam.txt", "wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("Write this to my file", "UTF-8"))
file1.close()
