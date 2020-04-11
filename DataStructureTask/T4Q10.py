# 10. 	Write a program in Python to complete the following task:

# Create two different list as in even_list and odd_list
# Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the
# even_list and if the entered number is odd append it to the odd list.
# Keep that in mind you can only add 5 items in each list
# Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

even_list = []
odd_list = []

while True:
    x = int(input('Please Enter either even or odd number between 1-50: '))
    if x in range(51):
        if x % 2 == 0:
            even_list.append(x)
            if len(even_list) == 5 and len(odd_list) >= 5:
                print(even_list[:5])
                print('The Sum of even_list:', sum(even_list[:5]))
                print('The Maximum value in even_list:', max(even_list[:5]))
                print(odd_list[:5])
                print('The Sum of odd_list:', sum(odd_list[:5]))
                print('The Maximum value in odd_list:', max(odd_list[:5]))
                break
            elif len(even_list) > 5:
                print('Maximum Input Value for even_list reached!!')
        else:
            odd_list.append(x)
            if len(odd_list) == 5 and len(even_list) >= 5:
                print(even_list[:5])
                print('The Sum of even_list:', sum(even_list[:5]))
                print('The Maximum value in even_list:', max(even_list[:5]))
                print(odd_list[:5])
                print('The Sum of odd_list:', sum(odd_list[:5]))
                print('The Maximum value in odd_list:', max(odd_list[:5]))
                break
            elif len(odd_list) > 5:
                print('Maximum Input Value for odd_list reached!!')
    else:
        print("Please Enter value between stated range!")
