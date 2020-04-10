# 7. Write a program to replace the last element in a list with another list.
# Sample data: [[1,3,5,7,9,10],[2,4,6,8]]
# Expected output: [1,3,5,7,9,2,4,6,8]

l_1 = [1, 3, 5, 7, 9, 10]
l_2 = [2, 4, 6, 8]
l_1[-1:] = l_2
print(l_1)