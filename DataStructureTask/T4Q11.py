# 11. Write a program to find out the occurrence of a specific word from an alphanumeric statement.
# Example: 12abcbacbaba344ab
# Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic

x = input('Please Enter an Alphanumeric statement: ')

for i in x:
    if i.isalpha():
        count = 0
        for j in range(len(x)):
            if i == x[j]:
                count += 1
        print(i, count)

