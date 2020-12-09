import random

# it gives integer no
random_number = random.randint(0, 10)
# print(random_number)
# It gives no
rand = random.random() * 100
# print(rand)

lst = ["Isaam", "SAif", "Sam", "Azzam", "Zam"]
choice = random.choice(lst)
# print(choice)

import sklearn
import time

seconds = time.time()
# print("Seconds since  epoch",seconds)
# time.sleep(3)
# print("This is printed immediately")
# time.sleep(2.4)
# print("This is printed after 2.4 seconds")

initial = time.time()
i = 0
# while i < 20:
    # print("This is Isaam")
    # i += 1
    # print("While loop ran in: ", time.time() - initial , "Seconds")
initial2 = time.time()
# for i in range(20):
# print("This is Sam")
# print("For Loop ran in: ", time.time() - initial2)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)
