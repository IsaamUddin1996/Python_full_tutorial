import pygame as py
import time
initial_time = time.time()
i = 1
while i < 10:
    print("Do Pushups")
    print(i)
    py.mixer.init()
    py.mixer.music.load('Ring10.wav')
    py.mixer.music.play(-1)
    userInput = input("Have you done your exercise? ")
    if userInput == "ExDone":
        py.mixer.music.stop()
        print("Exercises left: ", 14 - i)
    while py.mixer.music.get_busy():
        py.time.Clock().tick(10)
    write_file = open("Exer.txt", "a")
    write_file.write(f"You have Done Exercise {time.asctime(time.localtime(time.time()))}\n")
    write_file.close()
    time.sleep(3)
    i += 1

final_time = time.time()
print("You drank water in: ", final_time - initial_time)
