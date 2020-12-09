def searcher():
    import time
    #take 3 seconds to read task
    letter1 = "This is a book Psycology written by  Sir Isaam"
    letter2 = "This is a book Biology written by  Sir Zaveer"
    letter3 = "This is a book Data Base Science written by  Sir A.Q"
    letter4 = "This is a book Anatomy written by  Sir Wasay"
    letter5 = "This is a book Architecture written by  Sir Zeeshan"


    time.sleep(3)

    while True:
        text = ( yield )
        if text in letter1:
            print("It is found from letter 1")
        elif text in letter2:
            print("It is found from letter 2")
        elif text in letter3:
            print("It is found from letter 3")
        elif text in letter4:
            print("It is found from letter 4")
        elif text in letter5:
            print("It is found from letter 5")
        else:
            print("This text is not in any letter")
search = searcher()
print("Search started")
next(search)
yoursearch = input("What u want to search in letter:")
search.send(yoursearch)



