a = input("What is your name")
b = int(input("How much do you earn?"))
if b == 0:
    raise ZeroDivisionError("b is 0 so stopping the program")
if a.isalnum():
    #Agr program lengthy hai aur user start my hi naam ki jagah no. dal de tou usko yahen rook do
    raise Exception ("Numbers are not allowed")
# print(f"Hi {a}")

# c = input("Enter your name")
# try:
    # print(d)
# except Exception as e:
    # if c == "Sam":
    #     raise ValueError("Sam is blocked he is not allowed")
    # print("Exception handle")