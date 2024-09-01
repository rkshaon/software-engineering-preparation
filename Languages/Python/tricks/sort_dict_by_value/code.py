# How to sort a Python dict by value

import operator

# value
x = {'a': 4, 'c': 2, 'd': 1, 'b': 3, 'e': 5}
print(x)

# approach 1
sx1 = sorted(x.items(), key=lambda x: x[1])
print(sx1)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# approach 2
sx2 = sorted(x.items(), key=operator.itemgetter(1))
print(sx2)  # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
