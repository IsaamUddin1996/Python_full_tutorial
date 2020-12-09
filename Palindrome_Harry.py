'''
Author: Harry
Date: 15 April 2019
Purpose: Practice Problem For CodeWithHarry Channel
'''


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        print(
            f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")

def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    size = int(input("Enter the size of your list\n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number of the list\n")))
    print(f"You have entered {num_list}")

    print(f"Output List: {[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i] ) for i in range(size)]}")


    # new_list = []
    # for element in num_list:
    #     if element >10:
    #         n = next_palindrome(element)
    #         new_list.append(n)

    #     else:
    #         new_list.append(element)
    # print(f"Output List: {new_list}")
