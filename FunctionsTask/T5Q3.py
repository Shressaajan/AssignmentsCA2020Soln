# 3. Create a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return print(x)

unique_list([1,2,3,4,2,2,2,3,4,5,6,7,4,3,2])