'''Operators in Python
Arithmetic operator
Assignment operator
Comparison operator
Logical operator
Identity Operator
Membership operator
Bitwise operators'''

# Arthematic Operators
print("Arthematic operators")
print("5 + 6 = ", 5 + 6)
print("5 - 6= ", 5 - 6)
print("5 * 8 = ", 5 * 8)
print("5 / 6 = ", 5 / 6)
print("15 // 6 = ", 15 // 6)  # (//) it gives integer value
print("5 ** 6=", 5 ** 6)
print("5 % 5", 5 % 5)  # (%) it gives remainder value

print("Assignment operators")
x = 5
print(x)
x += 7
print(x)
x = x - 7
print(x)
x %= 7
print(x)
x *= 7
print(x)

# Comparison Operator
i = 5
print(i == 8)
print(i != 5)  # (!) it means not
print(i and 5)

# Logical operator
'''a = True
b = False
 print(a and a)
 print(a and b)
 print(a or b)'''

# Identity Operator
a = True
b = False
print(a is b)
print(a is not b)
print(5 is not  7)

#Membership Operators
list = [3,4,5,6,7,32,45,6]
print( 32 in list)
print(343 in list)
print(345 not in list)

#Bitwise Operators
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
print(0 & 1) # & it multiplies ( And gate)
print(0 & 2)
print(0 | 1) # | it adds the no (OR gate)
print(0 | 3)
