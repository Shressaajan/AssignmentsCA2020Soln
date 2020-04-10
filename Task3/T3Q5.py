# 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

a = list(range(1,20))
for i in a:
    if i % 2 == 0:
        a.remove(i)
print(a)