# 6. What is the output of the following code examples?
# a)    x=123
#    	   for i in x:
#    		print(i)
#
''' ==> It throws a TypeError stating ‘Int’ object is not iterable. '''

# b)i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(“error”)
# Soln.
# The output is:
# 0
# error
# 1
# error
# 2
''' ==> The loop will print 0 through 5, if the number is not 3, it will print error and when 
the number is 3, it ends the Loop. '''

# c) count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         Break
# Soln.
# The output is
# 0
# 1
# 2
# 3
# 4
''' ===> The loop helps to count starting from 0 adding 1 for every iteration until it is greater
# or equals 5 and it breaks, resulting in the end of the loop. '''