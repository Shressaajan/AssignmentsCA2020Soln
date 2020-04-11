#  14. 	What is the output of the following codes:
# (i)
def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)


# ==>> 2 is the output because, try has no condition to return 1 and finally returns 2 regardless.

# (ii)
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')


a()

# ==>> output is 'after f' because, there is NameError where 'f' is not defined and finally returns
# 'after f' even if try fails.
