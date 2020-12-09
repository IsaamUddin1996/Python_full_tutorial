# Take age or year or birth as an input from the user and tell them when they will turn 100 years old.
# (5 points) Don’t use any type of module like datetime or dateutils(-5 points).
# They can then optionally provide a year and your program must tell their age in that particular year.
# (3 points) You should be handling all sorts of errors like (2 points):
#     You are not yet born
#     You seem to be the oldest person alive
#     You can also handle any other error if possible!

userinput = int(input("For particular year press 1 or for know when u will 100 press 2 : "))
if userinput == 2:
    age = input("What is your age/Year of birth: ")
    if age.isalpha():
        raise Exception("Alphabets are not allowed")
    elif int(age) == 0:
        raise ZeroDivisionError("You are not born yet")
    elif len(age) > 4:
        print("Invalid input")
    elif len(age) == 3:
        if int(age) <= 150:
            print(f"You was 100 years old {int(age) - 100} before ")
        elif int(age) > 150:
            print("You are the oldest person on earth")
    elif len(age) == 2:
        print(f"You will turn 100 after {100 - int(age)} years")
    elif len(age) == 4:
        if int(age) < 1950:
            print("You have put wrong year of birth or you are alien")
        elif int(age) > 2020:
            print("You are not born yet")
        else:
            print(f"You will turn 100 in year {int(age) + 100}")
elif userinput == 1:
    born_year = input("Enter Your Birth Year: ")
    if born_year.isalpha():
        raise Exception("Alphabets are not allowed")
    elif int(born_year) == 0:
        raise ZeroDivisionError("You are not born yet")
    particular_year = input("Which year do you want to know your age")
    if particular_year.isalpha():
        raise Exception("Alphabets are not allowed")
    elif int(particular_year) == 0:
        raise ZeroDivisionError("You have put wrong year")
    print(f"Your age will be {int(particular_year) - int(born_year)}")
