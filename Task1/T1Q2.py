# 2. Create a variable of value type complex and swap it with another variable whose value
# is an integer.

a = 4 + 3j
b = 10
a, b = b, a
print(a)
print(b)
