# 9. Read the two parts of the question below: Write a program such that it asks users to “guess the lucky number”.
# If the correct number is guessed the program stops, otherwise it continues forever. Modify the program so that it
# asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for
# the answer to the question whether they want to continue guessing. The program stops if the user guesses the
# correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed
# the correct number)

ans = 777
num = int(input("Guess the Lucky Number:"))
while num != ans:
    x = input("Sorry, you guessed Wrong \nDo you want to try again? \nyes/no:")
    if x == 'yes':
        n_num = int(input("Enter a new number! \nHint: It's a three digit number. :"))
        if n_num == ans:
            print("CONGRATULATIONS!!! \nYou chose the lUCKY NUMBER")
            break
        else:
            continue
    elif x != 'yes' and x != 'no':
        print ('Enter valid value')
    else:
        print("Better luck next time!")
        break
else:
    print("CONGRATULATIONS!!! \nYou chose the LUCKY NUMBER")