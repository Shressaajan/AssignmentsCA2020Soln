# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

x = int(input('Please enter an integer either positive or negative: '))
while x > 0:
    print('Good Going')
    continue
else:
    print('It’s Over!')