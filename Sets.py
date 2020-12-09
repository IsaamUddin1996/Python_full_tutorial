s1 = {1, 43, 345, 55, 4, 45, 79, 5, 4, 4, 4, 42, 1, }
var = type(s1)
s1.add(4343)
s1.update([3,23,343,45,6,])
s1.discard(43)
set1 = {2, 4, 5,7,6}
set2 = {4, 6, 7, 8}
set3 = {7, 8, 9, 10}

# union of two sets
print("set1 U set2 U set3 : ", set1.union(set2,set3))

set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4,6,8}

# union of two sets
print("set1 intersection set2 : ", set1.intersection(set2))
# union of three sets
print("set1 intersection set2 intersection set3 :", set1.intersection(set2,set3))
print(var)
print(s1)