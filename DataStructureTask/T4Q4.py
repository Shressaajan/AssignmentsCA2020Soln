# 4. Create a list of thousand number using range and xrange and see the difference between each other.

x = range(1001)
print(x)
# In Python2, this range function gives the output as a list and not a range type, where as in python3,
# gives us the data type as range unless otherwise called.

# output:

# Python2:
# ==> [1, 2, 3,........, 1000]

# Python3:
# ==> range(1001)

x = xrange(1001)

# output:

# Python2:
# ==> xrange(1001)

# Python3:
# ==> NameError
# **Python3 doesn't take xrange



