# 7. Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.


def user_input():
    x = input("Please Enter 1st string: ")
    y = input("Please Enter 2nd string: ")
    if len(x) > len(y):
        print(x)
    elif len(x) < len(y):
        print(y)
    elif len(x) == len(y):
        print(x , '\n'+y)


user_input()