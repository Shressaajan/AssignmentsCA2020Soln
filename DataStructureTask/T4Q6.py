# 6. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number
# which is divisible by 3 and a multiple of 2.

x = []
for i in list(range(1100)):
    if i % 3 == 0 and i % 2 == 0:
        x.append(i)
print(x)
