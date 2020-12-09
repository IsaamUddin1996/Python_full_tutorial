import pygame as py
from datetime import datetime
import time
i = 1
while i < 4:
    print("Drink Water")
    print(i)
    py.mixer.init()
    py.mixer.music.load('Ring10.wav')
    py.mixer.music.play(-1)
    Userinput = input("Done?")
    if Userinput == "Drank":
        py.mixer.music.stop()
        print("No. of glasses left: ", 15 - i)
    while py.mixer.music.get_busy():
        py.time.Clock().tick(10)
    write_file = open("water.txt", "a")
    write_file.write(f"You Drank water at {datetime.now()}\n")
    write_file.close()
    time.sleep(1)
    i += 1
