def takeNameOfUser(name):
    retrieveOrlog = input("What do u want to do?,Retrieve or log?")
    if retrieveOrlog == "1":
        retrieve(name)
    elif retrieveOrlog == "2":
        log(name)

def retrieve(name):
    print("retrieve of", name)
    userinput = input("What do u want to do?Diet or Excercise?")
    if userinput == "1":
        diet(name,"retrieve")
    elif userinput == "2":
        exercise(name,"retrieve")

def log(name):

    userinput = input("What do u want to do?Diet or Excercise?")
    if userinput == "1":
        diet(name,"log")
    elif userinput == "2":
        exercise(name,"log")

def diet(name,fromWhere):
    if fromWhere == "log":
        writeFile(name,"diet")
    elif fromWhere == "retrieve":
        readFile(name,"diet")

def exercise(name,fromWhere):
    print("Crossbar")
    if fromWhere == "log":
        writeFile(name,"exercise")
    elif fromWhere == "retrieve":
        readFile(name,"exercise")

def writeFile(name,whichFile):
    time = getdate()
    if whichFile == "exercise":
        if name == "Sam":
            print("Write ur file for exercise for Sam")
            userInput = input("Enter exercise: ")
            f = open("SamExercise.txt", "a")
            f.write("[ " + str(time) + " ]" + userInput + "\n")
            f.close()

        elif name == "Zam":
            print("write ur file for exercise Zam")
            userInput = input("Enter exercise: ")
            f = open("ZamExercise.txt", "a")
            f.write("[ " + str(time) + " ]" + userInput + "\n ")
            f.close()

        elif name == "Saif":
            userInput = input("Enter exercise: ")
            f = open("SaifExercise.txt", "a")
            f.write("[ " + str(time) + " ]" + userInput +  "\n ")
            f.close()


    elif whichFile == "diet":
        if name == "Sam":
            userInput = input("Enter Diet: ")
            f = open("SamDiet.txt", "a")
            f.write("[ " + str(time) + " ]" + userInput + "\n ")
            f.close()


        elif name == "Zam":
            userInput = input("Enter Diet: ")
            print("write ur file for diet Zam")
            f = open("ZamDiet.txt", "a")
            f.write("[ " + str(time) + " ]" + userInput + "\n ")
            f.close()

        elif name == "Saif":
            print("write ur file for diet Saif")
            userInput = input("Enter Diet: ")
            f = open("SaifDiet.txt", "a")
            f.write("[ " + str(time) + " ]" + userInput + "\n")
            f.close()


def readFile(name,whichFile):
    if whichFile == "exercise":
        if name == "Sam":
            f = open("SamExercise.txt","r")
            print(f.read())
            f.close()
        elif name == "Zam":
            f = open("ZamExercise.txt", "r")
            print(f.read())
            f.close()
        elif name == "Saif":
            f = open("SaifExercise.txt", "r")
            print(f.read())
            f.close()

    elif whichFile == "diet":
        if name == "Sam":
            f = open("SamDiet.txt", "r")
            print(f.read())
            f.close()
        elif name == "Zam":
            f = open("ZamDiet.txt", "r")
            print(f.read())
            f.close()
        elif name == "Saif":
            f = open("SaifDiet.txt", "r")
            print(f.read())
            f.close()

def getdate():
    import datetime
    return datetime.datetime.now()


nameOfUser = input("Enter name: ")
takeNameOfUser(nameOfUser)

# Programming Principles :
# DRY = Don't Repeat Yourself'
