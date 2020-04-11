# 12. Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

x = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y = list(x)
z = []
a = ()
for i in y:
    if i % 2 == 0:
        z.append(i)
    a = tuple(z)
print(a)
print(type(a))