import pygame as py
import time
initial_time = time.time()
i = 1
while i < 16:
    print("Take relax for Eyes")
    print(i)
    py.mixer.init()
    py.mixer.music.load('abc.ogg')
    py.mixer.music.play(-1)
    Userinput = input("Done?")
    if Userinput == "EyDone":
          py.mixer.music.pause()
          print("No. of Exercises left: ", 16 - i)
    while py.mixer.music.get_busy():
        py.time.Clock().tick(10)
    Userinput = input("Done?")
    write_file = open("Exer.txt", "a")
    write_file.write(f"You relax ur Eyes at {time.asctime(time.localtime(time.time()))}\n")
    write_file.close()
    time.sleep(1)

    i += 1
final_time = time.time()
final_time =print("You drank water in: ", initial_time - final_time)