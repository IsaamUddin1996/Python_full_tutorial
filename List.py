# Lists

colleges = ['IIT', 'NIT', 'College of engineering']

print(colleges[2])

colleges[2] = "COE"

print(colleges[2])
print(colleges)
print(colleges[1:3])
list2 = ['table', 'chair', 'fan', 'clothes', 'bottle']

# list2.append('microphone')
list2.insert(3, 'microphone')
print(list2)
list2.remove('microphone')
print(list2 + ['pillow', 'tubelight', 'bed'])
print(list2)
print(len(list2))
print(max(list2))
print(min(list2))

list1 =[[1,2,3], [4,5,6], [7,8,9]]
for item in list1:
    for i in item:
        print(i)
