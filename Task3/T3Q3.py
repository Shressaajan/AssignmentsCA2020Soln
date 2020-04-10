# 3. Write a program to get the sum and multiply of all the items in a given list.

b = [2, 4, 6, 8, 10]
print("Sum of all numbers in list b:", sum(b))
res = 1
for i in b:
    res = res * i
print("multiplication of numbers:", res)