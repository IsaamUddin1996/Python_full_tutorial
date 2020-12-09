def funargs(normal, *args, **kwargs):  # hamesha pehle normal ya koi bhi pehle ayega phir *args aur phir *kwargs
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key, value in kwargs.items():

        print(f"{key}is a  {value}")


har = ["Sam", "Zam", "Saif", "Isaam", "Azzam"]
normal = "Iam a normal argument and the students are: "
kw = {"Saif": "Teacher",
      "Azzam": "Student",
      "Isaam": "Instructor"
      }
funargs(normal, *har,**kw )
