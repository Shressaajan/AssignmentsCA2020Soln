# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a
# hyphen-separated sequence after sorting them alphabetically.


def sorted_output(x):
    y = x.split('-')
    return print('-'.join(sorted(y)))

sorted_output("a-z-s-x-d-c-f-v-g-b-h-n")