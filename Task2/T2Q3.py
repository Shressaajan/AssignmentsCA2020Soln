# 3. Write a program in Python to implement the given flowchart:
# FlowChart on GoogleDoc

a, b, c = 10, 20, 30
avg = (a + b + c) / 3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("avg is higher than a,b,c")
elif avg > a and avg > b:
    print("avg is higher than a,b,c")
elif avg > a and avg > c:
    print("avg is higher than a,c")
elif avg > b and avg > c:
    print("avg is higher than b,c")
elif avg > a:
    print("avg is just higher than a")
elif avg > b:
    print("avg is just higher than b")
elif avg > c:
    print("avg is just higher than c")