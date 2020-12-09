#How many items required
#Run a for lopop
#What comprehension do you required= List,Dictionary,sets

n = int(input("How many loops do you required:"))
which_comprehension = input("Which Comprehension do you required")

print(which_comprehension)
if which_comprehension == "list":
    m = int(input("From whcih no do you need:"))
    ls = [i for i in range(n) if i % m == 0]
    print(ls)

elif which_comprehension == "dictionary":
    item = input("What Item do u required")
    dict1 = {i: f"{item}{n}" for i in range(n)}
    print(dict1)
elif which_comprehension == "sets":
    m = input("Which item do you need in your set")
    dresses = {n for n in [f"{m}",f"{m}",f"{m}"]}
    print(dresses)