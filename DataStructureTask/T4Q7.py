# 7. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with
# their index.

x = input('Please Enter a string: ')
y = x[::-1]
z = ['a', 'e', 'i', 'o', 'u']
for i in y:
    if i in z:
        print(i, y.index(i))
