
# Creat a lib class
# 1st func = Display all books
# 2nd func = lend book (who owns the book if it is not in the library
# 3rd func = add book
# 4th func = Return book

# -----Extracurricular activities

# Maintain a dictionary for library..
class Samlibrary:

    def __init__(self, library):
        self.library = library

    def display(self):
        return f"This is your library {self.library}"

    def lendbook(self):
        print(f"{self.library}")
        userinput = input("lend a book")
        if userinput not in self.library:
            return "It is not in the library"
        else:
         self.library.remove(userinput)
         return f"You lend this book {userinput} This is your library {self.library}"

    def addbook(self):
        userinput = input("add a book")
        if userinput  in  self.library:
            return "It is already in the library"
        else:
         self.library.append(userinput)
         return f"You add this book {userinput} This is your library {self.library}"

    def returnbook(self):
        userinput = input("Return the book")
        self.library.append(userinput)
        return f"You return this book {userinput} This is your library {self.library}"

Isaam = Samlibrary(["Hobbit", "Harry Potter", "Lord of the Rings", "Hope", "Old Days"])

while True:

   name = input("Enter Your name")

   choice = input(f"Enter What You want to do {name}  wtih your library:")
   if choice == "add":
       print(Isaam.addbook())
   elif choice == "display":
       print(Isaam.display())
   elif choice == "lend":
       print(Isaam.lendbook())
   elif choice == "return":
       print(Isaam.returnbook())
   else:
       print("Turn back to your Home")

   dict = {"Name": name,}
   n = int(input("How Many Books do u need?"))
   i = 1
   for i in range(n):
       k = input(f"Enter Book no.")
       v = input(choice)
       dict.update({"Book"+k:v})
   print(dict)