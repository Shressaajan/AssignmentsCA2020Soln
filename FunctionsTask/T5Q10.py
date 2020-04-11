# 10. Write a program which can filter() to make a list whose elements are even number
# between 1 and 20 ( both included)

seq = list(range(21))
res = list(filter(lambda x: x % 2 == 0, seq))
print(res)