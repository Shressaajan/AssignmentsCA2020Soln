# 6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

a = list(range(1,31))
b = a[:5]+a[-5:]
c = []
for i in b:
    i *= i
    c.append(i)
print(c)