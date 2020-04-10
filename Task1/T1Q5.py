# 5. Write a program to complete the task given below:
# a) Ask the user to enter any 2 numbers in between 1-10 and add both of them to another
# variable call z.
# b) Use z for adding 30 into it and print the final result by using variable result.

x = int(input("Enter a value between 1-10: "))
if x not in range(1, 11):
    print("Number must be between 1-10")

y = int(input("Enter a value between 1-10: "))
if y not in range(1, 11):
    print("Number must be between 1-10")

z = 30
print("Result: ", x + y + z)