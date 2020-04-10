# 3. Swap two numbers using the third variable as result name and do the same task without
# using any third variable.

# Using third variable:
a = int(input ('Enter a value for a'))
b = int(input ('Enter a value for b'))
print(a, b)

c = a
a = b
b = c
print(a,b)


# Without third variable:
a = int(input ('Enter a value for a'))
b = int(input ('Enter a value for b'))
a += b
b = a - b
a -= b
print(a, b)