# 5.Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the
# sentence capitalized.
# Sample input:
# Hello world
# Practice makes perfect
# Expected Output:
# HELLO WORLD
# PRACTICE MAKES PERFECT


def cap_str():
    cap_list = []
    num_str = int(input('Please Enter the number of lines of string you want to capitalize: '))
    count = 0
    while count < num_str:
        count += 1
        inp_str = input('Please Enter your string one line at a time: ')
        inp_str_list = [inp_str]
        for i in inp_str_list:
            cap_list.append(i.upper())

    for j in cap_list:
        print(j)


cap_str()
