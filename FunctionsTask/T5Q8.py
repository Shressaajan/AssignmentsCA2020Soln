# 8. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.


def sqr_tuple():
    x = list(range(1,21))
    y = []
    for i in x:
        i *= i
        y.append(i)
    z = tuple(y)
    return z

print(sqrt_tuple())