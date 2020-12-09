# Harry potter has got n number of apples. Harry has some students among whom, he wants to distribute the apples.
# These n number of apples are provided to harry by his friends and he can request for few more or few less apples.
# You need to print whether a number in range mn to mx is a divisor of n or not.
# Input:
# Take input n, mn and mx from the user
# Output:
# Print whether the numbers between mn and mx are divisor of n or not. If mn = mx, show that this is not a range and mn is equal to mx.
# Show the result for that number
# Example:
#
# If n is 20 and mn=2 and mx = 5
#
# 2 is a divisor of 20
#
# 3 is not a divisor of 20
#
# …
#
# 5 is a divisor of 20

mn =int(input("Enter mn range of students: "))
mx =int(input("Enter mx range of students: "))
n = int(input("Harry got Apples to distribute: "))
for i in range(mn,mx+1):
    print(i)
    if(i%n==0):
        print(f"{i} is a divisor of {n}")
    elif mn==mx:
        print("This is not a range")
    else:
        print(f"{i} is not a divisor of {n}")
