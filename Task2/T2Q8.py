# 8. Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

x = input("please enter desired word: ")
count1 = 0
count2 = 0
for i in x:
    if i.isdigit():
        count1 += 1
    elif i.isalpha():
        count2 += 1
print("Letters:", count2)
print("Digits:", count1)