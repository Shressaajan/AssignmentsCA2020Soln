# 8. If one data type value is assigned to ‘a’ variable and then a different data type
# value is assigned to ‘a’ again. Will it change the value. If Yes then Why?

# ⇒ Yes, when we assign a different data type to variable ‘a’, even if it already has a
# value of different data type, the value of the variable changes.
#       First of all, Python automatically takes care of the physical representation for the
# different data types, i.e. an integer value will be stored in a different memory location
# than a float or a string.
#       Secondly, the initial value is lost once the second assignment to the value is
# evaluated. The value stored in a variable is simply the last one assigned to it.