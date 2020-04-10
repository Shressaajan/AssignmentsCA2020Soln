# 8. Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d1.update(d2)
print("concatenated dictionary is:",d1)