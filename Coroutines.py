def searcher():
    import time
    #take 3 seconds to read task
    book = "This is a book Psycology written by  Sir Isaam"
    time.sleep(3)

    while True:
        text = ( yield )
        if text in book:
            print("Text in the book")

        else:
            print("Text is not in the book")

search = searcher()
print("Search started")
next(search)
search.send("Psycology")
search.send("Isaam")
yoursearch = input("What u want to search:")
search.send(yoursearch)



