# 1.	Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “c” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd Python Training”
# as a string.

x = int(input("Please Enter a Value Divisible by Either 3, 5 or Both: "))
if x % 3 == 0:
    print("Consultadd")
elif x % 5 == 0:
    print("c")
elif x % 3 == 0 and x % 5 == 0:
    print("Condultadd Python Training")
else:
    print("Please enter a valid value")