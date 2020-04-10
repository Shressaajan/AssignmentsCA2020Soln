# 8. Write a program in Python to iterate through the string “hello my name is abcde” and print the string which
# has even length of word.

x = 'Hello my name is abcde'
for i in x.split(' '):
    if len(i) % 2 == 0:
        print(i)
