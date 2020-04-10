# 2. Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If USer Enter 4 - Multiplication
# If User Enter 5 - Average
# Ask user to enter the 2 numbers in a variable for first and second for the first 4
# options mentioned above.
# Ask user to enter two more numbers as first1 and second2 for calculating the average
# as soon as user choose an option 5.
# At the end if the answer of any operation is Negative print a statement saying “zsa”
# NOTE: At a time user can perform one action at a time.

user_input = int(input("please choose from the following: \nEnter 1 for Addition \nEnter 2 for Subtraction \nEnter 3 "
                       "for Division \nEnter 4 for Multiplication \nEnter 5 for Average: "))

if user_input not in range(1, 6):
    print("Please enter a valid number")
elif user_input in range(1, 6):
    _1stNum = int(input("Please enter the first number you want to perform calculations: "))
    _2ndNum = int(input("Please enter the second number you want to perform calculations: "))
    if user_input in range(1, 5):
        if user_input == 1:
            print("Addition of:", _1stNum, _2ndNum, ":", _1stNum + _2ndNum)
            if (_1stNum + _2ndNum) < 0:
                print('zsa')
        if user_input == 2:
            print("Subtraction of:", _1stNum, _2ndNum, ":", _1stNum - _2ndNum)
            if (_1stNum - _2ndNum) < 0:
                print('zsa')
        if user_input == 3:
            print("Division of:", _1stNum, _2ndNum, ":", _1stNum / _2ndNum)
            if (_1stNum / _2ndNum) < 0:
                print('zsa')
        if user_input == 4:
            print("Multiplication of:", _1stNum, _2ndNum, ":", _1stNum * _2ndNum)
            if (_1stNum * _2ndNum) < 0:
                print('zsa')
    elif user_input == 5:
        print("Please enter 2 additional numbers for Average")
        _3rdNum = int(input("Your third number: "))
        _4thNum = int(input("Your fourth number: "))
        print("Your Average of:", _1stNum, _2ndNum, _3rdNum, _4thNum, "is: ",
              (_1stNum + _2ndNum + _3rdNum + _4thNum) / 4)
        if ((_1stNum + _2ndNum + _3rdNum + _4thNum) / 4) < 0:
            print('zsa')
