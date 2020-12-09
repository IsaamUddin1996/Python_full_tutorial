data = ["You are a good writer You","You have successfully pass this test","You got the talent","You are in your own",
        "the test was easy for you","the test has 5 questions","You the test is now being started are","test is easy test",]
dictionary = {}


# d = {'key': 'value'}
# print(d)
# {'key': 'value'}

# print(d)
# {'key': 'value', 'mynewkey': 'mynewvalue'}
x = {}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
for items in data:
        d = items.count("are")
        c = items.count("You")
        if c+d > 0:
                dictionary[items] = c+d
print(dictionary)
sort =(sorted(dictionary.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
print(sort)
#
#
#
#
# print(dictionary.items())
# answer = []
# final_answer = []
# # n =input("Enter search")
# for items in data:
#         d = items.count("are")
#         c = items.count("You")
#         answer.append( c + d )
#         h =dictionary.items()
# print(answer)
# for index in range(len(answer) - 1):
#         print(answer[index])
#         print("gap")
#         print(data[index])
#         if(answer[index] != 0):
#                 final_answer.append(data[index])
#
# print(final_answer)