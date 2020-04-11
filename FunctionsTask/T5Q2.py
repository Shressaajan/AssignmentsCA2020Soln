# 2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
# Expected Output:
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def user_str(x):
    count1 = 0
    count2 = 0
    for i in x:
        if i.isupper():
            count1 += 1
        if i.lower():
            count2 += 1
    print("No. of Upper case characters: ", count1)
    print("No. of Lower case Characters: ", count2)


user_str("ConSaLTadDPytTHon")
