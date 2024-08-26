# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

# way 1
if x == 1 or y == 1 or z == 1:
    print('passed')

# way 2
if 1 in (x, y, z):
    print('passed')

# way 3
# These only test for truthiness:
if x or y or z:
    print('passed')

# way 4
if any((x, y, z)):
    print('passed')
