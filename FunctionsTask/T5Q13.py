# 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567

import functools

a = [[1, 2, 3], [4, 5], [6, 7, 8]]
print(functools.reduce(lambda x, y: x + y, a))